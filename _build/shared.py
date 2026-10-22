# -*- coding: utf-8 -*-
"""Shared head / nav / footer and the small components every page is built from.
Run `python3 _build/build.py` from the repo root to regenerate every page.
No dependencies beyond the standard library."""

import html as _html
from team import AGENTS, BY, SIX, PRINCIPLE, PRINCIPLE_LONG, agent_href

SITE = "https://buildwithbnz.com"
BRAND = "BuildWithBNZ"
# Hero lede for the home page and the GC lander: the seven-agent team (FINAL), in plain words, naming only what a
# customer gets (Amanda's and Adam's work is BuildWithBNZ's own). On phones the .ph-hide parts drop out so both hero
# buttons show on the first screen; the short version still reads as whole sentences.
TEAM_LEDE = ('Sara runs operations and leads six specialist AI agents.<span class="ph-hide"> Taylor reads the drawings and builds the estimate, '
             'Emma checks job costs and invoices, and Kyle and Richard cover design concepts and contract review.</span> '
             'They work inside the files and systems you already use<span class="ph-hide"> — Drive, Gmail, Calendar, Notion, your project folders. '
             'Every project is scoped and priced in writing before we start</span>. You approve anything that leaves the building.')
INBOX = "saracooper@bnzbuildersinc.com"
# BuildWithBNZ (software) number per the FINAL team identity, rule 5. The legacy BNZ Builders pages keep their own.
PHONE = "+16462818368"        # tel: links
PHONE_TXT = "646-281-8368"    # what people read
PHONE_LD = "+1-646-281-8368"  # schema.org telephone
UPDATED = "2026-10-17"          # sitemap lastmod for the generated pages (build.py keeps the legacy pages' date)
LEGACY_UPDATED = "2026-09-17"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..900'
         '&family=Space+Grotesk:wght@400;500;600;700&display=swap">')

NAV_ITEMS = [("/crew/", "The crew"), ("/how-it-works/", "How it works"), ("/faq/", "FAQ")]

MENU_PROBLEM = [
    ("t", "Estimating &amp; takeoff", "Taylor reads the package and builds the estimate with every assumption shown.",
     ("unknown", "Unknown when it should be"), "/construction-estimating-ai/"),
    ("t", "Subcontractor bidding &amp; buyout", "Taylor requests and compares sub and vendor pricing.",
     ("waiting", "Waiting on — named"), "/subcontractor-procurement/"),
    ("s", "Operations &amp; approvals", "Sara runs Today, the queue and the Monday report.",
     ("verified", "Verified vs reported"), "/construction-project-management-ai/"),
    ("t", "Public work &amp; prevailing wage", "Wage schedules, addenda, bid forms, certified payroll docs handled by the book.",
     ("cross", "Cross-checked"), "/prevailing-wage-project-management/"),
]
MENU_CONTRACTOR = [
    ("General contractors", "/ai-for-general-contractors/"),
    ("Remodelers &amp; custom builders", "/commercial-construction-estimating/"),
    ("Specialty contractors", "/construction-bid-management/"),
    ("GCs bidding public work", "/prevailing-wage-project-management/"),
]

# ---------------------------------------------------------------- components

def chip(kind, text, dot=False):
    return '<span class="chip %s">%s%s</span>' % (kind, '<i class="dot"></i>' if dot else '', text)

def tx(s):
    """Escape plain text from team.py for HTML text or attributes."""
    return _html.escape(s, quote=True)

# The crew characters: a sheet with a folded corner, two rivets and one cut-out for the agent's job.
# Sara, Taylor and Emma are the original character sheet; the other four follow it.
# slug: (shape, body, facet, motion behind the body, motion over it). Motions are lit in #F5F3EE.
RIVETS = " M26 204a10 10 0 1 0 20 0a10 10 0 1 0 -20 0Z M194 204a10 10 0 1 0 20 0a10 10 0 1 0 -20 0Z"
SHEET = "M0 0H180L240 60V240H0Z"
LIT = 'fill="#F5F3EE"'
MARKS = {
    "sara": (SHEET + " M48 96H192V120H48Z" + RIVETS, "#EA580C", "#9A3A08",          # status bar
             '<g clip-path="url(#mw-sara)"><rect x="48" y="94" width="144" height="28" %s style="animation:saraBar 4.6s cubic-bezier(.2,.8,.2,1) infinite"/></g>' % LIT, ''),
    "amanda": (SHEET + " M92 78L164 120L92 162Z" + RIVETS, "#C9718A", "#85485A",     # play button
               '<path d="M92 78L164 120L92 162Z" %s style="animation:amaPlay 4.6s ease-in-out infinite"/>' % LIT, ''),
    "kyle": ("M0 84L84 0H180L240 60V240H0Z M82 96H116V130H82Z M124 96H158V130H124Z M82 138H116V172H82Z M124 138H158V172H124Z" + RIVETS,
             "#7385B8", "#4B577A",                                                   # roof and window
             ''.join('<rect x="%d" y="%d" width="34" height="34" %s style="animation:kyleLight 4.6s ease-in-out %.1fs infinite"/>' % (x, y, LIT, n * .3)
                     for n, (x, y) in enumerate([(82, 96), (124, 96), (124, 138), (82, 138)])), ''),
    "taylor": ("M180 0L240 60V240H0Z M204 64V150H139.5Z M38 204a10 10 0 1 0 20 0a10 10 0 1 0 -20 0Z M194 204a10 10 0 1 0 20 0a10 10 0 1 0 -20 0Z",
               "#C9A44F", "#8A6E33", '',                                             # set square
               '<path d="M204 64V150H139.5Z" fill="none" stroke="#F5F3EE" stroke-width="4" stroke-dasharray="46 212" style="animation:tayTrace 4.6s linear infinite"/>'),
    "emma": ("M0 0H180L240 60V92H132V102H118V138H132V148H240V240H0Z" + RIVETS, "#7F9C76", "#55684E", '',   # dock
             '<g clip-path="url(#mw-emma)"><rect x="144" y="107" width="26" height="26" %s style="animation:emmaDock 4.6s cubic-bezier(.2,.8,.2,1) infinite"/></g>' % LIT),
    "richard": (SHEET + " M48 80H192V96H48Z M48 112H192V128H48Z M48 144H140V160H48Z" + RIVETS, "#9A719E", "#654968",   # contract lines
                '<g clip-path="url(#mw-richard)">%s</g>' % ''.join(
                    '<rect x="48" y="%d" width="144" height="16" %s style="animation:richWrite 4.6s cubic-bezier(.2,.8,.2,1) %.1fs infinite"/>' % (y, LIT, n * .35)
                    for n, y in enumerate([80, 112, 144])), ''),
    "adam": (SHEET + " M52 84L112 122L52 160V137.2L76 122L52 106.8Z M126 136H190V158H126Z" + RIVETS, "#4E9CA6", "#31666D",   # terminal prompt
             '<rect x="126" y="136" width="64" height="22" %s style="animation:adamBlink 1.1s steps(1) infinite"/>' % LIT, ''),
}
MARK_WINDOWS = {"sara": '<rect x="48" y="96" width="144" height="24"/>', "emma": '<rect x="118" y="92" width="122" height="56"/>',
                "richard": '<rect x="48" y="80" width="144" height="16"/><rect x="48" y="112" width="144" height="16"/><rect x="48" y="144" width="92" height="16"/>'}

def crew_sprite():
    """All seven characters as one hidden SVG sprite per page. #mc-<slug> is static; #ma-<slug> floats, glints
    and runs its own motion (bnz.js swaps in the static one under prefers-reduced-motion)."""
    d = ['<linearGradient id="mglint" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F5F3EE" stop-opacity="0"/>'
         '<stop offset=".5" stop-color="#F5F3EE" stop-opacity=".28"/><stop offset="1" stop-color="#F5F3EE" stop-opacity="0"/></linearGradient>']
    d += ['<clipPath id="mw-%s">%s</clipPath>' % (k, r) for k, r in MARK_WINDOWS.items()]
    for k, (shape, body, facet, behind, over) in MARKS.items():
        d.append('<path id="mp-%s" fill-rule="evenodd" d="%s"/>' % (k, shape))
        d.append('<clipPath id="mcl-%s"><use href="#mp-%s"/></clipPath>' % (k, k))
        d.append('<g id="mc-%s"><use href="#mp-%s" fill="%s"/><path fill="%s" d="M180 0L240 60H180Z"/></g>' % (k, k, body, facet))
        d.append('<g id="ma-%s" style="animation:plFloat 5.2s ease-in-out infinite">%s<use href="#mp-%s" fill="%s"/>'
                 '<path d="M180 0L240 60H180Z" fill="%s" style="animation:plFacet 3.4s ease-in-out infinite"/>%s'
                 '<g clip-path="url(#mcl-%s)"><rect x="-40" y="-20" width="70" height="300" fill="url(#mglint)" style="animation:plGlint 4.6s ease-in-out infinite"/></g></g>' % (
                     k, behind, k, body, facet, over, k))
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>%s</defs></svg>\n' % ''.join(d)

def av(who, size=32, note=False, anim=False, label=True):
    """An agent's character. Old one-letter keys ('s', 't', 'e') still work.
    anim=True uses the moving version (float, glint, its own motion)."""
    a = BY[who]; k = a["slug"]
    aria = 'role="img" aria-label="%s"' % tx(a["short"]) if label else 'aria-hidden="true"'
    if anim:
        return ('<svg class="av av-%s" width="%d" height="%d" viewBox="-20 -20 280 280" style="overflow:visible" %s>'
                '<use href="#ma-%s" data-static="#mc-%s"/></svg>') % (k, size, size, aria, k, k)
    return '<svg class="av av-%s" width="%d" height="%d" viewBox="0 0 240 240" %s><use href="#mc-%s"/></svg>' % (k, size, size, aria, k)

def portrait(slug, cls=""):
    """An agent's character, big and moving, on its own panel."""
    a = BY[slug]
    return ('<figure class="portrait %s" role="img" aria-label="%s, %s">%s</figure>') % (
        cls, tx(a["name"]), tx(a["title"]), av(slug, 240, anim=True, label=False))

def thumb(slug):
    """An agent's character on a small square panel (org chart). Decorative: the name sits beside it."""
    return '<span class="thumb">%s</span>' % av(slug, 96, label=False)

def btn_book(cls="btn primary", label="Book a project review"):
    return '<a class="%s" href="/book/">%s <span class="g">↗</span></a>' % (cls, label)

# The onboarding path (/start/): brand-kit CTA wording (Brand Kit p6).
START_BTN = '<a class="btn ghost" href="/start/">Show us how your company works <span class="g">↗</span></a>'

def head(title, desc, path, og_title=None, jsonld=None, noindex=False):
    canon = SITE + path
    og_title = og_title or title
    ld = ''
    if jsonld:
        ld = '<script type="application/ld+json">%s</script>' % jsonld
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ''
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google-site-verification" content="uTyl7df14_U_o3kpXSZRk6JfZPx5DJSW35nNlX7l0Zs" />
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-883K8FQX0B"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-883K8FQX0B');</script>
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canon)s">
%(robots)s<meta name="theme-color" content="#0A0A0A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BuildWithBNZ">
<meta property="og:title" content="%(og)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:image" content="%(site)s/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(og)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(site)s/og.png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
%(fonts)s
<link rel="stylesheet" href="/assets/css/bnz.css">
<noscript><style>.fx,.stagger>*,.mock.rows>.row,.mock.rows tbody>tr,.mock.rows .line,.mock.rows .kpi{opacity:1;transform:none}</style></noscript>
%(ld)s</head>
<body>
<a class="skip" href="#main">Skip to content</a>
%(sprite)s''' % dict(sprite=crew_sprite(), title=esc(title), desc=esc(desc), canon=canon, og=esc(og_title), site=SITE, fonts=FONTS, ld=ld, robots=robots)

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('&amp;amp;', '&amp;')

def nav(current=""):
    links = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == current else '', t) for h, t in NAV_ITEMS)
    prob = ''.join(
        '<a class="row" href="%s">%s<div><b>%s</b><span>%s</span></div>%s</a>' % (href, av(who, 24), t, s, chip(c[0], c[1]))
        for who, t, s, c, href in MENU_PROBLEM)
    contr = ''.join('<a href="%s">%s</a>' % (h, t) for t, h in MENU_CONTRACTOR)
    mega = ('<div class="mega" role="menu">'
            '<div class="col"><h4 class="eyebrow mute">By problem</h4>%s</div>'
            '<div class="col list"><h4 class="eyebrow mute">By contractor</h4>%s</div>'
            '<div class="foot"><a href="/what-we-connect-to/">What we connect to →</a><a class="link" href="/book/">Book a project review ↗</a></div>'
            '</div>') % (prob, contr)
    drawer_prob = ''.join('<a href="%s">%s</a>' % (href, t) for _, t, _, _, href in MENU_PROBLEM)
    drawer_contr = ''.join('<a href="%s">%s</a>' % (h, t) for t, h in MENU_CONTRACTOR)
    drawer_links = ''.join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_ITEMS)
    return '''<header class="nav">
<div class="wrap">
<a class="brand" href="/" aria-label="BuildWithBNZ home"><span class="mark">B</span>BuildWithBNZ</a>
<nav class="nav-links" aria-label="Primary">
<div class="has-menu"><button type="button" aria-haspopup="true" aria-expanded="false">Solutions <span class="car">▼</span></button>%(mega)s</div>
%(links)s
</nav>
<a class="btn primary sm nav-cta" href="/book/">Book a project review <span class="g">↗</span></a>
<button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
</div>
<div class="drawer" id="drawer">
<details><summary>Solutions</summary><a href="/solutions/">All solutions</a>%(dprob)s%(dcontr)s<a href="/what-we-connect-to/">What we connect to</a></details>
%(dlinks)s
<a href="/start/">Show us how your company works</a>
<a href="tel:%(phone)s">Call %(phone_txt)s</a>
%(book)s
</div>
</header>
<main id="main">
''' % dict(mega=mega, links=links, dprob=drawer_prob, dcontr=drawer_contr, dlinks=drawer_links, book=btn_book(), phone=PHONE, phone_txt=PHONE_TXT)

def footer():
    return '''</main>
<footer>
<div class="wrap">
<div><a class="brand" href="/"><span class="mark">B</span>BuildWithBNZ</a><p class="addr" style="margin-top:10px">New York · <a href="mailto:%(inbox)s">%(inbox)s</a> · <a href="tel:%(phone)s">%(phone_txt)s</a></p><p class="addr ai-note">The crew are AI agents, not real people.</p></div>
<nav aria-label="Footer"><a href="/solutions/">Solutions</a><a href="/what-we-connect-to/">What we connect to</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav>
</div>
</footer>
<script src="/assets/js/bnz.js" defer></script>
</body>
</html>
''' % dict(inbox=INBOX, phone=PHONE, phone_txt=PHONE_TXT)

def section(cls, inner, id_=None, extra_cls=""):
    idattr = ' id="%s"' % id_ if id_ else ''
    return '<section class="%s %s"%s><div class="wrap">%s</div></section>\n' % (cls, extra_cls, idattr, inner)

def sec_head(eyebrow, h2, p=None, dark=True, tag="h2"):
    # tag="h1" renders the page's main heading at h2 size (one H1 per page).
    open_tag = '<h1 style="%s">' % "font-size:clamp(34px,4.6vw,58px)" if tag == "h1" else '<h2>'
    return '<div class="sec-head fx"><span class="eyebrow%s">%s</span>%s%s</%s>%s</div>' % (
        '' if dark else '', eyebrow, open_tag, h2, tag, '<p>%s</p>' % p if p else '')

def book_strip(dark=False):
    inner = ('<div class="split"><div class="fx"><span class="eyebrow">Start here</span>'
             '<h2 style="margin:14px 0 12px">Book a project review.</h2>'
             '<p class="lede">Bring one project. We\'ll show you what the crew would do with it.</p>'
             '<div class="strip-cta">%s%s</div>'
             '<p class="small muted" style="margin-top:12px">Not sure where to start? Two quick questions, then your details.</p></div>'
             '<div class="fx"><div class="cal-slot">30-minute Project Review with a real person.<br>'
             '<span style="text-transform:none;letter-spacing:0;font-size:14px;display:block;margin-top:8px">Fill in the short form on the booking page and we reply the same business day to set a time. Prefer to talk? Call <a href="tel:%s">%s</a>.</span></div></div></div>') % (btn_book(), START_BTN, PHONE, PHONE_TXT)
    return section('light' if not dark else 'dark', inner, id_="book")

def faq_items(items, first_open=2):
    out = []
    for i, (q, a) in enumerate(items):
        out.append('<details%s><summary>%s <span class="pm">+</span></summary><div class="a">%s</div></details>' % (
            ' open' if i < first_open else '', q, a))
    return '<div class="faq">%s</div>' % ''.join(out)

FAQ = [
    ("What does it cost?",
     "Every engagement starts with a Project Review — a real call about one real project. We return scope and one set price, in writing, for that project. Price moves only if scope moves. After the first project the crew stays on under a separate monthly arrangement covering hosting, monitoring and new projects. There is no price list because there is no standard project."),
    ("How long until the crew is live on my project?",
     "It starts with a Project Review about one real project. Scope and one set price come back in writing. Once you approve, the crew starts reading your package. One real project sets the pace — nothing is connected until you pick it."),
    ("Who sees my drawings and my numbers?",
     "You, the people you name, and the crew working your project. Access is scoped per project — a company that engages us for one job does not open its whole Drive. We start with read access, and anything that leaves the workspace waits on your approval. Your files stay in your systems; nothing is moved or copied out to be trained on."),
    ("Does the AI send anything without me?",
     "No. Taylor drafts requests for sub pricing and questions to the architect; Sara drafts the Monday report. Every send sits in your approvals queue until you approve, edit or send it back. The crew drafts. You decide."),
    ("Can it stamp drawings or act as my architect?",
     "No. Taylor reads drawings and specs, performs takeoffs and flags conflicts. Kyle prepares design concepts only: he is not a licensed architect, and his work is never presented as signed or sealed drawings. Licensed, stamped design responsibility stays with your architect or engineer of record. Design concepts are not licensed design, and we keep that line visible."),
    ("What happens when Taylor doesn't have enough information?",
     "The line reads UNKNOWN, with the reason and who has the missing item — \"fixture schedule not in the set, request from architect.\" The estimate total is withheld until every UNKNOWN is resolved. Taylor never fills a gap with a guess."),
    ("What if I already tried AI or software and it didn't stick?",
     "Most of it asked you to move your work into a new tool and then left you to run it. We do the opposite: the crew works inside the folders, inbox and calendar you already use, and we stay responsible for it working under the ongoing arrangement. If a piece isn't earning its place after the first project, that comes out in the Monday report and we change it."),
    ("Do I have to move off Drive / Gmail / my folders?",
     "No. Keep your tools. The crew connects to Drive, Gmail, Calendar, Workspace and Notion with read access first, and works inside them. Nothing is migrated."),
]

INTEGRATIONS_TODAY = [
    ("drive", "Google Drive", "Taylor reads the drawing set, specs and addenda from your project folder. Read access first.", "t"),
    ("gmail", "Gmail", "Taylor drafts requests for sub pricing and follow-ups; nothing sends until you approve.", "t"),
    ("cal", "Google Calendar", "Sara holds bid due dates, deadlines and quote promises against the week.", "s"),
    ("ws", "Google Workspace", "The estimate, scope document and Monday report land as files you own.", "s"),
    ("notion", "Notion", "Project notes and records read and updated in place.", "s"),
]
INTEGRATIONS_NEXT = [
    ("procore", "Procore", "Estimate lines will post to the job cost."),
    ("bt", "Buildertrend", "Schedules and daily logs will sync both ways."),
    ("qb", "QuickBooks", "Approved sub invoices will flow to the books."),
    ("sage", "Sage", "Job cost codes will map to estimate divisions."),
    ("bb", "Bluebeam", "Markups will read into Taylor's takeoff."),
    ("ps", "PlanSwift / STACK", "Existing takeoff files will import as Taylor's starting point."),
    ("ds", "DocuSign", "Approved contracts will route for signature."),
    ("m365", "Microsoft 365", "Outlook and OneDrive will work the way Gmail and Drive do today."),
    ("dbx", "Dropbox", "Project folders will read in place."),
    ("xl", "Excel", "Estimates will export to your own sheets."),
]

# monochrome marks, one per system — generic glyphs, never the brand's own colour logo
ICONS = {
    "drive": '<svg viewBox="0 0 24 24"><path d="M8.2 3h7.6l6 10.4-3.8 6.6H6L2.2 13.4zM9 5 4.6 12.6h4.2L13.2 5zm2.6 8.6-2.1 3.6h8.4l2.1-3.6z"/></svg>',
    "gmail": '<svg viewBox="0 0 24 24"><path d="M3 5h18v2.2l-9 5.6-9-5.6zm0 4.6 9 5.6 9-5.6V19H3z"/></svg>',
    "cal": '<svg viewBox="0 0 24 24"><path d="M4 5h16v15H4zm2 5v8h12v-8zm1-7h2v3H7zm8 0h2v3h-2z"/></svg>',
    "ws": '<svg viewBox="0 0 24 24"><path d="M4 4h7v7H4zm9 0h7v7h-7zM4 13h7v7H4zm9 0h7v7h-7z"/></svg>',
    "notion": '<svg viewBox="0 0 24 24"><path d="M5 4h11l3 3v13H5zm3 4v8h2v-5l4 5h2V8h-2v5L10 8z"/></svg>',
    "procore": '<svg viewBox="0 0 24 24"><path d="M12 3l9 5v8l-9 5-9-5V8zm0 2.3L5.3 9v6L12 18.7 18.7 15V9zM9 10h6v4H9z"/></svg>',
    "bt": '<svg viewBox="0 0 24 24"><path d="M3 20V10l9-7 9 7v10h-6v-6H9v6z"/></svg>',
    "qb": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 2a8 8 0 1 1 0 16 8 8 0 0 1 0-16zm-1 3h2v2h1.5a2.5 2.5 0 0 1 0 5H13v1h3v2h-3v2h-2v-2H9.5a2.5 2.5 0 0 1 0-5H11v-1H8V9h3z"/></svg>',
    "sage": '<svg viewBox="0 0 24 24"><path d="M4 6h16v3H4zm0 5h16v3H4zm0 5h10v3H4z"/></svg>',
    "bb": '<svg viewBox="0 0 24 24"><path d="M4 4h12a4 4 0 0 1 2.6 7 4 4 0 0 1-2.6 7H4zm3 3v3h8a1.5 1.5 0 0 0 0-3zm0 6v3h9a1.5 1.5 0 0 0 0-3z"/></svg>',
    "ps": '<svg viewBox="0 0 24 24"><path d="M3 3h18v18H3zm2 2v14h14V5zm2 2h4v4H7zm6 0h4v4h-4zM7 13h10v4H7z"/></svg>',
    "ds": '<svg viewBox="0 0 24 24"><path d="M4 17c3-1 4-6 6-6s2 5 5 5 3-4 5-4v2c-1 0-2 4-5 4s-4-5-5-5-3 6-6 6zM4 20h16v1H4z"/></svg>',
    "m365": '<svg viewBox="0 0 24 24"><path d="M4 4h7.5v7.5H4zm8.5 0H20v7.5h-7.5zM4 12.5h7.5V20H4zm8.5 0H20V20h-7.5z"/></svg>',
    "dbx": '<svg viewBox="0 0 24 24"><path d="M7 3l5 3.2L7 9.4 2 6.2zm10 0 5 3.2-5 3.2-5-3.2zM2 12.6 7 9.4l5 3.2-5 3.2zm15-3.2 5 3.2-5 3.2-5-3.2zM7 17l5-3.2 5 3.2-5 3.2z"/></svg>',
    "xl": '<svg viewBox="0 0 24 24"><path d="M3 3h18v18H3zm2 2v14h14V5zm3 3h2.2l1.8 2.8L13.8 8H16l-2.9 4 2.9 4h-2.2l-1.8-2.8L10.2 16H8l2.9-4z"/></svg>',
}

def tile(icon, name, line, who=None, next_=False):
    return ('<div class="tile%s"><div class="ic" aria-hidden="true">%s</div><div class="tx"><b>%s%s</b><span>%s</span></div>%s</div>') % (
        ' dim' if next_ else '', ICONS.get(icon, icon), name, ' ' + chip("next", "Next") if next_ else '', line, av(who, 22) if who else '')

def integrations(rows=3):
    """The waterfall (M7): brick rows of Beam-style tiles drifting down through a masked window.
    rows = how many rows are visible in the window (2 on the home page, 3 on the full section)."""
    tiles = [tile(i, n, l, w) for i, n, l, w in INTEGRATIONS_TODAY] + [tile(i, n, l, next_=True) for i, n, l in INTEGRATIONS_NEXT]
    # brick pattern: 3, 2, 3, 2 … (15 tiles → 3+2+3+2+3+2 = 15)
    pattern = [3, 2, 3, 2, 3, 2]
    out, k = [], 0
    for n in pattern:
        row = tiles[k:k + n]; k += n
        if not row: break
        out.append('<div class="brick n%d">%s</div>' % (len(row), ''.join(row)))
    track = ''.join(out)
    legend = ('<div class="legend fx"><span>%s Connected today</span><span>%s Next — future tense only, nothing reads as live</span>'
              '<span class="muted small">Icons are each system\'s own mark, monochrome. Hover to pause.</span></div>') % (
        '<i class="sw on"></i>', chip("next", "Next"))
    conv = '<div class="conveyor%s" aria-label="Systems the crew works inside"><div class="track">%s</div></div>' % (' two' if rows == 2 else '', track)
    static = '<div class="conv-static">%s</div>' % track
    return legend + conv + static + '<p class="small muted" style="margin-top:14px">Don\'t see yours? Bring it to the Project Review.</p>'

def sample_project_mock(strip=True):
    lines = ('[["ADDENDUM 02 RECEIVED · TAYLOR READING",["working","Working"]],'
             '["TAKEOFF MOVED 1,980 → 2,150 LF · VERIFIED AGAINST E-401",["verified","Verified"]],'
             '["TAYLOR · 2ND FOLLOW-UP SENT · HUDSON FEEDER CO.",["chasing","Chasing"]],'
             '["BID INVITATION DRAFTED · 4 SUBS · NEEDS YOU",["needs","Needs you"]],'
             '["SUB QUOTES 3 OF 7 IN · 1 LEVELED",["levelled","Leveled"]],'
             '["MONDAY REPORT DRAFTED · VERIFIED FIRST",["verified","Verified"]]]')
    s = ('<div class="strip" data-lines=\'%s\'><span class="txt">ADDENDUM 02 RECEIVED · TAYLOR READING</span>%s</div>' % (lines, chip("working", "Working"))) if strip else ''
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="dots"><i></i><i></i><i></i></div>%s'
            '<div class="title">Rockland Mixed-Use · 38 Units</div><div class="sub">Public work · prevailing wage · bid due in 11 days</div>'
            '<div class="crew">%s%s%s</div>'
            '<div class="tabs"><b>Overview</b><span>Files</span><span>Estimate</span><span>Subcontractors</span><span>Activity</span></div>'
            '<div class="row"><div><b>Addendum 02 — new</b><span>Taylor: "Changed the electrical scope — reissuing as Rev 2."</span></div>%s</div>'
            '<div class="row"><div><b>Subcontractors</b><span>Taylor: 7 invited · 3 quotes in · 2 chasing</span></div>%s</div>'
            '<div class="row needs"><div><b>Approve bid invitation to 4 electrical subs</b><span>Sara: "Drafted. Nothing sends without you."</span></div>%s</div>'
            '</div>') % (s, av("s", 24), av("t", 24), av("e", 24), chip("working", "Working", True), chip("verified", "Verified"), chip("needs", "Needs you"))

def monday_mock():
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="title">Monday report — week of Mar 9</div>'
            '<div class="kpis">'
            '<div class="kpi"><b class="count" data-count="2">0</b><span>Projects active</span></div>'
            '<div class="kpi"><b class="count" data-count="1">0</b><span>Estimate issued</span></div>'
            '<div class="kpi"><b class="count" data-count="3">0</b><span>Quotes collected</span></div>'
            '<div class="kpi needs"><b class="count" data-count="2">0</b><span>Waiting on you</span></div>'
            '<div class="kpi"><b class="count" data-count="4">0</b><span>Waiting on subs</span></div></div>'
            '<div class="line"><b>Waiting on subs:</b> Hudson Feeder Co. (quote), Valley Air &amp; Pipe (COI), Ramapo Rebar (W-9), Orangetown Pour (quote)</div>'
            '<div class="line"><b>Reported, not verified:</b> Addendum 03 rumoured per architect\'s office — unconfirmed.</div>'
            '</div>')
