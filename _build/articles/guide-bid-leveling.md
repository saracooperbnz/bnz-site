---
title_tag: "Bid Leveling in Construction: How to Set Up the Sheet | BNZ"
meta_description: "How to build a bid leveling sheet that holds up on bid day: the columns, the scope rows, plug values, and how it differs from a bid tab. Layout included."
url_slug: /guides/bid-leveling/
primary_keyword: bid leveling construction
secondary_keywords:
  - bid leveling template excel
  - bid tab construction
  - scope gaps in subcontractor bids
suggested_internal_links:
  - /blog/how-to-level-subcontractor-bids/ (existing Blog-1, anchor: "step-by-step guide to leveling sub bids") [OWNER DATA NEEDED: confirm Blog-1's live URL]
  - /emma/ (anchor: "Emma levels every scope")
  - /taylor/ (anchor: "Taylor's estimate")
  - /construction-bid-management/ (anchor: "bid management software")
  - /guides/subcontractor-bid-invitations/ (anchor: "write invitations that get comparable bids")
  - /book/ (anchor: "Book a Project Review")
status: DRAFT. Angle chosen to avoid duplicating Blog-1 (which covers the 7-step leveling process). This page is the sheet/template + bid tab angle. Cannibalization note: Blog-1 should target "how to level subcontractor bids"; this page keeps "bid leveling construction" per keyword map.
---

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is the difference between a bid tab and a bid leveling sheet?",
     "acceptedAnswer": {"@type": "Answer", "text": "A bid tab lists bids as submitted, side by side. A leveling sheet adjusts each bid to the same scope first, with plug values for gaps, so the totals can be compared fairly."}},
    {"@type": "Question", "name": "Can I level bids in Excel or Google Sheets?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes. Most contractors start with a spreadsheet. The key is that rows come from your scope baseline, not from the bids, and every plug value has a written source."}},
    {"@type": "Question", "name": "What goes in the rows of a leveling sheet?",
     "acceptedAnswer": {"@type": "Answer", "text": "The scope items a complete bid should cover, built from the drawings, specs, scope sheet and latest addendum, plus a few standard rows for addenda acknowledged, alternates, unit prices, exclusions and qualifications."}}
  ]
}
```

# Bid leveling in construction: how to set up the sheet

**The short answer:** A bid leveling sheet puts every sub's bid for one trade on the same scope. Rows are scope items from your documents. Columns are bidders. Each cell says Included, Excluded, Unclear or Extra, and every gap gets a plug value with a written source. The bottom line is the leveled total, not the base bid. This page is about building that sheet so it works.

## Bid tab vs. leveling sheet

People use the words loosely, so be clear inside your team:

- **Bid tab (bid tabulation):** bids as submitted, side by side. On public work the owner often publishes one after bid opening. It tells you who said what.
- **Leveling sheet:** the GC's internal sheet that adjusts each sub's bid to one scope before you choose who carries the trade. It tells you what each bid really costs.

You usually need both. The bid tab is the record. The leveling sheet is the decision. Good [bid management software for general contractors](/construction-bid-management/) keeps both in one place for each bid.

## The layout

One tab per trade package. Freeze the top rows and the first two columns.

**Header block (top of the tab):**
- Project name and number
- Trade / package (e.g., Division 26 Electrical)
- Bid documents set and latest addendum number
- Bid due date and time, with time zone
- Prepared by / date / revision

**Columns:**

| Column | What goes in it |
|---|---|
| A. Scope item | One line per item from your baseline |
| B. Source | Sheet or spec section (e.g., E-402, 26 05 19) |
| C. Your estimate | Your own number for the line, if you have one |
| D, E, F… one per bidder | Status code + note |
| Plug column per bidder | Dollar value carried for gaps, with source |

**Status codes (keep them to four):**
- **I** Included
- **X** Excluded (the sub said it's out)
- **?** Unclear (not mentioned, or wording is vague)
- **+** Extra (in the bid, but not in your scope)

**Rows at the bottom of every tab:**
1. Base bid as submitted
2. Addenda acknowledged (by number)
3. Plugs added (sum of plug column)
4. Extras removed
5. **Leveled total** = base bid + plugs − extras
6. Alternates (each on its own line, never in the total)
7. Unit prices
8. Allowances
9. Exclusions and qualifications, copied word for word
10. Schedule / lead time stated
11. COI and W-9 on file (Y/N)
12. Clarifications sent / answered (date)

## Where the rows come from

Build rows from the documents, not from the most detailed bid. Use the drawings, the specs, your trade scope sheet, Division 01 and the latest addendum. If a bidder raises an item you missed, add a row and note who raised it. Organize rows the way your estimate is organized (many estimators use CSI MasterFormat) so each sub's line sits next to your number. If your estimate comes from [AI construction estimating software](/construction-estimating-ai/), use its line items as the rows, and have [AI subcontractor coordination](/emma/) level each quote against them.

## Plug values that hold up

A plug is the amount you carry for scope a bidder left out. The plug is only as good as its source. In the plug column, write where the number came from:

- another bidder's price for the same item
- your own estimate line
- a supplier quote
- historical cost from a past job

If you can't source it, mark it UNKNOWN and go get the number. Don't guess.

## Scope gaps to check on every trade

These show up as "?" more than anything else. Add rows for them so they can't hide:

- Temporary power, lighting and protection
- Permits and inspections
- Hoisting, lifts and equipment
- Cleanup and debris removal
- Testing, commissioning and closeout documents
- Patching and firestopping at your penetrations
- Overtime or off-hours work required by the specs
- Bond, if the job requires sub bonds
- Prevailing wage, on public work

## Sheet mistakes that cost jobs

- Totals that include alternates.
- No addendum row, so a bid priced off old sheets looks cheapest.
- Plugs with no source, so nobody can defend the leveled number to the owner.
- Exclusions paraphrased instead of copied.
- One sheet for the whole job instead of one per trade.
- Leveling a bid that came in without the bid form you asked for. Send the [same clarification](/guides/subcontractor-bid-invitations/) to everyone it affects.

## How BuildWithBNZ does it (example workflow)

Emma collects quotes from sub replies in your Gmail and levels every scope against Taylor's estimate. Taylor's estimate is the baseline, with each line traced to a sheet or spec section, and UNKNOWN where the documents are missing information. Gaps go back to the sub as a drafted clarification that waits for your approval. The output is a leveled bid table per trade, saved in your own Google Drive.

[Book a Project Review](/book/) to see a leveled table on one of your bids.

## FAQ

**What's the difference between a bid tab and a leveling sheet?**
A bid tab shows bids as submitted. A leveling sheet adjusts them to the same scope first.

**Can I level bids in Excel or Google Sheets?**
Yes. Rows from your scope baseline, a sourced plug for every gap.

**What goes in the rows?**
Scope items from your documents, plus standard rows for addenda, alternates, unit prices, exclusions and qualifications.
