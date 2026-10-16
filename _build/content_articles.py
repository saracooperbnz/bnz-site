# -*- coding: utf-8 -*-
"""Pricing, integration and guide pages, built from the cleaned drafts in _build/articles/*.md.
Each .md has a small front-matter block (title_tag, meta_description, url_slug), a ```json FAQPage block
(emitted as JSON-LD) and a Markdown body. The H1 and 'short answer' become the hero; the rest is prose."""
import os, re, json, html as _h
from shared import *

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "articles")

# file -> (eyebrow, crew mark for the hero card)
ARTICLES = [
    ("how-pricing-works", "How pricing works", "s"),
    ("integrations-google-drive", "Integrations · Google Drive", "t"),
    ("integrations-gmail", "Integrations · Gmail", "e"),
    ("integrations-google-calendar", "Integrations · Google Calendar", "s"),
    ("integrations-notion", "Integrations · Notion", "e"),
    ("guide-coi-tracking-for-gcs", "Guide · COI tracking", "e"),
    ("guide-bid-leveling", "Guide · Bid leveling", "e"),
    ("guide-subcontractor-bid-invitations", "Guide · Invitations to bid", "e"),
]
# links in the drafts that point at pages that don't exist (yet) -> where they go instead
LINK_FIX = {"/integrations/": "/what-we-connect-to/"}

def load(name, art_dir=None):
    raw = open(os.path.join(art_dir or ART, name + ".md"), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", raw, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
        if mm and mm.group(2): meta[mm.group(1)] = mm.group(2)
    body = raw[m.end():]
    ld = None
    jm = re.search(r"```json\n(.*?)\n```", body, re.S)
    if jm:
        ld = json.loads(jm.group(1))
        body = body[:jm.start()] + body[jm.end():]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    return meta, ld, body

def inline(t):
    t = _h.escape(t, quote=False)
    def link(m):
        href = LINK_FIX.get(m.group(2), m.group(2))
        return '<a class="link" href="%s">%s</a>' % (href, m.group(1))
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t

def md(body):
    out, lines, i = [], body.split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith("### "): out.append("<h3>%s</h3>" % inline(l[4:])); i += 1; continue
        if l.startswith("## "): out.append("<h2>%s</h2>" % inline(l[3:])); i += 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            hd, rest = rows[0], [r for r in rows[1:] if not all(re.fullmatch(r":?-+:?", c) for c in r)]
            out.append('<div class="tbl"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                ''.join("<th>%s</th>" % inline(c) for c in hd),
                ''.join("<tr>%s</tr>" % ''.join("<td>%s</td>" % inline(c) for c in r) for r in rest)))
            continue
        if l.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            paras = re.split(r"\n\s*\n", "\n".join(q))
            out.append("<blockquote>%s</blockquote>" % ''.join("<p>%s</p>" % "<br>".join(inline(x) for x in p.split("\n")) for p in paras if p.strip()))
            continue
        if re.match(r"^(- |\d+\. )", l):
            tag = "ol" if re.match(r"^\d+\. ", l) else "ul"
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i])); i += 1
            out.append("<%s>%s</%s>" % (tag, ''.join("<li>%s</li>" % inline(x) for x in items), tag))
            continue
        p = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|- |\d+\. |\||>)", lines[i]):
            p.append(lines[i]); i += 1
        if p:
            # a bold line followed by its answer (FAQ style) -> keep the line break
            out.append("<p>%s</p>" % "<br>".join(inline(x) for x in p))
        else:
            i += 1
    return "\n".join(out)

def page_article(name, eyebrow, who, art_dir=None, extra_ld=None):
    meta, ld, body = load(name, art_dir)
    path = meta["url_slug"]
    h1 = re.search(r"^# (.+)$", body, re.M).group(1)
    body = body.replace("# %s\n" % h1, "", 1)
    sm = re.search(r"^\*\*The short answer:\*\*\s*(.+)$", body, re.M)
    lede = inline(sm.group(1)) if sm else ""
    if sm: body = body.replace(sm.group(0), "", 1)
    # visible FAQ section: rendered with the site's FAQ component instead of prose
    # the visible FAQ is rendered from the JSON-LD itself, so the two always match word for word
    faq = [(inline(q["name"]), inline(q["acceptedAnswer"]["text"])) for q in (ld or {}).get("mainEntity", [])]
    fm = re.search(r"^## FAQ\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if fm:
        body = body.replace(fm.group(0), "")
    # last section (the CTA) becomes the book strip, so drop it from the prose
    parts = re.split(r"(?=^## )", body, flags=re.M)
    if parts and re.search(r"\(/book/\)", parts[-1]) and len(parts[-1]) < 600:
        parts = parts[:-1]
    prose = md("".join(parts))
    if extra_ld:
        ld = [x for x in (extra_ld(meta, h1), ld) if x]
    jsonld = json.dumps(ld, ensure_ascii=False, separators=(",", ":")) if ld else None
    h = head(meta["title_tag"], meta["meta_description"], path, jsonld=jsonld)
    h += nav()
    card = ('<div class="card">%s<p class="muted" style="margin-top:14px">%s</p>'
            '<p style="margin-top:14px"><a class="link" href="/what-we-connect-to/">What the crew connects to →</a></p></div>') % (
        av(who, 56, anim=True), PITCH)
    h += ('<section class="dark hero"><div class="wrap"><div class="fx"><span class="eyebrow">%s</span><h1>%s</h1>'
          '<p class="lede">%s</p><div class="cta">%s<a class="link" href="/how-it-works/">See how it works</a></div></div>'
          '<div class="fx">%s</div></div></section>\n') % (eyebrow, inline(h1), lede, btn_book(), card)
    h += section("light", '<article class="prose fx">%s</article>' % prose)
    if faq:
        h += section("dark", '<div class="faq-grid"><div class="fx"><span class="eyebrow">FAQ</span><h2 style="margin-top:14px">Asked on every call.</h2></div><div class="fx">%s</div></div>' % faq_items(faq, len(faq)))
    h += book_strip()
    h += footer()
    return path, h
