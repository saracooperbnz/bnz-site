# -*- coding: utf-8 -*-
"""The seven BuildWithBNZ AI agents: the one data source every page reads.

Authority: BNZ_AI_Team_Identity_FINAL.pdf (approved by Bilal Mohammed, Oct 16 2026) for names, titles,
human partners, reporting line and faces. Role text: BuildWithBNZ_Meet_the_AI_Team_Section_REVIEW.pdf.
Approval limits: the sourced lines collected in the content brief (DESK, EXEC, GUIDE, REVIEW).
Faces: assets/team/*.webp, resized and compressed from the approved images only (never retouched,
regenerated, blended or swapped). Framing is done in CSS (object-fit / object-position).
img["av"] = (file, focal point, zoom) for the small round avatars. Taylor's and Richard's approved avatar
tiles cut the face at the right edge, so their small avatars frame the 4x5 portrait instead (CSS crop only).

Store plain text here. Pages escape it when they render it (titles contain "&")."""

AGENTS = [
    dict(slug="sara", key="s", name="Sara Cooper", short="Sara", pronoun=None, n="01",
         title="Chief Operations & AI Team Leader",
         partners="Bilal Mohammed", partners_label="Human partner", reports_to="Bilal Mohammed",
         role=("Sara runs the company command center: projects, bids and procurement, deadlines, approvals and open "
               "issues. She assigns and supervises the work of the other six agents. She gives Bilal morning "
               "priorities, evening results and urgent alerts."),
         card="Runs the command center: projects, bids, deadlines, approvals and open issues. Leads the other six agents and reports to Bilal.",
         limits=["Nothing is sent without a person's go.",
                 "Never touches a price. Any change goes back to the estimator.",
                 "Never pays bond premiums, shipping or fees.",
                 "Never calls a bid submitted without proof it arrived.",
                 "Doesn't sign, notarize or post bonds.",
                 "Never fixes a problem silently. It comes to you."],
         license=None, page="/sara/", accent="var(--ember)",
         img=dict(lg=(752, 1344), sm=(480, 858), fp="52% 30%", z=1.9, av=("avatar", "52% 16%", 1.3))),
    dict(slug="amanda", key=None, name="Amanda", short="Amanda", pronoun=None, n="02",
         title="Head of Marketing, Creative Production & Sales Research",
         partners="Sib, Tawheed, Candrin", partners_label="Human partners", reports_to="Sara Cooper",
         role=("Amanda owns the creative production pipeline: marketing strategy, UGC scripts, social content, "
               "advertising concepts and creative direction for every agent's content. She also runs contractor lead "
               "research and prepares sales outreach."),
         card="Marketing, content and contractor lead research. Everything she makes is a draft until Bilal approves it.",
         limits=["Everything she makes is a draft until Bilal approves it.",
                 "A person approves before any outreach goes out or anything is published.",
                 "Lead lists use verifiable sources only.",
                 "Never claims a software feature that isn't live, or a project BNZ didn't do."],
         license=None, page=None, accent=None,
         img=dict(lg=(784, 1168), sm=(480, 715), fp="45% 22%", z=1.9, av=("avatar", "45% 18%", 1.4))),
    dict(slug="kyle", key=None, name="Kyle", short="Kyle", pronoun=None, n="03",
         title="Head of Architecture & 7D Design",
         partners="Jose", partners_label="Human partner", reports_to="Sara Cooper",
         role=("Kyle produces 2D and 3D design concepts, before-and-after renovation concepts and construction "
               "sequencing. He works with Taylor so every design option is checked against cost."),
         card="Design concepts in 2D and 3D, before-and-after ideas and build sequence, checked against cost with Taylor.",
         limits=["Concepts only. Never presented as signed or sealed drawings.",
                 "Every design option goes to Taylor for quantities and cost before a client sees it.",
                 "Quantities come from field measurement or contract drawings.",
                 "Anything past concept design goes to the architect or engineer of record."],
         license="Not a licensed architect.", page=None, accent=None,
         img=dict(lg=(960, 960), sm=(480, 480), fp="54% 34%", z=1.7, av=("avatar", "54% 34%", 1.7))),
    dict(slug="taylor", key="t", name="Taylor", short="Taylor", pronoun="she/her", n="04",
         title="Chief Estimator & Preconstruction",
         partners="Bilal Mohammed + estimating team", partners_label="Human partners", reports_to="Sara Cooper",
         role=("Taylor finds and qualifies bid opportunities, reviews drawings, runs takeoffs and builds labor estimates "
               "with applicable prevailing-wage considerations. She requests and compares subcontractor and vendor "
               "pricing and prepares bid packages."),
         card="Finds and qualifies bids, reads drawings, runs takeoffs and builds the estimate. Never makes up a quantity, quote or price.",
         limits=["Never makes up quantities, quotes or prices.",
                 "A human estimator approves every price before it goes out.",
                 "Sara checks the bid, and nothing is submitted until you say send.",
                 "Every number carries a label, such as VERIFIED, ESTIMATE, QUOTE or UNKNOWN."],
         license=None, page="/taylor/", accent="var(--taylor)",
         img=dict(lg=(960, 1200), sm=(480, 600), fp="66% 26%", z=1.04, av=("sm", "68% 20%", 1.7))),
    dict(slug="emma", key="e", name="Emma", short="Emma", pronoun=None, n="05",
         title="Chief Finance & Accounting",
         partners="Bilal Mohammed", partners_label="Human partner", reports_to="Sara Cooper",
         role=("Emma covers job costing, QuickBooks reconciliation reviews, payroll verification, accounts payable and "
               "receivable, invoice tracking and cash-flow reporting."),
         card="Job costing, invoices, payables and receivables, payroll checks and cash-flow reports. Reviews and recommends.",
         limits=["Reviews and recommends. Never posts transactions or changes accounting records without authorization.",
                 "Nothing is posted until a person with authority approves it.",
                 "Your accountant or CPA reviews payroll and the books."],
         license=None, page="/emma/", accent="var(--emma)",
         img=dict(lg=(960, 1200), sm=(480, 600), fp="60% 30%", z=1.04, av=("avatar", "50% 50%", 1.04))),
    dict(slug="richard", key=None, name="Richard", short="Richard", pronoun=None, n="06",
         title="Contracts & Legal",
         partners="Yasmina", partners_label="Human partner", reports_to="Sara Cooper",
         role=("Richard supports contract and subcontract review, change-order documentation, scope exclusions, "
               "payment-dispute analysis and compliance research."),
         card="Contract and subcontract review support, change-order paperwork, payment-dispute and compliance research.",
         limits=["Legal interpretations and consequential decisions go to human legal review.",
                 "Change orders are written, priced by Taylor and signed before work starts.",
                 "Contract review support only. Not legal advice."],
         license="Not a licensed attorney.", page=None, accent=None,
         img=dict(lg=(960, 1200), sm=(480, 600), fp="66% 28%", z=1.04, av=("sm", "64% 24%", 1.6))),
    dict(slug="adam", key=None, name="Adam", short="Adam", pronoun=None, n="07",
         title="AI CTO, Software Engineering & Cybersecurity",
         partners="Adam (human developer)", partners_label="Human partner", reports_to="Sara Cooper",
         role=("Adam is the AI team's lead for software engineering and cybersecurity. He works with Adam, our human "
               "developer. His detailed responsibilities and approval limits have not been written down yet."),
         card="Leads software engineering and cybersecurity for the AI team, working with Adam, our human developer.",
         limits=["Software releases need Bilal's explicit approval first."], limits_label="Team-wide rule",
         note="The AI agent Adam and Adam, our human developer, are two different team members.",
         license=None, page=None, accent=None,
         img=dict(lg=(960, 540), sm=(480, 270), fp="45% 34%", z=1.04, av=("avatar", "50% 50%", 1.04))),
]

BY = {a["slug"]: a for a in AGENTS}
BY.update({a["key"]: a for a in AGENTS if a.get("key")})   # 's', 't', 'e' keep the older av() calls working
SIX = [a for a in AGENTS if a["slug"] != "sara"]            # REVIEW p1 order: Amanda, Kyle, Taylor, Emma, Richard, Adam

# The partnership principle. Sourced: "Agents prepare. People decide." (Team Guide p2, p19);
# a named human partner for every agent (FINAL pp 2-8).
PRINCIPLE = "Agents prepare. People decide."
PRINCIPLE_LONG = ("Every agent works with a human partner. Agents prepare the work; people approve every price, "
                  "signature, payment and send.")


def agent_href(a):
    """Agents with their own page link there; the other four link to their card on /crew/."""
    return a["page"] or "/crew/#%s" % a["slug"]
