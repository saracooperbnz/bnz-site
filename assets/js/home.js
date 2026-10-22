/* BuildWithBNZ home page (/) only. Motion runs only under html.js-motion (set in <head>): reduced motion or JS off
   shows the final frame and nothing moves. Here: reveals, words rising out of a blur, the hero entrance, the four steps
   pinned with one continuous handover (desktop), the crew line-up unveiling in 3D (desktop), the closing call revealed
   like a curtain (desktop), the glass nav, the phone action bar. Loops pause off screen. bnz.js runs the drawer. */
(function () {
  'use strict';
  var d = document, w = window;
  var root = d.documentElement; w.__rv = 1;
  var MO = root.classList.contains('js-motion') && !root.classList.contains('rv-all');
  var big = w.matchMedia('(min-width:1024px)');
  var IO = 'IntersectionObserver' in w;
  function $(s, r) { return (r || d).querySelector(s); }
  function all(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function watch(el, fn, th, rm) {
    if (!el || !IO) return;
    new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting, e); }); }, { threshold: th || 0, rootMargin: rm || '0px' }).observe(el);
  }
  function once(el, fn, th, rm) {
    if (!el) return;
    if (!IO) return fn();
    var o = new IntersectionObserver(function (es) { if (es.some(function (e) { return e.isIntersecting; })) { o.disconnect(); fn(); } }, { threshold: th || 0, rootMargin: rm || '0px' });
    o.observe(el);
  }
  var nav = $('.hnav'), hero = $('.h-hero'), vis = $('.h-vis'), how = $('#how'), lu = $('.lineup'), luStage = $('.lu-stage'),
      faq = $('.h-faq'), cta = $('.h-cta'), ctaH = $('#cta-h'), main = $('main');

  /* words: each word rises out of a blur once the heading passes 82% of the screen (the <span> in a heading keeps its words) */
  if (MO && IO) all('.blurin').forEach(function (el) {
    var n = 0;
    el.setAttribute('aria-label', el.textContent.replace(/\s+/g, ' ').trim());
    (function split(p) {
      [].slice.call(p.childNodes).forEach(function (node) {
        if (node.nodeType === 1) return split(node);
        if (node.nodeType !== 3) return;
        var f = d.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { f.appendChild(d.createTextNode(part)); return; }
          var s = d.createElement('span'); s.className = 'w'; s.setAttribute('aria-hidden', 'true');
          s.style.setProperty('--i', Math.min(n++, 14)); s.textContent = part; f.appendChild(s);
        });
        p.replaceChild(f, node);
      });
    })(el);
    // the closing heading waits under the questions on desktop, so the curtain starts it (see ctaFrame)
    once(el, function () { if (el !== ctaH || !curtain) el.classList.add('go'); else ctaWait = true; }, 0, '0px 0px -18% 0px');
  });

  /* hero: the windows tilt up once the fonts are in (600 ms at most); 700 ms later the question types itself */
  var q = vis && $('.q', vis), full, t, r;
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

  /* reveals: one observer; items arriving together are staggered top to bottom, left to right */
  all('.rv-s').forEach(function (m) { [].forEach.call(m.children, function (c, k) { c.style.setProperty('--i', k); }); });
  var rio = MO && IO ? new IntersectionObserver(function (es) {
    var hit = es.filter(function (e) { return e.isIntersecting; });
    hit.sort(function (a, b) { return (a.boundingClientRect.top - b.boundingClientRect.top) || (a.boundingClientRect.left - b.boundingClientRect.left); });
    hit.forEach(function (e, k) { e.target.style.setProperty('--rd', Math.min(k, 6) * 70 + 'ms'); e.target.classList.add('in'); rio.unobserve(e.target); });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0 }) : null;
  function inNow(el) { el.classList.add('in'); if (rio) rio.unobserve(el); }

  /* how it works: on desktop the four steps share one pinned stage and hand over continuously */
  var steps = how ? all('.st', how) : [], txt = steps.map(function (s) { return $('.st-txt', s); }),
      svis = steps.map(function (s) { return $('.st-vis', s); }), dots = how ? all('.dots button', how) : [],
      bars = dots.map(function (b) { return $('b', b); }), pinned = false, cur = -1, T = 0.22;
  function ss(x) { x = clamp(x); return x * x * (3 - 2 * x); }
  function wgt(f, i, n, fr) { var a = i === 0 ? 1 : ss((f - (i - T * fr)) / (T * fr)); var b = i === n - 1 ? 1 : 1 - ss((f - (i + 1 - T)) / (T * fr)); return a * b; }
  function hide(el, h) {
    if (el._h === h) return; el._h = h;
    el.style.visibility = h ? 'hidden' : '';
    if (h) el.setAttribute('aria-hidden', 'true'); else el.removeAttribute('aria-hidden');
  }
  function stepFrame(y, vh) {
    var range = M.howH - (vh - M.navH); if (range <= 0) return;
    var f = clamp((y + M.navH - M.howTop) / range) * 4, best = 0, bw = -1;
    steps.forEach(function (s, i) {
      var wc = wgt(f, i, 4, 0.45), wp = wgt(f, i, 4, 0.62), yy = (f < i ? 1 : -0.72) * (1 - wc) * 14, a = txt[i], v = svis[i];
      a.style.opacity = wc.toFixed(3); a.style.transform = 'translate3d(0,' + yy.toFixed(1) + 'px,0)';
      v.style.opacity = wp.toFixed(3); v.style.transform = 'scale(' + (1 - (1 - wp) * 0.028).toFixed(4) + ')';
      a.style.pointerEvents = wc < 0.5 ? 'none' : ''; v.style.pointerEvents = wp < 0.5 ? 'none' : '';
      hide(a, wc < 0.01); hide(v, wp < 0.01);
      s.classList.toggle('on', wc >= 0.01 || wp >= 0.01);
      if (wp > 0.6) v.classList.add('play'); else if (wp < 0.05) v.classList.remove('play');
      if (bars[i]) bars[i].style.transform = 'scaleX(' + clamp(f - i).toFixed(3) + ')';
      if (wc > bw) { bw = wc; best = i; }
    });
    if (best !== cur) { cur = best; dots.forEach(function (b, j) { if (j === cur) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); }); }
  }
  dots.forEach(function (b, i) {
    b.addEventListener('click', function () {
      measure();
      w.scrollTo({ top: M.howTop - M.navH + (i + 0.5) / 4 * (M.howH - (w.innerHeight - M.navH)), behavior: 'smooth' });
    });
  });
  // below 1024px each step plays once, when its picture is 40% on screen
  if (MO) svis.forEach(function (v) { once(v, function () { if (!pinned) v.classList.add('play'); }, 0.4); });

  /* the crew line-up: tilted back and assembled in layers as it scrolls in, flat once its top passes 35% (desktop) */
  var layers = [], ld = -1, luLast = -1, unveil = false;
  if (lu) {
    layers.push({ el: $('.lu-sara', lu), z: 260, th: 0.10 });
    all('.lu-label', lu).forEach(function (el) { layers.push({ el: el, z: 220, th: 0.16 }); });
    all('.lu-g li', lu).forEach(function (el, i) { layers.push({ el: el, z: 320, th: 0.30 + i * 0.05 }); });
  }
  function eo(k) { return 1 - Math.pow(1 - k, 3); }
  function luFrame(y, vh) {
    var u = clamp((vh * 0.95 - (M.luTop - y)) / (vh * 0.6));
    if (ld < 0) ld = u; else { ld += (u - ld) * 0.085; if (Math.abs(u - ld) < 0.0005) ld = u; }
    if (ld === luLast) return false;
    luLast = ld;
    var D = clamp(ld / 0.92), O = D < 0.5 ? 4 * D * D * D : 1 - Math.pow(-2 * D + 2, 3) / 2;
    if (O > 0.9999) { lu.style.transform = ''; lu.style.willChange = ''; }
    else { lu.style.transform = 'rotateX(' + ((1 - O) * 44).toFixed(2) + 'deg) scale(' + (0.86 + 0.14 * O).toFixed(4) + ')'; lu.style.willChange = 'transform'; }
    layers.forEach(function (L) {
      var n = eo(clamp((ld - L.th) / 0.22)), s = L.el.style;
      s.opacity = n.toFixed(3);
      s.transform = n > 0.999 ? '' : 'translate3d(0,' + ((1 - n) * -24).toFixed(1) + 'px,' + ((1 - n) * L.z).toFixed(0) + 'px)';
      s.filter = n > 0.995 ? '' : 'blur(' + ((1 - n) * 14).toFixed(1) + 'px)';
    });
    return ld !== u;
  }

  /* the closing call waits under the questions and is uncovered as they scroll away (desktop) */
  var curtain = false, fpS = -1, fpL = '', ctaWait = false, ctaVis = false;
  function ctaFrame(y, vh) {
    var fp = clamp((vh - (M.faqBottom - y)) / Math.min(M.ctaH, vh));
    if (fpS < 0) fpS = fp; else { fpS += (fp - fpS) * 0.12; if (Math.abs(fp - fpS) < 0.001) fpS = fp; }
    var v = fpS.toFixed(3); if (v !== fpL) { fpL = v; cta.style.setProperty('--fp', v); }
    cta.classList.toggle('off', fpS < 0.02);
    if (ctaWait && fpS > 0.3) { ctaWait = false; ctaH.classList.add('go'); }
    return fpS !== fp;
  }

  /* modes: pinned steps, the unveil and the curtain run on desktop with motion; everything else is plain flow */
  function modes() {
    var on = big.matches && MO;
    if (how && on !== pinned) {
      pinned = on; how.classList.toggle('pinned', on);
      if (!on) {
        txt.concat(svis).forEach(function (el) { el.style.opacity = el.style.transform = el.style.pointerEvents = ''; hide(el, false); });
        bars.forEach(function (b) { b.style.transform = ''; });
      }
      all('.rv', how).forEach(inNow);
    }
    if (lu && on !== unveil) {
      unveil = on; lu.classList.toggle('unveil', on); ld = luLast = -1;
      if (on) inNow(lu);
      else {
        lu.style.transform = lu.style.willChange = '';
        layers.forEach(function (L) { L.el.style.opacity = L.el.style.transform = L.el.style.filter = ''; });
      }
    }
    var c = on && !!cta && !!faq;
    if (c !== curtain) {
      curtain = c; fpS = -1; fpL = '';
      if (!c && cta) { cta.style.removeProperty('--fp'); cta.classList.toggle('off', !ctaVis); if (ctaWait) { ctaWait = false; ctaH.classList.add('go'); } }
    }
  }
  modes();
  all('.rv, .rv-s').forEach(function (el) { if (el.classList.contains('in')) return; if (rio) rio.observe(el); else el.classList.add('in'); });

  /* one scroll handler, once per frame; layout is read only in measure() */
  var busy = false, M = { navH: 72, heroH: 0, howTop: 0, howH: 0, luTop: 0, faqBottom: 0, ctaH: 0 };
  function top(el) { return el.getBoundingClientRect().top + w.pageYOffset; }
  function measure() {
    M.navH = nav ? nav.offsetHeight : 72;
    M.heroH = hero ? hero.offsetHeight : 0;
    if (how) { M.howTop = top(how); M.howH = how.offsetHeight; }
    if (luStage) M.luTop = top(luStage);
    if (faq) M.faqBottom = top(faq) + faq.offsetHeight;
    if (cta) M.ctaH = cta.offsetHeight;
  }
  function frame() {
    busy = false;
    var y = w.pageYOffset, vh = w.innerHeight, more = false;
    if (nav) nav.classList.toggle('solid', y > 8);
    if (MO && big.matches && vis && y < M.heroH + 200) vis.style.setProperty('--py', (-Math.min(y, M.heroH) * 0.08).toFixed(1) + 'px');
    if (pinned) stepFrame(y, vh);
    if (unveil && luFrame(y, vh)) more = true;
    if (curtain && ctaFrame(y, vh)) more = true;
    if (more) onScroll();
  }
  function onScroll() { if (!busy) { busy = true; requestAnimationFrame(frame); } }
  function refresh() { modes(); measure(); onScroll(); }
  var rz = false;
  w.addEventListener('scroll', onScroll, { passive: true });
  w.addEventListener('resize', function () { if (rz) return; rz = true; requestAnimationFrame(function () { rz = false; refresh(); }); });
  w.addEventListener('load', refresh);
  if (d.fonts && d.fonts.ready) d.fonts.ready.then(refresh);
  if (big.addEventListener) big.addEventListener('change', refresh);
  if (w.ResizeObserver && main) new ResizeObserver(function () { measure(); onScroll(); }).observe(main);
  measure(); frame();

  /* bento: a soft light follows a fine pointer */
  var bento = $('.bento'), pe = null, pq = false;
  if (bento && w.matchMedia('(hover:hover) and (pointer:fine)').matches) bento.addEventListener('pointermove', function (e) {
    pe = e; if (pq) return; pq = true;
    requestAnimationFrame(function () {
      pq = false;
      var c = pe.target.closest && pe.target.closest('.bc'); if (!c) return;
      var b = c.getBoundingClientRect();
      c.style.setProperty('--mx', Math.round(pe.clientX - b.left) + 'px'); c.style.setProperty('--my', Math.round(pe.clientY - b.top) + 'px');
    });
  }, { passive: true });

  /* phone action bar: up once the hero's Start here has scrolled away, down again over the closing call */
  var bar = $('.actbar'), hs = $('#hero-start'), past = false, inCta = false;
  function upd() { if (bar) bar.classList.toggle('show', past && !inCta); }
  watch(hs, function (v, e) { past = !v && e.boundingClientRect.top < 0; upd(); });
  watch(cta, function (v) { inCta = ctaVis = v; upd(); if (!curtain) cta.classList.toggle('off', !v); });

  /* loops pause off screen (the hero's light and dot above, the closing sky in ctaFrame) */
  all('.kyle-v').forEach(function (el) { watch(el, function (v) { el.classList.toggle('off', !v); }); });
})();
