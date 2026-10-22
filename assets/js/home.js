/* BuildWithBNZ home page (/) only. The hero windows tilt up into place and the question types itself, words blur in,
   the four steps pin on desktop, the crew line-up tilts flat, the nav turns to glass, the phone action bar slides up,
   loops pause off screen. bnz.js does the rest (entrances, row reveals, burger and drawer).
   Motion runs only under html.js-motion (set in <head>); reduced motion or JS off: the final frame, nothing moves. */
(function () {
  'use strict';
  var d = document, w = window;
  var root = d.documentElement; w.__rv = 1;
  var MO = root.classList.contains('js-motion') && !root.classList.contains('rv-all');
  var big = w.matchMedia('(min-width:1024px)');
  var IO = 'IntersectionObserver' in w;
  function $(s, r) { return (r || d).querySelector(s); }
  function all(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function watch(el, fn, th) {
    if (!el || !IO) return;
    new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting, e); }); }, { threshold: th || 0 }).observe(el);
  }

  /* words blur in: desktop only (the crew heading, once in view) */
  if (MO && big.matches && IO) all('.blurin').forEach(function (el) {
    var n = 0;
    [].slice.call(el.childNodes).forEach(function (node) {
      if (node.nodeType !== 3) return;
      var f = d.createDocumentFragment();
      node.textContent.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { f.appendChild(d.createTextNode(part)); return; }
        var s = d.createElement('span'); s.className = 'w'; s.style.setProperty('--i', n++); s.textContent = part; f.appendChild(s);
      });
      el.replaceChild(f, node);
    });
    watch(el, function (v) { if (v) el.classList.add('go'); }, 0.2);
  });

  /* hero: the windows tilt up once the fonts are in (600 ms at most); 700 ms later the question types itself
     (1.6 s at most), then the answers and their labels arrive */
  var vis = $('.h-vis'), q = vis && $('.q', vis), hero = $('.h-hero'), full, t, r;
  function typeIt() {
    var gap = Math.min(40, 1600 / full.length), k = 0;
    (function tick() {
      k++; t.textContent = full.slice(0, k); r.textContent = full.slice(k);
      if (k < full.length) return setTimeout(tick, gap);
      q.textContent = full; vis.classList.remove('anim'); vis.classList.add('play');
    })();
  }
  if (vis && MO) {
    if (q) {
      full = q.textContent;
      q.innerHTML = '<span class="t"></span><span class="r" aria-hidden="true"></span>';
      t = q.firstChild; r = q.lastChild; r.textContent = full;
      vis.classList.add('anim');
    }
    var went = false;
    var go = function () { if (went) return; went = true; requestAnimationFrame(function () { vis.classList.add('up'); if (q) setTimeout(typeIt, 700); }); };
    if (d.fonts && d.fonts.ready) d.fonts.ready.then(go);
    setTimeout(go, 600);
  }
  watch(hero, function (v) { hero.classList.toggle('off', !v); });

  /* how it works: pinned on desktop, one step per stretch of scrolling; stacked everywhere else */
  var how = $('#how'), steps = how ? all('.st', how) : [], dots = how ? all('.dots button', how) : [], cur = 0;
  function show(i) {
    if (i === cur) return; cur = i;
    steps.forEach(function (s, j) { s.classList.toggle('on', j === i); s.classList.toggle('past', j < i); });
    dots.forEach(function (b, j) { b.classList.toggle('on', j === i); if (j === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); });
  }
  function navH() { return $('.hnav') ? $('.hnav').offsetHeight : 72; }
  function range() { return how.offsetHeight - (w.innerHeight - navH()); }
  function layout() { if (how) how.classList.toggle('pinned', big.matches && MO); }
  dots.forEach(function (b, i) {
    b.addEventListener('click', function () {
      var top = how.getBoundingClientRect().top + w.pageYOffset - navH();
      w.scrollTo({ top: top + (i + 0.5) / 4 * range(), behavior: 'smooth' });
    });
  });
  layout();
  if (big.addEventListener) big.addEventListener('change', function () { layout(); frame(); });

  /* one scroll handler, once per frame: glass nav, the front window's parallax, the pinned step, the crew tilt */
  var nav = $('.hnav'), lu = $('.lineup'), busy = false, heroH = 0;
  function measure() { heroH = hero ? hero.offsetHeight : 0; }
  measure(); w.addEventListener('load', measure); if (d.fonts && d.fonts.ready) d.fonts.ready.then(measure);
  function frame() {
    busy = false;
    var vh = w.innerHeight;
    if (nav) nav.classList.toggle('solid', w.pageYOffset > 8);
    if (MO && big.matches && vis) { var y = w.pageYOffset; if (y < heroH + 200) vis.style.setProperty('--py', (-Math.min(y, heroH) * 0.08).toFixed(1) + 'px'); }
    if (how && how.classList.contains('pinned')) {
      var p = (navH() - how.getBoundingClientRect().top) / range();
      show(Math.max(0, Math.min(3, Math.floor(p * 4))));
    }
    if (lu) {
      var on = big.matches && MO;
      lu.classList.toggle('tilt', on);
      if (on) {
        var f = Math.max(0, Math.min(1, (1 - lu.getBoundingClientRect().top / vh) / 0.55));
        lu.style.setProperty('--tilt', (24 * (1 - f)).toFixed(2) + 'deg');
        lu.style.setProperty('--op', (0.4 + 0.6 * f).toFixed(3));
      }
    }
  }
  function onScroll() { if (!busy) { busy = true; requestAnimationFrame(frame); } }
  w.addEventListener('scroll', onScroll, { passive: true });
  w.addEventListener('resize', function () { measure(); onScroll(); });
  frame();

  /* phone action bar: up once the hero's Start here has scrolled away, down again over the final call to action */
  var bar = $('.actbar'), hs = $('#hero-start'), past = false, inCta = false;
  function upd() { if (bar) bar.classList.toggle('show', past && !inCta); }
  watch(hs, function (v, e) { past = !v && e.boundingClientRect.top < 0; upd(); });
  watch($('.h-cta'), function (v) { inCta = v; upd(); });

  /* loops (the aurora, Kyle's before/concept) pause off screen */
  all('.h-cta, .kyle-v').forEach(function (el) { watch(el, function (v) { el.classList.toggle('off', !v); }); });
})();
