(() => {
  const input=document.querySelector('.course-search');
  const prev=document.querySelector('.search-prev');
  const next=document.querySelector('.search-next');
  const count=document.querySelector('.search-count');
  const content=document.querySelector('main');
  let hits=[],current=-1;
  const escapeRegExp=value=>value.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  function clear(){document.querySelectorAll('mark.search-hit').forEach(mark=>mark.replaceWith(document.createTextNode(mark.textContent)));content?.normalize();hits=[];current=-1}
  function show(index){hits.forEach(hit=>hit.classList.remove('current'));if(!hits.length){count.textContent='0 Treffer';prev.disabled=true;next.disabled=true;return}current=(index+hits.length)%hits.length;hits[current].classList.add('current');count.textContent=`${current+1} von ${hits.length}`;prev.disabled=false;next.disabled=false;hits[current].scrollIntoView({behavior:'smooth',block:'center'})}
  function search(){clear();const term=input.value.trim();if(term.length<2){count.textContent=term?'Mind. 2 Zeichen':'0 Treffer';prev.disabled=true;next.disabled=true;return}const regex=new RegExp(escapeRegExp(term),'gi');const walker=document.createTreeWalker(content,NodeFilter.SHOW_TEXT,{acceptNode(node){if(!node.nodeValue.trim()||node.parentElement.closest('script,style,mark'))return NodeFilter.FILTER_REJECT;return node.nodeValue.toLocaleLowerCase('de-DE').includes(term.toLocaleLowerCase('de-DE'))?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT}});const nodes=[];while(walker.nextNode())nodes.push(walker.currentNode);nodes.forEach(node=>{const fragment=document.createDocumentFragment();let last=0;node.nodeValue.replace(regex,(match,offset)=>{fragment.append(node.nodeValue.slice(last,offset));const mark=document.createElement('mark');mark.className='search-hit';mark.textContent=match;fragment.append(mark);last=offset+match.length;return match});fragment.append(node.nodeValue.slice(last));node.replaceWith(fragment)});hits=[...document.querySelectorAll('mark.search-hit')];show(0)}
  input?.addEventListener('input',search);prev?.addEventListener('click',()=>show(current-1));next?.addEventListener('click',()=>show(current+1));input?.addEventListener('keydown',event=>{if(event.key==='Enter'){event.preventDefault();show(event.shiftKey?current-1:current+1)}if(event.key==='Escape'){input.value='';search();input.blur()}});
})();
