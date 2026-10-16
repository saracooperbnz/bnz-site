# -*- coding: utf-8 -*-
"""Internal-linking map (seo-internal-links-v1). One place for every money-page cross-link.
Anchors use each target page's primary keyword from keyword-map-v1.md, so the same URL is
always reached with the same descriptive anchor. BNZ Builders INC contractor pages are never linked here."""

# target -> keyword anchor (primary keyword of the target page)
A = {
    "/construction-estimating-ai/": "AI construction estimating software",
    "/taylor/": "AI takeoff software",
    "/construction-bid-management/": "bid management software for general contractors",
    "/subcontractor-procurement/": "subcontractor management software",
    "/emma/": "AI subcontractor coordination",
    "/sara/": "AI operations manager for construction",
    "/ai-for-general-contractors/": "AI assistant for general contractors",
    "/prevailing-wage-project-management/": "prevailing wage bid estimating",
    "/construction-project-management-ai/": "AI construction project management",
    "/commercial-construction-estimating/": "estimating software for remodelers and fit-outs",
    "/pricing/": "how BuildWithBNZ pricing works",
    "/guides/bid-leveling/": "how to level subcontractor bids",
    "/guides/subcontractor-bid-invitations/": "how to write a sub invitation to bid",
    "/guides/subcontractor-coi-tracking/": "how to track subcontractor COIs",
    "/integrations/google-drive/": "estimating from your Google Drive folder",
    "/integrations/gmail/": "bid invitations from your own Gmail",
    "/integrations/google-calendar/": "bid due dates in Google Calendar",
    "/integrations/notion/": "Notion for construction companies",
    "/how-it-works/": "how AI estimating works for contractors",
    "/faq/": "questions contractors ask",
    "/what-we-connect-to/": "construction AI integrations",
    "/blog/best-ai-estimating-software-for-general-contractors/": "best AI estimating software for general contractors",
    "/blog/planswift-vs-bluebeam/": "PlanSwift vs Bluebeam",
    "/blog/planhub-vs-constructconnect/": "PlanHub vs ConstructConnect",
    "/blog/procore-vs-buildertrend/": "Procore vs Buildertrend",
    "/blog/construction-estimating-software-for-small-business/": "construction estimating software for small business",
    "/blog/togal-ai-review/": "Togal AI review",
    "/blog/buildingconnected-pricing/": "BuildingConnected pricing",
    "/blog/downtobid-pricing/": "Downtobid pricing",
}

MONEY = ["/construction-estimating-ai/", "/taylor/", "/construction-bid-management/", "/subcontractor-procurement/",
         "/emma/", "/sara/", "/ai-for-general-contractors/", "/prevailing-wage-project-management/",
         "/construction-project-management-ai/", "/commercial-construction-estimating/"]

# money page -> sister pages, then related guides / integrations / blog posts
RELATED = {
    "/construction-estimating-ai/": ["/taylor/", "/commercial-construction-estimating/", "/prevailing-wage-project-management/",
                                     "/construction-bid-management/", "/pricing/", "/integrations/google-drive/", "/blog/togal-ai-review/", "/blog/best-ai-estimating-software-for-general-contractors/"],
    "/taylor/": ["/construction-estimating-ai/", "/commercial-construction-estimating/", "/prevailing-wage-project-management/",
                 "/emma/", "/pricing/", "/integrations/google-drive/", "/blog/togal-ai-review/", "/blog/planswift-vs-bluebeam/"],
    "/construction-bid-management/": ["/subcontractor-procurement/", "/emma/", "/construction-estimating-ai/",
                                      "/guides/bid-leveling/", "/guides/subcontractor-bid-invitations/", "/integrations/google-calendar/",
                                      "/blog/buildingconnected-pricing/", "/blog/downtobid-pricing/", "/blog/planhub-vs-constructconnect/"],
    "/subcontractor-procurement/": ["/emma/", "/construction-bid-management/", "/ai-for-general-contractors/",
                                    "/guides/subcontractor-coi-tracking/", "/guides/subcontractor-bid-invitations/", "/guides/bid-leveling/",
                                    "/integrations/gmail/"],
    "/emma/": ["/subcontractor-procurement/", "/construction-bid-management/", "/taylor/", "/sara/",
               "/guides/bid-leveling/", "/guides/subcontractor-bid-invitations/", "/guides/subcontractor-coi-tracking/",
               "/what-we-connect-to/", "/integrations/gmail/", "/blog/buildingconnected-pricing/"],
    "/sara/": ["/construction-project-management-ai/", "/ai-for-general-contractors/", "/taylor/", "/emma/",
               "/how-it-works/", "/faq/", "/integrations/google-calendar/", "/integrations/notion/"],
    "/ai-for-general-contractors/": ["/construction-estimating-ai/", "/construction-bid-management/", "/subcontractor-procurement/",
                                     "/construction-project-management-ai/", "/sara/", "/pricing/", "/guides/bid-leveling/",
                                     "/guides/subcontractor-coi-tracking/", "/blog/construction-estimating-software-for-small-business/"],
    "/prevailing-wage-project-management/": ["/construction-estimating-ai/", "/taylor/", "/construction-bid-management/",
                                             "/subcontractor-procurement/", "/guides/subcontractor-bid-invitations/", "/guides/subcontractor-coi-tracking/"],
    "/construction-project-management-ai/": ["/sara/", "/ai-for-general-contractors/", "/construction-bid-management/",
                                             "/integrations/google-calendar/", "/integrations/notion/", "/blog/procore-vs-buildertrend/"],
    "/commercial-construction-estimating/": ["/construction-estimating-ai/", "/taylor/", "/emma/",
                                             "/subcontractor-procurement/", "/pricing/", "/guides/bid-leveling/", "/blog/best-ai-estimating-software-for-general-contractors/"],
}

def pairs(page):
    return [(u, A[u]) for u in RELATED[page]]

def related_html(page, label="Related"):
    return '%s: %s' % (label, ' · '.join('<a class="link" href="%s">%s</a>' % (u, t) for u, t in pairs(page)))

WHY = {
    "/construction-estimating-ai/": "Estimates from your drawing set, every line sourced.",
    "/taylor/": "Taylor does the takeoff and prices it.",
    "/construction-bid-management/": "One workspace per bid, quotes leveled by trade.",
    "/subcontractor-procurement/": "Sub lists, invitations, COIs and W-9s.",
    "/emma/": "Emma chases subs and levels their quotes.",
    "/sara/": "Sara runs the approvals queue and the Monday report.",
    "/ai-for-general-contractors/": "Bid more work without adding estimating headcount.",
    "/prevailing-wage-project-management/": "Wage schedules, addenda and public bid forms.",
    "/construction-project-management-ai/": "Verified vs reported, and only the decisions that need you.",
    "/commercial-construction-estimating/": "Estimates that revise with a reason when scope moves.",
}

def home_html():
    """Homepage block: every money page, keyword anchor + one-line why."""
    return ''.join('<div class="card"><h3><a class="link" href="%s">%s</a></h3><p>%s</p></div>' % (u, A[u][0].upper() + A[u][1:], WHY[u]) for u in MONEY)
