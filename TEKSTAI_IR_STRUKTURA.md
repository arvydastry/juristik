# BUHALTERIJOS DEMO — svetainės struktūra, tekstai ir dizaino gairės

Dizaino maketas WordPress projektui.
Kryptis paimta iš kliento įsigyto **Salient „Business 3“** šablono (themenectar.com/salient/business-3).
Turinio struktūra ir tekstų pavyzdžiai — pagal **uab123.lt**, tačiau visi tekstai perrašyti savais žodžiais ir papildyti,
kad nesutaptų su originalu. Nuotraukos, video, adresas ir rekvizitai — **nenaudoti iš uab123.lt**;
naudojamos laisvos licencijos Pexels nuotraukos, o įmonės duomenys — demonstraciniai.

> **v3 — 2026-09-21: konservatyvi, statiška versija.** Klientas paprašė ramesnio, mažiau „modernaus“ dizaino, todėl:
> pašalintos sekcijos **Sektoriai**, **Komanda**, **Vilnius · visa Lietuva** (ir slenkanti sektorių juosta);
> nebeliko video fonų, parallax, slenkančių juostų, įslinkimo animacijų, skaitiklių, individualaus žymeklio ir kitų
> judesio efektų — žr. 5 skyrių. Ankstesnė (dinamiška) versija išsaugota `archyvas/maketas_v2_modernus.html`.
>
> **2026-09-21 (vėliau): įdėtas kliento logotipas „Juristik“** (antraštė, poraštė, mobilus meniu, naršyklės ikonos) ir iš hero pašalintas
> mygtukas „Kaip mes dirbame“ kartu su vaizdo įrašo langu — **puslapyje nebeliko nė vieno video**.
>
> **2026-09-21 (dar vėliau): pašalinta sekcija „Kainos“** (planai ir kainos skaičiuoklė) ir įrašyti **tikri įmonės rekvizitai** (Avelianaris, UAB).

**Publikuota:** kodas — https://github.com/arvydastry/juristik (vieša repozitorija) · peržiūra — **https://arvydastry.github.io/juristik/**
(GitHub Pages iš `main` šakos šaknies; puslapis turi `noindex, nofollow`). Atnaujinimas: `python3 build.py` → `git add -A && git commit` → `git push` —
GitHub Pages persidiegia pats per 1–3 min.

**Failai:**

| Failas | Paskirtis |
|---|---|
| `index.html` | Tas pats puslapis su vietinėmis nuotraukomis — jį rodo **GitHub Pages** (generuoja `build.py`) |
| `README.md` | Trumpas repozitorijos aprašas |
| `maketas.html` | Pagrindinis dizaino maketas (nuotraukos ir video kraunami iš Pexels — reikia interneto) |
| `maketas_lokalus.html` | Tas pats maketas su vietinėmis nuotraukomis iš `nuotraukos/` (video lieka nuotoliniai) |
| `deploy/` | Visiškai savarankiška versija (vietinės nuotraukos **ir** video) — Netlify / hostingui; `_headers`, `robots.txt`, `.htaccess` |
| `build.py` | `python3 build.py` — iš `maketas.html` sugeneruoja `maketas_lokalus.html`, `deploy/index.html` ir zip (trūkstamas nuotraukas atsisiunčia pats) |
| `logo/` | **Juristik logotipas**: tamsus ir baltas variantai (permatomas fonas), „J“ ženklas, ikonos (favicon, Apple, WP „Site Icon“), kliento originalas |
| `nuotraukos/` | Makete naudojamos Pexels nuotraukos (paruoštos kelti į WordPress medijos biblioteką) |
| `archyvas/` | `maketas_v2_modernus.html` — ankstesnė versija su efektais ir pašalintomis sekcijomis; `nuotraukos_v2/` — tik jai reikalingos nuotraukos |
| `TEKSTAI_IR_STRUKTURA.md` | Šis dokumentas — tekstai kopijavimui ir dizaino specifikacija |

---

## 1. Prekės ženklas ir rekvizitai

| Elementas | Reikšmė | Būsena |
|---|---|---|
| Prekės ženklas (logotipas, `<title>`) | **Juristik** | tikras |
| Juridinis pavadinimas | **Avelianaris, UAB** | tikras |
| Įmonės kodas | **306383900** | tikras |
| PVM mokėtojo kodas | **LT100017220013** | tikras |
| Adresas | **Lvivo g. 3-12, LT-07156 Vilnius** | tikras |
| Šūkis (hero) | Skaičiai tvarkoje. Verslas — laisvas augti. | pasiūlymas |
| Telefonas | +370 600 00000 | ⚠️ **demonstracinis** |
| El. paštas | info@buhalterijosdemo.lt | ⚠️ **demonstracinis** |
| Darbo laikas | I–V 8:00–17:00 | ⚠️ **demonstracinis** |
| Svetainės kalbos | **LT / EN / DE** (perjungiklis pagrindiniame meniu; žr. 3.4) | — |

Rekvizitai makete: poraštės kairiajame stulpelyje (pavadinimas, įmonės kodas, PVM kodas, adresas), autorių teisių eilutėje
(„© 2026 Avelianaris, UAB“), adresas — dar kontaktų bloke („Biuras“) ir poraštės stulpelyje „Kontaktai“.

### Logotipas — „Juristik“

Kliento pateiktas logotipas: serifinis užrašas **Juristik**, kurio „J“ raidėje — trys kylančios kolonos (teisės / augimo motyvas).
Spalva — tamsiai mėlyna **`#02325D`**. Originalas gautas kaip WEBP su baltu fonu (2000 × 750 px), todėl iš jo paruošti
variantai su **permatomu fonu** (aplankas `logo/`):

| Failas | Kam |
|---|---|
| `juristik-logo.png` (900 × 288) | Tamsiai mėlynas — balta antraštė. **Salient → Logo** (ir „Retina Logo“) |
| `juristik-logo-white.png` (900 × 288) | Baltas — permatoma antraštė virš hero, atvertas mobilus meniu, poraštė. **Salient → „Light logo for transparent header“** |
| `juristik-zenklas.png`, `juristik-zenklas-white.png` (431 × 512) | Tik „J“ ženklas — ten, kur pilnas logotipas netelpa (socialinių tinklų avataras ir pan.) |
| `favicon.ico` (16/32/48), `favicon-32.png`, `favicon-192.png` | Naršyklės kortelės ikona: baltas „J“ ant `#02325D` suapvalinto kvadrato |
| `apple-touch-icon.png` (180) · `site-icon-512.png` | iOS pradžios ekranas · **WordPress → Customize → Site Identity → Site Icon** |
| `juristik-logo-originalas.webp` | Kliento atsiųstas originalas |

Dydžiai makete: antraštėje **44 px aukščio** (≈ 138 px pločio; telefone 36 px), poraštėje 50 px. Aplink logotipą palikti bent pusės „J“ pločio
laisvą lauką. Logotipas nesikeičia slenkant (ta pati vieta ir dydis), keičiasi tik spalvos variantas.

> ⚠️ Variantai paruošti iš rastrinio failo. Jei klientas turi **vektorinį logotipą (SVG / AI / PDF)** — verta naudoti jį
> (ryškesnis dideliuose ekranuose, mažesnis failas).
>
> Logotipo mėlyna `#02325D` šiek tiek skiriasi nuo maketo firminės `#1B4B8F` ir tamsiosios `#0B1626` — tos pačios šeimos atspalviai,
> todėl dera; jei norėsis visiško vientisumo, maketo `--brand` galima sulyginti su logotipo spalva.

---

## 2. Dizaino sistema

### 2.1 Šriftai

Abu iš Google Fonts, abu turi **latin-ext** poaibį (lietuviški ą č ę ė į š ų ū ž veikia).

| Paskirtis | Šriftas | Svoris | Dydžiai |
|---|---|---|---|
| Antraštės (H1–H4) | **Alegreya Sans** | 500 (700 logotipe) | H1 36–58 px / lh 1,1; H2 28–40 px; H3 20–25 px; H4 19 px *(v3: sumažinta — mažiau „plakatinio“ įspūdžio)* |
| Tekstas, meniu, mygtukai | **Roboto** | 400 / 500 / 700 | Tekstas 17 px / lh 1,7; „lead“ 16,5–18,5 px, svoris 400 *(v3: nebenaudojamas plonas 300)* |
| Etiketės (eyebrow) | Roboto | 700 | 11,5 px, tarpraidis 0,22em, DIDŽIOSIOMIS |
| Atsiliepimų citatos | Roboto | 400 | 16 px / lh 1,66 |

> Salient „Business 3“ originale naudojami tie patys **Alegreya Sans** (antraštės) + **Roboto** (tekstas).

### 2.2 Spalvos

Salient „Business 3“ paletė (koralinė `#ff5433` + mėlyna `#5694ff`) pritaikyta konservatyvesniam
buhalterijos įvaizdžiui: pagrindinė tampa gilus jūrinis mėlynas, o koralinė — prislopinta terakota (tik akcentams).

| Kintamasis | HEX | Kur naudojama |
|---|---|---|
| `--ink` | `#0B1626` | Tekstas, tamsios sekcijos, poraštė |
| `--navy` | `#122740` | CTA juosta |
| `--navy-2` | `#0A1A2C` | Hero fonas, „Kodėl mes“ |
| `--brand` | `#1B4B8F` | Pagrindiniai mygtukai, ikonos, aktyvios būsenos |
| `--brand-hi` | `#2A63B4` | Užvedimo būsena |
| `--sky` | `#5694FF` | Akcentas ant tamsaus fono (iš Salient) |
| `--ember` | `#C9622F` | Pagrindinis CTA, etiketės brūkšnys, aktyvios būsenos (iš Salient `#ff5433`) |
| `--mist` | `#EDF2FA` | Šalta šviesi sekcija (iš Salient `#eaf1fd`) |
| `--sand` | `#FAF3EF` | Šilta šviesi sekcija (iš Salient `#fff0ed`) |
| `--mute` | `#5A6A7E` | Antrinis tekstas |
| `--line` | `#DEE5EF` | Linijos, rėmeliai |

### 2.3 Formos ir tarpai (v3)

- **Radiusas:** 4 px mygtukams ir laukams, 6 px kortelėms ir nuotraukoms.
- **Sekcijų tarpai:** `clamp(64px, 7,5vw, 112px)`; siauresnės — `clamp(48px, 5,5vw, 80px)` (tankiau nei v2).
- **Konteineris:** 1320 px; paraštės `clamp(20px, 4,6vw, 72px)`. Antraštė — platesnė (iki 1720 px), žr. 3.5.
- **Kortelės:** 1 px rėmelis `#DEE5EF`, baltas fonas; šešėliai tik labai švelnūs (`0 4px 12px rgba(11,22,38,.05)`).
- **Perėjimai:** vienintelis dekoratyvus perėjimas — **0,2 s spalvos / rėmelio pokytis užvedus**. Niekas nejuda, nesisuka, nedidėja.
- Grūdelių tekstūros, stiklo (blur) efektų ir didelių „plaukiojančių“ šešėlių nebėra.

---

## 3. Svetainės medis ir meniu

> **Atnaujinta 2026-09-21.** Meniu struktūra pakeista pagal kliento sąrašą. Kol kas kuriamas tik pirmas
> puslapis — vidiniai puslapiai dar nesukurti, todėl makete jų nuorodos rodo pranešimą
> „vidinis puslapis bus sukurtas kitame etape“.

### 3.1 Pagrindinis meniu

**Pradžia · Paslaugos ▾ · Buhalterinė apskaita ▾ · Užsieniečių įdarbinimas ▾ · Vokiškos licencijos gavimas · Kontaktai · [LT ▾] · [Gauti pasiūlymą]**

> ⚠️ **Prielaida:** kliento pirmoje eilutėje „Buhalterinė apskaita“ tarp pagrindinių punktų nepaminėta, bet jai
> aprašytas atskiras dropdown — todėl ji padaryta **pagrindiniu punktu** tarp „Paslaugos“ ir
> „Užsieniečių įdarbinimas“ (taip pat kaip uab123.lt). Jei turėjo būti „Paslaugų“ viduje — perkeliama per kelias minutes.

**Viršutinė juosta:** telefonas · el. paštas · darbo laikas | Nemokama konsultacija
(kalbų perjungiklis iš čia **perkeltas į pagrindinį meniu** — viršutinė juosta slenkant dingsta ir mobiliajame nerodoma.)

### 3.2 „Paslaugos“ — mega meniu

Kliento sąrašas (16 unikalių punktų) sugrupuotas į tris stulpelius + išskirtą kortelę. **Punktų pavadinimai — kliento,
stulpelių antraštės „Pakeitimai ir teisė“ bei „Licencijos ir dokumentai“ — mano pasiūlymas** (vientisas 16 eilučių
sąrašas būtų ~680 px aukščio ir sunkiai skaitomas).

| 01 · Įmonių steigimas *(antraštė – nuoroda)* | 02 · Pakeitimai ir teisė | 03 · Licencijos ir dokumentai | Kortelė |
|---|---|---|---|
| UAB, MB įmonių steigimas | Įmonės pavadinimo keitimas | Transporto licencija | **Konsultacija verslo pradžios klausimais** |
| UAB, MB įmonių pardavimas | Įstatų keitimas | A1 forma | etiketė „VERSLO PRADŽIA“ |
| Įmonės registracijos adresas | Vadovo keitimas | ESI išrašas | „Teisinė forma, mokesčiai, pirmieji žingsniai — aptarkime prieš steigiant, o ne po to.“ |
| Laikinojo įdarbinimo įmonių registravimas | Įmonės likvidavimas | JANGIS pildymas | nuoroda „Registruotis konsultacijai“ |
| | Teisinės paslaugos | Darbų saugos paslaugos | |

Pastabos:
- **„Transporto licencija“** kliento sąraše buvo įrašyta du kartus — meniu palikta vieną kartą.
- **„Konsultacija VERSLO PRADŽIOS klausimais“** — klientas ją išskyrė didžiosiomis raidėmis, todėl ji tapo
  išskirta kortele su nuotrauka (didžiosios raidės perkeltos į etiketę „VERSLO PRADŽIA“, kur jos natūralios).
- Pirmasis sąrašo įrašas „Įmonių steigimas“ panaudotas kaip pirmo stulpelio antraštė ir kartu nuoroda į bendrą puslapį.

### 3.3 Paprasti dropdown (ikona + pavadinimas + aprašas)

| Punktas | Dropdown įrašas | Aprašas (Salient „Description“ laukas) |
|---|---|---|
| **Buhalterinė apskaita** | Mokami mokesčiai | Kokius mokesčius ir kada moka Jūsų įmonė |
| | Registravimas PVM mokėtoju | Prašymas, pagrindimas VMI ir palydėjimas iki sprendimo |
| **Užsieniečių įdarbinimas** | Darbdaviams | Leidimai, dokumentai ir visas įdarbinimo procesas |
| | Darbuotojams (užsieniečiams) | Leidimas gyventi, darbo sutartis ir pirmieji žingsniai Lietuvoje |

Aprašai — mano pasiūlymas; jei nereikia, Salient'e tiesiog paliekamas tuščias „Description“ laukas.

### 3.4 Kalbų perjungiklis — LT · EN · DE

- **Kur:** pagrindinio meniu dešinėje (prieš CTA mygtuką) — gaublio ikona + kalbos kodas + rodyklė; išsiskleidžia
  skydelis su trimis eilutėmis (kodas, kalbos pavadinimas ta kalba, varnelė prie aktyvios).
  Mobiliajame — trys mygtukai meniu apačioje; papildomai — nuorodos poraštės apačioje.
- **Makete:** perjungus kalbą **išverčiamas tik meniu** (visi punktai, dropdown, mega meniu, CTA, viršutinė juosta) ir
  parodomas pranešimas, kad puslapio turinys bus išverstas kitame etape. Taip galima patikrinti, ar ilgi
  angliški ir vokiški punktai telpa — **išmatuota: telpa visuose pločiuose nuo 1366 px su ≥ 38 px atsarga.**
- **WordPress:** WPML arba Polylang; perjungiklis dedamas kaip meniu punktas (rodomi kalbų kodai, ne vėliavos).
  URL struktūra: LT — be priešdėlio, `/en/`, `/de/`. Nepamiršti `hreflang`.

**Meniu vertimai (juodraštis — prieš publikuojant turi peržiūrėti gimtakalbis, ypač DE):**

| LT | EN | DE |
|---|---|---|
| Pradžia | Home | Startseite |
| Paslaugos | Services | Leistungen |
| Buhalterinė apskaita | Accounting | Buchhaltung |
| Užsieniečių įdarbinimas | Employment of foreigners | Beschäftigung von Ausländern |
| Vokiškos licencijos gavimas | Obtaining a German licence | Deutsche Lizenz erhalten |
| Kontaktai | Contact | Kontakt |
| Gauti pasiūlymą | Get a quote | Angebot anfordern |
| Nemokama konsultacija | Free consultation | Kostenlose Beratung |
| I–V 8:00–17:00 | Mon–Fri 8:00–17:00 | Mo–Fr 8:00–17:00 |
| **Įmonių steigimas** | **Company formation** | **Firmengründung** |
| UAB, MB įmonių steigimas | UAB, MB company formation | Gründung von UAB und MB |
| UAB, MB įmonių pardavimas | UAB, MB companies for sale | Verkauf von UAB und MB |
| Įmonės registracijos adresas | Registered office address | Firmensitzadresse |
| Laikinojo įdarbinimo įmonių registravimas | Registration of temporary employment agencies | Registrierung von Zeitarbeitsfirmen |
| **Pakeitimai ir teisė** | **Changes & legal** | **Änderungen & Recht** |
| Įmonės pavadinimo keitimas | Company name change | Änderung des Firmennamens |
| Įstatų keitimas | Amendment of articles of association | Satzungsänderung |
| Vadovo keitimas | Change of director | Geschäftsführerwechsel |
| Įmonės likvidavimas | Company liquidation | Liquidation des Unternehmens |
| Teisinės paslaugos | Legal services | Rechtsdienstleistungen |
| **Licencijos ir dokumentai** | **Licences & documents** | **Lizenzen & Dokumente** |
| Transporto licencija | Transport licence | Transportlizenz |
| A1 forma | A1 certificate | A1-Bescheinigung |
| ESI išrašas | ESI certified extract | ESI-Registerauszug |
| JANGIS pildymas | JANGIS filing | JANGIS-Meldung |
| Darbų saugos paslaugos | Occupational safety services | Arbeitsschutz |
| Konsultacija verslo pradžios klausimais | Business start-up consultation | Gründungsberatung |
| Mokami mokesčiai | Taxes payable | Zu zahlende Steuern |
| Registravimas PVM mokėtoju | VAT registration | Umsatzsteuer-Registrierung |
| Darbdaviams | For employers | Für Arbeitgeber |
| Darbuotojams (užsieniečiams) | For employees (foreign nationals) | Für Arbeitnehmer (Ausländer) |

> DE punktas „Deutsche Lizenz erhalten“ sąmoningai trumpesnis už pažodinį „Erwerb der deutschen Lizenz“ —
> su pažodiniu variantu vokiškas meniu ties 1366 px nebetilptų.

### 3.5 Meniu pločio pakopos (išmatuota naršyklėje su „Juristik“ logotipu)

Šeši ilgi punktai + kalbos + CTA vienoje eilėje. Logotipas (≈ 138 px) siauresnis už buvusį tekstinį bloką, todėl
šriftą pavyko padidinti. Atsarga = laisvas plotis tarp logotipo ir meniu.

| Ekrano plotis | Šriftas / tarpai | Atsarga LT | Atsarga DE |
|---|---|---|---|
| ≥ 1700 px | 15 px, punkto paraštės 14 px, antraštės konteineris iki 1720 px | 177–212 px | 178–213 px |
| 1540–1699 px | 15 px, 13 px | nuo 85 px | nuo 86 px |
| 1400–1539 px | 14,5 px, 11 px | 48–88 px | 49–89 px |
| 1366–1399 px | 14,5 px, 10 px, CTA be rodyklės | 53–86 px | 54–87 px |
| < 1366 px | **mobilus meniu** (burger) + kalbos + CTA antraštėje | — | — |
| < 761 px | antraštėje tik logotipas ir burger; kalbos — meniu viduje; apačioje veiksmų juosta | — | — |

### 3.6 Mobilus meniu

Viso ekrano tamsus sluoksnis; punktai su vaikais — **akordeonas** (vienu metu atvertas vienas). „Paslaugos“ viduje —
tos pačios trys grupės su antraštėmis + konsultacijos kortelė; kiekvieno akordeono pirmas įrašas — nuoroda į patį
tėvinį puslapį („Visos paslaugos“, „… — apžvalga“). Apačioje: kalbos (LT / EN / DE), telefonas, el. paštas, darbo laikas.

### 3.7 Poraštė

Stulpeliai: **Paslaugos** (Įmonių steigimas · Buhalterinė apskaita · Užsieniečių įdarbinimas · Vokiškos licencijos gavimas ·
Transporto licencija · Teisinės paslaugos) · **Įmonė** (Apie mus · Atsiliepimai · Blogas · DUK — sekcijos
pirmame puslapyje) · **Kontaktai** + rekvizitai ir socialiniai tinklai. Apatinėje eilutėje — LT · EN · DE ir politikos nuorodos.

> Iš pagrindinio meniu išimti punktai (Apie mus, Atsiliepimai, Blogas) pirmame puslapyje **liko kaip sekcijos** (sekcija „Kainos“ pašalinta visai) —
> jie pasiekiami slenkant ir per poraštę.

---

## 4. Sekcijos ir tekstai

### 4.1 Hero (statinė nuotrauka)

- Etiketė: `BUHALTERINĖ APSKAITA · MOKESČIAI · VERSLO TEISĖ`
- **H1:** Skaičiai tvarkoje. / Verslas — *laisvas augti.* („laisvas augti“ — šviesiai mėlyna)
- Tekstas: „Pilnas apskaitos ciklas, mokesčių planavimas ir verslo teisė vienoje komandoje. Aiški kainodara sutartyje, asmeninis buhalteris ir atsakomybė už kiekvieną skaičių — be paslėptų mokesčių ir be paskutinės minutės skambučių.“
- Fonas: **statinė nuotrauka** — rankų paspaudimas (Pexels 4175026), **apversta horizontaliai**, kad rankos būtų dešinėje, o tekstui kairėje liktų ramus tamsus fonas; ant jos — tamsiai mėlynas šydas. Video fono nebėra.
- Mygtukas: **Nemokama konsultacija** (terakotinis, veda į kontaktų formą; anksčiau — „Pasiskaičiuoti kainą“, bet skaičiuoklės nebėra).
  Mygtukas „Kaip mes dirbame“ ir vaizdo įrašo langas pašalinti — video puslapyje nebėra.
- Pasitikėjimo juosta (keturi statiniai skaičiai):

| Skaičius | Paaiškinimas |
|---|---|
| **12** | Metai rinkoje ir nė vienos praleistos deklaracijos |
| **480+** | Aptarnaujamų Lietuvos įmonių |
| **4,9 / 5** | Vidutinis klientų įvertinimas |
| **24 val.** | Atsakome į klausimą darbo dienomis |

### 4.2 ~~Sektorių juosta~~ — pašalinta (v3)

Slenkanti sektorių juosta pašalinta kartu su sekcija „Sektoriai“.

### 4.3 Apie mus

- Etiketė: `APIE MUS`
- **H2:** Buhalterės — verslo patarėjos, o ne tik „popierių pildytojos“
- Tekstas: „Esame už procesų automatizavimą — dokumentus priimame elektroniniu būdu, integruojamės su e. parduotuvėmis, banku ir sandėlio programomis. Bet su Jumis dirbs gyvas, konkretus buhalteris, kuris žino Jūsų verslo sezoniškumą, klientus ir tai, kodėl kovo mėnesį sąskaitų visada dvigubai daugiau.“
- Trys punktai su varnelėmis:
  1. **Aiški kainodara sutartyje** — Kaina fiksuojama raštu ir keičiasi tik keičiantis Jūsų dokumentų srautui — apie tai informuojame iš anksto.
  2. **Profesinės civilinės atsakomybės draudimas** — Jei suklystame mes — klaidą ir jos pasekmes tvarkome mes. Jūsų verslas dėl to nenukenčia.
  3. **Keturios kalbos** — Aptarnaujame lietuvių, anglų, rusų ir lenkų kalbomis — patogu tarptautinėms komandoms ir užsienio savininkams.
- Ženkliukas ant nuotraukos: **98 %** klientų lieka su mumis ir antrais metais
- Nuotraukos: pagrindinė — posėdis prie stalo (Pexels 7433850), mažoji — buhalterė prie dokumentų (3784295). Video nebėra.
- Mygtukai: Susipažinkime · Paslaugos

### 4.4 Paslaugos (pagrindinis sąrašas)

Etiketė `KĄ DAROME`. **H2:** Viskas, kas susiję su skaičiais, — vienoje vietoje
Tekstas: „Nuo pirminio dokumento iki metinės ataskaitos ir pokalbio su banku. Nereikia ieškoti atskiro buhalterio, mokesčių konsultanto ir teisininko — dirbame kaip viena komanda.“

| Nr. | Paslauga | Aprašymas |
|---|---|---|
| 01 | **Pilna buhalterinė apskaita** | Pirminiai dokumentai, didžioji knyga, atsargos, ilgalaikis turtas, tarpinės ataskaitos vadovui — visas ciklas kas mėnesį. |
| 02 | **Mokesčiai ir deklaravimas** | PVM, GPM, Sodra, pelno mokestis, Intrastat ir OSS. Deklaracijos pateikiamos laiku, o apie terminus primename mes, ne VMI. |
| 03 | **Darbo užmokestis ir personalas** | Atlyginimų skaičiavimas, darbo sutartys ir jų pakeitimai, atostogų grafikai, komandiruotės, ligos ir priedų apskaita. |
| 04 | **Finansinės ataskaitos ir auditas** | Metinių finansinių ataskaitų rinkinys, teikimas Registrų centrui, pasiruošimas auditui, bankui ar investuotojui. |
| 05 | **Įmonių steigimas ir pertvarkymas** | UAB, MB ir VšĮ steigimas internetu, įstatų keitimas, kapitalo didinimas, reorganizavimas ir tvarkingas likvidavimas. |
| 06 | **Vadybinė apskaita ir konsultacijos** | Mokesčių scenarijų analizė, biudžetas, pinigų srautų prognozė ir ataskaitos, kurias supranta ne tik buhalteris. |

**Papildomai** — „Dažniausiai prireikia ir šito“ (6 kortelės):

| Nr. | Pavadinimas | Aprašymas |
|---|---|---|
| 07 | Registravimas PVM mokėtoju | Paruošiame prašymą, pagrindžiame veiklą VMI ir palydime iki sprendimo. Pasakome ir tada, kai registruotis dar per anksti. |
| 08 | Užsieniečių įdarbinimas | Leidimai dirbti ir laikinai gyventi, komandiravimas, „Blue Card“ — nuo dokumentų iki pirmos darbo dienos. |
| 09 | Registracijos adresas | Juridinis adresas Vilniuje su korespondencijos priėmimu ir skenavimu — patogu, kai veikla vyksta nuotoliniu būdu. |
| 10 | Apskaitos atkūrimas | Sutvarkome praeitį: atkuriame apskaitą, taisome deklaracijas ir paruošiame įmonę patikrinimui be panikos. |
| 11 | Buhalterijos peržiūra | Nepriklausoma „antroji nuomonė“ apie esamą apskaitą: kur permokate mokesčių, o kur rizikuojate baudomis. |
| 12 | Teisinės paslaugos verslui | Sutarčių rengimas ir peržiūra, prekės ženklo registracija, transporto licencijos, akcininkų susitarimai. |

### 4.5 Kodėl mes (tamsi sekcija su statine nuotrauka fone)

**H2:** Patikimas partneris — stabilus verslas
Tekstas: „Buhalterį keičiantys klientai dažniausiai mini tuos pačius tris dalykus: neaiškias sąskaitas, nepasiekiamą žmogų ir „sužinojau paskutinę dieną“. Mūsų darbo tvarka sukurta taip, kad nė vienas iš jų nepasikartotų.“

| Nr. | Antraštė | Tekstas |
|---|---|---|
| 01 | Jokių paslėptų mokesčių | Kaina nurodyta sutartyje ir apima viską, kas išvardyta paslaugų sąraše. Jei darbo apimtis auga, apie kainos pokytį sužinote iš anksto, o ne sąskaitoje. |
| 02 | Asmeninis buhalteris | Vienas žmogus, vienas telefono numeris, viena istorija. Nereikia kaskart iš naujo aiškinti, kuo užsiima Jūsų įmonė ir kodėl sąskaitos atrodo būtent taip. |
| 03 | Atsakome už savo darbą | Turime profesinės civilinės atsakomybės draudimą. Jei klaida mūsų — taisome ją mes ir padengiame pasekmes, o ne aiškiname, kad „taip pateikė klientas“. |
| 04 | Atsakymas per 24 valandas | Į laiškus ir žinutes atsakome per vieną darbo dieną. Skubiais mokestiniais klausimais — tą pačią dieną, nes sprendimai versle laukia retai. |
| 05 | Kalbame Jūsų kalba | Lietuvių, anglų, rusų ir lenkų. Dokumentus ir ataskaitas paruošiame ta kalba, kuria kalba Jūsų savininkai ar investuotojai. |
| 06 | Lankstus nutraukimas | Sutartį galima nutraukti be baudų ir papildomų įsipareigojimų. Duomenis ir dokumentus perduodame tvarkingai, per sutartą terminą. |

### 4.6 Skaičiai

**480+** aptarnaujamų įmonių visoje Lietuvoje · **12** metų nepertraukiamos praktikos ·
**4,9 / 5** klientų įvertinimas iš 214 atsiliepimų · **100 %** deklaracijų, pateiktų iki termino

### 4.7 Kaip dirbame (keturios kortelės viena po kitos)

**H2:** Keturi žingsniai nuo pirmo skambučio iki ramaus ketvirčio
Tekstas: „Perėjimas pas naują buhalterį atrodo baisiau, nei yra iš tikrųjų. Štai kaip tai vyksta pas mus — įskaitant tą dalį, apie kurią dažniausiai niekas neįspėja.“

**01 · Pokalbis ir įvertinimas**
Pasikalbame 30–40 minučių: ką ir kaip darote, kiek dokumentų sukuriate, kur dabar skauda. Peržiūrime kelis mėnesius dokumentų ir pasakome, kiek realiai kainuos apskaita — be „nuo“ ir be žvaigždučių.
*Trukmė: 1–2 darbo dienos · Kaina: nemokamai, be įsipareigojimų · Gaunate: raštišką pasiūlymą su paslaugų sąrašu*

**02 · Sutartis ir perėmimas**
Pasirašome sutartį su fiksuota kainodara. Perimame likučius iš ankstesnio buhalterio, patikriname jų teisingumą ir apie rastus neatitikimus pranešame Jums raštu — kad vėliau jie netaptų „mūsų“ klaidomis.
*Trukmė: 5–10 darbo dienų · Galima: pereiti bet kurį mėnesį, ne tik nuo sausio · Susipažįstate: su savo buhalteriu ir jo pavaduotoju*

**03 · Kasdienis darbas**
Dokumentus siunčiate patogiu kanalu — el. paštu, programėle arba tiesiogiai iš savo sistemos. Mes tvarkome, deklaruojame, primename apie artėjančius terminus ir mokėjimus. Klausimai neatidedami „iki mėnesio pabaigos“.
*Atsakymas: per 24 val. darbo dienomis · Priminimai: apie kiekvieną deklaraciją ir mokėjimą · Integracijos: bankas, e. parduotuvė, sandėlis, kasos*

**04 · Ataskaitos ir sprendimai**
Kas mėnesį gaunate trumpą ataskaitą vadovui: pelnas, skolos, mokėtini mokesčiai ir tai, į ką verta atkreipti dėmesį. Kartą per ketvirtį susėdame pokalbiui apie mokesčių scenarijus ir artimiausius sprendimus.
*Kas mėnesį: ataskaita vadovui, 1 puslapis · Kas ketvirtį: pokalbis apie mokesčius ir prognozę · Kartą per metus: finansinių ataskaitų rinkinys*

### 4.8 ~~Kainos~~ · 4.9 ~~Kainos skaičiuoklė~~ — pašalinta (2026-09-21)

Kliento sprendimu viešų kainų puslapyje nebėra: pašalinti trys planai (120 € / 250 € / nuo 300 €) ir interaktyvi skaičiuoklė.
Kartu pakeista viskas, kas į juos rėmėsi:

| Vieta | Buvo | Dabar |
|---|---|---|
| Hero mygtukas | „Pasiskaičiuoti kainą“ → skaičiuoklė | **„Nemokama konsultacija“** → kontaktų forma |
| Sekcijos „Paslaugos“ nuoroda dešinėje | „Visos paslaugos ir kainos“ → kainos | **„Gauti pasiūlymą“** → kontaktų forma |
| Meniu „Buhalterinė apskaita“ (pats punktas) ir mobilaus meniu „… — apžvalga“ | slinko į kainas | kaip ir kiti būsimi vidiniai puslapiai — pranešimas „bus sukurta kitame etape“ |
| Poraštė | nuoroda „Kainos“, mygtukas „Skaičiuoklė“ | nuorodos nebėra; mygtukas **„Gauti pasiūlymą“** |
| DUK 1 klausimas | minėjo 120 € / 250 € ir skaičiuoklę | atsakymas be konkrečių sumų (žr. 4.14) |

Planų tekstai ir skaičiuoklės formulė išliko `archyvas/maketas_v2_modernus.html`, jei kada prireiktų vidiniam puslapiui.

### 4.10 ~~Sektoriai~~ · 4.11 ~~Komanda~~ — pašalinta (v3)

Kliento sprendimu šių sekcijų pirmame puslapyje nebėra. Tekstai ir dizainas išliko `archyvas/maketas_v2_modernus.html`,
jei kada prireiktų (pvz. vidiniam puslapiui „Apie mus“).

### 4.12 Atsiliepimai (demonstraciniai)

> v3: vietoje slenkančios juostos — **statiškas 3 × 2 kortelių tinklelis** (planšetėje 2 stulpeliai, telefone 1).

**H2:** Patikimas partneris — stabilus verslas

1. „Perėjome vidury metų ir bijojome chaoso. Likučiai perimti per savaitę, o rastus ankstesnės apskaitos neatitikimus gavome surašytus raštu — pirmą kartą kas nors paaiškino, kas ten iš tikrųjų vyko.“ — *Vadovas, UAB „Girios kelias“ · statyba*
2. „Turime e. parduotuvę keturiose rinkose. Anksčiau OSS deklaracijos buvo mėnesio pabaigos siaubas, dabar tai tiesiog dar viena eilutė ataskaitoje. Integracija su sistema veikė nuo pirmos dienos.“ — *Savininkė, MB „Rytas prekyba“ · e. prekyba*
3. „Steigimas vyko nuotoliniu būdu, savininkai — užsienyje. Visi dokumentai buvo paruošti angliškai, o klausimus išsprendė vienas žmogus, o ne trys skirtingi skyriai.“ — *Plėtros vadovas, UAB „Baltic Craft“ · gamyba*
4. „Vertiname tai, kad apie mokesčių pokyčius sužinome iš buhalterio, o ne iš naujienų portalo. Ketvirtiniai pokalbiai keletą kartų sutaupė daugiau, nei kainuoja metinis aptarnavimas.“ — *Finansų vadovė, UAB „Nemuno linija“ · logistika*
5. „Dirbame su 40 darbuotojų ir nuolatine kaita. Darbo sutartys, atostogų grafikai ir Sodros ataskaitos tvarkomos taip, kad man nebereikia apie tai galvoti — tik pasirašyti.“ — *Direktorius, UAB „Žalias diskas“ · HoReCa*
6. „Ruošėmės investuotojo patikrinimui ir per tris savaites gavome sutvarkytą trejų metų apskaitą su paaiškinimais. Klausimų iš auditorių buvo mažiau, nei tikėjomės.“ — *Įkūrėjas, UAB „Vėjo startas“ · IT*

> Realioje svetainėje siūloma pridėti Google atsiliepimų nuorodą ir tikrų klientų pavadinimus (gavus sutikimą).

### 4.13 ~~Vilnius · visa Lietuva~~ — pašalinta (v3)

Sekcijos nebėra; kontaktų bloke „Biuras“ nebe nuoroda, o paprasta eilutė.

### 4.14 DUK

1. **Kiek kainuoja buhalterinė apskaita?** — Kaina priklauso nuo dokumentų srauto, darbuotojų skaičiaus, PVM statuso ir veiklos pobūdžio, todėl vienos kainos visiems nėra. Tikslią sumą pasakome per 1–2 darbo dienas — peržiūrėję kelių mėnesių dokumentus. Ji įrašoma į sutartį ir nesikeičia, kol nesikeičia darbo apimtis. Pirmas pokalbis ir pasiūlymas — nemokami.
2. **Ar galiu pereiti pas jus vidury metų?** — Taip, ir taip nutinka dažniau nei nuo sausio. Perimame likučius iš ankstesnio buhalterio, patikriname jų teisingumą ir raštu pateikiame rastus neatitikimus. Perėmimas paprastai trunka 5–10 darbo dienų, o Jūsų einamieji terminai per tą laiką nenukenčia.
3. **Kaip perduodu dokumentus?** — Patogiausiu Jums būdu: el. paštu, per debesų aplanką, mobiliąja programėle nufotografuojant kvitą arba automatiškai iš savo sistemos. Integruojamės su populiariausiomis e. parduotuvių, kasos ir sandėlio programomis bei banko išrašais. Popierinių dokumentų taip pat neatsisakome.
4. **Kas nutinka, jei buhalteris suklysta?** — Klaidą taisome mes ir savo sąskaita — įskaitant patikslintų deklaracijų teikimą bei bendravimą su VMI ar Sodra. Turime profesinės civilinės atsakomybės draudimą, kuris padengia dėl mūsų klaidos atsiradusius nuostolius. Draudimo liudijimą pateikiame kartu su sutartimi.
5. **Ar dirbate su e. prekyba ir užsienio klientais?** — Taip. Tvarkome OSS ir Intrastat ataskaitas, ES ir trečiųjų šalių sandorius, kelių valiutų apskaitą, grąžinimus bei prekybos platformų ataskaitas. Užsienio savininkams dokumentus ir ataskaitas paruošiame anglų kalba.
6. **Kada verta registruotis PVM mokėtoju?** — Privaloma — peržengus įstatyme nustatytą 12 mėnesių pajamų ribą arba įsigyjant prekių iš ES virš nustatytos sumos. Savanoriškai verta svarstyti tada, kai dauguma Jūsų klientų patys yra PVM mokėtojai arba planuojate stambias investicijas. Prieš registraciją visada suskaičiuojame abu scenarijus — kartais laukti yra pigiau.
7. **Ar padedate steigiant įmonę?** — Taip. Rezervuojame pavadinimą, paruošiame steigimo dokumentus, padedame su elektroniniu parašu, registracijos adresu ir banko sąskaitos atidarymu. Steigimas internetu paprastai trunka 1–3 darbo dienas. Kartu aptariame, kuri teisinė forma ir mokestinis modelis Jūsų atveju bus pigiausias.
8. **Kaip nutraukiama sutartis?** — Įspėjus prieš vieną mėnesį, be baudų ir papildomų mokesčių. Perduodame visus duomenis, dokumentus ir apskaitos registrus tokiu formatu, kurį priims naujas buhalteris. Laikome, kad klientas turi likti dėl kokybės, o ne dėl sutarties sąlygų.

> ⚠️ DUK tekstuose sąmoningai **nenurodytos konkrečios mokesčių ribos ir tarifai** (pvz., PVM riba eurais),
> nes jie keičiasi. Prieš publikuojant verta arba palikti taip, arba nurodyti datą, kada informacija atnaujinta.

### 4.15 Blogas (demo įrašai)

| Kategorija | Antraštė | Anonsas |
|---|---|---|
| PVM | PVM riba: kada registruotis ir ko nedaryti paskutinę savaitę | Trys tipinės klaidos, kurias įmonės daro artėdamos prie ribos, ir kodėl skubota registracija kartais brangesnė už savanorišką. |
| Darbo užmokestis | GPM ir Sodra: ką verta peržiūrėti darbo užmokesčio politikoje jau dabar | Priedai, naudos natūra, nuotolinio darbo kompensacijos — kur dažniausiai atsiranda nedeklaruotų pajamų rizika. |
| Ataskaitos | Metinė finansinė ataskaita per penkis žingsnius, be paskutinės nakties | Ką paruošti dar spalį, kokius likučius suderinti su tiekėjais ir kodėl inventorizacija nėra formalumas. |

### 4.16 CTA juosta

**H2:** Pirmas pokalbis nieko nekainuoja — o dažnai sutaupo daugiau, nei tikitės
Tekstas: „Papasakokite, kaip veikia Jūsų verslas. Peržiūrėsime kelis mėnesius dokumentų, pasakysime tikslią kainą ir tai, ką dabartinėje apskaitoje verta taisyti — net jei nuspręsite likti su esamu buhalteriu.“
Mygtukai: Užsisakyti konsultaciją · +370 600 00000

### 4.17 Kontaktai

**H2:** Susisiekime — „Atsakome darbo dienomis per 24 valandas. Jei klausimas skubus — skambinkite, telefonu dažniausiai atsakome iš karto.“

Forma: Vardas, pavardė · Įmonės pavadinimas · El. paštas · Telefonas · Dominanti paslauga (sąrašas) ·
Įmonės dydis (sąrašas) · Trumpai apie veiklą ir dokumentų srautą · sutikimo varnelė · **Siųsti užklausą**

Kontaktų eilutės: Telefonas · El. paštas · **Biuras — Lvivo g. 3-12, LT-07156 Vilnius** (nuoroda atidaro Google Maps) · Darbo laikas.

> **Vietos kortelė:** makete — Vilniaus verslo rajono panorama (Lvivo g. yra būtent šiame rajone) su adreso užrašu ir mygtuku
> „Atidaryti Google Maps“. Žymeklio ant vaizdo nėra sąmoningai: OpenStreetMap duomenyse Lvivo g. 3 namo numerio nėra, todėl tikslios vietos
> statiniame žemėlapyje pažymėti nepavyko. WordPress versijoje vietoj kortelės dedamas tikras Google Maps `iframe` su adresu „Lvivo g. 3, Vilnius“.

---

## 5. Judesys ir užvedimo būsenos (v3 — konservatyvi versija)

Principas: **puslapis statiškas.** Juda tik tai, ką lankytojas pats įjungia (meniu, akordeonas),
o užvedus pelę keičiasi tik **spalva arba rėmelis (0,2 s)** — niekas neslenka, nesisuka, nedidėja.

### 5.1 Kas liko

| Vieta | Elgsena |
|---|---|
| Mygtukai | Užvedus pasikeičia fono spalva (pvz. terakota → tamsesnė terakota, mėlyna → tamsiai mėlyna) |
| Nuorodos su rodykle | Užvedus pasikeičia teksto spalva |
| Meniu punktai | Spalva + 2 px linija ant antraštės apatinio krašto; aktyvus punktas liniją turi visada |
| Dropdown ir mega meniu | Atsiranda paprastu 0,16 s išryškėjimu, be slinkimo ir be pakopinių animacijų; eilutės užvedus gauna šviesų foną |
| Antraštė | Visada matoma (lipni); permatoma tik pačiame viršuje virš hero nuotraukos, paslinkus — balta. Logotipas atitinkamai baltas / tamsiai mėlynas |
| Paslaugų sąrašo eilutės | Užvedus — baltas fonas, mėlynas pavadinimas, terakotinis rodyklės apskritimas |
| Kortelės (papildomos paslaugos, straipsniai) | Užvedus — tamsesnis rėmelis ir labai švelnus šešėlis; kortelė nejuda |
| DUK akordeonas | Atsiveria per 0,3 s; „+“ virsta „−“ |
| Mobilus meniu | Akordeonas 0,3 s; punktai atsiranda visi iš karto |
| Pranešimas (toast) | Praneša apie dar nesukurtus vidinius puslapius ir kalbų versijas |

`prefers-reduced-motion` išjungia ir šiuos trumpus perėjimus. Klaviatūros fokusas — 2 px terakotinis kontūras.

### 5.2 Ko nebėra (palyginti su v2)

Visi video (fonai hero, „Apie mus“, „Kodėl mes“, CTA sekcijose ir lange atidaromas „Kaip mes dirbame“) · parallax · slenkančios juostos (sektoriai, atsiliepimai, poraštės užrašas) ·
įslinkimo (scroll reveal) animacijos ir antraštės „kaukė“ · skaitikliai (count-up) ir besipiešiantys žiedai · individualus pelės žymeklis ·
magnetiniai mygtukai · paskui pelę sekanti nuotrauka paslaugų sąraše · 3D pakrypimas ir „prožektorius“ kortelėse ·
nusipiešiantys rėmeliai · lipnios, viena ant kitos kraunamos proceso kortelės · blizgesio brūkšnys kainų kortelėse ·
meniu teksto ir ikonų „persivertimas“, mega meniu „užuolaida“ · antraštės slėpimas slenkant žemyn · slinkties progreso juosta ·
grūdelių tekstūra · pulsuojantys žymekliai (žemėlapis, video mygtukas, „Slinkite“ užuomina) · plaukiojančios formos etiketės
(dabar — klasikinės etiketės virš laukų).

---

## 6. Techninės pastabos WordPress diegimui

### 6.1 Rekomenduojama struktūra Salient tema

| Maketo sekcija | Salient / WPBakery elementas |
|---|---|
| Logotipas | *Salient → Header → Logo*: „Logo“ = `juristik-logo.png`, „Light logo for transparent header“ = `juristik-logo-white.png`, aukštis ≈ 44 px (mobiliajame 36 px); Site Icon = `site-icon-512.png` |
| Antraštė | Header Layout „Menu Left Aligned“ (kaip Business 3) + **Full Width Header** + Transparent Header; lipni (sticky), **be** „Hide Until Needed“; Secondary Header Bar — telefonas, el. paštas, darbo laikas |
| Meniu „Paslaugos“ | **Mega Menu** (įjungiama punkto „Salient menu item options → Mega Menu“): 2 lygio punktai = stulpelių antraštės, 3 lygio = nuorodos |
| Mega meniu kortelė | Paprasčiausia — 4-as stulpelis su **„Mega Menu Column Background Image“**; tiksliai kaip makete — **Global Section** metodas (skydelis kuriamas puslapių kūrimo įrankiu) |
| Dropdown su ikona ir aprašu | Punkto **Icon** skirtukas + WordPress **Description** laukas (Screen Options → Description) + temos nustatymas **„Header Dropdown Display Descriptions“** |
| Mygtukas „Gauti pasiūlymą“ | Meniu punktas su **„Menu Item Link Button Style“**; mobiliajame — **„Persist In Mobile Navigation Header“** |
| Kalbų perjungiklis | WPML / Polylang meniu punktas (kalbų kodai); galima pažymėti „Persist In Mobile Navigation Header“ |
| Mobilus meniu | Off Canvas Menu → stilius „Fullscreen“ + dropdown elgsena **„Inline“** (akordeonas) |
| Hero | Row su **fono nuotrauka** (ne video) + spalvos šydas, `vc_row-o-full-height`; vienas mygtukas „Nemokama konsultacija“ |
| Paslaugų sąrašas | Paprastos eilutės: numeris · pavadinimas · aprašas · rodyklė (Row su 4 stulpeliais ir apatine linija arba „Fancy Unordered List“); **be** „Mouse Follow Image“ |
| Papildomos paslaugos | Fancy Box / Icon Box tinklelis, 3 stulpeliai |
| Kodėl mes | Row su **fono nuotrauka** ir tamsiu šydu + Icon Box tinklelis 3 × 2 |
| Skaičiai | Paprastas tekstas 4 stulpeliuose su skiriamosiomis linijomis (jei naudojamas „Milestone“ — **išjungti skaičiavimo animaciją**) |
| Kaip dirbame | Keturios paprastos eilutės-kortelės viena po kitos (be sticky) |
| Atsiliepimai | Statiškas 3 stulpelių tinklelis (Testimonial elementai be slankiklio / be automatinio keitimo) |
| DUK | „Toggles / Accordion“ elementas |
| Blogas | „Recent Posts“ / „Post Grid“ |
| Kontaktai | Contact Form 7 arba WPForms + Google Maps iframe (adresas „Lvivo g. 3, Vilnius“) |

### 6.2 Ko nepamiršti

- **Šriftai:** Salient nustatymuose parinkti Alegreya Sans (antraštės) ir Roboto (tekstas), būtinai
  su `latin-ext` poaibiu, kitaip lietuviškos raidės kris į atsarginį šriftą.
- **Animacijos:** Salient stulpeliams ir eilutėms **neįjungti** „Column / Row Animation“ (fade in, reveal ir pan.), vaizdams — „Parallax“;
  tema pagal nutylėjimą jų neprideda, tad tiesiog nieko nežymėti. Mygtukų stilius — be „hover“ animacijų (tik spalva).
- **Video:** puslapyje nėra nė vieno — nei fonuose, nei lange.
- **Spalvos:** įrašyti į Salient „Color Scheme“ — Accent Color `#C9622F`, Extra Color 1 `#1B4B8F`,
  Extra Color 2 `#5694FF`.
- **Meniu plotis:** šeši ilgi punktai telpa tik nuo **1366 px** — Salient nustatyti *Header → Mobile Breakpoint ≈ 1366 px*,
  meniu šriftą 14–15 px, tarpus tarp punktų 8–14 px (žr. 3.5 lentelę). Verčiant į DE vengti ilgesnių punktų nei lietuviški.
- **Dropdown laikymas atvertu:** makete viršutinių punktų nuorodos užima visą antraštės aukštį, o skydelis prigludęs prie
  apatinio krašto — tarp punkto ir skydelio nėra „mirusios zonos“, kurioje `:hover` nutrūktų. Salient tai daro pats.
- **Antraštės būsenos:** permatoma (baltas tekstas) tik pačiame puslapio viršuje; vos paslinkus — balta su tamsiu tekstu ir lieka matoma visą laiką.
- **Hero nuotrauka** makete apversta per CSS (`transform: scaleX(-1)`); WordPress'e paprasčiau įkelti jau apverstą failą.
- **`overflow-x`:** makete naudojamas `overflow-x: clip` (ne `hidden`), nes `hidden` ant `body`
  sugadina `position: sticky` meniu. Jei temoje atsiras `overflow-x: hidden`, meniu „nukris“ žemyn.
- **SEO:** vienas `H1` puslapyje, sekcijų antraštės — `H2`, kortelių — `H3`/`H4` (makete taip ir yra).
- **Greitis:** nuotraukos su `loading="lazy"` (išskyrus hero), WebP formatas, `srcset` per WP.

### 6.3 Medija (v3)

Visos nuotraukos — **Pexels** (laisva licencija, autorystės nurodyti neprivaloma).

| Tipas | ID | Kur naudojama |
|---|---|---|
| Nuotrauka | 4175026 | **Hero fonas** — rankų paspaudimas (makete apversta horizontaliai) |
| Nuotrauka | 7433850 | „Apie mus“ — posėdis prie stalo |
| Nuotrauka | 3784295 | „Apie mus“ — mažoji nuotrauka (buhalterė prie dokumentų) |
| Nuotrauka (video kadras) | 7317314 | „Kodėl mes“ fonas — stiklinis biuras vakare |
| Nuotrauka (video kadras) | 8471105 | CTA juostos fonas — sutarties pasirašymas |
| Nuotrauka | 8927687, 7691692, 7658352 | Tinklaraščio kortelės |
| Nuotrauka | 34246394 | Kontaktai — vietos kortelė (Vilniaus verslo rajono panorama nuo Neries) |
| Nuotrauka | 33175650 | Mega meniu konsultacijos kortelė |

Failai atsisiųsti į `nuotraukos/` (`px<ID>_<plotis>.jpg`); v2 versijos nuotraukos perkeltos į `archyvas/nuotraukos_v2/`.

---

## 7. Kas dar liko nuspręsti klientui

1. ~~Rekvizitai~~ — gauti ir įrašyti (Avelianaris, UAB; 2026-09-21). **Dar trūksta:** tikro telefono, el. pašto ir darbo laiko
   (makete — +370 600 00000, info@buhalterijosdemo.lt, I–V 8:00–17:00). Taip pat: ar klientas turi **vektorinį logotipą**?
2. ~~Komandos nuotraukos~~ — sekcija „Komanda“ pašalinta (v3).
3. **Tikri atsiliepimai** — su įmonių pavadinimais ir sutikimais; verta prijungti Google atsiliepimus.
4. ~~Kainos ir skaičiuoklė~~ — sekcija „Kainos“ pašalinta (2026-09-21).
5. **Ar kainos bus kur nors rodomos** (pvz. vidiniame „Buhalterinė apskaita“ puslapyje), ar visada tik „pagal užklausą“?
6. **EN ir DE vertimai** — meniu vertimų juodraštis yra 3.4 skyriuje; turinį ir galutinius terminus turi peržiūrėti gimtakalbis.
   Makete kalbų perjungiklis verčia tik meniu.
7. **Blogo turinio planas** — kiek straipsnių per mėnesį ir kas juos rašys.
8. **„Buhalterinė apskaita“ — pagrindinis punktas ar „Paslaugų“ dalis?** Makete — pagrindinis (žr. prielaidą 3.1).
9. **Kas tiksliai yra „Vokiška licencija“** (transporto licencija Vokietijoje? laikinojo įdarbinimo leidimas — AÜG?).
   Nuo to priklausys puslapio turinys ir tikslus DE / EN punkto pavadinimas.
10. **Mega meniu grupių pavadinimai** „Pakeitimai ir teisė“ ir „Licencijos ir dokumentai“ — pasiūlymas, galima keisti.
11. **Pirmo puslapio turinys vs. naujas meniu:** sekcija „Paslaugos“ ir poraštės stulpelis „Įmonė“ vis dar atspindi ankstesnę
    (buhalterijos) struktūrą; naujų krypčių — užsieniečių įdarbinimo ir vokiškos licencijos — pirmame puslapyje dar nėra.
