// usage: node bingimg.mjs <cdp_port> "query" ["query"...] — opens one new tab, runs Bing image searches, prints top results (w x h, url, page title); closes the tab.
const port=process.argv[2], queries=process.argv.slice(3);
const tab=await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`,{method:'PUT'})).json();
const ws=new WebSocket(tab.webSocketDebuggerUrl); await new Promise(r=>ws.onopen=r);
let id=0; const pending={};
ws.onmessage=e=>{const m=JSON.parse(e.data); if(m.id&&pending[m.id]){pending[m.id](m);delete pending[m.id];}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pending[i]=r;ws.send(JSON.stringify({id:i,method,params}));});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
try{
  for(const q of queries){
    await send('Page.navigate',{url:'https://www.bing.com/images/search?q='+encodeURIComponent(q)});
    await sleep(4000);
    const r=await send('Runtime.evaluate',{returnByValue:true,expression:`[...document.querySelectorAll('a.iusc')].slice(0,15).map(a=>{try{const m=JSON.parse(a.getAttribute('m'));const info=a.closest('li')?.querySelector('.img_info span')?.textContent||'';return {u:m.murl,t:m.t,size:info}}catch(e){return null}}).filter(Boolean)`});
    console.log('### '+q); for(const x of (r.result.result.value||[])) console.log(x.size.padEnd(14),x.u,'|',x.t);
  }
} finally { await fetch(`http://127.0.0.1:${port}/json/close/${tab.id}`); ws.close(); }
