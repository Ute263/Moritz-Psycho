from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

old = '''  <header class="hero">
    <div class="eyebrow">Psychologie · Ergotherapie</div>
    <h1>Moritz’ digitales Lehrbuch</h1>
    <p class="lead">Teil 1 erklärt die beiden Klausurthemen <strong>Wahrnehmung</strong> und <strong>Motivation</strong> ausführlich, verständlich und mit direktem Bezug zur ergotherapeutischen Praxis.</p>
    <div class="nav"><a href="#wahrnehmung">Kapitel 1 · Wahrnehmung</a><a href="#motivation">Kapitel 2 · Motivation</a><a href="#klausurtraining">Klausurtraining</a></div>
  </header>'''

new = '''  <header class="hero">
    <div class="eyebrow">Psychologie · Ergotherapie</div>
    <h1>Moritz’ digitales Lehrbuch</h1>
    <p class="lead">Dieses Lehrbuch umfasst alle fünf klausurrelevanten Themen. Die Inhalte sind in drei übersichtliche Teile gegliedert und werden verständlich, fachlich korrekt und mit direktem Bezug zur Ergotherapie erklärt.</p>

    <div class="book-overview" aria-label="Kapitelübersicht">
      <a class="part-card part-one" href="#wahrnehmung">
        <span class="part-label">Teil 1</span>
        <strong>Kapitel 1 · Wahrnehmung</strong>
        <strong>Kapitel 2 · Motivation und Volition</strong>
        <small>Auf dieser Startseite</small>
      </a>
      <a class="part-card part-two" href="teil2.html">
        <span class="part-label">Teil 2</span>
        <strong>Kapitel 3 · Entwicklungspsychologie</strong>
        <strong>Kapitel 4 · Gedächtnis und Emotion</strong>
        <small>Zur zweiten Lehrbuchseite</small>
      </a>
      <a class="part-card part-three" href="teil3.html">
        <span class="part-label">Teil 3</span>
        <strong>Kapitel 5 · Kommunikation</strong>
        <small>Zur dritten Lehrbuchseite</small>
      </a>
    </div>

    <div class="nav"><a href="#wahrnehmung">Kapitel 1</a><a href="#motivation">Kapitel 2</a><a href="#klausurtraining">Klausurtraining Teil 1</a></div>
  </header>'''

if old not in text:
    raise SystemExit('Hero-Bereich wurde nicht gefunden')
text = text.replace(old, new, 1)

style = '''
    .book-overview{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:28px 0 10px}
    .part-card{display:flex;flex-direction:column;gap:7px;min-height:190px;padding:20px;border:1px solid var(--line);border-radius:20px;color:var(--ink);text-decoration:none;transition:transform .18s ease,box-shadow .18s ease}
    .part-card:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(43,64,80,.12)}
    .part-card strong{line-height:1.35}.part-card small{margin-top:auto;color:var(--muted)}
    .part-label{align-self:flex-start;padding:5px 10px;border-radius:999px;background:rgba(255,255,255,.72);font-weight:800}
    .part-one{background:var(--blue)}.part-two{background:var(--mint)}.part-three{background:var(--lilac)}
    @media(max-width:760px){.book-overview{grid-template-columns:1fr}.part-card{min-height:auto}}
    @media print{.book-overview{grid-template-columns:repeat(3,1fr)}}
'''
text = text.replace('  </style>', style + '\n  </style>', 1)

# Navigation unter dem Startbereich eindeutiger beschriften
text = text.replace('<a href="index.html">Teil 1 · Wahrnehmung & Motivation</a>', '<a href="index.html">Start & Teil 1 · Kapitel 1–2</a>', 1)
text = text.replace('<a href="teil2.html">Teil 2 · Entwicklung, Gedächtnis & Emotion</a>', '<a href="teil2.html">Teil 2 · Kapitel 3–4</a>', 1)
text = text.replace('<a href="teil3.html">Teil 3 · Kommunikation</a>', '<a href="teil3.html">Teil 3 · Kapitel 5</a>', 1)

path.write_text(text, encoding='utf-8')
print('Startseite neu geordnet')
