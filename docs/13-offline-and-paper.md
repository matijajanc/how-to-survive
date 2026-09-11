# 13 — Offline, Paper & Keeping the Plan Readable

*A survival plan stored on a website you cannot reach, or a phone that is dead,
is not a plan. This chapter makes the whole thing work with no internet, no
power, and no functioning device.*

---

## 1. The failure this prevents

Think through the actual sequence. The grid goes down, or the network congests,
or your phone dies on day three and the charger is useless. At that exact moment
you want to know: **how many drops of bleach per litre? what is the oral
rehydration recipe? what temperature kills botulism spores? which vent goes
high and which goes low?**

If the answer lives in a browser tab, a cloud document, a bookmark, or a GitHub
repository, you do not have it.

```
Website        → needs internet + power + a working device
Cloud document → needs internet + an account + power + a device
Phone PDF      → needs power + that specific device
Laptop file    → needs power + that specific device
E-reader       → needs occasional power (weeks per charge)
USB stick      → needs SOME working computer
★ PAPER        → needs daylight, or a candle
```

**Every layer above paper can fail simultaneously, and in a bad winter they
will.** Paper is the floor you build up from.

---

## 2. The rule: three copies, three formats, one off-site

Adapted from the standard backup rule, for a household:

| # | Copy | Format | Where |
|---|------|--------|-------|
| 1 | **Printed binder** | Paper | On the shelf, in the house, findable by anyone |
| 2 | **Laminated cards** | Paper | By the water store, the stove, the medical kit, the toilet |
| 3 | **E-reader or old phone** | Digital, offline | In the kit, charged, with the solar charger |
| 4 | **USB stick ×2** | Digital | One in the document pack, one with a relative in another town |
| 5 | **Repository clone** | Digital | On the family computer, so you can reprint and update |

**One copy must be off-site.** Fire, flood and theft are more likely than any
pandemic scenario, and they take the house, the binder and the USB stick in the
document drawer together.

---

## 3. What to print, in priority order

Printing 5,500 lines is about **150–200 A4 pages** double-sided. That is one
ream and an afternoon. But if you only print some of it, print it in this order.

### Tier 1 — print today, laminate, and post on the wall (8 pages)
**[`worksheets/quick-reference-cards.md`](../worksheets/quick-reference-cards.md)**
— the numbers you need under stress, by torchlight, without reading a chapter:
water treatment doses · oral rehydration recipe · bleach dilutions · carbon
monoxide rules · when to seek medical help · the trigger ladder · the Amber
72-hour list · the daily routine · your shut-off locations · your contacts.

**These ten cards are the single highest-value pages in the entire plan.**
Print two sets — one for the kitchen, one for the kit.

### Tier 2 — the working core (about 60 pages)
- [01 Water](01-water.md) · [04 Heating, cooking & fuel](04-heating-cooking-fuel.md) ·
  [05 Sanitation](05-sanitation-hygiene.md) · [06 Health & pandemic protocol](06-health-and-pandemic-protocol.md)
- [`worksheets/household-audit.md`](../worksheets/household-audit.md) — **print it
  and fill it in by hand.** A filled-in audit is worth more than the whole rest
  of the binder.
- [`worksheets/shopping-lists.md`](../worksheets/shopping-lists.md)
- [12 Operating cycles](12-operating-cycles-and-calendar.md) — the daily,
  weekly and seasonal routines

### Tier 3 — the rest of the plan (about 80 pages)
Chapters 00, 02, 03, 07–11, the drill log, and the inventory template.

### Tier 4 — the builds (about 50 pages)
[`builds/`](../builds/README.md). Print the ones you intend to build, when you
intend to build them — they are working drawings, so they will get wet, muddy
and annotated. **Print the chicken coop and the bucket filter regardless**;
those two get built by most households.

### How to print the whole thing in one go
Open **`offline/survival-plan.html`** in any browser and press Print. It is
formatted for A4: each chapter starts on a new page, tables and diagrams are
kept whole, dark backgrounds are dropped, and external web addresses are printed
in full after their link text so a paper reader can still see where something
came from.

**Print double-sided, punch it, and put it in a ring binder with dividers.**
A ring binder beats a stapled stack: you can reprint one chapter, you can add
your own notes, and you can pull out the page you need and take it to the job.

---

## 4. The offline bundle

Two files in [`offline/`](../offline/), both generated from the markdown sources:

| File | What it is | Use it when |
|---|---|---|
| **`survival-plan.html`** | The complete plan as **one self-contained page**. No network, no fonts, no images, no server, no CDN. Opens from a USB stick by double-clicking. Readable on a phone, works in dark mode, prints properly. | Any device with a browser |
| **`survival-plan.txt`** | The complete plan as **plain UTF-8 text**, wrapped to 78 columns, tables rendered as aligned columns. | E-readers, old phones, terminals, anything that chokes on HTML. Prints on anything. |

**Both are committed to the repository**, so downloading the repo as a ZIP from
a browser gives you the ready-to-use files with nothing to build or install.

### Rebuilding them
If you edit the plan — and you should, it is *your* plan — regenerate with:

```
python3 tools/build_offline.py      # or: make offline
```

The build script uses **only the Python standard library**: no `pip install`,
no internet, no pandoc, no Node. It runs on any machine with Python 3, today or
in ten years. It also self-checks the output and fails if the page would try to
fetch anything at all from the network.

```
make offline    build both files
make check      verify the build fetches nothing, without writing
make links      verify every internal link and anchor resolves
make print      print instructions
make clean      remove generated files
```

---

## 5. Devices that actually work when the power is uncertain

| Device | Battery life | Verdict |
|---|---|---|
| **E-reader (e-ink)** | **Weeks per charge**, ~1 Wh/day | ⭐ **The best offline library there is.** Holds thousands of books, sips power, readable in bright sun, charges from a tiny solar panel. Load it with this plan plus the reference library below. |
| **Old phone, wiped, airplane mode** | Days, as a dedicated reader | ⭐ Excellent second copy. No SIM, no apps, WiFi off, screen dim. It becomes a library, not a phone. |
| Current phone | 1–2 days | Fine, but it is doing ten other jobs and it will be flat |
| Tablet | 1–2 days | Good screen for build drawings; power-hungry |
| Laptop | Hours | Only for editing and printing, not for reading in a crisis |
| **Paper** | **Infinite** | ⭐ The one that cannot fail |

Charging all of these is covered by the **P0 tier** in
[Chapter 02](02-electricity.md) — a 20 W folding panel and a power bank, about
€150, which is the cheapest meaningful preparation in the whole plan.

### Honest note on digital media longevity
- **USB flash and SD cards:** reliable for a few years, then increasingly not.
  Unpowered charge leakage is real. **Copy the data to a fresh stick every 2
  years**, keep two sticks, and never treat one as an archive.
- **Hard drives:** fine while used, unreliable after years on a shelf.
- **Optical discs:** ordinary burned DVDs degrade in 5–10 years; archival
  M-DISC is rated far longer but you need a drive to read it.
- **Paper in a dry box:** decades to centuries, readable by anyone, no format
  obsolescence, no reader required.

**Conclusion: paper is the archive. Digital is the convenience.** Keep both, and
refresh the digital copies on the annual review (Chapter 12 §9).

---

## 6. The offline reference library — download and print BEFORE you need it

This plan is deliberately self-contained: **everything you need to act is in
these pages.** But a few outside references are genuinely worth having, and
every one of them must be obtained while you still have a connection.

### Get these now

| Reference | What it gives you | Note |
|---|---|---|
| **Where There Is No Doctor** (Hesperian) | Diagnosis and treatment when no professional is available. Written for exactly this situation. | Free digital editions from the publisher. **Print it, or at least the chapters on dehydration, wounds, infection and childbirth.** |
| **Where There Is No Dentist** (Hesperian) | Toothache, abscess, temporary fillings, extraction | Free digital editions. Toothache with no dentist is one of the most demoralising things in a long crisis. |
| **Tested home-canning times and pressures** (a national food-preservation extension service, or a current edition preserving book) | ⚠️ **Safety-critical.** Pressure and time for every low-acid food. | **Print the tables.** Do not improvise, and do not rely on family memory — this is the one place in the plan where getting it wrong is fatal. |
| A **regional vegetable growing guide** and a **seed-saving guide** | Sowing dates, spacings, isolation distances for your climate | Local beats generic |
| A **foraging guide with good photographs**, for your region | Wild food and medicine | ⚠️ Photographs matter. Never eat anything you have not positively identified. |
| **Paper maps** — road and topographic, your region | Navigation with no GPS | Plus a compass, and know how to use them |
| A **first aid manual** | The basics, on paper | Take the course too; the book is the reminder |
| Repair references | Bicycle, small engine, plumbing, electrics, sewing | Whatever matches the things you own |
| **Offline Wikipedia** (e.g. a Kiwix `.zim` archive) | An enormous general reference, fully offline | A medical or general subset fits on a phone; the full thing needs ~100 GB |
| **Offline maps** on the phone | Downloaded map regions that work in airplane mode | Download your region **and** the surrounding ones |
| Seed catalogue, tool manuals, appliance manuals | Part numbers, specifications | Save the PDFs, print the critical pages |

### The rule
> **Anything that exists only as a bookmark does not exist.**
> Download it, print the parts you would need in the dark, and put the files on
> the e-reader and both USB sticks.

Do a **download day** once a year, at the annual review. It takes two hours and
it is the cheapest preparation on the list.

---

## 7. Make it findable and readable by someone else

This is the [single-point-of-failure rule](11-tools-spares-money-documents.md)
applied to the plan itself. If only you can find it and only you understand it,
then you getting ill — which is exactly what a pandemic does — takes the whole
household's plan out with you.

```
[ ] The binder lives in ONE obvious, named place. Everyone knows where.
[ ] It is labelled on the spine, in plain language, not "prep stuff".
[ ] The quick-reference cards are ON THE WALL, not in the binder.
[ ] The household audit is filled in, in pen, at the front.
[ ] The system notes are written: how the power system starts, where the
    stopcock is, how the filter is backflushed, what the alarms mean.
[ ] At least two people have read the binder and run a drill from it.
[ ] The contacts card is filled in, including the out-of-area contact.
[ ] A relative in another town has a copy.
```

**Write in the binder.** Annotate it, correct it, add your own frost dates,
your own well depth, your own meter readings. A marked-up binder is a working
document; a pristine one has never been used.

---

## 8. Keeping it current

On the **annual review** (Chapter 12 §9):

1. Re-run the household audit — people, medicines and endurance all change.
2. Update the plan with what you learned from the year's drills.
3. `make offline` to regenerate the HTML and text files.
4. **Reprint the chapters that changed** and swap the pages in the binder.
5. Refresh both USB sticks onto **new** sticks; post one to the off-site holder.
6. Re-sync the e-reader.
7. Do the download day (§6).
8. Check the printed cards are still legible and still on the wall.

---

## 9. Offline checklist

```
[ ] offline/survival-plan.html opens with the network switched off
[ ] It prints correctly to A4 (chapters start on new pages)
[ ] Tier 1 quick-reference cards PRINTED and LAMINATED
[ ] Cards posted: kitchen, water store, stove, medical kit, toilet
[ ] Full plan printed and in a labelled ring binder
[ ] Household audit filled in BY HAND at the front of the binder
[ ] System notes written (power, water, stove, shut-offs)
[ ] E-reader or wiped old phone loaded, charged, in the kit
[ ] Solar panel + power bank that can charge it
[ ] 2 × USB sticks written; one held off-site by a relative
[ ] Repository cloned to the family computer so it can be reprinted
[ ] Reference library downloaded AND the critical parts printed
[ ] Canning time/pressure tables printed (safety-critical)
[ ] Paper maps of the region + a compass
[ ] Two people have read the binder and run a drill from it
[ ] Annual refresh scheduled in the December review
```

---

**🔨 Build it:** [All build plans](../builds/README.md) — construction plans for everything in this plan, in priority order

**Previous:** [12 — Operating cycles & calendar](12-operating-cycles-and-calendar.md) ·
**Back to:** [README](../README.md)
