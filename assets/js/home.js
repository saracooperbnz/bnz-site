/* BuildWithBNZ home page (/) only. Words blur in, the hero question types itself, the four steps pin on desktop,
   the crew line-up tilts flat, the nav turns solid, the phone action bar slides up, loops pause off screen.
   bnz.js does the rest (entrances, row reveals, burger and drawer). Reduced motion: final frame, nothing moves. */
(function () {
  'use strict';
  var d = document, w = window;
  var RM = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var big = w.matchMedia('(min-width:1024px)');
  var IO = 'IntersectionObserver' in w;
  function $(s, r) { return (r || d).querySelector(s); }
  function all(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function watch(el, fn, th) {
    if (!el || !IO) return;
    new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting, e); }); }, { threshold: th || 0 }).observe(el);
  }

  /* words blur in: desktop only (the H1 at load, the crew heading in view) */
  if (!RM && big.matches && IO) all('.blurin').forEach(function (el) {
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

  /* hero: the question types itself (1.6 s at most), then the answers and the yes-card arrive */
  var vis = $('.h-vis'), q = vis && $('.q', vis);
  if (q && !RM) {
    var full = q.textContent, gap = Math.min(40, 1600 / full.length), k = 0;
    q.innerHTML = '<span class="t"></span><span class="r" aria-hidden="true"></span>';
    var t = q.firstChild, r = q.lastChild;
    r.textContent = full;
    vis.classList.add('anim');
    setTimeout(function tick() {
      k++; t.textContent = full.slice(0, k); r.textContent = full.slice(k);
      if (k < full.length) return setTimeout(tick, gap);
      q.textContent = full; vis.classList.remove('anim'); vis.classList.add('play');
    }, 600);
  }

  /* how it works: pinned on desktop, one step per stretch of scrolling; stacked everywhere else */
  var how = $('#how'), steps = how ? all('.st', how) : [], dots = how ? all('.dots button', how) : [], cur = 0;
  function show(i) {
    if (i === cur) return; cur = i;
    steps.forEach(function (s, j) { s.classList.toggle('on', j === i); s.classList.toggle('past', j < i); });
    dots.forEach(function (b, j) { b.classList.toggle('on', j === i); if (j === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); });
  }
  function navH() { return $('.hnav') ? $('.hnav').offsetHeight : 72; }
  function range() { return how.offsetHeight - (w.innerHeight - navH()); }
  function layout() { if (how) how.classList.toggle('pinned', big.matches && !RM); }
  dots.forEach(function (b, i) {
    b.addEventListener('click', function () {
      var top = how.getBoundingClientRect().top + w.pageYOffset - navH();
      w.scrollTo({ top: top + (i + 0.5) / 4 * range(), behavior: 'smooth' });
    });
  });
  layout();
  if (big.addEventListener) big.addEventListener('change', function () { layout(); frame(); });

  /* one scroll handler, once per frame: solid nav, the pinned step, the crew tilt */
  var nav = $('.hnav'), lu = $('.lineup'), busy = false;
  function frame() {
    busy = false;
    var vh = w.innerHeight;
    if (nav) nav.classList.toggle('solid', w.pageYOffset > 8);
    if (how && how.classList.contains('pinned')) {
      var p = (navH() - how.getBoundingClientRect().top) / range();
      show(Math.max(0, Math.min(3, Math.floor(p * 4))));
    }
    if (lu) {
      var on = big.matches && !RM;
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
  w.addEventListener('resize', onScroll);
  frame();

  /* phone action bar: up once the hero's Start here has scrolled away, down again over the final call to action */
  var bar = $('.actbar'), hs = $('#hero-start'), past = false, inCta = false;
  function upd() { if (bar) bar.classList.toggle('show', past && !inCta); }
  watch(hs, function (v, e) { past = !v && e.boundingClientRect.top < 0; upd(); });
  watch($('.h-cta'), function (v) { inCta = v; upd(); });

  /* loops (the aurora, Kyle's before/concept) pause off screen */
  all('.h-cta, .kyle-v').forEach(function (el) { watch(el, function (v) { el.classList.toggle('off', !v); }); });
})();
