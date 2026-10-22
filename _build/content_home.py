# -*- coding: utf-8 -*-
from shared import *

def hero(eyebrow, h1, para, mock, cta=True, second=None):
    ctas = ('<div class="cta">%s%s</div>' % (btn_book(), second or '<a class="link" href="/how-it-works/">See how it works</a>')) if cta else ''
    return ('<section class="dark hero"><div class="wrap"><div class="fx"><span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lede">%s</p>%s</div><div class="fx">%s</div></div></section>\n') % (eyebrow, h1, para, ctas, mock)

WHO = [
    ("General contractors", "Bid more work without adding estimating headcount."),
    ("Remodelers &amp; custom builders", "Estimates and subs that keep pace with change orders."),
    ("Specialty contractors", "Your niche, your units, your production rates — learned once."),
    ("GCs bidding public work", "Prevailing wage, addenda and bid forms handled by the book."),
]

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

# ------------------------------------------------------------------ Sara on the home page
# What BuildWithBNZ is (Team Guide p3, Brand Kit p1), Sara's six (02 Sara), and four SAMPLE conversations, each tied to
# a capability the sources state (EXEC p13, REVIEW p2, Bid Submission Desk pp1-2). No real names, jobs or figures.

SARA_ASKS = ["Projects", "Deadlines", "Email + calendar", "Approvals", "Risks", "Priorities"]

def _you(text):
    return '<div class="row you"><div><b>You</b><span>%s</span></div></div>' % text

def _sara(text, state=None):
    return '<div class="row"><div class="msg">%s<div><b>Sara</b><span>%s</span></div></div>%s</div>' % (av("sara", 28), text, chip(*state) if state else '')

def _item(text, state):
    return '<div class="row"><div><b>%s</b></div>%s</div>' % (text, chip(*state))

def sara_examples():
    convos = [
        ("Morning priorities", _you("What needs me today?") + _sara("Three things.")
         + _item("Thursday's bid: 4 pages need your ink signature", ("needs", "Needs you"))
         + _item("Electrical quote still out", ("waiting", "Waiting on sub"))
         + _item("Insurance certificate names the wrong holder", ("needs", "Needs you"))),
        ("Before the bid is sealed", _you("Is the bid ready to go?")
         + _sara("Not yet. I checked the five things that get a bid thrown out: late, unsigned, incomplete, wrong certificates, bond short. Two are open.")
         + _sara("It stays Not submitted until tracking shows it was delivered.", ("reported", "Not submitted"))),
        ("Urgent alert", _sara("A new addendum was posted for Thursday's bid. Taylor is checking what changed.", ("working", "Checking"))
         + _sara("Your price stays exactly as you approved it until the estimator says otherwise.")),
        ("End of day", _you("What got done?")
         + _item("Done: bid forms filled in the owner's order", ("verified", "Verified"))
         + _item("Open: notary pages", ("waiting", "Open"))
         + _item("Send the packet to your office", ("needs", "Needs your yes"))),
    ]
    return '<div class="grid g2 stagger convos">%s</div>' % ''.join(
        '<div class="mock rows convo"><span class="sd">Sample</span><div class="eyebrow mute ct">%s</div>%s</div>' % (t, body) for t, body in convos)

def sara_section():
    intro = ('<div class="split sara-intro"><div class="fx">%s</div><div class="fx">'
             '<span class="eyebrow">Meet Sara · AI team leader</span><h2 class="sara-h">Sara runs the day.</h2>'
             '<p class="lede">BuildWithBNZ gives your company a team of seven AI agents for the office side of construction: '
             'bids, paperwork, deadlines and records. Sara leads them. They prepare the work. Your people approve every price, '
             'signature, payment and send, and your crews and subs still build the job. Built from real contractor workflows inside BNZ Builders.</p>'
             '<div class="asks"><p>Ask her: <b>"What does my company need to handle today?"</b></p><ul class="pills">%s</ul></div>'
             '<div class="sara-cta">%s%s</div><p class="small muted sara-note">Bring one bid. We\'ll walk through what Sara would do with it.</p>'
             '</div></div>') % (portrait("sara"), ''.join('<li>%s</li>' % x for x in SARA_ASKS),
                                btn_book(label="Book a demo"), START_BTN)
    ex = ('<div class="sara-ex"><div class="fx"><span class="eyebrow">How she works</span><h3 class="ex-h">Four sample conversations</h3>'
          '<p class="small muted">Samples only. No real names, jobs or numbers.</p></div>%s</div>') % sara_examples()
    team = ('<div class="team-strip fx"><span class="eyebrow mute">Her team · all six report to Sara · AI-generated characters</span><ul>%s</ul>'
            '<p style="margin-top:20px"><a class="link" href="/crew/">Meet the AI crew →</a></p></div>') % ''.join(
        '<li><a href="/crew/#%s">%s<b>%s</b><span>%s</span></a></li>' % (a["slug"], av(a["slug"], 56), tx(a["name"]), tx(a["title"])) for a in SIX)
    return intro + ex + team

def steps_grid(rows=False):
    out = []
    for i, (t, p, o, c) in enumerate(STEPS, 1):
        out.append('<div class="card step"><div class="num"><span class="count" data-count="%d" data-dur="240" data-pad="0">00</span></div><h3>%s</h3><p>%s</p>'
                   '<div class="oc"><div><b>Output:</b> %s</div><div><b>Control:</b> %s</div></div></div>' % (i, t, p, o, c))
    return '<div class="steps stagger%s">%s</div>' % (' rows' if rows else '', ''.join(out))

def work_cards():
    c1 = ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Intake summary</div>'
          '<div class="row"><div><b>Rockland Mixed-Use · 38 Units</b><span>Public work, prevailing wage · bid due in 11 days</span></div></div>'
          '<div class="row"><div><b>Package</b><span>Drawing set (142 sheets), specs, Addendum 01–02, wage schedule, bid form</span></div></div>'
          '<div class="row"><div><b>On it today</b><span>Owner + one PM</span></div></div>'
          '<div class="row"><div><b>Pain named on the call</b><span>Estimating bottleneck, sub follow-up</span></div></div>'
          '<div class="line"><b>What the crew would do with it</b> → walked through live</div></div>')
    c2 = ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Scope document · in writing</div>'
          '<div class="row"><div><b>What Taylor does</b><span>Takeoffs, estimate Rev 1, conflict log</span></div></div>'
          '<div class="row"><div><b>What Emma checks</b><span>Job costs and invoices</span></div></div>'
          '<div class="row"><div><b>What stays with you</b><span>Every approval, every send, the signature</span></div></div>'
          '<div class="row needs"><div><b>One set price</b><span>Agreed before work starts</span></div></div></div>')
    c3 = ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Project page</div>'
          '<div class="row"><div><b>Estimate Rev 2</b></div>%s</div>'
          '<div class="row"><div><b>Sub quotes · electrical</b></div>%s</div>'
          '<div class="row"><div><b>Bid form draft</b></div>%s</div>'
          '<div class="row needs"><div><b>Approve invitation · 4 subs</b></div>%s</div></div>') % (
        chip("working", "Working", True), chip("waiting", "Waiting on"), chip("verified", "Verified"), chip("needs", "Needs you"))
    cards = [
        ("The project review", c1, "A real call about one real project. No connection, no commitment — a walkthrough."),
        ("Scoped and priced", c2, "Price moves only if scope moves. That sentence is in the document."),
        ("Live in your workspace", c3, "The project page the crew and you share — files, estimate, subs, approvals."),
    ]
    return '<div class="grid g3 stagger work">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3>%s<p>%s</p></div>' % (t, m, p) for t, m, p in cards)

def proof():
    # The "one real project" card with empty metric slots is gone until Bilal approves a real, sourced example
    # (FINAL rule 4/5: no results in an agent's name, and BNZ Builders jobs are not BuildWithBNZ proof).
    return ('<div class="grid g2 stagger proof">'
            '<div class="card"><h3>The rules, stated as guarantees</h3>'
            '<blockquote>"Sara never claims something was completed unless verified. Never makes the owner\'s decision."</blockquote>'
            '<blockquote>"Taylor never invents a price. Says UNKNOWN when information is missing and always shows the logic."</blockquote>'
            '<blockquote>"Emma reviews and recommends. She never posts transactions or changes accounting records without authorization."</blockquote></div>'
            '<div class="card"><h3>How the crew catches its own mistakes</h3><p class="muted" style="margin-top:10px">Every estimate line, sub quote and claim is cross-checked before it reaches you. When two sources disagree — a spec section against a drawing sheet, a quote against a leveled scope — the item is flagged CONFLICT and held, not smoothed over. Anything the crew was told but hasn\'t confirmed stays marked REPORTED — NOT VERIFIED until it\'s checked against the document itself.</p></div>'
            '</div>')

def page_home():
    desc = "AI operating system for construction companies: seven AI agents led by Sara handle estimating, bids, paperwork and job costs. You approve every send."
    ld = ('{"@context":"https://schema.org","@graph":[{"@type":"Organization","name":"BuildWithBNZ","url":"%s","email":"%s","telephone":"%s","areaServed":"New York","description":"AI operating system for construction companies."},'
          '{"@type":"WebSite","name":"BuildWithBNZ","url":"%s"}]}') % (SITE, INBOX, PHONE_LD, SITE)
    h = head("AI Operating System for Construction Companies | BNZ", desc, "/", jsonld=ld)
    h += nav("/")
    h += hero("AI operating system for construction companies", "Run the company. Keep every decision.",
              TEAM_LEDE,
              sample_project_mock(), second=START_BTN)
    h += section("light strip", '<div class="cells stagger">%s</div>' % ''.join('<div><h3>%s</h3><p>%s</p></div>' % w for w in WHO))
    h += section("dark", sara_section(), id_="crew")
    h += section("light", sec_head("How it works", "Six steps to a project that runs itself.") + steps_grid(), id_="how-it-works")
    h += section("dark", sec_head("The work", "What you actually get.") + work_cards())
    h += section("light", '<div class="split"><div class="fx"><span class="eyebrow">Ongoing operations</span><h2 style="margin:14px 0 14px">Reported every Monday.</h2>'
                 '<p class="lede">After the first project, the crew stays on under a separate monthly arrangement. We host it, monitor it, add your next projects, and stay responsible for it working.</p></div>'
                 '<div class="fx">%s</div></div>' % monday_mock(), id_="ongoing")
    h += section("dark", sec_head("Proof", "Proof, not logos.") + proof())
    h += section("light", sec_head("What we connect to", "The systems the crew works inside.",
                                   "Keep your tools. Nothing is moved or replaced — read access first, and you approve anything that leaves.") + integrations(rows=2)
                 + '<p style="margin-top:18px"><a class="link" href="/what-we-connect-to/">Full list, and what each one does →</a></p>', id_="connect")
    h += section("dark", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h2 style="margin-top:14px">Asked on every call.</h2></div><div class="fx">%s</div></div>' % faq_items(FAQ), id_="faq")
    h += book_strip()
    h += footer()
    return h
