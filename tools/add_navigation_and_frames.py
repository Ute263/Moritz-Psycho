from pathlib import Path

FILES = [Path('index.html'), Path('teil2.html'), Path('teil3.html')]

STYLE = r'''
    /* Einheitliche Navigation und dekorative Überschriftenrahmen */
    html{scroll-behavior:smooth}
    h2{position:relative;padding:18px 22px;border:2px solid #c8dde5;border-radius:20px;background:linear-gradient(135deg,var(--blue),#ffffff);box-shadow:0 7px 18px rgba(79,127,143,.08)}
    h2::before{content:"";position:absolute;left:18px;right:18px;bottom:-7px;height:7px;border-radius:0 0 10px 10px;background:var(--mint)}
    h3{padding:12px 16px;border-left:6px solid var(--accent);border-radius:12px;background:var(--lilac);box-shadow:0 3px 10px rgba(79,127,143,.06)}
    h4{display:inline-block;padding:5px 10px;border-radius:10px;background:var(--peach)}
    .back-to-top{position:fixed;right:18px;bottom:18px;z-index:50;display:flex;align-items:center;gap:8px;padding:12px 15px;border:1px solid #b8cbd2;border-radius:999px;background:rgba(255,253,249,.96);color:var(--ink);text-decoration:none;font-weight:800;box-shadow:0 10px 28px rgba(43,64,80,.18);backdrop-filter:blur(8px)}
    .back-to-top:hover{transform:translateY(-2px);background:var(--blue)}
    .page-switcher{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 24px;padding:14px;border:1px solid var(--line);border-radius:18px;background:var(--paper)}
    .page-switcher a{padding:9px 13px;border-radius:999px;background:var(--mint);color:var(--ink);text-decoration:none;font-weight:750}
    @media(max-width:560px){.back-to-top span{display:none}.back-to-top{padding:13px 16px;font-size:1.2rem}h2{padding:15px 17px}h3{padding:10px 13px}}
    @media print{.back-to-top,.page-switcher{display:none!important}h2,h3{box-shadow:none}}
'''

SWITCHER = '''\n  <nav class="page-switcher" aria-label="Lehrbuchteile">\n    <a href="index.html">Teil 1 · Wahrnehmung & Motivation</a>\n    <a href="teil2.html">Teil 2 · Entwicklung, Gedächtnis & Emotion</a>\n    <a href="teil3.html">Teil 3 · Kommunikation</a>\n  </nav>\n'''

BACK = '''\n  <a class="back-to-top" href="#seitenanfang" aria-label="Zurück zum Seitenanfang">↑ <span>Zum Anfang</span></a>\n'''

for path in FILES:
    text = path.read_text(encoding='utf-8')
    if 'Einheitliche Navigation und dekorative Überschriftenrahmen' not in text:
        text = text.replace('  </style>', STYLE + '\n  </style>')
    if 'id="seitenanfang"' not in text:
        text = text.replace('<body>', '<body id="seitenanfang">', 1)
    if 'class="page-switcher"' not in text:
        text = text.replace('  <main>', SWITCHER + '\n  <main>', 1)
    if 'class="back-to-top"' not in text:
        text = text.replace('</body>', BACK + '\n</body>', 1)
    path.write_text(text, encoding='utf-8')
