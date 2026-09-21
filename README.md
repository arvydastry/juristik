# „Juristik“ svetainės dizaino maketas

Avelianaris, UAB (prekės ženklas **Juristik**) svetainės pirmo puslapio dizaino maketas, parengtas pagal Salient temos šabloną
[„Business 3“](https://themenectar.com/salient/business-3/). Svetainė bus daroma su WordPress ir Salient tema,
todėl makete naudojami tik tokie sprendimai, kuriuos Salient atkartoja savo elementais.

**Peržiūra:** https://arvydastry.github.io/juristik/

Klientas norėjo konservatyvaus, statiško dizaino — puslapyje nėra video, parallax, slenkančių juostų ar įslinkimo
animacijų; užvedus pelę keičiasi tik spalva.

## Failai

| Failas | Kas tai |
|---|---|
| `index.html` | Pradžios puslapis — jį rodo GitHub Pages (nuotraukos ir logotipas iš šios repozitorijos) |
| `maketas.html` | **Šaltinis.** Tas pats puslapis, tik nuotraukos kraunamos iš Pexels. Redaguojamas tik šis failas |
| `maketas_lokalus.html` | Šaltinio kopija su vietinėmis nuotraukomis (peržiūrai be interneto) |
| `build.py` | Iš `maketas.html` sugeneruoja `index.html`, `maketas_lokalus.html`, `deploy/` ir zip Netlify Drop'ui |
| `TEKSTAI_IR_STRUKTURA.md` | Visi tekstai, meniu struktūra su EN / DE vertimais, dizaino sistema, Salient diegimo gairės, atviri klausimai |
| `logo/` | Juristik logotipas (tamsus ir baltas, permatomas fonas), „J“ ženklas, naršyklės ir WordPress ikonos |
| `nuotraukos/` | Makete naudojamos Pexels nuotraukos |
| `deploy/` | Savarankiška versija Netlify ar kitam hostingui (`_headers`, `netlify.toml`, `robots.txt`, `.htaccess`) |
| `archyvas/` | Ankstesnė, dinamiška maketo versija (su efektais, video ir vėliau pašalintomis sekcijomis) |

## Peržiūra

Atidarykite `index.html` naršyklėje arba paleiskite vietinį serverį:

```bash
python3 -m http.server 8777
```

Po bet kokio `maketas.html` pakeitimo:

```bash
python3 build.py
```

## Ką verta žinoti peržiūrint

- Apačioje dešinėje esanti žymė „Dizaino maketas“ skirta tik maketui, į WordPress ji nekeliama.
- Kuriamas tik pirmas puslapis. Meniu nuorodos į vidinius puslapius rodo pranešimą „bus sukurta kitame etape“.
- Kalbų perjungiklis (LT · EN · DE) makete verčia tik meniu — taip matyti, kad ilgi vokiški punktai telpa.
  Tikroje svetainėje kalbas valdys WPML arba Polylang.
- Užklausos forma duomenų nesiunčia, ji tik parodo, kaip veiks.
- Kontaktuose vietoje žemėlapio — verslo rajono nuotrauka su nuoroda į Google Maps; WordPress versijoje bus tikras žemėlapis.
- Puslapis pažymėtas `noindex`, kad maketas nepatektų į paieškos sistemas.

## Laukiantys patikslinimai

Surašyti `TEKSTAI_IR_STRUKTURA.md` 7 skyriuje: tikras telefonas, el. paštas ir darbo laikas (rekvizitai jau tikri),
tikri klientų atsiliepimai, EN ir DE vertimų peržiūra, kas tiksliai yra „vokiška licencija“, vektorinis logotipas,
ir pirmo puslapio turinio suderinimas su nauja meniu struktūra.
