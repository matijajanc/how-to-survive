# Offline Bundle

**The whole plan, in two files that need no internet, no server, no apps and no
installation.** Copy them to a phone, a USB stick, an e-reader and a printer.

| File | What it is |
|---|---|
| **`survival-plan.html`** | The complete plan as **one self-contained page**. Double-click it and it opens in any browser, with a searchable contents list, dark mode for night reading, and a print layout for A4. No CDN, no web fonts, no images, no trackers — it references nothing outside itself. |
| **`survival-plan.txt`** | The complete plan as **plain UTF-8 text**, wrapped to 78 columns with tables rendered as aligned columns. For e-readers, old phones, terminals, and any printer that exists. |

Both files are **committed to the repository**, so downloading the repo as a ZIP
gives you working copies with nothing to build.

---

## Use it

**Read it:** open `survival-plan.html` in any browser — from a USB stick, a
phone's Files app, anywhere. It works with the network switched off. It works
with JavaScript disabled (you just lose the contents filter box).

**Print it:** open the HTML and press Print → A4, double-sided. Each chapter
starts on a new page; tables, diagrams and warning boxes are kept whole; dark
backgrounds are dropped. About 150–200 pages. Put it in a labelled ring binder.

**Print only the essentials:** print
[`worksheets/quick-reference-cards.md`](../worksheets/quick-reference-cards.md)
and laminate it — 11 cards with the numbers you need at 3 a.m. by torchlight.
See [Chapter 13](../docs/13-offline-and-paper.md#3-what-to-print-in-priority-order)
for the full print order.

---

## Rebuild it

After editing any source file:

```
make offline        # or: python3 tools/build_offline.py
```

| Command | Does |
|---|---|
| `make offline` | Build both files |
| `make check` | Verify the page references nothing external, writing nothing |
| `make links` | Verify every internal link and heading anchor resolves |
| `make all` | `links` then `offline` |
| `make print` | How to get a paper copy |
| `make clean` | Remove the generated files (sources untouched) |

**The build uses only the Python standard library.** No `pip install`, no
network, no pandoc, no Node — so it still works on an offline machine, or in ten
years. The build fails loudly if the generated page would try to fetch anything
at all.

---

## Why this exists

A plan stored on a website you cannot reach, or a phone that is dead, is not a
plan:

```
Website        → needs internet + power + a working device
Cloud document → needs internet + an account + power + a device
Phone PDF      → needs power + that specific device
E-reader       → needs occasional power (weeks per charge)
USB stick      → needs SOME working computer
★ PAPER        → needs daylight, or a candle
```

Keep copies at several of those levels at once. See
[Chapter 13 — Offline, paper & keeping the plan readable](../docs/13-offline-and-paper.md).

---

**Back to:** [README](../README.md)
