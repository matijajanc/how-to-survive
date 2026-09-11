#!/usr/bin/env python3
"""
Build the offline bundle for the How To Survive plan.

Produces, from the markdown sources:
  offline/survival-plan.html   one self-contained file, no network of any kind
  offline/survival-plan.txt    plain UTF-8 text, for e-readers and dumb devices

Design constraints, which are the whole point of this file:
  * Python standard library ONLY. No pip, no network, no pandoc.
  * The output must contain zero external references: no CDN, no web fonts,
    no images, no scripts fetched from anywhere.
  * It must run on any machine, offline, years from now.

Usage:  python3 tools/build_offline.py [--check]
        --check  build to a temp buffer and verify, writing nothing
"""

import os
import re
import sys
import html
import textwrap
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "offline")

# --------------------------------------------------------------------------
# Document order. This is the reading order of the whole plan.
# --------------------------------------------------------------------------
DOCUMENT_ORDER = [
    "README.md",
    "docs/00-planning-framework.md",
    "docs/01-water.md",
    "docs/02-electricity.md",
    "docs/03-food-storage.md",
    "docs/04-heating-cooking-fuel.md",
    "docs/05-sanitation-hygiene.md",
    "docs/06-health-and-pandemic-protocol.md",
    "docs/07-land-and-garden.md",
    "docs/08-animals-and-protein.md",
    "docs/09-apartment-playbook.md",
    "docs/10-security-community-communications.md",
    "docs/11-tools-spares-money-documents.md",
    "docs/12-operating-cycles-and-calendar.md",
    "docs/13-offline-and-paper.md",
    "builds/README.md",
    "builds/01-water-builds.md",
    "builds/02-power-builds.md",
    "builds/03-cooking-heat-builds.md",
    "builds/04-sanitation-builds.md",
    "builds/05-food-storage-builds.md",
    "builds/06-garden-builds.md",
    "builds/07-animal-builds.md",
    "builds/08-apartment-builds.md",
    "worksheets/quick-reference-cards.md",
    "worksheets/household-audit.md",
    "worksheets/shopping-lists.md",
    "worksheets/drill-log.md",
    "worksheets/inventory-template.csv",
]

# Short names for the contents page.
SECTION_TITLES = {
    "README.md": "Start here",
    "worksheets/inventory-template.csv": "Inventory template",
}


# --------------------------------------------------------------------------
# Slugs
# --------------------------------------------------------------------------
def heading_slug(text):
    """GitHub's heading-anchor algorithm, so source cross-links keep working.

    Note each space becomes its own hyphen; runs are NOT collapsed.
    """
    t = re.sub(r"<[^>]+>", "", text.strip())
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.lower()
    keep = []
    for ch in t:
        if ch.isalnum() or ch in "-_":
            keep.append(ch)
        elif ch.isspace():
            keep.append(" ")
        # punctuation, symbols and emoji are dropped
    return "".join(keep).strip().replace(" ", "-")


def file_slug(relpath):
    base = relpath.replace("\\", "/")
    if base == "README.md":
        return "start-here"
    if base == "builds/README.md":
        return "builds-index"
    return re.sub(r"[^a-z0-9]+", "-", os.path.splitext(base)[0].lower()).strip("-")


# --------------------------------------------------------------------------
# Inline markdown
# --------------------------------------------------------------------------
CODE_SPAN = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
# non-greedy, and tolerant of nested *italics* inside the bold span
BOLD = re.compile(r"\*\*([^\n]+?)\*\*")
ITALIC = re.compile(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)")


class Inline:
    """Renders inline markdown, rewriting cross-file links to in-page anchors."""

    def __init__(self, anchors, external_notes):
        self.anchors = anchors          # normalised relpath -> file slug
        self.external = external_notes  # collected external URLs

    def resolve(self, srcfile, url):
        """Return (href, is_external)."""
        if url.startswith(("http://", "https://", "mailto:")):
            self.external.add(url)
            return url, True
        path_part, _, frag = url.partition("#")
        if not path_part:                       # same-file anchor
            target = srcfile
        else:
            target = os.path.normpath(
                os.path.join(os.path.dirname(srcfile), path_part)
            ).replace("\\", "/")
        slug = self.anchors.get(target)
        if slug is None:
            return "#" + heading_slug(frag) if frag else "#top", False
        return ("#%s--%s" % (slug, frag)) if frag else ("#" + slug), False

    def render(self, srcfile, text):
        spans = []

        def stash_code(m):
            spans.append(html.escape(m.group(1)))
            return "\x00CODE%d\x00" % (len(spans) - 1)

        text = CODE_SPAN.sub(stash_code, text)
        text = html.escape(text, quote=False)

        def do_link(m):
            label, url = m.group(1), m.group(2)
            href, is_ext = self.resolve(srcfile, url)
            cls = ' class="ext"' if is_ext else ""
            return '<a href="%s"%s>%s</a>' % (html.escape(href, quote=True), cls, label)

        # links are escaped text at this point, so re-find them on the escaped string
        text = LINK.sub(do_link, text)
        text = BOLD.sub(r"<strong>\1</strong>", text)
        text = ITALIC.sub(r"<em>\1</em>", text)
        for i, code in enumerate(spans):
            text = text.replace("\x00CODE%d\x00" % i, "<code>%s</code>" % code)
        return text


# --------------------------------------------------------------------------
# Block parser -> HTML
# --------------------------------------------------------------------------
class Block:
    """Line-based markdown block parser covering the subset used in this repo:
    headings, paragraphs, fenced code, GFM tables, ul/ol with one nesting
    level, blockquotes and horizontal rules."""

    def __init__(self, inline, srcfile, slug, toc):
        self.inline = inline
        self.srcfile = srcfile
        self.slug = slug
        self.toc = toc
        self.out = []
        self.seen = {}

    def anchor(self, text):
        s = heading_slug(text)
        n = self.seen.get(s, 0)
        self.seen[s] = n + 1
        if n:
            s = "%s-%d" % (s, n)
        return "%s--%s" % (self.slug, s)

    def run(self, lines):
        i, n = 0, len(lines)
        while i < n:
            line = lines[i]

            if line.startswith("```"):
                i += 1
                buf = []
                while i < n and not lines[i].startswith("```"):
                    buf.append(lines[i])
                    i += 1
                i += 1
                self.out.append(
                    "<pre><code>%s</code></pre>" % html.escape("\n".join(buf))
                )
                continue

            if not line.strip():
                i += 1
                continue

            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                lvl, txt = len(m.group(1)), m.group(2).strip()
                aid = self.anchor(txt)
                if lvl <= 2:
                    self.toc.append((self.slug, lvl, aid, txt))
                self.out.append(
                    '<h%d id="%s">%s</h%d>'
                    % (lvl, aid, self.inline.render(self.srcfile, txt), lvl)
                )
                i += 1
                continue

            if re.match(r"^\s*([-*_])\s*\1\s*\1[\s\-*_]*$", line):
                self.out.append("<hr>")
                i += 1
                continue

            # GFM table: a pipe row followed by a separator row
            if line.lstrip().startswith("|") and i + 1 < n and \
               re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                rows = []
                while i < n and lines[i].lstrip().startswith("|"):
                    rows.append(lines[i])
                    i += 1
                self.emit_table(rows)
                continue

            if line.lstrip().startswith(">"):
                buf = []
                while i < n and lines[i].lstrip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                inner = Block(self.inline, self.srcfile, self.slug, [])
                inner.seen = self.seen
                inner.run(buf)
                self.out.append("<blockquote>%s</blockquote>" % "".join(inner.out))
                continue

            if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
                i = self.emit_list(lines, i)
                continue

            buf = []
            while i < n and lines[i].strip() and not lines[i].startswith("```") \
                    and not re.match(r"^#{1,6}\s", lines[i]) \
                    and not lines[i].lstrip().startswith(">") \
                    and not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) \
                    and not lines[i].lstrip().startswith("|") \
                    and not re.match(r"^\s*([-*_])\s*\1\s*\1[\s\-*_]*$", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            if buf:
                self.out.append(
                    "<p>%s</p>" % self.inline.render(self.srcfile, " ".join(buf))
                )
            else:
                i += 1
        return self.out

    def emit_table(self, rows):
        def cells(r):
            r = r.strip()
            if r.startswith("|"):
                r = r[1:]
            if r.endswith("|"):
                r = r[:-1]
            return [c.strip() for c in r.split("|")]

        head = cells(rows[0])
        body = [cells(r) for r in rows[2:]]
        h = ["<div class='tablewrap'><table><thead><tr>"]
        for c in head:
            h.append("<th>%s</th>" % self.inline.render(self.srcfile, c))
        h.append("</tr></thead><tbody>")
        for row in body:
            h.append("<tr>")
            for c in row:
                h.append("<td>%s</td>" % self.inline.render(self.srcfile, c))
            h.append("</tr>")
        h.append("</tbody></table></div>")
        self.out.append("".join(h))

    def emit_list(self, lines, i):
        n = len(lines)
        base = len(lines[i]) - len(lines[i].lstrip())
        ordered = bool(re.match(r"^\s*\d+\.\s", lines[i]))
        tag = "ol" if ordered else "ul"
        self.out.append("<%s>" % tag)
        item = None
        while i < n:
            line = lines[i]
            if not line.strip():
                if i + 1 < n and re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i + 1]) \
                        and (len(lines[i + 1]) - len(lines[i + 1].lstrip())) >= base:
                    i += 1
                    continue
                break
            indent = len(line) - len(line.lstrip())
            m = re.match(r"^\s*([-*+]|\d+\.)\s+(.*)$", line)
            if m and indent <= base:
                if item is not None:
                    self.out.append("<li>%s</li>" %
                                    self.inline.render(self.srcfile, " ".join(item)))
                item = [m.group(2)]
                i += 1
            elif m and indent > base:
                if item is not None:
                    self.out.append("<li>%s" %
                                    self.inline.render(self.srcfile, " ".join(item)))
                    item = None
                    i = self.emit_list(lines, i)
                    self.out.append("</li>")
                else:
                    i = self.emit_list(lines, i)
            elif indent > base and item is not None:
                item.append(line.strip())
                i += 1
            else:
                break
        if item is not None:
            self.out.append("<li>%s</li>" %
                            self.inline.render(self.srcfile, " ".join(item)))
        self.out.append("</%s>" % tag)
        return i


# --------------------------------------------------------------------------
# Stylesheet. Inlined into the page: no font files, no external stylesheet.
# --------------------------------------------------------------------------
CSS = """
:root{
  --bg:#fbfaf7; --fg:#1b1a17; --muted:#5d5a52; --rule:#d8d4c8;
  --accent:#7a4a17; --codebg:#f2efe7; --tablehead:#efece3; --warn:#8a2f1d;
  --maxw:46rem;
}
@media (prefers-color-scheme:dark){
  :root{ --bg:#15150f; --fg:#e8e4d9; --muted:#a49f92; --rule:#3a382f;
         --accent:#d8a35e; --codebg:#1f1e17; --tablehead:#23221a; --warn:#e08a72; }
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,
       "Helvetica Neue",Arial,"Noto Sans",sans-serif;
}
.wrap{max-width:var(--maxw); margin:0 auto; padding:0 1rem 5rem}
a{color:var(--accent); text-decoration:underline; text-underline-offset:.15em}
a:hover{text-decoration-thickness:2px}
h1,h2,h3,h4,h5,h6{line-height:1.25; margin:2em 0 .6em; font-weight:700}
h1{font-size:1.85rem; letter-spacing:-.01em}
h2{font-size:1.4rem; border-bottom:2px solid var(--rule); padding-bottom:.25em}
h3{font-size:1.15rem}
h4,h5,h6{font-size:1rem}
p,ul,ol,blockquote{margin:0 0 1em}
ul,ol{padding-left:1.4em}
li{margin:.3em 0}
li>ul,li>ol{margin:.3em 0}
hr{border:0; border-top:1px solid var(--rule); margin:2.2em 0}
blockquote{
  margin-left:0; padding:.7em 1em; border-left:4px solid var(--accent);
  background:var(--codebg); border-radius:0 4px 4px 0;
}
blockquote p:last-child{margin-bottom:0}
code{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  font-size:.9em; background:var(--codebg); padding:.12em .35em; border-radius:3px;
}
pre{
  background:var(--codebg); border:1px solid var(--rule); border-radius:5px;
  padding:.85em 1em; overflow-x:auto; margin:0 0 1.2em;
}
pre code{
  background:none; padding:0; font-size:.82rem; line-height:1.38;
  white-space:pre; display:block;
}
.tablewrap{overflow-x:auto; margin:0 0 1.3em; -webkit-overflow-scrolling:touch}
table{border-collapse:collapse; width:100%; font-size:.92rem}
th,td{border:1px solid var(--rule); padding:.42em .6em; text-align:left;
      vertical-align:top}
th{background:var(--tablehead); font-weight:700}
tbody tr:nth-child(even){background:rgba(125,125,125,.06)}

/* masthead + contents */
.masthead{border-bottom:3px solid var(--accent); margin-bottom:2rem; padding:2.5rem 0 1.2rem}
.masthead h1{margin:0 0 .3rem; font-size:2.1rem}
.masthead .sub{color:var(--muted); margin:0}
.meta{color:var(--muted); font-size:.86rem; margin-top:1rem}
.toc{margin:0 0 3rem}
.toc ol{list-style:none; padding-left:0; margin:0; counter-reset:none}
.toc .chapter{margin:.9em 0 .3em; font-weight:700}
.toc .sub{padding-left:1.4em; font-size:.93rem; margin:.12em 0}
.toc .sub.lvl2{padding-left:2.6em; color:var(--muted)}
#tocfilter{display:none; width:100%; padding:.55em .7em; font-size:1rem;
  border:1px solid var(--rule); border-radius:5px; background:var(--codebg);
  color:var(--fg); margin-bottom:1rem}
.section{border-top:1px solid var(--rule); padding-top:1.5rem; margin-top:3rem}
.section:first-of-type{border-top:0}
.backtop{display:block; margin:2.5rem 0 0; font-size:.85rem; color:var(--muted)}
.notice{
  border:2px solid var(--warn); border-radius:5px; padding:.9em 1.1em;
  margin:1.5rem 0; background:var(--codebg);
}
.notice p:last-child{margin-bottom:0}

/* ---- print ---------------------------------------------------------- */
@media print{
  :root{ --bg:#fff; --fg:#000; --muted:#444; --rule:#999; --accent:#000;
         --codebg:#f4f4f4; --tablehead:#e8e8e8; --warn:#000; }
  body{font-size:10.5pt; line-height:1.45}
  .wrap{max-width:none; padding:0}
  .noprint,#tocfilter,.backtop{display:none !important}
  .section{break-before:page; page-break-before:always; border-top:0; margin-top:0}
  .section:first-of-type{break-before:auto; page-break-before:auto}
  h1,h2,h3,h4{break-after:avoid; page-break-after:avoid}
  pre,blockquote,table,.notice{break-inside:avoid; page-break-inside:avoid}
  tr,li{break-inside:avoid; page-break-inside:avoid}
  pre code{font-size:7.8pt; line-height:1.3; white-space:pre-wrap}
  table{font-size:8.5pt}
  .tablewrap{overflow:visible}
  a{color:#000; text-decoration:none}
  a.ext::after{content:" <" attr(href) ">"; font-size:8pt; word-break:break-all}
}
@page{ margin:15mm 14mm 16mm; }
"""

# Inline, dependency-free. The page is fully usable with JavaScript disabled.
JS = """
(function(){
  var box=document.getElementById('tocfilter');
  if(!box) return;
  box.style.display='block';
  var items=[].slice.call(document.querySelectorAll('.toc li'));
  box.addEventListener('input',function(){
    var q=box.value.toLowerCase().trim();
    items.forEach(function(li){
      li.hidden = q ? li.textContent.toLowerCase().indexOf(q)===-1 : false;
    });
  });
})();
"""


# --------------------------------------------------------------------------
# CSV -> markdown table (for the inventory template)
# --------------------------------------------------------------------------
def csv_to_markdown(path, title):
    import csv as _csv
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(_csv.reader(fh))
    if not rows:
        return "# %s\n\n(empty)\n" % title
    head = [h.replace("_", " ") for h in rows[0]]
    out = ["# %s" % title, ""]
    out.append("A starter inventory. Keep one row per stored item; the point is "
               "the *review by* column, which tells you what expires next. "
               "The machine-readable copy is `worksheets/inventory-template.csv`.")
    out.append("")
    out.append("| " + " | ".join(head) + " |")
    out.append("|" + "|".join(["---"] * len(head)) + "|")
    for r in rows[1:]:
        r = (r + [""] * len(head))[:len(head)]
        out.append("| " + " | ".join(c.replace("|", "/") for c in r) + " |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Plain-text renderer (e-readers, terminals, dumb devices, any printer)
# --------------------------------------------------------------------------
# Emoji and symbols replaced for plain-text readers. Order matters: the
# variation-selector forms must be listed before their bare code points.
TEXT_SYMBOLS = {
    "\U0001F3E1": "[LAND]",   # house with garden  -> land/house track
    "\U0001F3E2": "[FLAT]",   # office building    -> apartment track
    "\u2B1B": "[BOTH]",       # black large square -> applies to both tracks
    "\U0001F528": "[BUILD]",
    "\u26A0\uFE0F": "[!]", "\u26A0": "[!]", "\U0001F6A8": "[!!]",
    "\u2705": "[YES]", "\u274C": "[NO]",
    "\U0001F7E2": "[GREEN]", "\U0001F7E1": "[AMBER]",
    "\U0001F7E0": "[ORANGE]", "\U0001F534": "[RED]", "\u26AB": "[BLACK]",
    "\u2B50": "*", "\u2605": "*",     # stars: value rating
    "\u2B24": "#", "\u25CB": ".",     # filled/hollow circle: skill rating
    # subscripts, for readers with limited fonts
    "\u2080": "0", "\u2081": "1", "\u2082": "2", "\u2083": "3", "\u2084": "4",
    "\u2085": "5", "\u2086": "6", "\u2087": "7", "\u2088": "8", "\u2089": "9",
}
TEXT_WIDTH = 78


def to_text_inline(s):
    for k, v in TEXT_SYMBOLS.items():
        s = s.replace(k, v)
    s = CODE_SPAN.sub(r"\1", s)

    def lnk(m):
        label, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://")):
            return "%s <%s>" % (label, url)
        return label
    s = LINK.sub(lnk, s)
    s = BOLD.sub(r"\1", s)
    s = ITALIC.sub(r"\1", s)
    return s


def table_to_text(rows, width=TEXT_WIDTH, min_col=9, gap=2):
    """Render a GFM table as plain text.

    Preference order: natural-width columns, then columns shrunk and wrapped to
    fit, then one record block per row if there are simply too many columns.
    """
    def cells(r):
        r = r.strip()
        if r.startswith("|"):
            r = r[1:]
        if r.endswith("|"):
            r = r[:-1]
        return [to_text_inline(c.strip()) for c in r.split("|")]

    head = cells(rows[0])
    ncol = len(head)
    body = [(cells(r) + [""] * ncol)[:ncol] for r in rows[2:]]

    def longest(text):
        return max([len(w) for w in text.split()] or [0])

    natural = [max([len(head[c])] + [len(r[c]) for r in body] or [0])
               for c in range(ncol)]
    avail = width - gap * (ncol - 1)

    widths = natural[:]
    if sum(widths) > avail:
        # shave the widest column repeatedly, never below min_col or below the
        # longest single word in it (so words are not chopped mid-way)
        floors = [max(min_col, min(longest(head[c]),
                                   max([longest(r[c]) for r in body] or [0]) or min_col))
                  for c in range(ncol)]
        # never shave a column out of existence (empty columns have width 0)
        floors = [max(1, min(f, natural[c])) for c, f in enumerate(floors)]
        guard = 0
        while sum(widths) > avail and guard < 10000:
            guard += 1
            j, best = -1, 0
            for c in range(ncol):
                if widths[c] > floors[c] and widths[c] > best:
                    j, best = c, widths[c]
            if j < 0:
                break
            widths[j] -= 1

    widths = [max(1, w) for w in widths]

    if sum(widths) <= avail:
        out, multiline = [], False
        def emit(row):
            nonlocal multiline
            wrapped = [textwrap.wrap(row[c], widths[c]) or [""] for c in range(ncol)]
            height = max(len(w) for w in wrapped)
            if height > 1:
                multiline = True
            for k in range(height):
                line = (" " * gap).join(
                    (wrapped[c][k] if k < len(wrapped[c]) else "").ljust(widths[c])
                    for c in range(ncol))
                out.append(line.rstrip())
        emit(head)
        out.append((" " * gap).join("-" * widths[c] for c in range(ncol)))
        for r in body:
            before = len(out)
            emit(r)
            if multiline and len(out) - before > 1:
                out.append("")
        return out

    # too many columns to tabulate: one labelled block per row
    out = []
    for r in body:
        for c, val in enumerate(r):
            if not val.strip():
                continue
            label = (head[c] or ("col%d" % (c + 1))) + ": "
            wrapped = textwrap.wrap(val, max(20, width - len(label))) or [""]
            out.append(label + wrapped[0])
            for extra in wrapped[1:]:
                out.append(" " * len(label) + extra)
        out.append("")
    return out


def markdown_to_text(md, title):
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    out.append("=" * TEXT_WIDTH)
    out.append(title.upper())
    out.append("=" * TEXT_WIDTH)
    out.append("")
    while i < n:
        line = lines[i]

        if line.startswith("```"):
            i += 1
            while i < n and not lines[i].startswith("```"):
                out.append("  " + to_text_inline(lines[i]).rstrip())
                i += 1
            i += 1
            out.append("")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl, txt = len(m.group(1)), to_text_inline(m.group(2).strip())
            out.append("")
            if lvl == 1:
                out.append(txt)
                out.append("=" * min(len(txt), TEXT_WIDTH))
            elif lvl == 2:
                out.append(txt)
                out.append("-" * min(len(txt), TEXT_WIDTH))
            else:
                out.append(("  " * (lvl - 3)) + txt)
            out.append("")
            i += 1
            continue

        if re.match(r"^\s*([-*_])\s*\1\s*\1[\s\-*_]*$", line):
            out.append("")
            out.append("-" * TEXT_WIDTH)
            out.append("")
            i += 1
            continue

        if line.lstrip().startswith("|") and i + 1 < n and \
           re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.extend(table_to_text(rows))
            out.append("")
            continue

        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]).strip())
                i += 1
            # join first: a bold span may wrap across source lines
            para = to_text_inline(" ".join(b for b in buf if b))
            for w in (textwrap.wrap(para, TEXT_WIDTH - 2) or [""]):
                out.append("| " + w)
            out.append("")
            continue

        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if m:
            indent = " " * (len(m.group(1)) + 2)
            marker = m.group(2) if m.group(2)[0].isdigit() else "-"
            raw = [m.group(3)]
            i += 1
            while i < n and lines[i].strip() and \
                    not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) and \
                    not lines[i].startswith("```") and \
                    not re.match(r"^#{1,6}\s", lines[i]) and \
                    not lines[i].lstrip().startswith("|"):
                raw.append(lines[i].strip())
                i += 1
            # join first: a bold span may wrap across source lines
            body = to_text_inline(" ".join(raw))
            first = "%s%s %s" % (" " * len(m.group(1)), marker, body)
            wrapped = textwrap.wrap(first, TEXT_WIDTH,
                                    subsequent_indent=indent + " " * len(marker))
            out.extend(wrapped or [first])
            continue

        if not line.strip():
            if out and out[-1] != "":
                out.append("")
            i += 1
            continue

        buf = []
        while i < n and lines[i].strip() and not lines[i].startswith("```") \
                and not re.match(r"^#{1,6}\s", lines[i]) \
                and not lines[i].lstrip().startswith(">") \
                and not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) \
                and not lines[i].lstrip().startswith("|") \
                and not re.match(r"^\s*([-*_])\s*\1\s*\1[\s\-*_]*$", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        para = to_text_inline(" ".join(buf))
        out.extend(textwrap.wrap(para, TEXT_WIDTH) or [""])
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------
def load_sources():
    """Return [(relpath, title, markdown)] in document order."""
    docs = []
    for rel in DOCUMENT_ORDER:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            sys.stderr.write("warning: missing %s (skipped)\n" % rel)
            continue
        if rel.endswith(".csv"):
            title = SECTION_TITLES.get(rel, "Inventory template")
            md = csv_to_markdown(path, title)
        else:
            md = open(path, encoding="utf-8").read()
            m = re.search(r"^#\s+(.*)$", md, re.M)
            title = SECTION_TITLES.get(rel) or (m.group(1).strip() if m else rel)
        docs.append((rel, title, md))
    return docs


def build_html(docs, stamp):
    anchors = {rel: file_slug(rel) for rel, _, _ in docs}
    # cross-links point at the .csv path too
    anchors["worksheets/inventory-template.csv"] = file_slug(
        "worksheets/inventory-template.csv")
    external = set()
    inline = Inline(anchors, external)

    toc, sections = [], []
    for rel, title, md in docs:
        slug = file_slug(rel)
        blk = Block(inline, rel, slug, toc)
        toc.append((slug, 0, slug, title))          # chapter entry
        body = blk.run(md.split("\n"))
        sections.append(
            '<section class="section" id="%s">\n%s\n'
            '<a class="backtop" href="#contents">&uarr; Contents</a>\n</section>'
            % (slug, "\n".join(body))
        )

    # contents
    toc_html = ['<nav class="toc" id="contents"><h2>Contents</h2>',
                '<input id="tocfilter" type="search" placeholder="Filter contents'
                ' (type to search)" aria-label="Filter contents">', "<ol>"]
    for slug, lvl, aid, txt in toc:
        label = html.escape(re.sub(r"\*\*?", "", txt))
        if lvl == 0:
            toc_html.append('<li class="chapter"><a href="#%s">%s</a></li>'
                            % (aid, label))
        else:
            toc_html.append('<li class="sub lvl%d"><a href="#%s">%s</a></li>'
                            % (lvl, aid, label))
    toc_html.append("</ol></nav>")

    ext_list = ""
    if external:
        items = "".join('<li><code>%s</code></li>' % html.escape(u)
                        for u in sorted(external))
        ext_list = ("<p>This document links to %d external address(es), listed in "
                    "the offline chapter. They will not work without a network — "
                    "everything you need to act is contained in this file.</p>"
                    "<ul>%s</ul>" % (len(external), items))

    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>How To Survive — Household Pandemic Resilience Plan</title>
<style>%s</style>
</head>
<body>
<div class="wrap" id="top">
<header class="masthead">
<h1>How To Survive</h1>
<p class="sub">A household pandemic resilience plan — water, power, food, heat,
sanitation, health, growing, animals, security and the cycles that repeat.</p>
<div class="notice">
<p><strong>This file is complete and works offline.</strong> It needs no network,
no fonts, no server and no apps. Save it, copy it to a phone, a USB stick and an
e-reader, and print it. Use your browser's Print command for a paper copy —
it is formatted for A4 with each chapter starting on a new page.</p>
</div>
<p class="meta">Built %s · %d sections · Metric units, EUR, temperate
continental Central Europe · Not medical advice — see the chapter on health.</p>
</header>
%s
%s
<section class="section" id="offline-selfcheck">
<h1>About this file</h1>
<p>Generated from the markdown sources by <code>tools/build_offline.py</code>,
which uses only the Python standard library. To rebuild it on any machine, with
no network and nothing installed beyond Python 3:</p>
<pre><code>python3 tools/build_offline.py</code></pre>
<p>The page contains no external stylesheets, scripts, fonts, images or trackers.
Everything — layout, contents, search — is inside this one file. The small piece
of JavaScript only filters the contents list; with JavaScript disabled the page
is fully readable and printable.</p>
%s
<a class="backtop" href="#contents">&uarr; Contents</a>
</section>
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, stamp, len(docs), "\n".join(toc_html), "\n".join(sections),
       ext_list, JS)
    return doc, external


def build_text(docs, stamp):
    parts = []
    bar = "#" * TEXT_WIDTH
    parts.append(bar)
    parts.append("#  HOW TO SURVIVE — HOUSEHOLD PANDEMIC RESILIENCE PLAN")
    parts.append("#  Plain-text edition. Complete, offline, no network needed.")
    parts.append("#  Built %s" % stamp)
    parts.append(bar)
    parts.append("")
    parts.append("CONTENTS")
    parts.append("-" * TEXT_WIDTH)
    for idx, (_, title, _) in enumerate(docs, 1):
        parts.append("%2d. %s" % (idx, re.sub(r"\*\*?", "", title)))
    parts.append("")
    for idx, (rel, title, md) in enumerate(docs, 1):
        parts.append("")
        parts.append(markdown_to_text(md, "%d. %s" % (idx, title)))
    return "\n".join(parts) + "\n"


def self_check(doc):
    """Fail loudly if anything in the page would need a network to render."""
    problems = []
    for pat, what in (
        (r"<script[^>]+src\s*=", "external script"),
        (r"<link[^>]+rel=[\"']?stylesheet", "external stylesheet"),
        (r"<img[^>]+src\s*=", "image"),
        (r"@import", "CSS @import"),
        (r"url\(\s*[\"']?https?:", "remote CSS url()"),
        (r"<iframe", "iframe"),
        (r"integrity\s*=", "subresource integrity (implies a CDN)"),
    ):
        if re.search(pat, doc, re.I):
            problems.append(what)
    return problems


def main():
    check_only = "--check" in sys.argv
    stamp = datetime.date.today().isoformat()
    docs = load_sources()
    if not docs:
        sys.stderr.write("error: no source documents found\n")
        return 2

    doc_html, external = build_html(docs, stamp)
    doc_text = build_text(docs, stamp)

    problems = self_check(doc_html)
    if problems:
        sys.stderr.write("OFFLINE CHECK FAILED — page would fetch: %s\n"
                         % ", ".join(problems))
        return 1

    if not check_only:
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(os.path.join(OUT_DIR, "survival-plan.html"), "w",
                  encoding="utf-8") as fh:
            fh.write(doc_html)
        with open(os.path.join(OUT_DIR, "survival-plan.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write(doc_text)

    print("offline bundle: %d sections" % len(docs))
    print("  survival-plan.html  %7.1f KB" % (len(doc_html.encode()) / 1024))
    print("  survival-plan.txt   %7.1f KB" % (len(doc_text.encode()) / 1024))
    print("  external links      %7d (listed in the page; none are loaded)"
          % len(external))
    print("  offline self-check  PASSED — no external resources referenced")
    if check_only:
        print("  (--check: nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
