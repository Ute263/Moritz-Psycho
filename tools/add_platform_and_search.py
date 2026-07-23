from pathlib import Path

FILES = [Path('index.html'), Path('teil2.html'), Path('teil3.html')]

SEARCH_CSS = r'''
.search-panel{position:sticky;top:10px;z-index:40;display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:18px 0;padding:14px;border:1px solid var(--line);border-radius:18px;background:rgba(255,253,249,.96);box-shadow:0 8px 24px rgba(43,64,80,.12);backdrop-filter:blur(10px)}
.search-panel input{flex:1 1 280px;min-width:0;padding:12px 14px;border:1px solid #b8cbd2;border-radius:12px;font:inherit;color:var(--ink);background:white}
.search-panel button,.platform-link{border:0;border-radius:12px;padding:11px 13px;font:inherit;font-weight:800;color:var(--ink);background:var(--blue);cursor:pointer;text-decoration:none}
.search-panel button:disabled{opacity:.45;cursor:default}.search-count{min-width:92px;text-align:center;font-weight:800;color:var(--muted)}
mark.search-hit{background:#ffe36e;color:inherit;padding:0 .08em;border-radius:3px}mark.search-hit.current{outline:3px solid #e09a00;background:#ffd24a}
.platform-screen{min-height:100vh;padding:clamp(18px,4vw,48px);background:linear-gradient(180deg,#f7fbfc,#fbfaf6)}
.platform-inner{max-width:1120px;margin:auto}.platform-hero{background:var(--paper);border:1px solid var(--line);border-radius:30px;padding:clamp(26px,5vw,52px);box-shadow:0 14px 45px rgba(43,64,80,.09)}
.course-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:28px}.course-tile{display:flex;flex-direction:column;gap:10px;min-height:210px;padding:24px;border:1px solid var(--line);border-radius:24px;background:white;text-align:left;color:var(--ink);font:inherit;box-shadow:0 8px 22px rgba(43,64,80,.07)}
button.course-tile{cursor:pointer}.course-tile:not(.disabled):hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(43,64,80,.13)}.course-icon{font-size:2.25rem}.course-title{font-size:1.35rem;font-weight:850}.course-description{color:var(--muted)}.course-status{margin-top:auto;align-self:flex-start;padding:6px 10px;border-radius:999px;background:var(--mint);font-weight:800;font-size:.9rem}.course-tile.disabled{opacity:.7;background:#f8f8f7}.course-tile.disabled .course-status{background:var(--yellow)}
.course-psychology{background:linear-gradient(145deg,var(--blue),#fff)}.course-medical{background:linear-gradient(145deg,var(--mint),#fff)}.course-anatomy{background:linear-gradient(145deg,var(--peach),#fff)}.course-disease{background:linear-gradient(145deg,var(--lilac),#fff)}.course-more{background:linear-gradient(145deg,var(--yellow),#fff)}
.course-shell-hidden{display:none!important}.platform-hidden{display:none!important}
@media(max-width:820px){.course-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:560px){.course-grid{grid-template-columns:1fr}.search-panel{top:4px}.search-panel input{flex-basis:100%}.course-tile{min-height:170px}}
@media print{.search-panel,.platform-screen{display:none!important}.course-shell-hidden{display:block!important}}
'''

PLATFORM_HTML = r'''
<div class="platform-screen" id="lernplattform">
  <div class="platform-inner">
    <section class="platform-hero">
      <div class="eyebrow">Lernen · Ergotherapie</div>
      <h1>Moritz’ Lernplattform</h1>
      <p class="lead">Alle Kurse an einem Ort. Wähle einen Kurs aus und finde Lerninhalte später über die Suche besonders schnell wieder.</p>
      <div class="course-grid" aria-label="Kursübersicht">
        <button class="course-tile course-psychology" id="open-psychology" type="button"><span class="course-icon">🧠</span><span class="course-title">Psychologie</span><span class="course-description">Vorbereitung auf die Psychologie-Klausur mit fünf Kapiteln, Fallbeispielen und Musterlösungen.</span><span class="course-status">Kurs öffnen</span></button>
        <div class="course-tile course-medical disabled"><span class="course-icon">🩺</span><span class="course-title">Medizinische Grundlagen</span><span class="course-description">Hier kann später ein weiteres Skript oder ein neuer Kurs ergänzt werden.</span><span class="course-status">Wird ergänzt</span></div>
        <div class="course-tile course-anatomy disabled"><span class="course-icon">🦴</span><span class="course-title">Anatomie</span><span class="course-description">Platz für Lerntexte, Übersichten und Prüfungsvorbereitung.</span><span class="course-status">Wird ergänzt</span></div>
        <div class="course-tile course-disease disabled"><span class="course-icon">💊</span><span class="course-title">Krankheitslehre</span><span class="course-description">Ein weiterer Kurs kann später unkompliziert hinzugefügt werden.</span><span class="course-status">Wird ergänzt</span></div>
        <div class="course-tile course-more disabled"><span class="course-icon">📚</span><span class="course-title">Weitere Kurse</span><span class="course-description">Freier Platz für zusätzliche Skripte und Lernbereiche.</span><span class="course-status">Vorbereitet</span></div>
      </div>
    </section>
  </div>
</div>
'''

SEARCH_HTML = r'''
<div class="search-panel" role="search" aria-label="Kurs durchsuchen">
  <a class="platform-link" href="index.html" data-platform-link>🏠 Lernplattform</a>
  <input class="course-search" type="search" placeholder="Kapitel oder Begriff suchen …" aria-label="Kapitel oder Begriff suchen">
  <button class="search-prev" type="button" title="Vorheriger Treffer">↑</button>
  <button class="search-next" type="button" title="Nächster Treffer">↓</button>
  <span class="search-count" aria-live="polite">0 Treffer</span>
</div>
'''

SEARCH_JS = r'''
<script>
(() => {
  const normalise = value => value.toLocaleLowerCase('de-DE');
  const escapeRegExp = value => value.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const panel = document.querySelector('.search-panel');
  const input = panel?.querySelector('.course-search');
  const prev = panel?.querySelector('.search-prev');
  const next = panel?.querySelector('.search-next');
  const count = panel?.querySelector('.search-count');
  const content = document.querySelector('main');
  let hits = [];
  let current = -1;

  function clearHits(){
    document.querySelectorAll('mark.search-hit').forEach(mark => mark.replaceWith(document.createTextNode(mark.textContent)));
    content?.normalize(); hits=[]; current=-1;
  }
  function showCurrent(index){
    hits.forEach(hit => hit.classList.remove('current'));
    if(!hits.length){count.textContent='0 Treffer';prev.disabled=true;next.disabled=true;return;}
    current=(index+hits.length)%hits.length; hits[current].classList.add('current');
    count.textContent=`${current+1} von ${hits.length}`; prev.disabled=false; next.disabled=false;
    hits[current].scrollIntoView({behavior:'smooth',block:'center'});
  }
  function search(){
    clearHits(); const term=input.value.trim();
    if(term.length<2){count.textContent=term?'Mind. 2 Zeichen':'0 Treffer';prev.disabled=true;next.disabled=true;return;}
    const regex=new RegExp(escapeRegExp(term),'gi');
    const walker=document.createTreeWalker(content,NodeFilter.SHOW_TEXT,{acceptNode(node){
      if(!node.nodeValue.trim()||node.parentElement.closest('script,style,mark,.search-panel')) return NodeFilter.FILTER_REJECT;
      return normalise(node.nodeValue).includes(normalise(term))?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;
    }});
    const nodes=[]; while(walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node=>{
      const fragment=document.createDocumentFragment(); let last=0;
      node.nodeValue.replace(regex,(match,offset)=>{fragment.append(node.nodeValue.slice(last,offset));const mark=document.createElement('mark');mark.className='search-hit';mark.textContent=match;fragment.append(mark);last=offset+match.length;return match;});
      fragment.append(node.nodeValue.slice(last)); node.replaceWith(fragment);
    });
    hits=[...document.querySelectorAll('mark.search-hit')]; showCurrent(0);
  }
  input?.addEventListener('input',search); prev?.addEventListener('click',()=>showCurrent(current-1)); next?.addEventListener('click',()=>showCurrent(current+1));
  input?.addEventListener('keydown',event=>{if(event.key==='Enter'){event.preventDefault();showCurrent(event.shiftKey?current-1:current+1)}if(event.key==='Escape'){input.value='';search();input.blur();}});

  const platform=document.getElementById('lernplattform'); const shell=document.querySelector('.shell'); const openButton=document.getElementById('open-psychology');
  if(platform&&shell){
    shell.classList.add('course-shell-hidden');
    const openCourse=()=>{platform.classList.add('platform-hidden');shell.classList.remove('course-shell-hidden');window.scrollTo({top:0,behavior:'smooth'});};
    const openPlatform=event=>{event.preventDefault();clearHits();if(input) input.value='';shell.classList.add('course-shell-hidden');platform.classList.remove('platform-hidden');window.scrollTo({top:0,behavior:'smooth'});};
    openButton?.addEventListener('click',openCourse);
    document.querySelectorAll('[data-platform-link]').forEach(link=>link.addEventListener('click',openPlatform));
    if(location.hash&&location.hash!=='#lernplattform') openCourse();
  }
})();
</script>
'''

for path in FILES:
    text = path.read_text(encoding='utf-8')
    if 'mark.search-hit' not in text:
        text = text.replace('</style>', SEARCH_CSS + '\n</style>', 1)
    if path.name == 'index.html' and 'id="lernplattform"' not in text:
        text = text.replace('<body id="seitenanfang">', '<body id="seitenanfang">' + PLATFORM_HTML, 1)
    if 'class="search-panel"' not in text:
        marker = '<main>'
        text = text.replace(marker, SEARCH_HTML + marker, 1)
    if 'const normalise' not in text:
        text = text.replace('</body>', SEARCH_JS + '\n</body>', 1)
    path.write_text(text, encoding='utf-8')
