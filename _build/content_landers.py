# -*- coding: utf-8 -*-
"""Seven problem-based SEO landing pages. Each is one door into the same crew."""
from shared import *
from content_home import hero
from content_pages import est_mock, bids_mock, today_mock, public_mock

LANDERS = [
    dict(slug="construction-estimating-ai", who="t",
         title="AI Construction Estimating: Takeoffs With Sources Shown",
         eyebrow="Estimating & takeoff", h1="Estimates that show their work.",
         lede="Taylor reads the full bid package — drawings, specs, addenda, wage schedule, bid form — performs the takeoff, prices labor, material and sub lines, and issues an estimate where every line traces to a sheet or a spec section. Missing information reads UNKNOWN, never a guess.",
         desc="Construction estimating AI for GCs and specialty contractors: takeoffs from the drawing set, sheet and spec conflicts flagged, every assumption shown.",
         mock=est_mock,
         pains=[("The package arrives Friday, the bid is due in eleven days", "Taylor starts reading the same day. Rev 1 comes back with a conflict log and an UNKNOWN list so you know what to chase before you price."),
                ("Addendum 02 changes the electrical scope", "Replace the sheets; Taylor reissues Rev 2 with the delta line by line. A revision with a reason, not a restart."),
                ("The fixture schedule isn't in the set", "The line reads UNKNOWN with the reason and who has it. The total is withheld until it's resolved. A request to the architect is drafted for your approval.")],
         faq=[0, 5, 4]),
    dict(slug="subcontractor-procurement", who="t",
         title="Subcontractor Procurement AI: Bids & Sub Quotes | BNZ",
         eyebrow="Subcontractor bidding & buyout", h1="Every sub, every quote, every document — named.",
         lede="Taylor requests and compares sub and vendor pricing and levels each quote against her estimate, line by line. Requests for pricing go out only after you approve them. Sara tracks the deadlines and what is still open on each bid, and brings you the decisions.",
         desc="Subcontractor procurement AI: build the sub list, send bid invitations, chase quotes, collect COIs and W-9s. Nothing goes to a sub without approval.",
         mock=bids_mock,
         pains=[("Seven invited, three quotes in, and nobody knows who's blocking", "Sara keeps one status page per bid: what's done, what's open, who owns it and what needs you."),
                ("A quote comes in short two items", "Scope is leveled line by line against Taylor's estimate. GAP — 2 ITEMS is marked before the number is compared."),
                ("A sub's insurance certificate expires Friday", "Sara puts the date on the calendar and brings you the decision. She never fixes a problem silently; the call is yours.")],
         faq=[3, 2, 6]),
    dict(slug="construction-bid-management", who="t",
         title="Construction Bid Management With AI | BuildWithBNZ",
         eyebrow="Bid management for specialty contractors", h1="Run the bid, not the spreadsheet.",
         lede="One workspace per bid: files with versions, Taylor's estimate with assumptions and her bid table per trade, and Sara's approvals queue. Specialty contractors get their niche, units and production rates learned once and reused on every bid.",
         desc="Construction bid management for specialty contractors: one workspace per bid, versioned files, estimate assumptions, sub quotes leveled per trade.",
         mock=bids_mock,
         pains=[("Every bid starts from a blank spreadsheet", "Your divisions, units and production rates are the estimate template. Taylor prices the new package against them."),
                ("Addenda land in three inboxes", "Files live in one place with versions and a 'read by Taylor' tick. Replace a sheet and the estimate reissues."),
                ("Bid day is a scramble for missing paperwork", "Sara checks every page of the bid packet before it is sealed: signatures, forms, addenda, insurance certificates and bond. Anything missing comes to you.")],
         faq=[1, 3, 7]),
    dict(slug="construction-project-management-ai", who="s",
         title="Construction Project Management AI | BuildWithBNZ",
         eyebrow="Operations & approvals", h1="Only the decisions that need you.",
         lede="Sara runs Today, the approvals queue and the Monday report. She supervises the other six agents, catches what falls between them, and marks every claim Verified or Reported — never blending the two. What reaches you is a short queue of real decisions.",
         desc="Construction project management AI: a Today board split into verified and reported, an approvals queue where you decide, and a weekly Monday report.",
         mock=today_mock,
         pains=[("'It's done' turns out to mean 'someone said it's done'", "Done — Verified and Done — Reported are two lists. Reported items become Verified only when checked against the document."),
                ("You are the bottleneck on every send", "Bid invitations, follow-ups and requests are drafted into one queue with Approve · Edit · Send back. Ten minutes a day clears it."),
                ("Monday starts with 'where are we?'", "The Monday report: projects active, estimates issued, quotes collected, waiting on you, waiting on subs — named — and anything reported-not-verified.")],
         faq=[3, 6, 1]),
    dict(slug="ai-for-general-contractors", who="s",
         title="AI for General Contractors: Estimating, Subs, Ops | BNZ",
         eyebrow="General contractors", h1="Bid more work without adding estimating headcount.",
         lede=TEAM_LEDE,
         desc="AI for general contractors: Sara leads six AI agents. Taylor builds estimates and compares sub pricing, Emma checks job costs and invoices.",
         mock=sample_project_mock,
         pains=[("You've been sold software before and it didn't stick", "The crew works inside the folders, inbox and calendar you already use. Nothing is migrated, and we stay responsible for it working."),
                ("Estimating is the ceiling on how much you can bid", "Taylor reads the package the same week you approve. Rev 1 with a conflict log and an UNKNOWN list, then Rev 2 when the addendum lands."),
                ("Sub quotes come in on different scopes", "Taylor requests and compares sub and vendor pricing and levels each quote against her estimate, so you compare like with like.")],
         faq=[0, 1, 6]),
    dict(slug="commercial-construction-estimating", who="t",
         title="Estimating for Remodelers & Fit-Out Contractors | BNZ",
         eyebrow="Remodelers & custom builders", h1="Estimates and subs that keep pace with change orders.",
         lede="Remodel and fit-out work changes under you. Taylor reissues the estimate as a revision with a reason every time the scope moves and re-levels the affected sub scopes; Sara brings you the delta and the decisions, not the whole job again.",
         desc="Commercial construction estimating for remodelers, custom builders and fit-out contractors: estimates that revise with a reason when scope moves.",
         mock=est_mock,
         pains=[("The client changes the finish spec mid-bid", "Replace the spec section; Taylor reprices division 09 and shows the delta line by line. Nothing else moves."),
                ("Three subs quoted three different scopes", "Taylor levels each against the estimate and marks the gaps before you compare numbers."),
                ("The change order needs a number today", "Taylor prices from the same basis as the original estimate — the logic is attached, so the client can see why.")],
         faq=[0, 5, 1]),
    dict(slug="prevailing-wage-project-management", who="t",
         title="Prevailing Wage Project Management & Public Bids | BNZ",
         eyebrow="Public work & prevailing wage", h1="Public work, handled by the book.",
         lede="Wage schedules, addenda, bid forms and certified payroll documents. Taylor matches the wage schedule to the county and prices to it line by line; Emma verifies payroll against it. Anything the crew was told but hasn't confirmed stays marked Reported until it's checked against the document itself.",
         desc="Prevailing wage project management for New York GCs bidding public work: county wage schedules, addenda checks, bid forms and certified payroll.",
         mock=public_mock,
         pains=[("The wage schedule is from the wrong county — or last year's", "Taylor matches the schedule to the county and the date, and the match reads VERIFIED against the document, not assumed."),
                ("Addendum 03 is 'coming' according to the architect's office", "That stays REPORTED — NOT VERIFIED on the Monday report until the document is in the set."),
                ("One missing signature can throw out the bid", "Sara checks every page of the packet before it is sealed — signatures, notary pages, addenda, certificates and bond. It stays Not submitted until there is proof it arrived.")],
         faq=[4, 2, 0]),
]

# Links from each lander to the agent page that does that work (Oct 2026 roles:
# Sara runs operations, Taylor does estimating plus sub pricing and leveling, Emma does finance).
AGENT_LINKS = {
    "construction-estimating-ai": [("taylor", "See how Taylor builds the estimate")],
    "commercial-construction-estimating": [("taylor", "See how Taylor builds the estimate")],
    "subcontractor-procurement": [("taylor", "See how Taylor requests and levels sub pricing")],
    "construction-bid-management": [("taylor", "See how Taylor requests and levels sub pricing")],
    "prevailing-wage-project-management": [("taylor", "See how Taylor handles prevailing wage in the estimate"), ("sara", "See how Sara runs the day")],
    "construction-project-management-ai": [("sara", "See how Sara runs the day"), ("emma", "See how Emma checks the job costs")],
    "ai-for-general-contractors": [("sara", "See how Sara runs the day"), ("taylor", "See how Taylor builds the estimate"), ("emma", "See how Emma checks the job costs")],
}

def page_lander(L):
    path = "/%s/" % L["slug"]
    h = head(L["title"], L["desc"], path)  # full title incl. brand, kept <= 60 chars
    h += nav()
    h += hero(L["eyebrow"], L["h1"], L["lede"], L["mock"](False) if L["mock"] is not sample_project_mock else sample_project_mock())
    pains = ''.join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (q, a) for q, a in L["pains"])
    h += section("light", sec_head("On your project", "What changes on day one.") + '<div class="grid g3 stagger pain">%s</div>' % pains)
    h += section("dark", sec_head("How it works", "Scoped and priced in writing before we start.",
                                  "Every engagement starts with a Project Review about one real project. We return scope and one set price, in writing. Price moves only if scope moves. After the first project the crew stays on under a separate monthly arrangement — hosting, monitoring, new projects, a Monday report.")
                 + '<p><a class="link" href="/how-it-works/">The six steps, with what you see at each →</a></p>'
                 + ''.join('<p><a class="link" href="/%s/">%s →</a></p>' % (slug, txt) for slug, txt in AGENT_LINKS.get(L["slug"], [])))
    h += section("light", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h2 style="margin-top:14px">Asked on every call.</h2></div><div class="fx">%s</div></div>' % faq_items([FAQ[i] for i in L["faq"]], 1))
    h += book_strip(dark=True)
    h += footer()
    return h
