#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate every BuildWithBNZ page from _build/content_*.py.
Usage (from the repo root):  python3 _build/build.py
Then:                        python3 _build/check.py
The legacy BNZ Builders contractor pages (/about /services /public-works /credentials
/careers /subcontract /work /capability-statement) are NOT generated here and are left as they are."""
import os, sys, datetime, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from shared import SITE, UPDATED
import content_home, content_pages, content_landers, content_articles, content_blog

def write(path, html):
    full = os.path.join(ROOT, path.lstrip('/'))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    return path

PAGES = {
    "/index.html": content_home.page_home,
    "/solutions/index.html": content_pages.page_solutions,
    "/crew/index.html": content_pages.page_crew,
    "/sara/index.html": lambda: content_pages.page_agent("sara"),
    "/taylor/index.html": lambda: content_pages.page_agent("taylor"),
    "/emma/index.html": lambda: content_pages.page_agent("emma"),
    "/how-it-works/index.html": content_pages.page_how,
    "/what-we-connect-to/index.html": content_pages.page_connect,
    "/faq/index.html": content_pages.page_faq,
    "/book/index.html": content_pages.page_book,
    "/thanks/index.html": content_pages.page_thanks,
    "/login/index.html": lambda: content_pages.page_redirect("/", "Moved — BuildWithBNZ"),
    "/privacy/index.html": content_pages.page_privacy,
    "/terms/index.html": content_pages.page_terms,
    "/contact/index.html": content_pages.page_contact,
    "/404.html": content_pages.page_404,
    "/architecture/index.html": lambda: content_pages.page_redirect("/how-it-works/", "Moved — How it works"),
}
for L in content_landers.LANDERS:
    PAGES["/%s/index.html" % L["slug"]] = (lambda L=L: content_landers.page_lander(L))

for _n, _e, _w in content_articles.ARTICLES:
    PAGES[content_articles.load(_n)[0]["url_slug"] + "index.html"] = (lambda n=_n, e=_e, w=_w: content_articles.page_article(n, e, w)[1])

PAGES["/blog/index.html"] = lambda: content_blog.page_index()[1]
for _n, _e, _w in content_blog.POSTS:
    PAGES["/blog/%s/index.html" % _n] = (lambda n=_n, e=_e, w=_w: content_blog.post(n, e, w)[1])

# URLs that go in the sitemap: generated public pages + the untouched legacy pages
SITEMAP_EXTRA = ["/about/", "/services/", "/public-works/", "/credentials/", "/careers/", "/subcontract/", "/work/", "/capability-statement/"]
NOINDEX = {"/thanks/index.html", "/login/index.html", "/404.html", "/architecture/index.html"}

def lastmod(path):
    """Date the built file last changed: its last commit date, or today if it differs from HEAD."""
    rel = path.lstrip('/')
    try:
        dirty = subprocess.run(["git", "status", "--porcelain", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if not dirty:
            d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
            if d: return d
    except OSError:
        pass
    return datetime.date.today().isoformat() if dirty else UPDATED

def main():
    written = []
    for path, fn in PAGES.items():
        written.append(write(path, fn()))
    gen = []
    for path in PAGES:
        if path in NOINDEX: continue
        gen.append((path.replace("index.html", ""), lastmod(path)))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    # software pages: no <priority> (Google ignores it), lastmod = when the page last really changed
    for u, lm in gen:
        sm.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (SITE, u, lm))
    # legacy BNZ Builders INC pages: left exactly as before (owner decision pending)
    for u in SITEMAP_EXTRA:
        sm.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>0.4</priority></url>' % (SITE, u, UPDATED))
    sm.append('</urlset>\n')
    write("/sitemap.xml", '\n'.join(sm))
    write("/robots.txt", "User-agent: *\nAllow: /\nDisallow: /thanks/\n\nSitemap: %s/sitemap.xml\n" % SITE)
    print("wrote %d pages + sitemap.xml + robots.txt" % len(written))

if __name__ == "__main__":
    main()
