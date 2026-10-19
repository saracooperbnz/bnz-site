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

ALLOWED_PREFIX = ("/book/", "/sara/", "/taylor/", "/emma/", "/faq/", "/crew/", "/how-it-works/", "/solutions/", "/what-we-connect-to/", "/blog/")
META = {  # descriptions trimmed to <=155 chars
 "best-ai-estimating-software-for-general-contractors": "Best AI estimating software for general contractors in 2026: Togal, Kreo, Beam AI, Bobyard, Handoff and BuildWithBNZ: published prices, sources and fit.",
 "buildingconnected-pricing": "BuildingConnected pricing in 2026: Autodesk quotes it through sales, so here's what drives the price, what Pro and Bid Board Pro include, and alternatives.",
 "construction-estimating-software-for-small-business": "Construction estimating software for small business: free plans, what to check before you buy, quick picks by work type, and when software isn't the fix.",
 "downtobid-pricing": "Downtobid pricing for GCs and subs as of Oct 2026, from its own site: what you get, who it fits, its limits, and when a different setup fits better.",
 "planswift-vs-bluebeam": "PlanSwift vs Bluebeam Revu for construction takeoff in 2026: how each is priced, what each does well, the limits, and which one fits your estimating team.",
 "togal-ai-review": "Togal AI review for US contractors: the published price, what independent studies found on accuracy, where estimators say it falls short, and other fits.",
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

def fix_lists(md):
    """Insert a blank line before a list that directly follows a text line, so Markdown renders it as a list."""
    out, prev = [], ""
    for line in md.split("\n"):
        is_item = re.match(r"\s*([-*]|\d+\.)\s", line)
        prev_item = re.match(r"\s*([-*]|\d+\.)\s|\s*\|", prev)
        if is_item and prev.strip() and not prev_item:
            out.append("")
        out.append(line); prev = line
    return "\n".join(out)

def faq_from_page(body):
    """Build FAQPage JSON-LD from the visible '## FAQ' section so the schema matches the page word for word."""
    m = re.search(r'^## FAQ\s*$(.*?)(?=^## |\Z)', body, re.M | re.S)
    if not m: return None
    qa = re.findall(r'^\*\*(.+?)\*\*\s*\n(.+?)(?=\n\s*\n|\n\*\*|\Z)', m.group(1), re.M | re.S)
    plain = lambda t: re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).replace("**", "").strip()
    items = [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": " ".join(plain(a).split())}} for q, a in qa]
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items} if items else None

def parse(path):
    raw = open(path, encoding="utf-8").read()
    _, fm, body = raw.split("---", 2)
    title = re.search(r'^title_tag: "(.*)"', fm, re.M).group(1)
    desc = re.search(r'^meta_description: "(.*)"', fm, re.M).group(1)
    slug = re.search(r'^url_slug: (\S+)', fm, re.M).group(1).strip("/").split("/")[-1]
    dp = re.search(r'^date_published: "?(\d{4}-\d{2}-\d{2})', fm, re.M); dm = re.search(r'^date_modified: "?(\d{4}-\d{2}-\d{2})', fm, re.M)
    dates = {}
    if dp: dates["datePublished"] = dp.group(1); dates["dateModified"] = dm.group(1) if dm else dp.group(1)
    desc = META.get(slug, desc); assert len(desc) <= 155, (slug, len(desc))
    faq = None
    m = re.search(r'```json\s*(\{.*?\})\s*```', body, re.S)
    if m: faq = json.loads(m.group(1)); body = body[:m.start()] + body[m.end():]
    # drop editorial notes (whole lines and inline)
    body = re.sub(r'^\s*\[(VERIFY|OWNER DATA NEEDED)[^\]]*\]\s*$\n?', '', body, flags=re.M)
    body = re.sub(r'\s*\[(VERIFY|OWNER DATA NEEDED)[^\]]*\]', '', body)
    h1 = re.search(r'^# (.+)$', body, re.M).group(1).strip()
    body = re.sub(r'^# .+$\n?', '', body, count=1, flags=re.M)
    body = fix_lists(body)
    body = fix_links(slug, body)
    faq = faq_from_page(body) or faq
    return dict(title=title, desc=desc, slug=slug, faq=faq, h1=h1, body=body, dates=dates)

def render(p):
    url = "/blog/%s/" % p["slug"]
    html = markdown.markdown(p["body"], extensions=["tables", "sane_lists"])
    html = html.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', html)
    has_book = 'href="/book/"' in html
    article = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"][:110], "description": p["desc"],
               **p["dates"], "mainEntityOfPage": SITE + url, "image": SITE + "/og.png",
               "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
               "publisher": {"@type": "Organization", "name": BRAND, "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/og.png"}}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": SITE + url}]}
    ld = [article, crumbs] + ([p["faq"]] if p["faq"] else [])
    h = head(p["title"], p["desc"], url, jsonld=json.dumps(ld, ensure_ascii=False).replace("</", "<\\/"))
    h = h.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">', 1)
    h = h.replace("</head>", STYLE + "</head>")
    h += nav()
    cta = ('<div class="fx" style="margin-top:40px;padding-top:24px;border-top:1px solid rgba(255,255,255,.15)">'
           '<h2 style="margin-top:0">Bring one real project.</h2><p class="lede">Book a Project Review and see what Sara, Taylor and Emma would do with your next bid.</p>'
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
