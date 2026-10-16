#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the /blog/ index and posts from _build/blog/*.md using the shared site template.
Usage (from the repo root): python3 _build/build_blog.py
Does not touch any other page. Internal links are limited to pages that exist on the site;
anything else is turned into plain text. Editorial notes ([VERIFY: ...], [OWNER DATA NEEDED: ...]) are not rendered."""
import os, re, sys, json, glob
import markdown
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from shared import SITE, BRAND, head, nav, footer, section, btn_book, esc

PUBLISHED = "2026-10-16"
ALLOWED_PREFIX = ("/book/", "/sara/", "/taylor/", "/emma/", "/faq/", "/crew/", "/how-it-works/", "/solutions/", "/what-we-connect-to/", "/blog/")
META = {  # descriptions trimmed to <=155 chars
 "best-ai-estimating-software-for-general-contractors": "A fair roundup of AI estimating and takeoff software for US general contractors: what each tool does, published prices with sources, and who it fits.",
 "buildingconnected-pricing": "BuildingConnected doesn't publish prices. What Autodesk says, what third-party listings report, what Pro and Bid Board Pro include, and other options.",
 "construction-estimating-software-for-small-business": "Estimating software for small construction businesses: free options, what to check before you buy, and when to get help instead of another tool.",
 "downtobid-pricing": "Downtobid pricing for GCs and subs (Oct 2026), what it does well, its limits, and when a different setup fits better. Sources linked.",
 "planswift-vs-bluebeam": "PlanSwift vs Bluebeam Revu for construction takeoff: what each does well, their limits, and which fits your team. Sources linked.",
 "togal-ai-review": "A Togal.AI review for US contractors: the published price, where the AI takeoff works well, where it falls short, and when another tool fits better.",
}
STYLE = ('<style>.post table{width:100%;border-collapse:collapse;margin:18px 0;font-size:15px}.post th,.post td{border:1px solid rgba(255,255,255,.15);'
         'padding:8px 10px;text-align:left;vertical-align:top}.post .tbl{overflow-x:auto}.post ol{padding-left:22px}.post a:not(.btn){text-decoration:underline}'
         '.post-list{list-style:none;padding:0}.post-list li{margin:0 0 22px}.post-list a{font-size:20px;font-weight:600}</style>')
unlinked = []

def ok(url):
    if url == "/": return True
    return url.startswith(ALLOWED_PREFIX)

def fix_links(slug, md):
    def rep(m):
        text, url = m.group(1), m.group(2)
        if url.startswith("/") and not ok(url.split("#")[0]):
            unlinked.append((slug, url, text))
            return '[Project Review](/book/)' if text.strip() == url else text
        return m.group(0)
    return re.sub(r'(?<!\!)\[([^\]]+)\]\((/[^)\s]*)\)', rep, md)

def parse(path):
    raw = open(path, encoding="utf-8").read()
    _, fm, body = raw.split("---", 2)
    title = re.search(r'^title_tag: "(.*)"', fm, re.M).group(1)
    desc = re.search(r'^meta_description: "(.*)"', fm, re.M).group(1)
    slug = re.search(r'^url_slug: (\S+)', fm, re.M).group(1).strip("/").split("/")[-1]
    desc = META.get(slug, desc); assert len(desc) <= 155, (slug, len(desc))
    faq = None
    m = re.search(r'```json\s*(\{.*?\})\s*```', body, re.S)
    if m: faq = json.loads(m.group(1)); body = body[:m.start()] + body[m.end():]
    # drop editorial notes (whole lines and inline)
    body = re.sub(r'^\s*\[(VERIFY|OWNER DATA NEEDED)[^\]]*\]\s*$\n?', '', body, flags=re.M)
    body = re.sub(r'\s*\[(VERIFY|OWNER DATA NEEDED)[^\]]*\]', '', body)
    h1 = re.search(r'^# (.+)$', body, re.M).group(1).strip()
    body = re.sub(r'^# .+$\n?', '', body, count=1, flags=re.M)
    body = fix_links(slug, body)
    return dict(title=title, desc=desc, slug=slug, faq=faq, h1=h1, body=body)

def render(p):
    url = "/blog/%s/" % p["slug"]
    html = markdown.markdown(p["body"], extensions=["tables", "sane_lists"])
    html = html.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', html)
    has_book = 'href="/book/"' in html
    article = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"][:110], "description": p["desc"],
               "datePublished": PUBLISHED, "dateModified": PUBLISHED, "mainEntityOfPage": SITE + url, "image": SITE + "/og.png",
               "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
               "publisher": {"@type": "Organization", "name": BRAND, "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/og.png"}}}
    ld = [article] + ([p["faq"]] if p["faq"] else [])
    h = head(p["title"], p["desc"], url, jsonld=json.dumps(ld, ensure_ascii=False).replace("</", "<\\/"))
    h = h.replace("</head>", STYLE + "</head>")
    h += nav()
    cta = ('<div class="fx" style="margin-top:40px;padding-top:24px;border-top:1px solid rgba(255,255,255,.15)">'
           '<h2 style="margin-top:0">Bring one real project.</h2><p class="lede">Book a free Project Review and see what Sara, Taylor and Emma would do with your next bid.</p>'
           '<div style="margin-top:18px">%s</div></div>') % btn_book()
    h += section("dark", '<article class="prose post fx"><p class="eyebrow"><a href="/blog/">Blog</a></p><h1 style="margin-top:14px">%s</h1>%s%s</article>'
                 % (p["h1"], html, cta), extra_cls="first")
    h += footer()
    return url, h

def write(rel, html):
    full = os.path.join(ROOT, rel.lstrip("/")); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8", newline="\n").write(html)

def main():
    posts = [parse(f) for f in sorted(glob.glob(os.path.join(HERE, "blog", "*.md")))]
    items = []
    for p in posts:
        url, html = render(p); write(url + "index.html", html)
        items.append('<li><a href="%s">%s</a><p>%s</p></li>' % (url, p["h1"], esc(p["desc"])))
    desc = "Plain-English guides for US general contractors on estimating, takeoff and bid software: prices with sources, fit and limits."
    ld = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "BuildWithBNZ Blog", "url": SITE + "/blog/", "description": desc})
    h = head("Blog — BuildWithBNZ", desc, "/blog/", jsonld=ld).replace("</head>", STYLE + "</head>") + nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">Blog</span><h1 style="margin-top:14px">Estimating and bid software, explained.</h1>'
                 '<p class="lede">%s</p><ul class="post-list">%s</ul><div style="margin-top:30px">%s</div></div>' % (desc, "".join(items), btn_book()), extra_cls="first")
    h += footer(); write("/blog/index.html", h)
    print("wrote /blog/ + %d posts" % len(posts))
    for u in unlinked: print("UNLINKED", *u, sep=" | ")
if __name__ == "__main__": main()
