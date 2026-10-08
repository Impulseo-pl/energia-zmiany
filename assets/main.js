(function(){
  var root=document.documentElement, body=document.body;

  // nawigacja mobilna
  var burger=document.querySelector('.burger');
  if(burger){
    burger.addEventListener('click',function(){
      var open=body.classList.toggle('nav-open');
      burger.setAttribute('aria-expanded',open?'true':'false');
    });
    document.addEventListener('click',function(e){
      if(body.classList.contains('nav-open') && !e.target.closest('.nav') && !e.target.closest('.burger')){
        body.classList.remove('nav-open');burger.setAttribute('aria-expanded','false');
      }
    });
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'){body.classList.remove('nav-open');burger.setAttribute('aria-expanded','false');}
    });
  }

  // cień nagłówka po przewinięciu
  var header=document.querySelector('.header');
  function onScroll(){ if(header) header.classList.toggle('scrolled',window.scrollY>8); }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

  // reveal
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } });
    },{rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(function(el){ el.classList.add('in'); }); }

  // filtry wpisów
  var filters=document.querySelector('.filters');
  if(filters){
    filters.addEventListener('click',function(e){
      var b=e.target.closest('button'); if(!b) return;
      filters.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b);});
      var cat=b.dataset.cat;
      document.querySelectorAll('.post[data-cat]').forEach(function(p){
        p.hidden = !(cat==='all' || p.dataset.cat===cat);
      });
    });
  }

  // formularz (demo — wysyłka podłączana przy wdrożeniu)
  document.querySelectorAll('form.js-demo').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var m=f.querySelector('.form-msg'); if(m) m.classList.add('show');
    });
  });

  var y=document.querySelector('[data-year]'); if(y) y.textContent=new Date().getFullYear();
})();
