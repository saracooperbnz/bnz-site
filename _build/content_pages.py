# -*- coding: utf-8 -*-
from shared import *
from content_home import hero, STEPS, nav_home, footer_home, ico

# ------------------------------------------------------------------ A8 solutions

def est_mock(moment=False):
    basis = ('<span data-type="Wage sched. line 16 × takeoff; waste 5%">Wage sched. line 16 × takeoff; waste 5%</span>' if moment
             else 'Wage sched. line 16 × takeoff; waste 5%')
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Estimate excerpt · division 26</div>'
            '<table><thead><tr><th>Line item</th><th>Qty</th><th>Unit</th><th>Source</th><th>Basis</th></tr></thead><tbody>'
            '<tr><td>Branch wiring · floors 2–4</td><td>38,400</td><td>LF</td><td class="mute">E-402–E-405</td><td class="mute">%s</td></tr>'
            '<tr><td>Light fixtures %s</td><td>—</td><td>EA</td><td class="mute">Fixture schedule</td><td class="mute">Not in the set — request from architect</td></tr>'
            '</tbody></table><div class="line">Total withheld until 2 UNKNOWN items resolved</div></div>') % (basis, chip("unknown", "Unknown"))

def bids_mock(moment=False):
    q2 = '<span data-swap="Received">Not received</span>' if moment else 'Not received'
    s2 = ('<span class="chip levelled" data-swap="Leveled|chip levelled">Gap — 2 items</span>'.replace('class="chip levelled"', 'class="chip conflict"') if moment else chip("conflict", "Gap — 2 items"))
    a2 = '<span data-swap="None — ready for your review">Chasing — 2nd follow-up sent Tue</span>' if moment else 'Chasing — 2nd follow-up sent Tue'
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Electrical bids</div>'
            '<table><thead><tr><th>Sub</th><th>Quote</th><th>COI</th><th>W-9</th><th>Scope</th><th>Next action</th></tr></thead><tbody>'
            '<tr><td>Garnerville Line &amp; Load</td><td>Received</td><td>✓</td><td>✓</td><td>%s</td><td class="mute">None — ready for your review</td></tr>'
            '<tr><td>Hudson Feeder Co.</td><td>%s</td><td>✓</td><td>✓</td><td>%s</td><td class="mute">%s</td></tr>'
            '<tr><td>Spring Valley Power</td><td>Received</td><td class="mute">exp. Fri</td><td>✓</td><td>%s</td><td class="mute">COI renewal needed</td></tr>'
            '</tbody></table><div class="line">Quote amounts are shown as received / not received. Figures live in the leveling sheet.</div></div>') % (
        chip("levelled", "Leveled"), q2, s2, a2, chip("levelled", "Leveled"))

def finance_mock(moment=False):
    return ('<div class="mock rows"><span class="sd">Sample layout</span><div class="eyebrow mute" style="margin-bottom:8px">Reconciliation review</div>'
            '<div class="row"><div><b>Matched</b><span>Entries that agree with the record</span></div><span class="mval">—</span></div>'
            '<div class="row"><div><b>Needs a job assigned</b><span>Entries with no job yet</span></div><span class="mval">—</span></div>'
            '<div class="row needs"><div><b>Duplicate risk</b><span>Held for a person to decide</span></div>%s</div>'
            '<div class="line"><b>Checkpoint:</b> Emma reviews → Emma recommends → Sara logs it → a person with authority approves → an approved person posts</div>'
            '<div class="line">No figures shown. Emma never posts or edits records without authorization.</div></div>') % chip("needs", "Needs approval")

def today_mock(moment=False):
    slide = ' data-slide' if moment else ''
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Today</div>'
            '<div class="cols">'
            '<div class="col needs"><h5>Needs you</h5><div class="row needs"%s><div><b>Approve request to architect</b></div></div><div class="row needs"><div><b>Bid invitation · 4 subs</b></div></div></div>'
            '<div class="col"><h5>In progress</h5><div class="row"><div><b>Estimate Rev 2</b></div>%s</div><div class="row"><div><b>Chasing 2 quotes</b></div>%s</div></div>'
            '<div class="col"><h5>Done</h5><div class="row"><div><b>3 sub quotes logged</b></div>%s</div><div class="row"><div><b>Wage schedule matched</b></div>%s</div></div>'
            '</div></div>') % (slide, chip("working", "Working", True), chip("chasing", "Chasing"),
                               ('<span class="chip reported" data-swap="Verified|chip verified">Reported</span>' if moment else chip("reported", "Reported")),
                               chip("verified", "Verified"))

def public_mock(moment=False):
    v = '<span class="chip reported" data-swap="Verified|chip verified">Checking</span>' if moment else chip("verified", "Verified")
    return ('<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">Project files · public work</div>'
            '<div class="row"><div><b>Prevailing wage schedule · Rockland Co.</b><span>✓ read by Taylor</span></div></div>'
            '<div class="row"><div><b>Addendum 02</b><span>✓ read by Taylor</span></div></div>'
            '<div class="row"><div><b>Bid form</b><span>✓ read by Taylor</span></div></div>'
            '<div class="eyebrow mute" style="margin:14px 0 4px">Cross-check result</div>'
            '<div class="row"><div><b>Wage schedule matched to county</b></div>%s</div>'
            '<div class="row"><div><b>Addendum 03 per architect\'s office</b></div>%s</div></div>') % (v, chip("reported", "Reported — not verified"))

SOLUTIONS = [
    ("t", "Taylor · solution 1 of 4", "Estimating &amp; takeoff",
     "Taylor takes the full bid package — drawings, specs, addenda, wage schedules, bid forms. She performs takeoffs, flags conflicts between sheets and specs, and prices labor, material and sub lines. Every line traces to a sheet or a spec section; missing information reads UNKNOWN, with the reason and who has it.",
     "an estimate with its logic attached.", "Taylor says UNKNOWN rather than guessing.", est_mock, "/construction-estimating-ai/"),
    ("t", "Taylor · solution 2 of 4", "Subcontractor bidding &amp; buyout",
     "Taylor requests and compares sub and vendor pricing and levels each quote against her estimate, line by line. Requests for pricing go out only after you approve them. Sara tracks the deadlines and what is still open on each bid.",
     "a leveled bid table per trade.", "nothing goes to a sub without your approval.", bids_mock, "/subcontractor-procurement/"),
    ("s", "Sara · solution 3 of 4", "Operations &amp; approvals",
     "Sara runs Today, the approvals queue and the Monday report. She supervises the other six agents, catches what falls between them, and marks every claim Verified or Reported — never blending the two. What reaches you is a short queue of real decisions.",
     "a Monday report and an approvals queue.", "she brings you only the decisions that need you. You sign. She doesn't.", today_mock, "/construction-project-management-ai/"),
    ("t", "Taylor + Emma · solution 4 of 4", "Public work &amp; prevailing wage",
     "Wage schedules, addenda, bid forms and certified payroll documents handled by the book. Taylor matches the wage schedule to the county and prices to it line by line; Emma verifies payroll against it. Anything the crew was told but hasn't confirmed stays marked Reported until it's checked against the document itself.",
     "bid forms and payroll docs that pass review.", "every claim is checked against the document itself.", public_mock, "/prevailing-wage-project-management/"),
]

def diagram():
    six = ''.join('<li>%s<b>%s</b><span>%s</span></li>' % (av(a["slug"], 56), tx(a["short"]), tx(a["title"])) for a in SIX)
    return ('<div class="diagram fx"><div class="owner">You — the owner</div><div class="arrow">↑ you approve every price, signature and send</div>'
            '<div class="lead">%s<b>Sara Cooper</b><span>%s</span></div>'
            '<ul class="six" aria-label="The six agents who report to Sara">%s</ul>'
            '<p class="small muted dia-cap">Inside BuildWithBNZ, Sara reports to Bilal Mohammed. On your project, the decisions are yours.</p></div>') % (
        av("sara", 112), tx(BY["sara"]["title"]), six)

def page_solutions():
    desc = "Four solutions, one crew: estimating & takeoff, subcontractor bidding & buyout, operations & approvals, and public work & prevailing wage."
    h = head("AI Construction Estimating, Bidding & Ops | BuildWithBNZ", desc, "/solutions/")
    h += nav()
    h += hero("Solutions", "The job, not the software.",
              "Every solution below is one part of one crew, working inside one project workspace. Pick the problem that hurts; the rest of the crew comes with it.",
              sample_project_mock())
    cards = []
    for who, eyebrow, title, p, out, ctl, mock, href in SOLUTIONS:
        color = {"t": "var(--taylor)", "e": "var(--emma)", "s": "var(--ember)"}[who]
        cards.append('<article class="scard"><div><span class="eyebrow" style="color:%s">%s</span><h3 style="margin-top:12px;font-size:clamp(24px,3vw,36px)">%s</h3><p>%s</p>'
                     '<div class="oc"><div><b>Output:</b> %s</div><div><b>Control:</b> %s</div></div>'
                     '<p style="margin-top:16px"><a class="link" href="%s">Read the full page →</a></p></div>%s</article>' % (
                         color, eyebrow, title, p, out, ctl, href, mock(True)))
    h += section("dark", '<div class="stack">%s</div>' % ''.join(cards), id_="solutions")
    h += section("light", sec_head("One crew", "One crew. Whichever door you came in.",
                                   "Pick one solution and the other three come with it — same workspace, same rules, same approvals queue.") + diagram())
    h += section("dark", sec_head("What we connect to", "The systems the crew works inside.",
                                   "Keep your tools. Nothing is moved or replaced — read access first, and you approve anything that leaves.") + integrations(), id_="connect")
    h += section("light", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h2 style="margin-top:14px">Asked on every call.</h2></div><div class="fx">%s</div></div>' % faq_items([FAQ[0], FAQ[3], FAQ[2], FAQ[7]], 0))
    h += book_strip(dark=True)
    h += footer()
    return h

# ------------------------------------------------------------------ A2 crew

def org_chart():
    """REVIEW p1: Bilal (final authority) > Sara Cooper > the six. Nested lists so screen readers hear the hierarchy."""
    sara = BY["sara"]
    six = ''.join('<li%s><a href="#%s">%s<b>%s</b><span>%s</span></a></li>' % (
        ' class="acc" style="--acc:%s"' % a["accent"] if a["accent"] else '', a["slug"], thumb(a["slug"]), tx(a["name"]), tx(a["title"])) for a in SIX)
    return ('<div class="org-wrap"><ul class="org" aria-label="Reporting line">'
            '<li><div class="org-boss"><span class="eyebrow">Final authority</span><b>Bilal Mohammed</b></div>'
            '<ul><li class="org-mid"><a class="org-lead" href="#sara" style="--acc:%s">%s<b>%s</b><span>%s</span></a>'
            '<ul class="org-six">%s</ul></li></ul></li></ul>'
            '<p class="org-cap">All seven agents are AI-generated characters. Bilal Mohammed is a real person.</p></div>') % (
        sara["accent"], thumb("sara"), tx(sara["name"]), tx(sara["title"]), six)

def agent_card(a, lead=False):
    acc = ' style="--acc:%s"' % a["accent"] if a["accent"] else ''
    name = tx(a["name"]) + (' <small>(%s)</small>' % a["pronoun"] if a["pronoun"] else '')
    ident = '<div class="ac-id"><span class="ac-n">%s / 07</span><h3>%s</h3><p class="ac-title">%s</p></div>' % (a["n"], name, tx(a["title"]))
    meta = '<dl class="ac-meta"><div><dt>%s</dt><dd>%s</dd></div><div><dt>Reports to</dt><dd>%s</dd></div></dl>' % (
        a["partners_label"], tx(a["partners"]), tx(a["reports_to"]))
    badge = '<p class="ac-badge">%s</p>' % tx(a["license"]) if a["license"] else ''
    note = '<p class="ac-note">%s</p>' % tx(a["note"]) if a.get("note") else ''
    body = ('%s%s<p class="ac-h">Role</p><p class="ac-role">%s</p>%s<p class="ac-h">%s</p><ul class="ac-limits">%s</ul>%s') % (
        meta, badge, tx(a["role"]), note, a.get("limits_label", "Approval limits"), ''.join('<li>%s</li>' % tx(l) for l in a["limits"]),
        '<p class="ac-more"><a class="link" href="%s">Meet %s →</a></p>' % (a["page"], a["short"]) if a["page"] else '')
    pic = portrait(a["slug"])
    if lead:
        return '<article class="card agent-card lead%s" id="%s"%s>%s<div class="ac-main">%s%s</div></article>' % (' acc' if acc else '', a["slug"], acc, pic, ident, body)
    return '<article class="card agent-card%s" id="%s"%s><div class="ac-head">%s%s</div>%s</article>' % (' acc' if acc else '', a["slug"], acc, pic, ident, body)

def team_flow():
    """EXEC p19: how the team works together, in plain words. Platform and model names deliberately left out.
    EXEC is BuildWithBNZ's internal handbook (Bilal approves); for a customer the yes is theirs (GUIDE p5, DESK p1)."""
    par = [("taylor", "checks quantities and costs."), ("kyle", "handles designs and concepts."), ("emma", "reviews the money side."),
           ("richard", "checks contract risk."), ("amanda", "turns approved results into content.")]
    return ('<ol class="flow stagger">'
            '<li><b>A goal comes in.</b></li>'
            '<li><b>Sara hands out the work.</b></li>'
            '<li><b>Each specialist does their part</b> and checks with the others.<ul>%s</ul></li>'
            '<li><b>Sara checks everyone\'s work and pulls it together.</b></li>'
            '<li><b>A person says yes</b> before anything is sent, spent, published or changed in the books.</li></ol>'
            '<p class="small muted fx" style="margin-top:18px">Inside BuildWithBNZ, that person is Bilal Mohammed. On your projects, it is your own people.</p>') % (
        ''.join('<li>%s<span><b>%s</b> %s</span></li>' % (av(k, 32), BY[k]["short"], t) for k, t in par))

def page_crew():
    desc = "Seven AI agents for the office side of construction, led by Sara Cooper: bids, paperwork, deadlines and records. Every agent works with a human partner."
    h = head("AI Team for Construction Companies: 7 Agents | BuildWithBNZ", desc, "/crew/")
    h += nav("/crew/")
    intro = ('<div class="team-intro"><div class="fx"><span class="eyebrow">Official AI team</span><h1 class="team-h">Meet the AI team</h1>'
             '<p class="lede">Seven AI agents for the office side of construction: bids, paperwork, deadlines and records. Sara Cooper leads them. '
             'Every agent works with a human partner. %s</p>'
             '<div class="report-box"><span class="eyebrow mute">Reporting line</span><p>All six agents report to Sara Cooper. Sara reports to Bilal Mohammed, '
             'a real person and the final authority over BuildWithBNZ\'s AI team. On your projects, your own people approve every price, signature and send.</p></div>'
             '<div class="cta">%s%s</div></div>'
             '<div class="fx">%s</div></div>') % (PRINCIPLE, btn_book(), START_BTN, org_chart())
    h += section("dark", intro, extra_cls="first team-top")
    cards = agent_card(BY["sara"], lead=True) + '<div class="agent-grid">%s</div>' % ''.join(agent_card(a) for a in SIX)
    h += section("light", sec_head("The team", "Seven agents. One team.", "Each card shows the agent's title, human partner, who they report to, their role and their approval limits. %s" % PRINCIPLE, dark=False) + cards
                 + '<p class="footnote">All seven are AI-generated characters, not real people. Every agent works with a human partner.</p>', id_="team")
    h += section("dark", '<div class="split flow-split"><div class="fx"><span class="eyebrow">How they work together</span>'
                 '<h2 style="margin:14px 0 14px">Sara sits at the center.</h2>'
                 '<p class="lede">The specialists talk to each other directly. Sara checks everyone\'s work and pulls it together. Nothing is sent, awarded, signed or paid without a person\'s yes.</p></div>'
                 '<div>%s</div></div>' % team_flow())
    h += section("light", sec_head("Each one, in depth", "Go deeper on one.", dark=False) +
                 '<div class="grid g3 stagger">%s</div>' % ''.join(
                     '<a class="card" href="%s">%s<h3 style="margin-top:14px">%s</h3><p class="muted" style="margin:8px 0 12px">%s</p><span class="link">Meet %s →</span></a>' % (
                         a["page"], av(a["slug"], 64), tx(a["name"]), tx(a["title"]), a["short"]) for a in AGENTS if a["page"]), extra_cls="deeper")
    h += book_strip(dark=True)
    h += footer()
    return h

# ------------------------------------------------------------------ A5 agent pages

# Page copy for the three agents that have their own page. Title, desc and h1 are the live SEO strings, except
# Emma's title and desc, which described an older sub-coordination role (fixed Oct 2026 to match team.py).
# Everything else follows FINAL / REVIEW (see team.py).
AGENT_PAGES = {
    "sara": dict(title="Sara — Sara runs the company's day | BuildWithBNZ", h1="Sara runs the company's day.",
                 checks=["Runs the Today board — what needs you, what's in progress, what's done",
                         "Assigns and supervises the work of the other six agents",
                         "Gives morning priorities, evening results and urgent alerts",
                         "Keeps one approvals queue — every send waits on you",
                         "Marks every claim Verified or Reported — never blends them",
                         "Checks every page of a bid packet before it is sealed",
                         "Drafts the Monday report"],
                 rule="Never claims something was completed unless verified. Never makes the owner's decision.",
                 states=[("verified", "Verified"), ("reported", "Reported — not verified")],
                 states_note="Verified means checked against the document. Reported means someone said so. Sara never lets one look like the other.",
                 mock_label="Today — her board", mock=lambda: today_mock(False),
                 desc="Sara is the construction COO in the BuildWithBNZ crew: Today board, approvals queue, Monday report. Never claims done unless verified."),
    "taylor": dict(title="Taylor — Taylor reads every sheet | BuildWithBNZ", h1="Taylor reads every sheet.",
                   checks=["Finds and qualifies bid opportunities",
                           "Reads the drawings, specs, addenda, wage schedule and bid form",
                           "Performs takeoffs and flags conflicts between sheets and specs",
                           "Builds labor estimates with prevailing wage where it applies",
                           "Requests and compares sub and vendor pricing",
                           "Prepares the bid package with assumptions, sources and revision history"],
                   rule="Never makes up a quantity, quote or price. Says UNKNOWN when information is missing and always shows the logic.",
                   states=[("unknown", "Unknown"), ("showing", "Showing the work"), ("working", "Revising")],
                   states_note="UNKNOWN is deliberate: it names what's missing and who has it. It is never a blank.",
                   mock_label="Her part of the workspace — estimate, division 26", mock=lambda: est_mock(False),
                   desc="Taylor is the BuildWithBNZ estimating agent: takeoffs, conflicts, labor/material/sub pricing, every assumption shown. Never invents a price."),
    "emma": dict(title="Emma: AI Job Costing & Construction Accounting | BNZ", h1="Emma checks the job costs.", checks_h="What she covers",
                 checks=["Keeps job costing for each project",
                         "Reviews reconciliations against the books",
                         "Verifies payroll",
                         "Tracks invoices, payables and receivables",
                         "Prepares cash-flow reports",
                         "Recommends — a person with authority approves and posts"],
                 rule="She reviews and recommends. She does not post transactions or change accounting records without authorization.",
                 states=[("working", "Reviewing"), ("needs", "Needs approval"), ("verified", "Verified")],
                 states_note="Nothing is posted until a person with authority approves it. Your accountant or CPA reviews payroll and the books. QuickBooks is not connected.",
                 mock_label="Her part of the workspace — reconciliation review", mock=lambda: finance_mock(False),
                 desc="Emma is the BuildWithBNZ finance agent: job costing, invoices, payables and receivables, payroll checks and cash-flow reports. She reviews and recommends."),
}

def page_agent(slug):
    p = AGENT_PAGES[slug]; a = BY[slug]
    h = head(p["title"], p["desc"], "/%s/" % slug)
    h += nav()
    name = tx(a["name"]) + (' <small>(%s)</small>' % a["pronoun"] if a["pronoun"] else '')
    meta = '<dl class="ac-meta"><div><dt>%s</dt><dd>%s</dd></div><div><dt>Reports to</dt><dd>%s</dd></div></dl>' % (
        a["partners_label"], tx(a["partners"]), tx(a["reports_to"]))
    h += ('<section class="dark agent-hero" style="--acc:%s"><div class="wrap"><div class="fx"><span class="eyebrow">AI team · %s / 07</span><h1 style="margin:16px 0 20px;font-size:clamp(40px,6vw,80px)">%s</h1>'
          '<p class="ac-title">%s · %s</p><p class="lede">%s</p>%s<div class="cta" style="margin-top:26px">%s</div></div><div class="fx">%s</div></div></section>\n') % (
        a["accent"], a["n"], p["h1"], name, tx(a["title"]), tx(a["role"]), meta, btn_book(),
        portrait(slug, "big"))
    h += section("light", ('<div class="split"><div class="fx"><h2 style="font-size:clamp(28px,3.4vw,40px);margin-bottom:18px">%s</h2><ul class="checks">%s</ul></div>'
                           '<div class="fx"><div class="pull">"%s"</div><div class="eyebrow mute" style="margin-top:24px">Her states</div><div class="states">%s</div><p class="muted small">%s</p></div></div>') % (
        p.get("checks_h", "On your project, she…"), ''.join('<li>%s</li>' % c for c in p["checks"]), p["rule"], ''.join(chip(k, t) for k, t in p["states"]), p["states_note"]))
    h += section("dark", '<div class="sec-head fx"><span class="eyebrow">%s</span></div><div class="fx">%s</div>' % (p["mock_label"], p["mock"]()))
    h += section("light", sec_head("The rest of the team", "Seven agents. One team.", dark=False) +
                 '<div class="grid g3 stagger mini">%s</div>' % ''.join(
                     '<a class="card" href="%s">%s<h3 style="margin-top:14px">%s</h3><p class="muted" style="margin:8px 0 12px">%s</p><span class="link">Meet %s →</span></a>' % (
                         agent_href(o), av(o["slug"], 64), tx(o["name"]), tx(o["title"]), o["short"]) for o in AGENTS if o["slug"] != slug))
    h += book_strip(dark=True)
    h += footer()
    return h

# ------------------------------------------------------------------ A6 how it works

def step_mocks():
    return [
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row"><div><b>Booked: Project Review · Thu 10:00</b><span>Bring: one project, drawings or bid package, who\'s on it. A real person takes the call.</span></div></div></div>',
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row"><div><b>What Taylor does</b></div></div><div class="row"><div><b>What Emma checks</b></div></div><div class="row"><div><b>What stays with you</b></div></div><div class="row needs"><div><b>One set price — agreed before work starts</b></div></div></div>',
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row"><div><b>Drive</b></div>%s</div><div class="row"><div><b>Gmail</b></div>%s</div><div class="row"><div><b>Calendar</b></div>%s</div><div class="row"><div><b>Notion</b></div>%s</div></div>' % (
            chip("verified", "✓ read"), chip("verified", "✓ read"), chip("verified", "✓ read"), chip("reported", "Not connected")),
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row"><div><b>Estimate Rev 1 · 31 lines · division 26</b></div>%s</div><div class="row"><div><b>Light fixtures — schedule missing</b></div>%s</div></div>' % (
            chip("showing", "Showing the work"), chip("unknown", "Unknown")),
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row"><div><b>Electrical · 7 invited · 3 quotes in</b></div>%s</div><div class="row needs"><div><b>Bid invitation · 4 subs — drafted</b></div>%s</div></div>' % (
            chip("levelled", "Leveled"), chip("needs", "Needs you")),
        '<div class="mock rows"><span class="sd">Sample data</span><div class="eyebrow mute" style="margin-bottom:8px">What you see</div><div class="row needs"><div><b>Today · 3 items need you</b></div>%s</div><div class="row"><div><b>Everything else · running</b></div>%s</div></div>' % (
            chip("needs", "Needs you"), chip("verified", "Verified")),
    ]

def page_how():
    desc = "Six steps: Project Review, one set price in writing, connect your files, Taylor reads the package and levels sub pricing, Sara runs the job."
    h = head("How BuildWithBNZ Works: Six Steps for Contractors", desc, "/how-it-works/")
    h += nav("/how-it-works/")
    mocks = step_mocks()
    rows = []
    for i, (t, p, o, c) in enumerate(STEPS, 1):
        rows.append('<div class="card step"><div><div class="num"><span class="count" data-count="%d" data-dur="240" data-pad="0">00</span></div><h3 style="font-size:clamp(24px,3vw,34px)">%s</h3><p>%s</p>'
                    '<div class="oc"><div><b>Output:</b> %s</div><div><b>Control:</b> %s</div></div></div>%s</div>' % (i, t, p, o, c, mocks[i - 1]))
    h += section("light", sec_head("How it works", "Six steps to a project that runs itself.", tag="h1") + '<div class="steps rows stagger">%s</div>' % ''.join(rows), extra_cls="first")
    h += section("dark", '<div class="split"><div class="fx"><span class="eyebrow">Then the crew stays on</span><h2 style="margin:14px 0 14px">Reported every Monday.</h2>'
                 '<p class="lede">Ongoing operations: a separate monthly arrangement — hosting, monitoring, new projects, and a report every Monday. We stay responsible for it working.</p>'
                 '<div style="margin-top:22px">%s</div></div><div class="fx">%s</div></div>' % (btn_book(), monday_mock()), id_="ongoing")
    h += book_strip()
    h += footer()
    return h

# ------------------------------------------------------------------ what we connect to

def page_connect():
    desc = "The BuildWithBNZ crew works inside Google Drive, Gmail, Google Calendar and Notion, with read access first. Keep your tools: nothing is moved or replaced."
    h = head("Construction AI for Google Drive, Gmail & Notion | BNZ", desc, "/what-we-connect-to/")
    h += nav()
    h += section("dark", sec_head("What we connect to", "The systems the crew works inside.",
                                  "Keep your tools. Nothing is moved or replaced — read access first, and you approve anything that leaves.", tag="h1") + integrations(), extra_cls="first")
    h += section("light", sec_head("How access works", "Read first. Send only with you.") +
                 '<div class="grid g3 stagger">'
                 '<div class="card"><h3>Read access first</h3><p class="muted" style="margin-top:10px">The crew starts by reading the project folder, the inbox threads you point it at, and the calendar. Nothing is moved, renamed or copied out.</p></div>'
                 '<div class="card"><h3>Scoped per project</h3><p class="muted" style="margin-top:10px">Access follows the scope document: Company → Project → Purchased services → Assigned agents → Allowed workflows. One project does not open your whole Drive.</p></div>'
                 '<div class="card"><h3>Sends wait for you</h3><p class="muted" style="margin-top:10px">Bid invitations, follow-ups and requests to the architect are drafted into the approvals queue. Nothing leaves under your name unseen.</p></div>'
                 '</div>')
    h += section("dark", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h2 style="margin-top:14px">On connecting.</h2></div><div class="fx">%s</div></div>' % faq_items([FAQ[7], FAQ[2], FAQ[3]], 3))
    h += book_strip()
    h += footer()
    return h

# ------------------------------------------------------------------ FAQ

def page_faq():
    desc = "Answers to what contractors ask on the call: what it costs, how long until the crew is live, who sees your drawings, and whether the AI sends anything."
    ld = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ','.join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', '\\"'), a.replace('"', '\\"')) for q, a in FAQ)
    h = head("FAQ — Asked on Every Call | BuildWithBNZ", desc, "/faq/", jsonld=ld)
    h += nav("/faq/")
    h += section("dark", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h1 style="margin-top:14px;font-size:clamp(34px,4.6vw,58px)">Asked on every call.</h1><p class="muted" style="margin-top:14px">Direct answers, the way a GC actually asks. If yours isn\'t here, bring it to the Project Review.</p></div><div class="fx">%s</div></div>' % faq_items(FAQ, 8), extra_cls="first")
    h += book_strip()
    h += footer()
    return h

# ------------------------------------------------------------------ A7 book + thanks

def lead_form():
    return ('<form class="lead" method="post" action="https://formsubmit.co/%s" novalidate>'
            '<input type="hidden" name="_subject" value="New inquiry — Project Review">'
            '<input type="hidden" name="_template" value="table">'
            '<input type="hidden" name="_next" value="%s/thanks/">'
            '<input type="hidden" name="_captcha" value="false">'
            '<label class="hp" aria-hidden="true">Leave empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label>'
            '<div class="two"><label>Your name<input name="name" required autocomplete="name" autocapitalize="words" autocorrect="off" spellcheck="false" enterkeyhint="next"></label><label>Company<input name="company" required autocomplete="organization" autocapitalize="words" enterkeyhint="next"></label></div>'
            '<div class="two"><label>Email<input name="email" type="email" required autocomplete="email" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="next"></label><label>Phone<input name="phone" type="tel" inputmode="tel" autocomplete="tel" enterkeyhint="next"></label></div>'
            '<label>Contractor type<select name="contractor_type"><option value="">Choose one</option><option>General contractor</option><option>Remodeler / custom builder</option><option>Specialty contractor</option><option>GC bidding public work</option><option>Other</option></select></label>'
            '<label>The project — what is it, where is it, what hurts<textarea name="project" required enterkeyhint="done" placeholder="e.g. 4-story mixed-use in Rockland County, public work, bid due in 11 days. Estimating is the bottleneck."></textarea></label>'
            '<div class="two"><label>Bid due (if any)<input name="bid_due" type="date"></label><label>Link to drawings or the bid package (optional)<input name="files_link" type="url" placeholder="Drive or Dropbox link"></label></div>'
            '<div class="err">Please fill in your name, company, email and the project.</div>'
            '<button class="btn primary" type="submit">Book a project review <span class="g">↗</span></button>'
            '<p class="note">A real person takes this call. We reply the same business day to set a time. No prices on this site because there is no standard project — scope and one set price come back in writing after the review.</p>'
            '</form>') % (INBOX, SITE)

def page_book():
    desc = "Book a Project Review with BuildWithBNZ. Bring one project and we'll show you what the crew would do with it. A real person takes this call."
    h = head("Book a Project Review | BuildWithBNZ", desc, "/book/")
    h += nav()
    h += ('<section class="light book hero"><div class="wrap"><div class="fx"><span class="eyebrow">Start here</span><h1 style="margin:16px 0 14px;font-size:clamp(40px,6vw,76px)">Book a project review.</h1>'
          '<p class="lede">Bring one project. We\'ll show you what the crew would do with it.</p>'
          '<div class="eyebrow mute" style="margin-top:30px">What to bring</div><div class="bring">'
          '<div><i>1</i><div><b>One project</b><span>Live or recent — the one that hurts is the best one.</span></div></div>'
          '<div><i>2</i><div><b>Drawings or the bid package</b><span>Whatever you have — PDFs, a Drive folder, a link.</span></div></div>'
          '<div><i>3</i><div><b>Who\'s on it</b><span>Who estimates, who chases subs, who signs.</span></div></div></div>'
          '<p class="muted small" style="margin-top:12px">Prefer to talk? <a class="link" href="tel:%s">%s</a> · <a class="link" href="mailto:%s">%s</a></p></div>'
          '<div class="fx"><div class="card" id="lead">%s</div></div></div></section>\n') % (PHONE, PHONE_TXT, INBOX, INBOX, lead_form())
    h += ('<script>(function(){var f=document.querySelector(\'form.lead\');if(f){f.addEventListener(\'submit\',function(){if(typeof gtag===\'function\'){gtag(\'event\',\'generate_lead\',{form:\'book\'});}});}})();</script>\n')
    h += footer()
    return h

# ------------------------------------------------------------------ /start/ — onboarding (mmc-app #65 pattern)
# Three short steps: two big-button questions here, then the existing /book/ form (step 3, the only conversion).
# A real GET form, so it works without JavaScript. Only answer codes ever reach a URL (GA records page URLs).

# START_TYPES (the contractor types) lives in shared.py: /start/, /get-started/, the report form and the home page use it.
START_BRING = [("bid", "A bid we're pricing now"), ("job", "A job we're building now"), ("unsure", "Not sure yet")]

def _choices(name, opts):
    return '<div class="choices">%s</div>' % ''.join(
        '<input class="sr" type="radio" name="%s" id="%s-%s" value="%s"><label for="%s-%s">%s</label>' % (name, name, v, v, name, v, t) for v, t in opts)

def page_start():
    desc = "Two quick questions, then your details on the booking form. A person from our team gets back to you to set up a demo."
    h = head("Show Us How Your Company Works | BuildWithBNZ", desc, "/start/")
    h += nav()
    call = '<p class="st-call">Rather talk? <a href="tel:%s">Call %s</a></p>' % (PHONE, PHONE_TXT)
    h += ('<section class="dark first start-page"><div class="wrap">'
          '<span class="eyebrow">Book a demo · 3 short steps</span>'
          '<h1>Show us how your company works.</h1>'
          '<p class="lede">Two quick questions, then your details. A person from our team gets back to you to set up the demo.</p>'
          '<form class="start" method="get" action="/book/#lead">'
          '<input type="hidden" name="from" value="start">'
          '<div class="st-progress" aria-hidden="true"><progress max="3" value="1"></progress></div>'
          '<fieldset data-step="1"><legend><span class="st-n">Step 1 of 3</span>What kind of work do you do?</legend>%s'
          '<div class="st-actions"><button type="button" class="btn primary xl" data-next>Continue</button></div></fieldset>'
          '<fieldset data-step="2"><legend><span class="st-n">Step 2 of 3</span>What will you show us?</legend>'
          '<p class="hint">Bring one bid or one job. Drawings, specs, whatever you have.</p>%s'
          '<div class="st-actions"><button type="submit" class="btn primary xl">Next: your details</button>'
          '<button type="button" class="btn quiet" data-back>Back</button></div></fieldset>'
          '</form>%s'
          '<div class="st-next"><span class="eyebrow mute">What happens next</span><ol>'
          '<li>You send your details on the booking form. That\'s step 3.</li>'
          '<li>A person from our team gets back to you to set a time.</li>'
          '<li>We walk through one bid or job with you, and what Sara and the team would do with it.</li>'
          '<li>If it\'s a fit, you get a written proposal. Nothing is connected until you say yes, one system at a time.</li>'
          '</ol></div>'
          '</div></section>\n') % (_choices("type", START_TYPES), _choices("bring", START_BRING), call)
    h += footer()
    return h

# ------------------------------------------------------------------ /get-started/ — the onboarding form (founders, 21 Oct 2026)
# For people coming from Bilal's Instagram ("the link's in my bio"). Four short steps with big answers on a phone.
# Without JavaScript it is one plain POST to the inquiries inbox (like /book/); with it, bnz.js steps through it and sends
# it through LEAD_ENDPOINT, with the same mail-client fallback. Required: contractor type, name, and a mobile or an email.

GS_HANDOFF = ["Estimates and takeoffs", "Sub quotes", "Job costs and invoices", "Scheduling and project tracking",
              "Contracts and change orders", "Design visuals"]
GS_SIZE = ["Just me", "2 to 5 people", "6 to 20 people", "21 to 50 people", "More than 50"]
GS_TIME = ["Morning", "Midday", "Afternoon", "Evening", "Any time"]
GS_HEARD = ["Instagram @bilal.baxx", "Instagram @bnzbuilders", "Google", "A friend", "Other"]

def _gs_choices(name, labels, kind="radio", cls="", required=False, labelled=None):
    """Big answer buttons. The value is the label itself, so the email reads plainly."""
    out = []
    for i, t in enumerate(labels):
        out.append('<input class="sr" type="%s" name="%s" id="gs-%s-%d" value="%s"%s><label for="gs-%s-%d">%s</label>' % (
            kind, name, name, i, esc(t), ' required' if required and i == 0 else '', name, i, t))
    group = ' role="%s" aria-labelledby="%s"' % ("radiogroup" if kind == "radio" else "group", labelled) if labelled else ''
    return '<div class="choices%s"%s>%s</div>' % (' ' + cls if cls else '', group, ''.join(out))

def onboard_form():
    total = 4
    def legend(n, q):
        return '<legend><span class="st-n">Step %d of %d</span>%s</legend>' % (n, total, q)
    back = '<button type="button" class="btn-quiet" data-back>Back</button>'
    nxt = '<button type="button" class="btn-primary xl" data-next>Continue <span class="arr" aria-hidden="true">→</span></button>'
    return ('<form class="onboard" method="post" action="https://formsubmit.co/%(inbox)s">'
            '<input type="hidden" name="_subject" value="New onboarding request — Start here">'
            '<input type="hidden" name="_template" value="table">'
            '<input type="hidden" name="_next" value="%(site)s/get-started/thanks/">'
            '<input type="hidden" name="_captcha" value="false">'
            '<label class="hp" aria-hidden="true">Leave empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label>'
            '<div class="st-progress" aria-hidden="true"><i><b></b></i><i><b></b></i><i><b></b></i><i><b></b></i></div>'
            # 1 — contractor type (the same labels as /start/ and the /book/ form)
            '<fieldset data-step="1">%(l1)s%(types)s'
            '<p class="err" role="alert">Pick the kind of work you do.</p>'
            '<div class="st-actions">%(nxt)s</div></fieldset>'
            # 2 — what to hand off first (pick any)
            '<fieldset data-step="2">%(l2)s<p class="hint">Pick any that fit. You can change this on the call.</p>%(handoff)s'
            '<div class="st-actions">%(nxt)s%(back)s</div></fieldset>'
            # 3 — the company
            '<fieldset data-step="3">%(l3)s'
            '<label class="fld">Company name<input name="company" autocomplete="organization" autocapitalize="words" enterkeyhint="next"></label>'
            '<label class="fld">City and state<input name="city_state" autocomplete="address-level2" autocapitalize="words" enterkeyhint="next" placeholder="e.g. Yonkers, NY"></label>'
            '<p class="fld-h" id="gs-size-h">How many people work at your company?</p>%(size)s'
            '<label class="fld">The software and tools you use now <span class="opt">(optional)</span><input name="tools_now" enterkeyhint="next" placeholder="e.g. spreadsheets, email, a takeoff program"></label>'
            '<div class="st-actions">%(nxt)s%(back)s</div></fieldset>'
            # 4 — how to reach them
            '<fieldset data-step="4">%(l4)s'
            '<label class="fld">Your name<input name="name" required autocomplete="name" autocapitalize="words" autocorrect="off" spellcheck="false" enterkeyhint="next"></label>'
            '<label class="fld">Mobile number<input name="phone" type="tel" inputmode="tel" autocomplete="tel" enterkeyhint="next"></label>'
            '<label class="fld">Email<input name="email" type="email" autocomplete="email" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="next"></label>'
            '<p class="fld-n">A mobile number or an email is enough.</p>'
            '<p class="fld-h" id="gs-time-h">Best time to call</p>%(time)s'
            '<p class="fld-h" id="gs-heard-h">How did you hear about us?</p>%(heard)s'
            '<p class="err" role="alert">Add your name, and a mobile number or an email, so we can reach you.</p>'
            '<div class="st-actions"><button type="submit" class="btn-primary xl">Send <span class="arr" aria-hidden="true">→</span></button>%(back)s</div>'
            '<p class="note">A real person from our team calls you back. Your answers go to our team only. <a class="link" href="/privacy/">Privacy</a></p>'
            '</fieldset>'
            '</form>') % dict(
        inbox=INBOX, site=SITE, total=total, nxt=nxt, back=back,
        l1=legend(1, "What kind of work do you do?"),
        l2=legend(2, "What should the crew take off your plate first?"),
        l3=legend(3, "About your company"),
        l4=legend(4, "How do we reach you?"),
        types=_gs_choices("contractor_type", [t for _, t in START_TYPES], required=True),
        handoff=_gs_choices("hand_off_first", GS_HANDOFF, kind="checkbox", cls="multi"),
        size=_gs_choices("team_size", GS_SIZE, cls="compact", labelled="gs-size-h"),
        time=_gs_choices("best_time", GS_TIME, cls="compact", labelled="gs-time-h"),
        heard=_gs_choices("how_heard", GS_HEARD, cls="compact", labelled="gs-heard-h"))

def page_get_started():
    """Same look as the home page (home.css, Geist, the focus nav): the brand, Book a call and the phone, no Start here."""
    desc = "Tell us about your company in four short steps on your phone. A real person from our team calls you back to set up your AI office crew."
    h = head("Start Here — Tell Us About Your Company | BuildWithBNZ", desc, "/get-started/",
             body_attrs='class="home gs" data-colorway="a"', extra_css="/assets/css/home.css")
    h += nav_home(focus=True)
    h += ('<section class="gs-page"><div class="lf" aria-hidden="true"><i></i></div><div class="wrap">'
          '<h1>Tell us about your company.</h1>'
          '<p class="lede">Four short steps. Then a real person from our team calls you back to set things up. Nothing is connected until you say yes.</p>'
          '<div class="gs-card">%s</div>'
          '<div class="gs-talk"><p>Rather talk?</p><a class="btn-ghost lg" href="tel:%s">%s Call %s</a><a class="tlink" href="/book/">Book a call</a></div>'
          '</div></section>\n') % (onboard_form(), PHONE, ico("phone", 20), PHONE_TXT)
    h += footer_home(minimal=True)
    return h

def page_get_started_thanks():
    h = head("Thanks — we'll call you back | BuildWithBNZ", "Your answers are in. A real person from our team calls you back.", "/get-started/thanks/", noindex=True,
             body_attrs='class="home gs" data-colorway="a"', extra_css="/assets/css/home.css")
    h += nav_home(focus=True)
    h += ('<section class="gs-page"><div class="lf" aria-hidden="true"><i></i></div><div class="wrap"><div class="gs-card gs-thanks">'
          '<span class="gs-ok" aria-hidden="true">%s</span><span class="tagp">Received</span>'
          '<h1 class="gs-thanks-h">Thanks. A real person will call you back.</h1>'
          '<p class="lede">Someone from our team will call you to talk through your company and what the crew would take on first. '
          'Keep one bid or one job in mind. That is what we walk through.</p>'
          '<p>Rather pick a time now?</p>'
          '<p class="gs-done"><a class="btn-primary lg" href="/book/">Book a call <span class="arr" aria-hidden="true">→</span></a>'
          '<a class="btn-ghost lg" href="tel:%s">Call %s</a></p>'
          '</div></div></section>\n') % (ico("check", 28), PHONE, PHONE_TXT)
    h += footer_home(minimal=True)
    return h

def page_thanks():
    h = head("Thanks — we'll be in touch | BuildWithBNZ", "Your Project Review request is in. A real person replies the same business day.", "/thanks/", noindex=True)
    h += nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">Received</span><h1 style="margin-top:14px;font-size:var(--fs-h2)">Your project review request is in.</h1>'
                 '<p class="lede">A real person replies the same business day to set a time. Have the drawings or the bid package handy — that\'s what we walk through on the call.</p>'
                 '<p style="margin-top:18px"><a class="btn ghost" href="/how-it-works/">See how it works <span class="g">↗</span></a></p></div>', extra_cls="first")
    h += footer()
    return h

# ------------------------------------------------------------------ /workflow-report/ — the content funnel (founders' plan, 19 Oct 2026)
# The intro plays free; the report costs an email; the thanks page offers the call. Klaviyo's two IDs are public
# (its client API is made for the browser). Until they're set, requests reach the inbox the way /book/ does.

KLAVIYO_COMPANY = ""   # Klaviyo public API key (site ID)
KLAVIYO_LIST = ""      # list ID of the report list; its flow sends the report and the follow-ups
INTRO_VIDEO = ""       # embed URL of the short intro (YouTube, Vimeo or Loom); empty shows the sample project

REPORT_PARTS = [
    ("Where the hours go", "The work that eats your week — takeoffs, sub quotes, bid paperwork, the Monday report — laid out against how you work today."),
    ("What to hand off first", "The one or two jobs the crew would take on first, and what they would look like on your next bid or job."),
    ("What stays with you", "Every price, every send and every signature stays yours. The report shows where you would approve."),
]

def report_form():
    types = ''.join('<option>%s</option>' % t for _, t in START_TYPES)
    return ('<form class="lead report" method="post" action="https://formsubmit.co/%s" novalidate data-klaviyo-company="%s" data-klaviyo-list="%s">'
            '<input type="hidden" name="_subject" value="New request — Workflow report">'
            '<input type="hidden" name="_template" value="table">'
            '<input type="hidden" name="_next" value="%s/workflow-report/thanks/">'
            '<input type="hidden" name="_captcha" value="false">'
            '<label class="hp" aria-hidden="true">Leave empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label>'
            '<div class="two"><label>Your name<input name="name" required autocomplete="name" autocapitalize="words" autocorrect="off" spellcheck="false" enterkeyhint="next"></label><label>Email<input name="email" type="email" required autocomplete="email" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="next"></label></div>'
            '<div class="two"><label>Company<input name="company" autocomplete="organization" autocapitalize="words" enterkeyhint="next"></label><label>Contractor type<select name="contractor_type"><option value="">Choose one</option>%s</select></label></div>'
            '<label>What eats the most time? (optional)<textarea name="time_sink" enterkeyhint="done" placeholder="e.g. Takeoffs on every bid, chasing sub quotes, the Friday paperwork."></textarea></label>'
            '<label class="consent"><input type="checkbox" name="consent" value="yes" required>Email me the report and occasional follow-ups from BuildWithBNZ. Unsubscribe any time.</label>'
            '<div class="err">Please add your name and email, and tick the box so we can email you the report.</div>'
            '<button class="btn primary" type="submit">Send me the free report <span class="g">↗</span></button>'
            '<p class="note">Free, and no call needed. Your email is used for the report and our follow-ups only. <a class="link" href="/privacy/">Privacy</a></p>'
            '</form>') % (INBOX, esc(KLAVIYO_COMPANY), esc(KLAVIYO_LIST), SITE, types)

def page_report():
    desc = "Watch the short intro, then get a free workflow report for your company: where the hours go, what the crew would take on first, and what stays with you."
    h = head("Free Contractor Workflow Report | BuildWithBNZ", desc, "/workflow-report/")
    h += nav()
    media = ('<div class="video"><iframe src="%s" title="BuildWithBNZ intro" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>' % esc(INTRO_VIDEO)
             if INTRO_VIDEO else sample_project_mock())
    h += ('<section class="dark hero"><div class="wrap"><div class="fx"><span class="eyebrow">Free for contractors</span><h1>Where does your week go?</h1>'
          '<p class="lede">Watch the short intro. Then tell us how you bid and run jobs, and we\'ll email you a free workflow report for your company.</p>'
          '<div class="cta"><a class="btn primary" href="#report">Get the free report <span class="g">↓</span></a><a class="link" href="/crew/">Meet the crew</a></div></div>'
          '<div class="fx">%s</div></div></section>\n') % media
    parts = ''.join('<div class="card"><h3>%s</h3><p>%s</p></div>' % p for p in REPORT_PARTS)
    h += section("light", sec_head("The report", "What's in it.") + '<div class="grid g3 stagger pain">%s</div>' % parts)
    h += section("dark", '<div class="split"><div class="fx"><span class="eyebrow">Free workflow report</span>'
                 '<h2 style="margin:14px 0 12px">Get the free report.</h2>'
                 '<p class="lede">A few details and it\'s on its way to your inbox.</p>'
                 '<p class="small muted" style="margin-top:12px">Rather talk now? <a class="link" href="/book/">Book a project review</a> or <a class="link" href="tel:%s">call %s</a>.</p></div>'
                 '<div class="fx"><div class="card">%s</div></div></div>' % (PHONE, PHONE_TXT, report_form()), id_="report")
    h += footer()
    return h

def page_report_thanks():
    h = head("Thanks — your report is on its way | BuildWithBNZ", "Your workflow report request is in.", "/workflow-report/thanks/", noindex=True)
    h += nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">Received</span><h1 style="margin-top:14px;font-size:var(--fs-h2)">Your report is on its way.</h1>'
                 '<p class="lede">Watch your inbox for the workflow report. Want to walk through it on a real project? Book a project review and bring one bid or one job.</p>'
                 '<p style="margin-top:18px">%s</p></div>' % btn_book(), extra_cls="first")
    h += footer()
    return h

# ------------------------------------------------------------------ login, legal, 404, contact

def page_login():
    h = head("Login — Customer Workspace | BuildWithBNZ", "The BuildWithBNZ workspace is opened per project after your Project Review. Access is by invitation.", "/login/", noindex=True)
    h += nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">Customer workspace</span><h2 style="margin-top:14px">Access is by invitation.</h2>'
                 '<p class="lede">The workspace is opened per project once scope and price are agreed in writing. If you\'re a customer and your invitation hasn\'t arrived, email <a class="link" href="mailto:%s">%s</a> from the address on your scope document.</p>'
                 '<p style="margin-top:18px">%s</p></div>' % (INBOX, INBOX, btn_book("btn ghost", "New here? Book a project review")), extra_cls="first")
    h += footer()
    return h

def page_privacy():
    h = head("Privacy — BuildWithBNZ", "How BuildWithBNZ handles the information you share with us: the Project Review form, project files, and the workspace.", "/privacy/")
    h += nav()
    h += section("dark", '''<div class="prose fx"><span class="eyebrow">Privacy</span><h1 style="margin-top:14px;font-size:clamp(28px,3.5vw,40px);margin-bottom:12px">Privacy policy.</h1>
<p class="lede">This covers the BuildWithBNZ website and workspace, operated by BNZ Builders Inc. Last updated: October 2026.</p>
<h3>What we collect</h3>
<p>When you book a Project Review we collect what you type into the form: your name, company, email, phone, contractor type, a description of the project, an optional bid date and an optional link to your files. The form is relayed to our inquiries inbox.</p>
<p>This site uses Google Analytics to count visits and form sends. It is not sent what you type into a form.</p>
<p>When you fill in the Start here form we collect what you choose to give us: your name, mobile number, email, company, contractor type, city and state, team size, the work you would like handed off first, the tools you use now, how you heard about us, the best time to call, and the page or post that sent you to us. We use them to call you back and set up your company. The form is relayed to our inquiries inbox.</p>
<p>When you ask for the free workflow report we collect your name, email, and, if you give them, your company, contractor type and what takes the most time. We use them to send the report and the follow-up emails you agreed to. Every email has an unsubscribe link.</p>
<h3>Project files</h3>
<p>During a Project Review you may share drawings, specs, addenda and bid documents. They are used to prepare the walkthrough and, if we go ahead, the scope document. They are not used to train models, are not shared outside the people working your project, and are deleted on request.</p>
<h3>The workspace</h3>
<p>Once a project is scoped, the crew connects to the systems named in your scope document — Google Drive, Gmail, Google Calendar, Google Workspace, Notion — with read access first. Access is scoped per project. Anything that leaves the workspace (an email to a subcontractor, a request to an architect) waits in your approvals queue until you approve it.</p>
<h3>Who we share with</h3>
<p>Nobody, beyond the service providers needed to run the site and the workspace (hosting, email relay, our email platform for the report and its follow-ups, the model providers that process your project documents under our agreements with them). We do not sell or rent your information.</p>
<h3>Your rights</h3>
<p>Ask us what we hold about you, ask us to correct it, or ask us to delete it: <a class="link" href="mailto:%s">%s</a>.</p>
</div>''' % (INBOX, INBOX), extra_cls="first")
    h += footer()
    return h

def page_terms():
    h = head("Terms — BuildWithBNZ", "Terms covering the BuildWithBNZ website, Project Review, scope documents and the workspace.", "/terms/")
    h += nav()
    h += section("dark", '''<div class="prose fx"><span class="eyebrow">Terms</span><h1 style="margin-top:14px;font-size:clamp(28px,3.5vw,40px);margin-bottom:12px">Terms of service.</h1>
<p class="lede">These terms cover your use of the BuildWithBNZ website and workspace, operated by BNZ Builders Inc. Last updated: October 2026.</p>
<h3>The service</h3>
<p>BuildWithBNZ provides a team of seven AI agents, led by Sara, that work inside a construction project workspace. The agents prepare drafts, estimates, reports and document reviews. Anything that leaves your company is sent only after you review and approve it. The agents do not sign, award, pay or commit on your behalf.</p>
<h3>Engagement</h3>
<ul>
<li>Every engagement starts with a Project Review about one real project. There is no charge for the review.</li>
<li>If we proceed, you receive a scope document stating what the crew will do, what it will not do, and one set price for that project, in writing, before work starts. Price moves only if scope moves, and only by written agreement.</li>
<li>After the first project the crew can stay on under a separate written arrangement for ongoing operations — hosting, monitoring, new projects and a weekly report. Its terms are set out in that document.</li>
<li>No prices are published on this website because every project is scoped individually.</li>
</ul>
<h3>Your responsibilities</h3>
<ul>
<li>You are responsible for reviewing drafts, estimates and documents before they are sent, submitted or relied upon.</li>
<li>Estimates are prepared from the documents you provide. Where information is missing the estimate says UNKNOWN; it is not a bid, a quote or a guarantee of cost.</li>
<li>Kyle's design concepts are not licensed design, and Kyle is not a licensed architect. Stamped drawings and engineering remain the responsibility of your architect or engineer of record.</li>
<li>Richard's contract review support is not legal advice, and Richard is not a licensed attorney. Legal interpretations and decisions stay with your own attorney.</li>
<li>Keep your workspace credentials secure. Each workspace belongs to one company and one or more scoped projects.</li>
</ul>
<h3>Liability</h3>
<p>To the extent permitted by law, BNZ Builders Inc. is not liable for indirect or consequential loss arising from use of the service, and our total liability under an engagement is limited to the amount paid for that engagement.</p>
<h3>Contact</h3>
<p><a class="link" href="mailto:%s">%s</a></p>
</div>''' % (INBOX, INBOX), extra_cls="first")
    h += footer()
    return h

def page_404():
    h = head("Page not found — BuildWithBNZ", "That page isn't here.", "/404.html", noindex=True)
    h += nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">404</span><h1 style="margin-top:14px;font-size:var(--fs-h2)">That page isn\'t here.</h1>'
                 '<p class="lede">It may have moved. Try the crew, how it works, or head back home.</p>'
                 '<p style="margin-top:18px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn ghost" href="/">Home <span class="g">↗</span></a><a class="btn ghost" href="/crew/">The crew <span class="g">↗</span></a>%s</p></div>' % btn_book(), extra_cls="first")
    h += footer()
    return h

def page_contact():
    desc = "Contact BuildWithBNZ. The fastest route is a Project Review — bring one project and we'll show you what the crew would do with it."
    h = head("Contact | BuildWithBNZ", desc, "/contact/")
    h += nav()
    h += section("dark", '<div class="prose fx"><span class="eyebrow">Contact</span><h1 style="margin-top:14px;font-size:clamp(28px,3.5vw,40px);margin-bottom:12px">Talk to a real person.</h1>'
                 '<p class="lede">The fastest route is a Project Review — bring one project and we\'ll show you what the crew would do with it. Or reach us directly.</p>'
                 '<p style="margin-top:18px"><a class="link" href="mailto:%s">%s</a> · <a class="link" href="tel:%s">%s</a></p>'
                 '<p style="margin-top:22px">%s</p></div>' % (INBOX, INBOX, PHONE, PHONE_TXT, btn_book()), extra_cls="first")
    h += footer()
    return h

def page_redirect(to, title):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title><meta name="robots" content="noindex">'
            '<meta http-equiv="refresh" content="0; url=%s"><link rel="canonical" href="%s%s"></head>'
            '<body><p>Moved: <a href="%s">%s%s</a></p></body></html>\n') % (title, to, SITE, to, to, SITE, to)
