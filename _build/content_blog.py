# -*- coding: utf-8 -*-
"""/blog/: competitor price and review posts, built from _build/blog/*.md with the article template.
Each post gets Article + FAQPage JSON-LD. Competitor prices stay only where sourced and dated in the text."""
import os, json
from shared import *
import content_articles as CA
from links import A

HERE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(HERE, "blog")
POSTS = [
    ("togal-ai-review", "Blog · Togal AI review", "t"),
    ("buildingconnected-pricing", "Blog · BuildingConnected pricing", "e"),
    ("downtobid-pricing", "Blog · Downtobid pricing", "e"),
    ("best-ai-estimating-software-for-general-contractors", "Blog · AI estimating software roundup", "t"),
    ("planswift-vs-bluebeam", "Blog · PlanSwift vs Bluebeam", "t"),
]

def article_ld(meta, h1):
    url = SITE + meta["url_slug"]
    d = meta.get("date_published", UPDATED)
    return {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": meta["meta_description"],
            "url": url, "mainEntityOfPage": url, "datePublished": d, "dateModified": d, "inLanguage": "en-US",
            "author": {"@type": "Organization", "name": "BuildWithBNZ", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "@id": SITE + "/#organization", "name": "BuildWithBNZ"},
            "image": SITE + "/og.png"}

def post(name, eyebrow, who):
    return CA.page_article(name, eyebrow, who, art_dir=BLOG, extra_ld=article_ld)

def page_index():
    path = "/blog/"
    cards = []
    for n, e, w in POSTS:
        meta = CA.load(n, BLOG)[0]
        cards.append('<a class="card" href="%s"><span class="eyebrow mute">%s</span><h3 style="margin-top:10px">%s</h3><p class="muted" style="margin-top:8px">%s</p><span class="link">Read →</span></a>'
                     % (meta["url_slug"], e.replace("Blog · ", ""), meta["title_tag"], meta["meta_description"]))
    ld = json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": "BuildWithBNZ Blog", "url": SITE + path,
                     "publisher": {"@id": SITE + "/#organization"}}, ensure_ascii=False, separators=(",", ":"))
    h = head("Construction Software Pricing & Reviews Blog | BuildWithBNZ",
             "Sourced, dated reviews and price breakdowns of construction takeoff, estimating and bidding software for US contractors.", path, jsonld=ld)
    h += nav()
    h += ('<section class="dark hero"><div class="wrap"><div class="fx"><span class="eyebrow">Blog</span><h1>Construction software, priced and reviewed.</h1>'
          '<p class="lede">What bidding and takeoff tools cost and what they actually do, with every figure sourced and dated. Prices change, so confirm with the vendor.</p></div></div></section>\n')
    guides = ' · '.join('<a class="link" href="%s">%s</a>' % (u, A[u]) for u in ("/guides/bid-leveling/", "/guides/subcontractor-bid-invitations/", "/guides/subcontractor-coi-tracking/", "/guides/prevailing-wage-bidding/"))
    money = ' · '.join('<a class="link" href="%s">%s</a>' % (u, A[u]) for u in ("/construction-estimating-ai/", "/construction-bid-management/", "/taylor/", "/emma/"))
    h += section("light", '<div class="grid g3 stagger">%s</div><p class="fx" style="margin-top:22px">Guides: %s</p><p class="fx" style="margin-top:10px">What BuildWithBNZ does: %s</p>' % (''.join(cards), guides, money))
    h += book_strip()
    h += footer()
    return path, h
