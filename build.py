#!/usr/bin/env python3
"""
Buhalterijos demo — išvestinių failų generatorius.

Šaltinis visada yra maketas.html (nuotraukos ir video iš Pexels CDN). Iš jo sugeneruojama:
  · index.html            — tas pats puslapis su vietinėmis nuotraukomis; jį rodo GitHub Pages (repozitorijos šaknis)
  · maketas_lokalus.html  — nuotraukos iš ./nuotraukos
  · deploy/index.html     — viskas vietoje (nuotraukos, logotipas, ikonos), paruošta Netlify / hostingui
  · buhalterijos-demo-netlify.zip

Naudojimas:  python3 build.py
Trūkstamos nuotraukos atsisiunčiamos automatiškai.
"""
import hashlib, os, re, shutil, ssl, sys, urllib.request, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'maketas.html')
IMG_DIR = os.path.join(ROOT, 'nuotraukos')
LOGO_DIR = os.path.join(ROOT, 'logo')
DEPLOY = os.path.join(ROOT, 'deploy')
ZIP = os.path.join(ROOT, 'buhalterijos-demo-netlify.zip')

# nuotolinis video -> vietinis failas deploy/video/. v3 (statiškoje) versijoje liko tik vaizdo įrašas,
# atidaromas lange mygtuku „Kaip mes dirbame“; kiti įrašai palikti sąraše, jei fonai kada nors grįžtų.
VIDEOS = {
    'https://videos.pexels.com/video-files/853822/853822-hd_1920_1080_25fps.mp4': 'video/hero.mp4',
    'https://videos.pexels.com/video-files/6563857/6563857-hd_1280_720_25fps.mp4': 'video/apie.mp4',
    'https://videos.pexels.com/video-files/7317314/7317314-hd_1920_1080_25fps.mp4': 'video/kodel.mp4',
    'https://videos.pexels.com/video-files/8471105/8471105-hd_1920_1080_25fps.mp4': 'video/cta.mp4',
    'https://videos.pexels.com/video-files/7593780/7593780-hd_1920_1080_25fps.mp4': 'video/procesas.mp4',
}


def image_map(html):
    """Pexels nuotraukos URL -> nuotraukos/px<ID>_<plotis>.jpg (atsisiunčia, jei failo nėra)."""
    ctx = ssl._create_unverified_context()
    mapping = {}
    for url in sorted(set(re.findall(r'https://images\.pexels\.com/[^"\'\s)]+', html))):
        m = re.search(r'/(?:photos|videos)/(\d+)/', url)
        w = re.search(r'[?&]w=(\d+)', url)
        name = 'px%s_%s.jpg' % (m.group(1) if m else hashlib.md5(url.encode()).hexdigest()[:8], w.group(1) if w else 'x')
        path = os.path.join(IMG_DIR, name)
        if not os.path.exists(path):
            os.makedirs(IMG_DIR, exist_ok=True)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=60, context=ctx) as r, open(path, 'wb') as f:
                f.write(r.read())
            print('  atsisiųsta:', name)
        mapping[url] = 'nuotraukos/' + name
    return mapping


def localize(html, mapping):
    for url, local in mapping.items():
        html = html.replace(url, local)
    return html


def main():
    html = open(SRC, encoding='utf-8').read()
    mapping = image_map(html)

    # 1) maketas_lokalus.html
    lok = localize(html, mapping)
    lok = lok.replace('mokesčiai verslui</title>', 'mokesčiai verslui (vietinės nuotraukos)</title>', 1)
    lok = lok.replace('<i></i>Dizaino maketas · demo turinys', '<i></i>Dizaino maketas · vietinės nuotraukos', 1)
    open(os.path.join(ROOT, 'maketas_lokalus.html'), 'w', encoding='utf-8').write(lok)

    # 2) deploy/index.html
    dep = localize(html, mapping)
    used_videos = set()
    for url, local in VIDEOS.items():
        if url not in dep:
            continue                      # šio video makete nebėra (pvz. fonas pakeistas nuotrauka)
        if not os.path.exists(os.path.join(DEPLOY, local)):
            sys.exit('KLAIDA: trūksta failo deploy/' + local)
        dep = dep.replace(url, local)
        used_videos.add(os.path.basename(local))
    if 'pexels.com' in dep:
        sys.exit('KLAIDA: deploy versijoje liko nuorodų į pexels.com')
    os.makedirs(os.path.join(DEPLOY, 'nuotraukos'), exist_ok=True)
    used_images = {os.path.basename(v) for v in mapping.values()}
    for name in used_images:
        shutil.copy2(os.path.join(IMG_DIR, name), os.path.join(DEPLOY, 'nuotraukos', name))
    # logotipas ir ikonos — keliaujama tik tie failai, į kuriuos makete yra nuoroda
    logo_used = sorted(set(re.findall(r'logo/([\w.-]+)', dep)))
    dlogo = os.path.join(DEPLOY, 'logo'); os.makedirs(dlogo, exist_ok=True)
    for fn in os.listdir(dlogo):
        if fn not in logo_used:
            os.remove(os.path.join(dlogo, fn))
    for fn in logo_used:
        if not os.path.exists(os.path.join(LOGO_DIR, fn)):
            sys.exit('KLAIDA: trūksta failo logo/' + fn)
        shutil.copy2(os.path.join(LOGO_DIR, fn), os.path.join(dlogo, fn))
    # deploy/ yra sugeneruotas aplankas — nebenaudojami medijos failai iš jo išmetami
    removed = []
    for sub, keep, ext in (('nuotraukos', used_images, '.jpg'), ('video', used_videos, '.mp4')):
        d = os.path.join(DEPLOY, sub)
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                if fn.endswith(ext) and fn not in keep:
                    os.remove(os.path.join(d, fn)); removed.append(sub + '/' + fn)
            if not os.listdir(d):
                os.rmdir(d)               # tuščias aplankas (pvz. video/, kai video nebeliko)
    if removed:
        print('  iš deploy/ pašalinta nebenaudojamų failų: %d' % len(removed))
    unused_src = sorted(f for f in os.listdir(IMG_DIR) if f.endswith('.jpg') and f not in used_images)
    if unused_src:
        print('  nuotraukos/ turi makete nenaudojamų failų: %d (galima perkelti į archyvas/)' % len(unused_src))
    open(os.path.join(DEPLOY, 'index.html'), 'w', encoding='utf-8').write(dep)
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(dep)      # GitHub Pages (šaknis): nuotraukos/ ir logo/ keliai tie patys

    # 3) zip
    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(DEPLOY):
            for fn in files:
                if fn == '.DS_Store':
                    continue
                full = os.path.join(base, fn)
                z.write(full, os.path.relpath(full, DEPLOY))

    print('maketas.html          %7d B' % len(html.encode()))
    print('maketas_lokalus.html  %7d B' % len(lok.encode()))
    print('index.html            %7d B  (GitHub Pages)' % len(dep.encode()))
    print('deploy/index.html     %7d B  (nuotraukų: %d, video: %d, logo failų: %d)' % (len(dep.encode()), len(used_images), len(used_videos), len(logo_used)))
    print('zip                   %7.1f MB' % (os.path.getsize(ZIP) / 1048576))


if __name__ == '__main__':
    main()
