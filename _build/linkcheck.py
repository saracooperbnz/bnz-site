#!/usr/bin/env python3
"""Quick internal-link checker over the built HTML: every href/src starting with / must resolve
to a file or dir/index.html, and every #fragment on an internal page link must exist as an id.
Usage: python3 _build/linkcheck.py  → exit 1 on any broken link."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def target(url):
    p = os.path.join(ROOT, url.lstrip("/"))
    for c in (p, os.path.join(p, "index.html")):
        if os.path.isfile(c): return c
bad = n = 0
for dp, _, fs in os.walk(ROOT):
    if "/.git" in dp or "/_build" in dp: continue
    for f in fs:
        if not f.endswith(".html"): continue
        src = os.path.join(dp, f); html = open(src, encoding="utf-8").read()
        for href in re.findall(r'(?:href|src)="(/[^"]*)"', html):
            if href.startswith("//"): continue
            n += 1; url, _, frag = href.split("?")[0].partition("#")
            t = target(url) if url else src
            if not t: bad += 1; print("BROKEN", os.path.relpath(src, ROOT), "->", href); continue
            if frag and t.endswith(".html") and not re.search(r'id="%s"' % re.escape(frag), open(t, encoding="utf-8").read()):
                bad += 1; print("BAD ANCHOR", os.path.relpath(src, ROOT), "->", href)
print("%d internal links checked, %d broken" % (n, bad)); sys.exit(1 if bad else 0)
