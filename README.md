# How To Survive — A Household Pandemic Resilience Plan

A complete, step-by-step plan for getting a household through a severe pandemic
with degraded or interrupted public services: water, electricity, food, heat,
sanitation, medicine and security.

Two tracks run through every chapter:

- **🏡 LAND** — you have a house with a garden, yard, field or orchard.
- **🏢 APARTMENT** — you have a flat, a balcony at best, and shared infrastructure.

> **📴 Works offline.** The entire plan is also built into a single
> self-contained file — [`offline/survival-plan.html`](offline/survival-plan.html)
> — that needs no internet, no server and nothing installed. Copy it to a phone,
> a USB stick and an e-reader, and **print it**. Rebuild it any time with
> `make offline` (Python standard library only).

Units are metric. Prices are indicative EUR. The garden calendar is written for
**temperate continental Central Europe** (Slovenia/Austria/N. Italy/Croatia —
last frost mid-April to mid-May, first frost mid-October). Adjust dates to your
own frost dates; everything else transfers.

---

## Read this first: what this plan actually assumes

A pandemic is **not** an instant apocalypse. It is a long, grinding degradation.
Planning for the wrong shape of event is the single most common and most
expensive mistake people make.

What actually happens, in rough order:

1. **Weeks 0–4** — News, then panic buying. Shelves empty of exactly the things
   you need (flour, oil, tinned goods, paracetamol, toilet paper, baby formula).
   Prices spike. This is the moment when preparing becomes impossible, expensive,
   and antisocial. **Everything in this plan must be bought before this point.**
2. **Months 1–6** — Lockdowns or voluntary isolation. Hospitals saturate;
   *ordinary* illness (appendicitis, heart attack, childbirth, a broken arm)
   becomes far more dangerous than usual. Supply chains work but stutter.
   Some goods simply vanish for months.
3. **Months 2–12+** — Staff absence hits infrastructure: water treatment,
   electricity distribution, fuel logistics, waste collection, pharmacy
   restocking. You get **intermittent** services, not zero services. Rolling
   blackouts. Boil-water notices. Rubbish uncollected. Deliveries halted.
   Cash-only, then barter at the margins.
4. **Year 1–3** — Economic damage, inflation, unemployment, shortages of spare
   parts and imported goods. Recovery is uneven. This is the long tail where
   "self-sufficiency" actually pays off.

**Design target: 12 months of intermittent utilities, and 3 months of no
resupply at all, while never leaving your property.**

That is the standard this whole plan is written against. It is achievable for a
normal household on a normal budget, if you start early and build in order.

---

## The four hard truths

1. **You cannot become fully self-sufficient.** Nobody is. Not on a hectare, not
   with chickens, not with solar. You will still need salt, fuel, medicine,
   spare parts, seed and metal. The goal is not independence — it is
   **reducing dependence, buying time, and lowering your exposure.** A household
   that needs a shop once a month instead of twice a week is enormously safer.
2. **Skills beat gear.** A €3,000 solar system you have never wired, a pressure
   canner you have never used, and a garden you have never grown will all fail
   at the worst moment. Every purchase in this plan carries an implied homework
   assignment: use it now, while mistakes are cheap.
3. **You survive with neighbours, not against them.** The lone fortress is a
   fantasy that gets people killed. Three to eight cooperating households can
   share a well, a generator, a watch rotation, a nurse and a freezer. One
   household cannot do any of that, and cannot sleep.
4. **The things that kill people are boring.** Not raiders. Dehydration,
   dysentery from bad sanitation, hypothermia in an unheated house, an untreated
   infection, a missed insulin dose, and carbon monoxide from cooking indoors.
   Spend your money and attention in that order.

---

## The priority order (spend money in this sequence)

Rank everything by **how fast its absence kills you**. Never buy from a lower
tier while a higher tier has a gap.

| # | Need | You survive without it for | Chapter |
|---|------|---------------------------|---------|
| 1 | Air, warmth, shelter | 3 hours (exposure/CO) | [04](docs/04-heating-cooking-fuel.md) |
| 2 | Critical medication | Hours to days (insulin, cardiac, epilepsy, steroids) | [06](docs/06-health-and-pandemic-protocol.md) |
| 3 | Water | 3 days | [01](docs/01-water.md) |
| 4 | Sanitation & hygiene | ~1 week before disease | [05](docs/05-sanitation-hygiene.md) |
| 5 | Food | 3 weeks (but you are useless after 1) | [03](docs/03-food-storage.md) |
| 6 | Light, power, information | Weeks (morale and safety collapse first) | [02](docs/02-electricity.md) · [10](docs/10-security-community-communications.md) |
| 7 | Renewable food production | Months (matters from month 3 onward) | [07](docs/07-land-and-garden.md) · [08](docs/08-animals-and-protein.md) · [09](docs/09-apartment-playbook.md) |
| 8 | Security, repair, money | Ongoing | [10](docs/10-security-community-communications.md) · [11](docs/11-tools-spares-money-documents.md) |

---

## The four readiness levels

Do not try to jump to Level 3. Complete each level fully — across *all*
categories — before starting the next. A household with 12 months of rice and no
water plan is less prepared than one with two weeks of everything.

| Level | Endurance | Rough cost (family of 4) | Time to build |
|-------|-----------|--------------------------|---------------|
| **L0 — Ready** | 72 hours, no utilities | €250 – €500 | One weekend |
| **L1 — Buffered** | 2 weeks, no resupply | €800 – €1,800 | One month |
| **L2 — Isolated** | 3 months, no resupply; power & water for critical loads | €3,000 – €8,000 | 3 – 6 months |
| **L3 — Self-renewing** | 12 months, with food/energy/water production that repeats | €8,000 – €25,000 | 1 – 3 years |

L3 is the only level that includes **cycles** — things that regenerate: seed you
saved, chicks that hatched, compost you made, wood you seasoned. Everything below
L3 is a countdown timer. See [Chapter 12](docs/12-operating-cycles-and-calendar.md).

---

## How to use this repository

**Step 1 — Measure where you actually are.**
Fill in [`worksheets/household-audit.md`](worksheets/household-audit.md). It takes
about an hour and tells you your current survival time in days, per category.
Do not buy anything before you do this.

**Step 2 — Read the planning framework.**
[`docs/00-planning-framework.md`](docs/00-planning-framework.md) — how to set
targets, budget, sequence purchases, and define the trigger points that tell you
*when* to act.

**Step 3 — Work the categories in priority order.**
Chapters 01 → 06 are universal and come first. Then take your track:
[07](docs/07-land-and-garden.md) + [08](docs/08-animals-and-protein.md) if you
have land, [09](docs/09-apartment-playbook.md) if you do not.

**Step 4 — Buy from the tiered lists.**
[`worksheets/shopping-lists.md`](worksheets/shopping-lists.md) — exactly what to
buy at each level, in purchase order, with quantities for your household size.

**Step 5 — Test it. Then test it again.**
[`worksheets/drill-log.md`](worksheets/drill-log.md) — the blackout weekend, the
water-off day, the isolation drill. Untested preparation is a guess.

**Step 6 — Build what you need.**
[`builds/`](builds/README.md) — construction plans with dimensions, cut lists,
materials and costs, ordered so the highest-value builds come first. A bucket
water filter takes 30 minutes; the chicken coop takes a weekend.

**Step 7 — Make it work offline.**
[`offline/survival-plan.html`](offline/survival-plan.html) is the whole plan in
one self-contained file — no internet, no server, no apps. Open it in any
browser, or print it. A plan you cannot reach in a blackout is not a plan; see
[Chapter 13](docs/13-offline-and-paper.md).

**Step 8 — Run the cycles.**
[`docs/12-operating-cycles-and-calendar.md`](docs/12-operating-cycles-and-calendar.md)
— the daily, weekly, monthly and seasonal routines that keep stock rotated,
gardens producing, and animals breeding. This is the part that turns a stockpile
into a system.

---

## Contents

### Planning
- **[00 — Planning framework](docs/00-planning-framework.md)** — threat model, household audit, levels, budget tiers, sequencing, the Green/Amber/Red trigger ladder, common mistakes.

### Universal survival systems (do these first, both tracks)
- **[01 — Water](docs/01-water.md)** — how much you need, storage, rainwater, wells, filtration, purification, greywater, apartment water sources.
- **[02 — Electricity](docs/02-electricity.md)** — load audit, solar sizing, batteries, inverters, generators, fuel, wiring safety, the four power tiers.
- **[03 — Food storage](docs/03-food-storage.md)** — calorie maths, the one-year staple base, packing for 25-year shelf life, nutrition gaps, preservation (canning, fermenting, drying, curing), rotation.
- **[04 — Heating, cooking & fuel](docs/04-heating-cooking-fuel.md)** — the warm-room strategy, insulation, firewood maths, stoves, cooking fuel ranking, fuel-efficient cooking, carbon monoxide.
- **[05 — Sanitation & hygiene](docs/05-sanitation-hygiene.md)** — the thing that actually kills people; toilets without water, humanure, greywater, laundry, soap, menstrual and infant supplies, waste and vector control.
- **[06 — Health & pandemic protocol](docs/06-health-and-pandemic-protocol.md)** — prescription buffers, the medical stock list, PPE, isolation room, decontamination, ventilation, dental, mental health, when to break isolation for care.

### Production — the land track 🏡
- **[07 — Land & garden](docs/07-land-and-garden.md)** — how much land per person, calorie-dense crops, bed layout, the hungry gap, seed saving, soil fertility without inputs, perennials, water in the garden, pests, tools.
- **[08 — Animals & protein](docs/08-animals-and-protein.md)** — chickens (and the feed problem nobody plans for), rabbits, quail, goats, pigs, bees, fish; breeding cycles that actually renew; slaughter, butchery and preservation.

### Production — the apartment track 🏢
- **[09 — Apartment playbook](docs/09-apartment-playbook.md)** — honest limits, sprouts and microgreens (the real answer), mushrooms, fermentation, container growing, quail, balcony solar, bucket toilets, cooking indoors safely, vertical-building failure modes.

### Holding it together
- **[10 — Security, community & communications](docs/10-security-community-communications.md)** — OPSEC, layered security, the mutual-aid group, the charity plan, radios, offline information, family contact plan.
- **[11 — Tools, spares, money & documents](docs/11-tools-spares-money-documents.md)** — hand tools, the spares kit, single points of failure, cash, barter goods, the document pack, skills to learn.
- **[12 — Operating cycles & calendar](docs/12-operating-cycles-and-calendar.md)** — daily/weekly/monthly/seasonal/annual routines, the garden year month by month, the livestock year, the rotation and maintenance schedule.

### Offline & paper
- **[13 — Offline, paper & keeping the plan readable](docs/13-offline-and-paper.md)** — what to print and in what order, the three-copies rule, devices that work when power is uncertain, media longevity, the offline reference library to download before you need it, keeping it findable by someone other than you.

### Build plans 🔨
- **[Build index](builds/README.md)** — every build in priority order, with time, cost and skill level; plus the tool kit, timber sizes, fixings, mesh and safety fundamentals.
- **[01 — Water builds](builds/01-water-builds.md)** — bucket gravity filter, tippy-tap, first-flush diverter, IBC stand and manifold, slow sand filter, solar water heater, ollas and drip.
- **[02 — Power builds](builds/02-power-builds.md)** — the complete 12 V solar system with cable-sizing and fusing tables, DC lighting circuit, insulated battery box, adjustable tilt frame, generator noise screen.
- **[03 — Cooking & heat builds](builds/03-cooking-heat-builds.md)** — rocket stoves, haybox/thermal cooker, solar oven, solar dehydrator, wood store, warm-room tent.
- **[04 — Sanitation builds](builds/04-sanitation-builds.md)** — bucket toilet, urine diverter, humanure compost bays, handwash station, plunger washing machine, greywater mulch basin.
- **[05 — Food storage builds](builds/05-food-storage-builds.md)** — root cellar, buried barrel cellar, root clamp, cool pantry, mylar packing station, cold smoker, curing racks.
- **[06 — Garden builds](builds/06-garden-builds.md)** — no-dig beds, three-bay compost, insect mesh cage, cold frame, low tunnel, walk-in polytunnel, seed rack, liquid feed barrel.
- **[07 — Animal builds](builds/07-animal-builds.md)** — **the full chicken coop plan**, predator-proof run, chicken tractor, feeders and drinkers, rabbit hutch, quail cage, black soldier fly bucket, fodder rack.
- **[08 — Apartment builds](builds/08-apartment-builds.md)** — sprouting rack, microgreen shelf, mushroom bucket, wormery, self-watering containers, balcony rain catch, air cleaner, under-bed storage.

### Worksheets
- **[Quick-reference cards](worksheets/quick-reference-cards.md)** — ⭐ **print these first.** The numbers you need at 3 a.m. by torchlight: water treatment doses, oral rehydration, bleach dilutions, carbon monoxide, when to seek help, the trigger ladder, the daily routine, your shut-offs and contacts.
- **[Household audit](worksheets/household-audit.md)** — fill this in second.
- **[Shopping lists](worksheets/shopping-lists.md)** — tiered, in buy-order, with quantities.
- **[Drill log](worksheets/drill-log.md)** — the tests that prove it works.
- **[Inventory template](worksheets/inventory-template.csv)** — what you have, where, expiry.

---

## Legal, ethical and medical note

- Prepare **early and gradually**. Buying a year of food over twelve months is
  prudent; buying it in the week panic starts takes it from someone who needs it
  that day. The ethical way to prepare is the same as the effective way: start now.
- Follow public health guidance and get vaccinated. Nothing in this plan is a
  substitute for medical care, and none of it is medical advice — build your
  medication buffer *with* your doctor and pharmacist, never by skipping doses.
- Well drilling, rainwater use, greywater, wood stoves, solar grid connection,
  livestock keeping, slaughter, waste disposal and firearms are all regulated and
  the rules differ by country and municipality. Check before you build.
- Keep helping people. A household that is calm, stocked and healthy is the one
  that can afford to help neighbours — which is exactly what makes the street
  around you survivable.
