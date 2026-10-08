#!/usr/bin/env python3
"""Składa podstrony z _pages/*.html + wspólny layout. Uruchom: python3 tools/build.py"""
import hashlib, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://impulseo-pl.github.io/energia-zmiany/"
TEL = "+48 601 479 750"
TEL_HREF = "+48601479750"
MAIL = "kontakt@energiazmiany.pl"

PAGES = [
    # plik, tytuł, opis, etykieta w nav (None = poza nav)
    ("index.html", "Energia Zmiany — Wojciech Łysik | Dotacje i doradztwo dla małych firm",
     "Wojciech Łysik, ENERGIA ZMIANY: pozyskiwanie dofinansowań, szkolenia i doradztwo dla małych firm, projekt Nauczyciel na swoim. Tel. 601 479 750.", None),
    ("wsparcie-dla-firm.html", "Wsparcie dla małych firm — dotacje, szkolenia, warsztaty | Energia Zmiany",
     "Praktyczne wsparcie dla małych firm: jak pozyskiwać środki na rozwój, rozliczać dotacje i obniżać koszty. Bezpłatne spotkanie 1:1. Tel. 601 479 750.", "Wsparcie dla firm"),
    ("nauczyciel-na-swoim.html", "Nauczyciel na swoim — własna firma po odejściu ze szkoły | Energia Zmiany",
     "Projekt NAUCZYCIEL NA SWOIM: krok po kroku od pomysłu do własnej firmy, z dotacją na start. Tel. 601 479 750.", "Nauczyciel na swoim"),
    ("wspomaganie-zdrowia.html", "Wspomaganie leczenia chorób cywilizacyjnych | Energia Zmiany",
     "Metody wspomagające zdrowie i regenerację: fale milimetrowe RGA MED, wodoroterapia, biofeedback BIOSYN QS Pro. Tel. 601 479 750.", "Zdrowie"),
    ("o-mnie.html", "O mnie — Wojciech Łysik | Energia Zmiany",
     "Wojciech Łysik: ekspert od funduszy unijnych, samorządowiec z ponad 34-letnim stażem. Ponad 976 tys. zł dofinansowań dla 28 firm od 2023 r.", "O mnie"),
    ("baza-wiedzy.html", "Baza wiedzy i aktualności | Energia Zmiany",
     "Artykuły i aktualności o dotacjach, prowadzeniu małej firmy i zdrowiu. Energia Zmiany, Wojciech Łysik.", "Baza wiedzy"),
    ("kontakt.html", "Kontakt — umów bezpłatne spotkanie | Energia Zmiany",
     "Kontakt z Wojciechem Łysikiem: tel. 601 479 750 (8:00–20:00), kontakt@energiazmiany.pl, Adelin, ul. Oliwkowa 54.", "Kontakt"),
]

def h(path):
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]

def nav(current):
    items = []
    for f, _, _, label in PAGES:
        if not label:
            continue
        cur = ' aria-current="page"' if f == current else ""
        items.append(f'<a href="{f}"{cur}>{label}</a>')
    items.append('<a class="btn btn-primary" href="kontakt.html#formularz">Bezpłatne spotkanie</a>')
    return "\n        ".join(items)

LAYOUT = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}img/logo.webp">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={vcss}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"ENERGIA ZMIANY Wojciech Łysik","url":"{base}","telephone":"{tel}","email":"{mail}","founder":{{"@type":"Person","name":"Wojciech Łysik"}},"address":{{"@type":"PostalAddress","streetAddress":"ul. Oliwkowa 54","postalCode":"07-230","addressLocality":"Adelin","addressCountry":"PL"}},"areaServed":"PL","openingHours":"Mo-Su 08:00-20:00"}}</script>
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
<div class="topbar">
  <div class="wrap">
    <span class="hide-sm">Telefon: <b>8:00–20:00</b></span>
    <a href="tel:{telhref}">{tel}</a>
    <a href="mailto:{mail}">{mail}</a>
  </div>
</div>
<header class="header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Energia Zmiany — strona główna">
      <img src="img/logo.webp" alt="Logo Energia Zmiany" width="48" height="48">
      <span class="brand-txt"><b>Energia Zmiany</b><small>Wojciech Łysik</small></span>
    </a>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Główna nawigacja">
        {nav}
    </nav>
  </div>
</header>
<main id="tresc">
{content}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html">
          <img src="img/logo.webp" alt="" width="48" height="48">
          <span class="brand-txt"><b>Energia Zmiany</b><small>Wojciech Łysik</small></span>
        </a>
        <p>ENERGIA ZMIANY WOJCIECH ŁYSIK<br>ul. Oliwkowa 54, 07-230 Adelin</p>
      </div>
      <div>
        <h4>Oferta</h4>
        <ul>
          <li><a href="wsparcie-dla-firm.html">Wsparcie dla małych firm</a></li>
          <li><a href="nauczyciel-na-swoim.html">Nauczyciel na swoim</a></li>
          <li><a href="wspomaganie-zdrowia.html">Wspomaganie leczenia chorób cywilizacyjnych</a></li>
        </ul>
      </div>
      <div>
        <h4>Strona</h4>
        <ul>
          <li><a href="o-mnie.html">O mnie</a></li>
          <li><a href="baza-wiedzy.html">Baza wiedzy</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
          <li><a href="#" aria-disabled="true">Polityka prywatności</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:{telhref}">{tel}</a></li>
          <li><a href="mailto:{mail}">{mail}</a></li>
          <li>Telefon: 8:00–20:00</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>© <span data-year>2026</span> ENERGIA ZMIANY Wojciech Łysik</span>
    <span>Projekt strony: Impulseo</span>
  </div>
</footer>
<script src="assets/main.js?v={vjs}" defer></script>
</body>
</html>
"""

def main():
    vcss, vjs = h("assets/styles.css"), h("assets/main.js")
    for f, title, desc, _ in PAGES:
        content = (ROOT / "_pages" / f).read_text(encoding="utf-8")
        content = content.replace("{TEL}", TEL).replace("{TEL_HREF}", TEL_HREF).replace("{MAIL}", MAIL)
        url = BASE if f == "index.html" else BASE + f
        out = LAYOUT.format(title=title, desc=desc, url=url, base=BASE, vcss=vcss, vjs=vjs,
                            tel=TEL, telhref=TEL_HREF, mail=MAIL, nav=nav(f), content=content.strip())
        (ROOT / f).write_text(out, encoding="utf-8")
        print("ok", f)

if __name__ == "__main__":
    main()
