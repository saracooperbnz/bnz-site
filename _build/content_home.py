# -*- coding: utf-8 -*-
from shared import *

def hero(eyebrow, h1, para, mock, cta=True, second=None):
    ctas = ('<div class="cta">%s%s</div>' % (btn_book(), second or '<a class="link" href="/how-it-works/">See how it works</a>')) if cta else ''
    return ('<section class="dark hero"><div class="wrap"><div class="fx"><span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lede">%s</p>%s</div><div class="fx">%s</div></div></section>\n') % (eyebrow, h1, para, ctas, mock)

STEPS = [
    ("Project review", "A real call about one real project. You bring the drawings; we walk through exactly what the crew would do with them.",
     "a written walkthrough of your project.", "you pick the project; nothing is connected yet."),
    ("Scope and one set price", "We return scope and one set price, in writing, for that project. Not a plan, not a tier — a document you can hold us to.",
     "a signed scope, price in writing.", "price moves only if scope moves."),
    ("Connect your files", "Drive, Gmail, Calendar, Notion, your project folders. The crew works inside the tools you already use.",
     "a connected workspace, nothing moved.", "nothing is moved or replaced. Read access first."),
    ("Taylor reads the package", "Drawings, specs, addenda, wage schedules, bid forms. Takeoffs, conflicts, pricing — every assumption and source shown.",
     "an estimate with its logic attached.", "Taylor says UNKNOWN rather than guessing."),
    ("Taylor compares sub pricing", "Taylor requests and compares sub and vendor pricing and levels each quote against her estimate, line by line.",
     "a leveled bid table per trade.", "nothing goes to a sub without your approval."),
    ("Sara runs it", "She supervises the team, catches what falls between them, and brings you a short queue of the decisions that need you.",
     "a Monday report and an approvals queue.", "she brings you only the decisions that need you. You sign. She doesn't."),
]


# ================================================================== the home page (build spec, 21 Oct 2026)
# Layout and feel from beam.ai; the words and facts are ours. One main action everywhere on the page: Start here
# (/get-started/, the onboarding form). The second: Book a call (/book/) or the phone.
# Every agent line comes from team.py (its card, title and limits, never role). Mocks carry a Sample tag and no money
# figures. No logos, testimonials, numbers-as-proof, badges or integrations that aren't live.
# Colours are tokens in assets/css/home.css (colorway A, the current brand). Motion is assets/js/home.js.

HOME_START = "/get-started/"

ICON = {
    "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
    "folder": '<path d="M3.5 7A1.5 1.5 0 0 1 5 5.5h4l2 2.5h8a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 19.5H5A1.5 1.5 0 0 1 3.5 18z"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
    "tag": '<path d="M3.5 12.5v-8a1 1 0 0 1 1-1h8l8 8a1.5 1.5 0 0 1 0 2.1l-6.9 6.9a1.5 1.5 0 0 1-2.1 0z"/><circle cx="8.5" cy="8.5" r="1.4"/>',
    "person": '<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.2-4 4.1-5.8 7.5-5.8s6.3 1.8 7.5 5.8"/>',
    "phone": '<path d="M6.5 3.5h3l1.5 4-2 1.5a11 11 0 0 0 6 6l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z"/>',
    "send": '<path d="M12 19V5M6 11l6-6 6 6"/>',
    "chat": '<path d="M5 5.5h14a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 17H10l-4.5 3.5V17H5a1.5 1.5 0 0 1-1.5-1.5V7A1.5 1.5 0 0 1 5 5.5z"/>',
    "list": '<path d="M9 7h10.5M9 12h10.5M9 17h10.5"/><circle cx="5" cy="7" r="1"/><circle cx="5" cy="12" r="1"/><circle cx="5" cy="17" r="1"/>',
    "calendar": '<rect x="4" y="5.5" width="16" height="15" rx="2"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
}

def ico(name, size=24, cls="ico"):
    return ('<svg class="%s" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (cls, size, size, ICON[name])

def bmark(size=32):
    return '<span class="bm" style="--s:%dpx" aria-hidden="true">B</span>' % size

SAMPLE = '<span class="sd">Sample</span>'

def lim(slug, text):
    """A rule quoted word for word from team.py: the build stops if the source wording changes."""
    assert text in BY[slug]["limits"], (slug, text)
    return tx(text)

def fake_btns(cls="fbtns"):
    return '<span class="%s" aria-hidden="true"><span class="fa">Approve</span><span class="fg">Send back</span></span>' % cls

# ------------------------------------------------------------------ nav + footer (home only)

def nav_home(focus=False):
    """The drawer sits outside the header: the header's blur (once solid) would otherwise trap the fixed drawer inside it.
    focus=True (/get-started/ and its thanks page): the brand, Book a call and the phone. No links, no burger, no drawer."""
    if focus:
        return ('<header class="hnav solid">\n<div class="wrap">\n'
                '<a class="hbrand" href="/" aria-label="BuildWithBNZ home">%s<span>BuildWithBNZ</span></a>\n'
                '<div class="hcta f"><a class="btn-ghost sm" href="/book/">Book a call</a>'
                '<a class="btn-ghost sm call" href="tel:%s">%s <span>Call %s</span></a></div>\n'
                '</div>\n</header>\n<main id="main">\n') % (bmark(32), PHONE, ico("phone", 18), PHONE_TXT)
    prob = ''.join('<a href="%s">%s</a>' % (href, t) for _, t, _, _, href in MENU_PROBLEM)
    contr = ''.join('<a href="%s">%s</a>' % (h, t) for t, h in MENU_CONTRACTOR)
    return '''<header class="hnav">
<div class="wrap">
<a class="hbrand" href="/" aria-label="BuildWithBNZ home">%(bm)s<span>BuildWithBNZ</span></a>
<nav class="hlinks" aria-label="Primary"><a href="#how">How it works</a><a href="#crew">The crew</a><a href="#faq">Questions</a></nav>
<div class="hcta"><a class="btn-ghost sm" href="/book/">Book a call</a><a class="btn-primary sm" href="%(start)s">Start here</a></div>
<button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
</div>
</header>
<div class="drawer" id="drawer">
<a class="btn-primary xl" href="%(start)s">Start here</a>
<a class="btn-ghost xl" href="/book/">Book a call</a>
<a href="tel:%(phone)s">Call %(phone_txt)s</a>
<a href="#how">How it works</a>
<a href="#crew">The crew</a>
<a href="#faq">Questions</a>
<details><summary>Solutions</summary><a href="/solutions/">All solutions</a>%(prob)s%(contr)s<a href="/what-we-connect-to/">What we connect to</a></details>
</div>
<main id="main">
''' % dict(bm=bmark(32), start=HOME_START, phone=PHONE, phone_txt=PHONE_TXT, prob=prob, contr=contr)

def footer_home(minimal=False):
    """minimal=True (/get-started/ and its thanks page): no phone action bar and no home.js; bnz.js stays."""
    cols = [("Product", [("/how-it-works/", "How it works"), ("/crew/", "The crew"), ("/solutions/", "Solutions"), ("/what-we-connect-to/", "What we connect to")]),
            ("Start", [(HOME_START, "Start here"), ("/book/", "Book a call"), ("/workflow-report/", "Free workflow report")]),
            ("Company", [("/faq/", "FAQ"), ("/contact/", "Contact"), ("/privacy/", "Privacy"), ("/terms/", "Terms")])]
    nav_cols = ''.join('<div><p class="hf-h">%s</p><ul>%s</ul></div>' % (t, ''.join('<li><a href="%s">%s</a></li>' % l for l in links)) for t, links in cols)
    return '''</main>
<footer class="hfoot">
<div class="wrap">
<div class="hf-brand"><a class="hbrand" href="/">%(bm)s<span>BuildWithBNZ</span></a>
<p class="hf-tag">The AI office crew for contractors.</p>
<p class="hf-addr">New York</p><p class="hf-contact"><a href="mailto:%(inbox)s">%(inbox)s</a><a href="tel:%(phone)s">%(phone_txt)s</a></p>
<p class="hf-ai">The crew are AI agents, not real people.</p></div>
<nav class="hf-cols" aria-label="Footer">%(cols)s</nav>
<p class="hf-copy">© 2026 BuildWithBNZ</p>
</div>
</footer>
%(bar)s<script src="/assets/js/bnz.js" defer></script>
%(homejs)s</body>
</html>
''' % dict(bm=bmark(32), inbox=INBOX, phone=PHONE, phone_txt=PHONE_TXT, cols=nav_cols,
       bar='' if minimal else ('<div class="actbar"><a class="btn-primary" href="%s">Start here</a><a class="btn-ghost call" href="tel:%s" aria-label="Call %s">%s</a></div>\n' % (
           HOME_START, PHONE, PHONE_TXT, ico("phone", 22))),
       homejs='' if minimal else '<script src="/assets/js/home.js" defer></script>\n')

# ------------------------------------------------------------------ 1 hero

def _ans(i, who, text, kind, label, hot=False):
    """One answer row. The chip sits inside .at, so on a phone it can follow the text inline."""
    return '<li%s style="--i:%d">%s<span class="at"><span>%s</span>%s</span></li>' % (' class="hot"' if hot else '', i, av(who, 22), text, chip(kind, label))

def home_hero():
    rail = ''.join('<i%s>%s</i>' % (' class="on"' if k == "chat" else '', ico(k, 18)) for k in ("chat", "list", "folder", "calendar"))
    body1 = ('<p class="qyou"><b>You</b><span class="q">Where does the Maple Street job stand? What have we spent, what\'s missing, and what\'s blocking us?</span></p>'
             '<ul class="ans"><li class="say" style="--i:0">%s<span class="at"><b>Sara</b>I checked with Emma and Taylor. Here\'s where it stands.</span></li>'
             '%s%s%s%s</ul>') % (
        av("sara", 28, label=False),
        _ans(1, "emma", "Spent so far: 68% of the budget, matched to the invoices.", "verified", "Verified"),
        _ans(2, "sara", "Windows: the supplier hasn't confirmed the order.", "waiting", "Waiting on supplier"),   # procurement is Sara's (team.py)
        _ans(3, "taylor", "Electrical sub says a new quote is coming. Nothing in writing yet.", "reported", "Reported, not verified"),
        _ans(4, "sara", "Blocking: change order 3 isn't signed.", "needs", "Needs you", hot=True))
    w1 = ('<div class="win w1"><div class="wrail" aria-hidden="true">%s%s</div><div class="wpane">'
          '<div class="whead">%s<span class="crumb"><span class="c1">Maple Street<i aria-hidden="true">›</i></span><b>Ask Sara</b></span>'
          '<span class="wcrew">%s%s%s</span>%s</div><div class="wbody">%s</div></div></div>') % (
        bmark(24), rail, bmark(18), av("sara", 22), av("taylor", 22), av("emma", 22), SAMPLE, body1)
    yes = ''.join('<div class="yes"><div><b>%s</b><span>%s</span></div>%s</div>' % (t, n, fake_btns()) for t, n in [
        ("Change order 3", "Written by Richard, priced by Taylor"), ("Follow-up to the window supplier", "Drafted by Sara")])
    w2 = ('<div class="win w2"><div class="wpane"><div class="whead"><i class="wdot" aria-hidden="true"></i><b>Needs your yes · 2</b>%s</div>'
          '<div class="wbody">%s<p class="wfoot">%s Nothing goes out until you approve it.</p></div></div></div>') % (SAMPLE, yes, ico("lock", 14))
    return ('<section class="hs h-hero"><div class="lf" aria-hidden="true"><i></i></div><div class="wrap">'
            '<h1>An AI office crew<br class="dk"> for contractors.</h1>'
            '<p class="lede">Sara and her AI specialists prepare your bids, estimates, invoices and contract paperwork. '
            'You approve every price, signature, payment and send.</p>'
            '<a class="btn-primary lg" id="hero-start" href="%s">Start here <span class="arr" aria-hidden="true">→</span></a>'
            '<p class="h-alt"><span class="h-alt-t">A few quick questions.</span> <span class="h-or">Or</span> <a href="/book/">book a call</a><span class="h-sep" aria-hidden="true"> · </span><a href="tel:%s">%s</a></p>'
            '<figure class="h-vis" aria-label="Sample: Sara answers a question about a job">%s%s</figure>'
            '</div></section>\n') % (HOME_START, PHONE, PHONE_TXT, w1, w2)

# ------------------------------------------------------------------ 2 the rule (where beam has a customer quote: we have none)

def home_rule():
    return ('<section class="hs h-rule" aria-labelledby="rule-h"><div class="wrap">'
            '<h2 id="rule-h" class="sr">The rule every agent follows</h2>'
            '<figure class="rule rv"><blockquote><p>The crew prepares the work. Your people approve every price, signature, payment and send.</p></blockquote>'
            '<figcaption>%s<i class="vr"></i><span><b>How every BuildWithBNZ agent works</b><span>%s</span></span></figcaption></figure>'
            '<p class="rule-note rv rv-b">Built from real contractor workflows inside BNZ Builders, New York.</p>'
            '</div></section>\n') % (bmark(28), PRINCIPLE)

# ------------------------------------------------------------------ 3 how it works (pinned on desktop, stacked elsewhere)

def _rows(rows):
    return ''.join('<div class="row%s" style="--i:%d"><div><b>%s</b>%s</div>%s</div>' % (
        ' hot' if hot else '', i, b, '<span>%s</span>' % s if s else '', end) for i, (b, s, end, hot) in enumerate(rows))

def _step_vis():
    types = ''.join('<li%s>%s</li>' % (' class="on"' if i == 0 else '', t) for i, (_, t) in enumerate(START_TYPES))
    v1 = ('<figure class="st-vis ph rv" aria-label="Sample: the first question of the Start here form">'
          '<div class="phone">%s<p class="pn-s">Step 1 of 4</p><i class="pbar"><i></i></i>'
          '<p class="pn-q">What kind of work do you do?</p><ul class="pn-o">%s</ul><span class="pn-b" aria-hidden="true">Continue</span></div></figure>') % (SAMPLE, types)
    v2 = ('<figure class="st-vis rv" aria-label="Sample: what a Project Review covers"><div class="mock pcard">%s<p class="mt">Project Review</p>%s</div></figure>') % (SAMPLE, _rows([
        ("Your project", "12-unit renovation · bid due in 11 days", "", False),
        ("What you bring", "Drawings, specs, addenda, bid form", "", False),
        ("On the call", "You and someone from our team", "", False),
        ("What you see", "What the crew would do with it, live", "", False)]))
    v3 = ('<figure class="st-vis rv" aria-label="Sample: a scope document"><div class="mock pcard">%s<p class="mt">Scope · in writing</p>%s</div></figure>') % (SAMPLE, _rows([
        ("What Taylor does", "Takeoffs, the estimate, a conflict log", "", False),
        ("What Emma checks", "Job costs and invoices", "", False),
        ("What stays with you", "Every approval, every send, the signature", "", False),
        ("One set price", "Agreed before work starts", "", True)]))
    v4 = ('<figure class="st-vis rv" aria-label="Sample: the approvals queue"><div class="mock pcard">%s<p class="mt">Needs you · 3</p>%s</div></figure>') % (SAMPLE, _rows([
        ("Bid invitation to 4 electrical subs", "Drafted by Taylor", fake_btns(), False),
        ("Drywall sub's invoice matches the approved quote", "Checked by Emma", chip("verified", "Verified"), False),
        ("Monday report", "Drafted by Sara", chip("reported", "Drafted"), False)]))
    return [v1, v2, v3, v4]

STEPS4 = [
    ("Step 1 · Tell us", "Tell us how your company works.",
     "A few quick questions on your phone: what kind of work you do, and what you'd like the crew to take off your plate first.", ("Start here", HOME_START)),
    ("Step 2 · Project Review", "Walk us through one real job.",
     "A real call about one real project. Bring the drawings or the bid. We show you what the crew would do with it. Nothing gets connected.", ("Book a call", "/book/")),
    ("Step 3 · Scope and price", "Get the scope and one price, in writing.",
     "For that project. Price moves only if scope moves, and that sentence is in the document.", None),
    ("Step 4 · The crew works", "The crew works. You approve.",
     "They work inside the email, files and calendar you already use. Sara brings you a short list of decisions. Nothing goes out without your yes.", None),
]
# The step-4 chips (Gmail, Google Drive, Google Calendar, Notion) stay off until Adam confirms each one works for a
# customer today (STATUS.md: no OAuth yet).

def home_how():
    vis = _step_vis()
    steps = []
    for i, ((tag, h2, p, link), v) in enumerate(zip(STEPS4, vis)):
        a = '<a class="pill-link" href="%s">%s <span aria-hidden="true">›</span></a>' % (link[1], link[0]) if link else ''
        steps.append('<div class="st%s" data-i="%d"><div class="st-txt rv"><span class="tagp">%s</span><h2>%s</h2><p>%s</p>%s</div>%s</div>' % (
            ' on' if i == 0 else '', i, tag, h2, p, a, v))
    dots = ''.join('<button type="button" aria-label="Step %d"><i><b></b></i></button>' % (i + 1) for i in range(4))
    return ('<section class="hs h-how" id="how" aria-label="How it works"><div class="pin"><div class="wrap">'
            '<div class="steps4">%s<div class="dots" role="group" aria-label="Go to step">%s</div></div>'
            '</div></div></section>\n') % (''.join(steps), dots)

# ------------------------------------------------------------------ 4 + 5 the crew: line-up, then one card each

def _lu(slug):
    a = BY[slug]
    return '<li>%s<b>%s</b><span>%s</span></li>' % (av(slug, 64, label=False), tx(a["short"]), tx(a["title"]))

def _kyle_plan(concept):
    """A blueprint of a kitchen (left) and a living room (right): double-line walls, a door swing, counters, a sofa,
    a dimension line and a dotted grid. The concept opens the wall, adds an island and tints the open room."""
    k = 1 if concept else 0
    grid = ('<defs><pattern id="kg%d" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".6" fill="currentColor" stroke="none"/></pattern></defs>'
            '<rect width="200" height="120" fill="url(#kg%d)" stroke="none" opacity=".22"/>') % (k, k)
    room = '<rect class="rf" x="18" y="18" width="164" height="84"/>' if concept else ''
    wall = ('<path d="M98 18v12M102 18v12M98 30h4"/>' if concept else
            '<path d="M98 18v40M102 18v40M98 58h4M98 78v24M102 78v24M98 78h4"/><path class="thin" d="M102 78h20M102 58a20 20 0 0 1 20 20"/>')
    island = '<rect class="isl" x="78" y="52" width="44" height="13" rx="1.5"/>' if concept else ''
    return ('<svg viewBox="0 0 200 120" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '%s%s<rect x="14" y="14" width="172" height="92"/><rect x="18" y="18" width="164" height="84"/>%s'
            '<path class="thin" d="M22 22h56v9H31v35h-9z"/>'
            '<rect class="thin" x="136" y="84" width="40" height="12" rx="2"/><rect class="thin" x="146" y="64" width="20" height="10" rx="1.5"/>%s'
            '<path class="thin" d="M14 6v6M186 6v6M14 9h172"/>'
            '<text x="56" y="90" text-anchor="middle">Kitchen</text><text x="142" y="42" text-anchor="middle">Living</text></svg>') % (grid, room, wall, island)

def _card(slug, side, rule, vis="", cls="", text=None, note=None):
    a = BY[slug]
    tag = ('<span class="tagp jobs">On your jobs</span>' if side == "jobs" else '<span class="tagp ours">On our side</span>')
    notes = ''.join('<p class="bc-n">%s</p>' % tx(n) for n in [a["license"], note] if n)
    return ('<article class="bc%s rv" id="c-%s"><header class="bc-h">%s<div><div class="bc-nm"><h3>%s</h3>%s</div><p>%s</p></div></header>'
            '<div class="bc-x"><p class="bc-t">%s</p><p class="bc-l">%s<span>%s</span></p>%s</div>%s</article>') % (
        ' ' + cls if cls else '', slug, av(slug, 40, label=False), tx(a["name"]), tag, tx(a["title"]),
        tx(text or a["card"]), ico("check", 14), lim(slug, rule), notes, vis)

def home_crew():
    sara = BY["sara"]
    lineup = ('<div class="lu-stage"><figure class="lineup rv" aria-label="Sara Cooper leads six AI agents. On your jobs: Taylor, Emma, Richard and Kyle. On our side: Amanda and Adam.">'
              '<div class="lu-sara">%s<b>%s</b><span>%s</span></div>'
              '<div class="lu-groups"><div class="lu-g jobs"><p class="lu-label">On your jobs</p><ul>%s</ul></div>'
              '<div class="lu-g ours"><p class="lu-label">On our side</p><ul>%s</ul></div></div></figure></div>') % (
        av("sara", 96, anim=True, label=False), tx(sara["name"]), tx(sara["title"]),
        ''.join(_lu(s) for s in ("taylor", "emma", "richard", "kyle")), ''.join(_lu(s) for s in ("amanda", "adam")))

    sara_v = ('<div class="bc-v sara-v"><figure class="mock rv-s" aria-label="Sample: Sara\'s morning priorities">%s<p class="mt">Morning priorities</p>'
              '<div class="row you"><div><b>You</b><span>What needs me today?</span></div></div>'
              '<div class="row"><div class="msg">%s<div><b>Sara</b><span>Three things.</span></div></div></div>%s</figure>'
              '<div class="askwrap" aria-hidden="true"><div class="askbar"><span>Ask Sara: what does my company need to handle today?</span><i>%s</i></div></div></div>') % (
        SAMPLE, av("sara", 24, label=False), _rows([
            ("Thursday's bid: 4 pages need your ink signature", "", chip("needs", "Needs you"), False),
            ("Electrical quote still out", "", chip("waiting", "Waiting on sub"), False),
            ("Insurance certificate names the wrong holder", "", chip("needs", "Needs you"), False)]), ico("send", 18))
    taylor_v = '<figure class="bc-v mock rv-s scan" aria-label="Sample: estimate lines, each with a label">%s<p class="mt">Estimate lines</p>%s</figure>' % (SAMPLE, _rows([
        ("Slab on grade · 2,150 SF", "", chip("verified", "Verified"), False),
        ("Doors and frames · from sub", "", chip("quote", "Quote"), False),
        ("Site lighting", "", chip("estimate", "Estimate"), False),
        ("Plumbing fixtures · schedule not in the set", "", chip("unknown", "Unknown"), False)]))
    emma_v = ('<figure class="bc-v mock rv-s" aria-label="Sample: invoices checked against the job">%s<p class="mt">Invoices this week</p>%s'
              '<div class="line jbar"><span>Job cost: 68%% of budget</span><i><i style="width:68%%"></i></i></div></figure>') % (SAMPLE, _rows([
                  ("Drywall sub · invoice 14", "Matches the approved quote", chip("verified", "Verified"), False),
                  ("Plumber · invoice 9", "2 lines not in the contract", chip("needs", "Needs you"), False)]))
    richard_v = '<figure class="bc-v mock rv-s" aria-label="Sample: a change order">%s<p class="mt">Change order 3</p>%s</figure>' % (SAMPLE, _rows([
        ("Added: 2 windows, 2nd floor", "", "", False), ("Priced by Taylor", "", "", False),
        ("Signed before work starts", "", chip("needs", "Waiting for signature"), False)]))
    kyle_v = ('<figure class="bc-v mock kyle-v" aria-label="Sample: a before plan and a design concept">%s<p class="mt">Kitchen and living room</p>'
              '<div class="plans"><div class="pl before">%s<span>Before</span></div><div class="pl concept">%s<span>Concept</span></div></div>'
              '<p class="kchip">%s</p></figure>') % (SAMPLE, _kyle_plan(False), _kyle_plan(True), chip("verified", "Cost checked by Taylor"))
    you = ('<article class="bc you-c rv" id="c-you"><header class="bc-h"><span class="you-i">%s</span><div><div class="bc-nm"><h3>You</h3></div><p>Owner · the final say</p></div></header>'
           '<div class="bc-x"><p class="bc-t">You approve every price, signature, payment and send. The crew never makes the owner\'s decision.</p></div>%s</article>') % (
        ico("person", 22), ('<figure class="bc-v mock you-v" aria-label="Sample: a decision waiting for you">%s<p class="mt">Needs your yes</p>'
                            '<div class="row hot"><div><b>Change order 3</b><span>Written by Richard, priced by Taylor</span></div>%s</div></figure>') % (SAMPLE, fake_btns()))
    cards = (_card("sara", "jobs", "Nothing is sent without a person's go.", sara_v, "wide",
                   text=sara["card"].replace(" and reports to Bilal", ""))   # the reporting line belongs on /crew/
             + _card("taylor", "jobs", "Every number carries a label, such as VERIFIED, ESTIMATE, QUOTE or UNKNOWN.", taylor_v, "tall")
             + _card("emma", "jobs", "Nothing is posted until a person with authority approves it.", emma_v)
             + _card("richard", "jobs", "Contract review support only. Not legal advice.", richard_v)
             + _card("kyle", "jobs", "Concepts only. Never presented as signed or sealed drawings.", kyle_v)
             + _card("amanda", "ours", "Never claims a software feature that isn't live, or a project BNZ didn't do.", cls="short")
             + _card("adam", "ours", "Software releases need Bilal's explicit approval first.", cls="short", note=BY["adam"]["note"])
             + you)
    return ('<section class="hs h-crew" id="crew" aria-labelledby="crew-h"><div class="wrap">'
            '<div class="crew-head">'
            '<h2 id="crew-h" class="blurin">Meet the crew: seven AI agents, led by Sara. You stay in charge.</h2>'
            '<p class="lede rv">Sara leads six specialists. Four of them work on your jobs with her. Two work on BuildWithBNZ itself.</p></div>'
            '%s<div class="bento">%s</div>'
            '<p class="more rv rv-b"><a class="tlink" href="/crew/">See each agent\'s limits and human partner&nbsp;→</a></p>'
            '</div></section>\n') % (lineup, cards)

# ------------------------------------------------------------------ 6 how to read the answers (where beam has logos + a case study)

RULES = [("sara", "Never touches a price. Any change goes back to the estimator."),
         ("taylor", "A human estimator approves every price before it goes out."),
         ("sara", "Never calls a bid submitted without proof it arrived."),
         ("taylor", "Sara checks the bid, and nothing is submitted until you say send."),
         ("emma", "Your accountant or CPA reviews payroll and the books."),
         ("kyle", "Every design option goes to Taylor for quantities and cost before a client sees it."),
         ("richard", "Legal interpretations and consequential decisions go to human legal review."),
         ("sara", "Never fixes a problem silently. It comes to you.")]
LABELS = [("verified", "Verified", "Checked against the document itself."),
          ("reported", "Reported, not verified", "Someone said it. Nobody has checked it yet."),
          ("unknown", "Unknown", "Information is missing. The crew won't guess."),
          ("conflict", "Conflict", "Two documents disagree. Held for you, not smoothed over."),
          ("needs", "Needs you", "Waiting for your decision.")]

def home_read():
    tiles = ''.join('<li class="rv"><span>%s%s</span><p>%s</p></li>' % (av(s, 20, label=False), tx(BY[s]["short"]), lim(s, r)) for s, r in RULES)   # the agent first: a lead-in on a phone
    labels = ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (chip(k, t), m) for k, t, m in LABELS)
    return ('<section class="hs h-read" aria-labelledby="read-h"><div class="wrap">'
            '<h2 id="read-h" class="stmt blurin">No made-up numbers. <span>Every answer the crew gives you carries a label, so you can see what\'s been checked and what hasn\'t.</span></h2>'
            '<p class="stmt-l rv rv-b"><a class="tlink" href="/how-it-works/">See how it works&nbsp;→</a></p>'
            '<div class="read-grid"><ul class="rtiles" aria-label="Rules the crew follows">%s</ul>'
            '<div class="labels rv"><h3>The labels</h3><dl>%s</dl></div></div>'
            '</div></section>\n') % (tiles, labels)

# ------------------------------------------------------------------ 7 trust band (where beam has certification badges: we claim none)

TRUST = [("eye", "Read access first", "Nothing is moved or replaced."),
         ("folder", "One job at a time", "The crew sees the project you pick, not your whole drive."),
         ("check", "You approve every send", "Emails, prices, signatures and payments wait for you."),
         ("lock", "Your files stay yours", "They stay in your systems. Nothing is copied out to train AI."),   # Adam to confirm (same promise as the FAQ)
         ("tag", "Every answer labeled", "Verified, reported or unknown. Never a guess."),
         ("person", "A person behind every agent", "Each agent works with a named person on our team.")]

def home_trust():
    cells = ''.join('<li class="rv"><span class="tc-i">%s</span><b>%s</b><span>%s</span></li>' % (ico(i), t, l) for i, t, l in TRUST)
    return ('<section class="hs h-trust" aria-labelledby="trust-h"><div class="wrap">'
            '<div class="center rv"><h2 id="trust-h">Your files, your numbers, your call.</h2>'
            '<p class="lede">Plain rules for how the crew handles your files, your numbers and anything that goes out.</p></div>'
            '<ul class="tcells">%s</ul></div></section>\n') % cells

# ------------------------------------------------------------------ 8 questions (not on beam; kept to four)

HOME_FAQ = [
    ("What does it cost?", "It starts with a Project Review: a real call about one real project. Then we send you the scope and one set price "
     "for that project, in writing. Price moves only if scope moves."),
    ("Do I have to change my software?", "No. The crew works inside the email, files and calendar you already use. Nothing is moved or "
     "replaced, and it starts with read access."),
    ("Does the AI send anything without me?", "No. Every email, price, signature and payment waits for your yes. The crew drafts. You decide."),
    ("Is this for my company?", "It's built for general contractors, remodelers and custom builders, specialty contractors, and GCs bidding "
     "public work. Not sure? Call <a href=\"tel:%s\">%s</a>." % (PHONE, PHONE_TXT)),
]

def home_faq():
    items = ''.join('<details%s><summary><span>%s</span><i class="pm" aria-hidden="true"></i></summary><div class="a"><p>%s</p></div></details>' % (
        ' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(HOME_FAQ))
    return ('<section class="hs h-faq" id="faq" aria-labelledby="faq-h"><div class="wrap">'
            '<div class="rv"><h2 id="faq-h">Questions contractors ask first.</h2><p><a class="tlink" href="/faq/">All questions&nbsp;→</a></p></div>'
            '<div class="hfaq rv">%s</div></div></section>\n') % items

# ------------------------------------------------------------------ 9 final call to action

def home_cta():
    return ('<section class="h-cta" aria-labelledby="cta-h"><div class="wrap">'
            '<h2 id="cta-h" class="blurin">Run the company. Keep every decision.</h2>'
            '<p class="cta-sub">Answer a few questions about your company. A real person gets back to you the same business day.</p>'
            '<div class="cta-b"><a class="btn-primary lg" href="%s">Start here</a><a class="btn-ghost lg" href="/book/">Book a call</a></div>'
            '<p class="cta-call">Or call <a href="tel:%s">%s</a></p>'
            '</div></section>\n') % (HOME_START, PHONE, PHONE_TXT)

def page_home():
    title = "AI Office Crew for Contractors | BuildWithBNZ"
    desc = ("Sara and her AI crew prepare bids, estimates, invoices and contract paperwork for contractors. "
            "You approve every price, signature, payment and send.")
    ld = ('{"@context":"https://schema.org","@graph":[{"@type":"Organization","name":"BuildWithBNZ","url":"%s","email":"%s","telephone":"%s","areaServed":"New York","description":"AI office crew for construction companies."},'
          '{"@type":"WebSite","name":"BuildWithBNZ","url":"%s"}]}') % (SITE, INBOX, PHONE_LD, SITE)
    h = head(title, desc, "/", jsonld=ld, body_attrs='class="home" data-colorway="a"', extra_css="/assets/css/home.css")
    h += nav_home()
    h += home_hero() + home_rule() + home_how() + home_crew() + home_read() + home_trust() + home_faq() + home_cta()
    h += footer_home()
    return h
