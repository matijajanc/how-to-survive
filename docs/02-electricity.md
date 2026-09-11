# 02 — Electricity

*You do not need "power". You need a short list of specific things to keep
working. Identify that list, shrink it, then build the smallest system that
covers it. Everyone who does it the other way round wastes thousands of euros.*

---

## 1. Step one: the load audit (do this before spending anything)

List every device, its wattage, and hours per day. Multiply. That gives you
**watt-hours per day (Wh/day)** — the only number that matters for sizing.

```
Wh/day = Watts × hours per day
1,000 Wh = 1 kWh
```

Measure real wattage with a **plug-in energy meter (€10–15)**. Do not trust
labels — they show peak, not average. Leave the meter on the fridge for 24 hours;
the result will surprise you.

### Typical loads

| Device | Watts | Typical Wh/day | Notes |
|---|---|---|---|
| Phone charge | 10 W | 15–25 | Trivial. Two phones ≈ 40 Wh |
| LED bulb / lamp | 5–9 W | 30–60 for a house | 4 lamps × 4 h = ~100 Wh |
| LED headlamp / lantern | 1–3 W | 10 | The cheapest light there is |
| Laptop | 30–65 W | 150–300 | |
| Radio / DAB / shortwave | 3–10 W | 20–50 | |
| Internet router + modem | 10–20 W | 240–480 | Surprisingly hungry; runs 24 h |
| **Fridge-freezer, A+++, modern** | 100 W when running | **300–500** | Compressor cycles ~25–35% of the time |
| Fridge-freezer, 10+ years old | 150 W | 700–1,400 | Replacing an old fridge can halve your whole system cost |
| **Chest freezer, full, A++** | 100 W | **400–700** | Full freezers are far more efficient than empty ones |
| Washing machine (cold/30 °C) | 150–500 W | 300–600 per load | The heating element is the load; cold wash is cheap |
| Washing machine (60 °C) | 2,000 W | 1,000–1,500 per load | Avoid |
| Well pump (submersible, ½ HP) | 400–800 W running, 2–3 kW surge | 200–600 | **Surge is the problem, not the running load** |
| Circulation pump (heating) | 20–60 W | 500–1,400 | Runs constantly in winter. A gas boiler is useless without it |
| Boiler control/ignition | 50–150 W | 200–800 | |
| CPAP (no humidifier) | 30–60 W | 250–500 | **Life-critical for some — size for it explicitly** |
| Oxygen concentrator | 300–600 W | 4,000–10,000 | Huge. Needs a real system or a generator |
| Medical fridge (insulin) | 50–80 W | 200–400 | Can share the main fridge |
| LED grow light (microgreens) | 20–40 W | 240–560 | 12–16 h/day |
| Kettle | 2,000 W | 200 per boil | **Never on battery — boil on gas or wood** |
| Microwave | 1,000 W | 100 per 6 min | Occasional use only |
| Electric hob / oven | 2,000–3,000 W | Thousands | **Never. Cook with fuel, not electricity.** |
| Electric heater | 2,000 W | 20,000+ | **Never. See Ch. 04.** |
| Immersion heater | 3,000 W | Thousands | Never |
| Power tools (drill, grinder) | 500–1,500 W | Short bursts | Fine with a decent inverter |

### The three tiers of load

Sort your list into these three buckets. **This sorting is the whole exercise.**

**TIER 1 — LIFE CRITICAL. Must never stop.**
Medical devices (CPAP, oxygen, insulin cooling), phone charging, one light,
the radio. *Typical total: 100–800 Wh/day.* Anyone can afford to cover this.

**TIER 2 — HIGH VALUE. Protects food, health and sanity.**
Fridge, freezer, water pump, more lighting, laptop, router, tool charging,
washing machine occasionally. *Typical total: 1,000–2,500 Wh/day.*

**TIER 3 — COMFORT. Nice, sacrificable.**
TV, gaming, dishwasher, hair dryer, air conditioning, electric cooking,
electric heating. *Typical total: 3,000–20,000 Wh/day.*
**Tier 3 should never touch your off-grid system.** Trying to include it is what
makes people conclude "solar is unaffordable". It isn't — Tier 3 is.

Write your three totals here:
```
Tier 1: _______ Wh/day      Tier 2: _______ Wh/day      Tier 3: _______ Wh/day
```

---

## 2. Step two: cut the load before you buy generation

Every watt-hour you remove is a watt-hour you never have to generate, store,
convert or repair. **Efficiency is 5–10× cheaper than generation.**

| Action | Cost | Saves |
|---|---|---|
| Replace all bulbs with LED | €30 | 80–90% of lighting load |
| Replace a 10-year-old fridge with A+++ | €400 | 400–900 Wh/day — often pays back the whole battery |
| Keep the freezer full (water bottles fill the gaps) | Free | 10–20%, plus 48 h of cold if power fails |
| Move the fridge/freezer out of the warm kitchen, into a cool cellar/garage in winter | Free | Up to 40% in winter |
| Add a thermal cooker/haybox and pressure cooker | €60–120 | 50–70% of cooking energy |
| Wash cold, dry on a line | Free | 60–80% of laundry energy |
| 12 V DC LED strips and USB charging direct from the battery | €40 | Avoids 10–15% inverter loss *and* lets you switch the inverter off entirely |
| Switch the inverter OFF when not in use | Free | Idle draw is 10–30 W = **240–700 Wh/day wasted on nothing** |
| Use headlamps instead of room lighting | €20 | 90% of lighting |
| Kill standby loads with switched power strips | €15 | 100–400 Wh/day |

**Do all of these before buying a single panel.** A household that cuts Tier 2
from 2,500 to 1,200 Wh/day halves the cost of its entire power system.

---

## 3. The four power tiers — pick one

| | **P0 — Lights & phones** | **P1 — Essentials** | **P2 — Household core** | **P3 — Whole-house off-grid** |
|---|---|---|---|---|
| **Covers** | Phones, LED lights, radio | + fridge, laptop, router, tools | + freezer, water pump, washing machine, workshop | + heat pump, cooking, most things except resistive heat |
| **Daily energy** | 100–300 Wh | 1,000–1,500 Wh | 3,000–6,000 Wh | 10,000–20,000 Wh |
| **Solar** | 50–150 W | 400–800 W | 1.5–3 kW | 5–10 kW |
| **Battery** | 250–600 Wh | 1.2–2.5 kWh | 5–10 kWh | 15–30 kWh |
| **Inverter** | none / 300 W | 1,000–1,500 W | 2,400–3,600 W | 5–8 kW hybrid |
| **Cost** | €150–400 | €900–2,000 | €4,000–9,000 | €12,000–30,000 |
| **Who** | Everyone, immediately. Apartment L0/L1 | Apartment L2, house L1 | House L2 — **the sweet spot** | House L3, or homes with electric heat |

**Recommendation for almost everybody: build P0 now (this month, €200), then jump
to P1 or P2 as budget allows.** P0 alone removes the panic from a blackout.

---

## 4. Sizing the system properly

### Solar — the winter problem

A solar panel's rating is its output in perfect conditions. Real daily yield
depends on **peak sun hours (PSH)** for your location and month.

**Central Europe (≈46 °N), fixed panels at ~35° tilt facing south:**

| Month | PSH/day | Yield per 1 kW of panels |
|---|---|---|
| June–July | 5.0 – 5.5 | 4.0 – 4.5 kWh/day |
| April / August | 4.0 – 4.5 | 3.2 – 3.6 kWh/day |
| March / September | 3.0 | 2.4 kWh/day |
| October | 2.0 | 1.6 kWh/day |
| **November–January** | **0.8 – 1.2** | **0.6 – 1.0 kWh/day** |

Apply a **system derate of 0.75–0.8** for wiring, controller, temperature,
dirt and inverter losses — the yields above already include it.

> **The rule that matters: size for December, not for June.**
> Winter yield is **4–6× worse** than summer. In Central Europe you may also get
> 5–10 consecutive overcast days in December with near-zero output.

**Worked example — P2 system, family of four:**
```
Winter critical load (fridge, freezer, lights, comms, pump) = 2,000 Wh/day
December yield per kW                                        = 0.8 kWh/day
Panels needed for December autonomy  = 2,000 / 800           = 2.5 kW
```
2.5 kW of panels costs about €700–1,000 today. In June the same array makes
11 kWh/day — a massive surplus, which is exactly why a **winter generator or wood
heat is part of the design**, not an admission of failure.

**Practical compromises:**
- Size panels for ~60–70% of winter need and cover the gap with a generator
  running 1–2 hours on the worst days. This is far cheaper than doubling the array.
- **Over-panel the charge controller** (within its voltage limits) — panels are
  now the cheapest component. A 30% oversize massively improves dull-day output.
- **Steepen the tilt in winter** (latitude + 15°, so ~60° at 46 °N). Adjustable
  mounts gain 20–30% in December and shed snow. Two tilt changes a year is a
  10-minute job with real returns.
- **Keep panels clear of snow.** A dusted panel makes nothing. Steep tilt + a soft
  brush on a pole.
- **Shade is catastrophic, not proportional.** One shaded cell can cut a whole
  string's output by 50%+. Survey the winter sun path (the sun is very low from
  November to February — trees and buildings that don't shade in June will in
  December).

### Batteries — LiFePO₄, essentially always

| | Lead-acid (AGM/flooded) | **LiFePO₄ (LFP)** |
|---|---|---|
| Usable depth of discharge | 50% (going deeper kills it) | 80–100% |
| Cycle life | 300–800 | **3,000–6,000** |
| Usable kWh from a "5 kWh" bank | 2.5 kWh | 4.5–5 kWh |
| Cost per **usable** kWh over life | High | **3–5× lower** |
| Weight | 2–3× heavier | Light |
| Charging | Fussy, needs absorption/float stages, gasses | Simple, fast, sealed |
| Cold charging | Tolerant | **Must not charge below 0 °C** without a heater/BMS protection |
| Upfront cost | €100–150/kWh | €200–350/kWh |

**Buy LiFePO₄** unless you are salvaging free lead-acid. It is cheaper per
delivered kilowatt-hour, safer than other lithium chemistries (no thermal
runaway in normal use), and vastly less maintenance.

**Sizing:** aim for **1.5 – 2 days of your critical load** in usable capacity.
Enough to ride through one bad day and a night without hitting empty.
```
Critical load 2,000 Wh/day × 1.5 days = 3,000 Wh usable
LiFePO₄ at 90% usable                → 3.3 kWh nominal → buy 4–5 kWh
```
**Cold weather:** keep the battery indoors, above 5 °C. A LiFePO₄ bank in an
unheated garage in January will refuse to charge and you will think it's broken.
Either buy cells with built-in low-temperature cut-off and heating, or site the
bank inside.

### Charge controller
- **MPPT, always.** It harvests 15–30% more than PWM, more in cold and dull
  conditions, and lets you use cheap high-voltage panels with a low-voltage
  battery. The price difference is €50.
- Size the controller for panel current with headroom (e.g. 2.5 kW at 24 V ≈
  100 A → a 100 A MPPT).
- **Buy a spare controller.** It is the most likely electronic failure point,
  it's small and cheap, and without it your panels and battery are decorations.

### Inverter
- **Pure sine wave.** Modified sine damages motors, fridges, chargers, and
  medical devices, and buzzes in audio. Never buy modified sine for a household.
- Size for **peak surge**, not average. A fridge compressor or a well pump draws
  3–6× its running wattage for a second or two at start. A 500 W pump may need a
  2,000–3,000 W inverter.
- **Low-frequency (transformer) inverters** handle surge far better than
  high-frequency ones — worth the extra cost and weight if you must start pumps.
- **Idle consumption matters enormously.** A 3 kW inverter idling at 25 W burns
  600 Wh/day doing nothing — potentially a third of your generation. Switch it
  off when it isn't needed, and run lights and USB directly from 12 V DC.
- A **hybrid/all-in-one inverter-charger** (inverter + MPPT + mains charger +
  transfer switch in one box) is the simplest choice for P2/P3 and handles
  grid/generator/solar changeover automatically.

### System voltage
- 12 V for P0/P1 (huge choice of cheap 12 V appliances, pumps and lights).
- 24 V or 48 V for P2/P3 (thinner cables, less loss, cheaper per watt).
- Rule of thumb: over ~1.5 kW of load, go 24 V or 48 V.

---

## 5. Generators — the honest assessment

A generator is a **fuel-to-electricity converter, not an energy source.** Its
endurance equals your fuel store, and fuel is the hardest thing to store.

**Fuel maths.** A small inverter generator makes roughly **2.5–3.5 kWh per litre
of petrol** at good load, much worse when lightly loaded. A 5 kWh day therefore
costs ~2 L/day → **60 L/month → 180 L for three months.** Storing 180 L of petrol
safely is a serious undertaking, and petrol only keeps 6–12 months with stabiliser.

**Therefore: never run a generator to supply loads directly all day.** Instead:

> **The right pattern — batch charging.** Run the generator at 60–80% load
> (its efficient point) for 1–2 hours, charging the battery bank *and* running
> the fridge/freezer/washing machine/tools at the same time. Then shut it down
> and live off the battery. This cuts fuel use by 60–80%, quarters the noise
> exposure, and multiplies engine life.

**Choosing one**
- **Inverter generators** (Honda EU22i and clones): quiet (~50–60 dB), clean
  power safe for electronics, fuel-efficient at part load. 2–2.5 kW is enough for
  battery charging plus a fridge. ~€500–1,500.
- **Dual-fuel (petrol + LPG)** is the strategic choice: **propane stores
  indefinitely**, burns clean, doesn't gum the carburettor, and is easy to buy and
  store in 11 kg cylinders. ~€600–1,200.
- Conventional open-frame 5–7 kW sets are cheap and loud, and produce dirty power.
  Fine for tools and pumps, poor for electronics and terrible for OPSEC.
- **Diesel** stores longer than petrol (1–2 years, longer with biocide and a
  sealed tank), is more efficient, but the small sets are loud and expensive.

**Fuel storage**
| Fuel | Shelf life | Notes |
|---|---|---|
| Petrol | 3–6 months bare · 12–24 months with stabiliser (Stabil/Aspen) | Buy ethanol-free if available; ethanol absorbs water and destroys carburettors. Alkylate petrol (Aspen) stores 3–5 years but is expensive. |
| Diesel | 12 months · 2–5 years with biocide + stabiliser, sealed, cool | Watch for diesel bug (microbial growth) — use a biocide |
| **Propane / LPG** | **Indefinite** | **The best fuel to store.** 11 kg cylinder ≈ 150 kWh of heat. No degradation, no spillage, no fire risk if stored outside and upright. |
- Store fuel **outside the house** in approved containers, in the shade, away from
  ignition sources, and check your local legal storage limits (often 20–30 L of
  petrol domestically).
- **Rotate petrol through your car** every 6 months — that's the trick that makes
  fuel storage practical.
- Keep the generator's own consumables: oil, oil filter, air filter, **spark
  plugs**, and a spare carburettor (€20 and the #1 failure item on small engines).

**Safety — this kills people every single winter**
- **NEVER run a generator indoors, in a garage, in a cellar, in a porch, or near
  an open window.** Carbon monoxide is odourless and kills in minutes. Not "with
  the door open". Outside, ≥ 5 m from any opening, with the exhaust pointed away.
- **CO alarms in every sleeping area and in the room with any combustion.** €20
  each. Non-negotiable. See Ch. 04.
- **Never backfeed** a generator into a wall socket to power the house. It kills
  line workers, destroys your appliances, and is illegal. Use a **manual transfer
  switch or a breaker interlock kit**, installed by an electrician (€150–400).
  Without one, run extension leads to specific appliances only.
- Let it cool before refuelling. Petrol on a hot exhaust is a fire.

### Other generation, honestly assessed
- **Wind:** small turbines rarely produce what's claimed. Only worth it on an
  exposed site with genuine average wind ≥ 5 m/s, on a tall mast. Most domestic
  wind is money better spent on panels. *But:* wind produces in winter when solar
  doesn't, so a good site makes an excellent complement.
- **Micro-hydro:** if you have a stream with head and flow, this is the best
  off-grid power there is — 24/7, year-round, weather-independent. Even 200 W
  continuous = 4.8 kWh/day, better than a large solar array in winter. Investigate
  seriously if you have water rights.
- **Pedal generator:** a fit person sustains 50–100 W. One hour of hard pedalling
  ≈ 75 Wh ≈ what a €30 solar panel makes in an afternoon for free. Good for
  morale and fitness; not a power strategy.
- **Thermoelectric (stove-top TEG, Peltier):** 5–15 W. Charges a phone off a wood
  stove. A nice redundancy, not a system.
- **Car alternator:** your car is a 1–2 kW generator you already own. A €30
  inverter on the cigarette socket gives 150 W; wired directly to the battery
  with a proper 1,000 W inverter it will run a fridge while idling. Idling burns
  ~1 L/h, so use it as an emergency charger, not a habit. **Same CO rules — never
  in a garage.**

---

## 6. Wiring it safely

- **DC side:** correct cable gauge for current and run length (undersized DC cable
  is the classic fire cause — voltage drop under 3%), **fuse or breaker within
  30 cm of the battery positive**, fuses on every branch, a main isolator switch
  you can reach in the dark.
- **Battery location:** ventilated, above freezing, not in the living space if
  lead-acid (hydrogen gas), secured so it can't shift, not above or below
  anything precious.
- **AC side:** anything connecting to house wiring must be done by a qualified
  electrician, with an RCD/GFCI and correct earthing, and must be legal in your
  jurisdiction. A transfer switch or interlock is mandatory.
- **Grid-tied solar does NOT work in a blackout.** Standard grid-tie inverters
  shut down when the grid drops (anti-islanding), by law. If you already have
  solar, check whether it has a **hybrid inverter with battery and an EPS/backup
  output** — if not, your panels are useless in exactly the situation you bought
  them for. Retrofitting a hybrid inverter + battery is the fix.
- **Label everything.** Breakers, cables, polarity, what circuit feeds what.
  Write the system diagram on paper and pin it next to the equipment. In six
  months, at 3 a.m., in the dark, you will not remember.

---

## 7. Keeping food cold without much power

This is usually the biggest single reason to have power at all.

- A **full chest freezer** holds food safely for **48 hours unopened** (24 h for
  an upright fridge-freezer). Fill air gaps with bottles of water — the frozen
  mass is thermal storage.
- **Freeze bottles of water** as your "battery" — move them into the fridge
  compartment during outages.
- **Chest beats upright** by a wide margin (cold air doesn't fall out when opened).
  A chest freezer plus a thermostat controller can also run *as a fridge* at a
  fraction of a normal fridge's energy (~100–200 Wh/day).
- **Duty-cycle it:** run the freezer hard while the sun is up, let it coast
  overnight. A well-insulated full freezer barely drifts.
- **Winter is free refrigeration.** From November to March in Central Europe, an
  insulated box on the north side of the house, a cellar, or an unheated pantry
  does the job for nothing. Plan the year so freezer contents are lowest in
  summer — preserve by canning and drying instead (Ch. 03).
- **Root cellar** (land track): a properly built cellar holds 2–8 °C year-round
  with **zero energy** and stores potatoes, roots, apples and cabbages for months.
  It is the highest-return "appliance" on a homestead. See Ch. 03 §7.

---

## 8. Lighting — cheap, and hugely important for morale

- **Headlamps first.** 1–3 W, hands free, directional. Buy one per person plus
  two spares. This is the most cost-effective light in existence.
- **Rechargeable AA/AAA (Eneloop-type) + a USB charger.** ~€60 for 16 cells and a
  charger, and then you never buy batteries again. Standardise the whole house on
  **one cell size** so everything is interchangeable.
- **12 V LED strip** along a ceiling, run direct from the battery: 5 W lights a
  whole room and needs no inverter.
- **Solar garden lights** — bring them in at night. Crude but free and endless.
- **Candles and oil lamps:** useful backup, but they are a fire risk, consume
  oxygen and produce soot and CO. Keep them for ambience and last resort, never
  unattended, never near children. Paraffin/lamp oil stores indefinitely.
- **Light discipline:** blackout curtains. In a dark street, a lit window is a
  billboard. See Ch. 10.

---

## 9. Build sequence

### 🏢 Apartment
1. **Now (€150):** 2 × 20,000 mAh power banks · 100 W folding panel with USB/DC ·
   4 headlamps · 16 rechargeable AA + charger · wind-up/solar radio.
2. **L1 (€400–800):** A 500–1,000 Wh portable power station (LiFePO₄, pure sine,
   e.g. EcoFlow/Bluetti/Anker class) + 200 W of folding or balcony panels. This
   single purchase covers lights, phones, laptop, router and a CPAP — and it's
   plug-and-play, which matters when you cannot modify the building.
3. **L2 (€1,200–2,500):** 1.5–2 kWh station + 400 W balcony solar (check local
   rules — plug-in "balcony solar" up to 600–800 W is now legal in several
   European countries) + a 12 V compressor cool box (40 W) as an efficient fridge.
4. Never a generator in a flat. There is nowhere safe to run it.

### 🏡 Land / house
1. **Now (€200):** P0 kit as above, plus a plug-in energy meter and LED conversion.
2. **L1 (€900–1,800):** 400–600 W panels · 100 Ah/12 V LiFePO₄ (1.2 kWh) ·
   30 A MPPT · 1,000–1,500 W pure sine inverter · proper fusing and cable ·
   12 V LED lighting circuit.
3. **L2 (€4,000–8,000):** 2–3 kW panels on an adjustable mount · 5–10 kWh LiFePO₄
   at 24/48 V · 3 kW hybrid inverter-charger · transfer switch installed by an
   electrician · 2.2 kW dual-fuel inverter generator + 4 × 11 kg propane
   cylinders · A+++ chest freezer · **spare MPPT controller, spare fuses, spare
   cable, spare connectors**.
4. **L3 (€12,000+):** 5 kW+ array · 15 kWh storage · well pump on DC · micro-hydro
   or wind if the site supports it · full house backup circuits · second inverter
   held as a spare.

---

## 10. Electricity checklist

```
[ ] Energy meter bought; fridge/freezer actually measured
[ ] Loads sorted into Tier 1 / 2 / 3 and totals written down
[ ] All efficiency measures done BEFORE buying generation
[ ] Tier 1 (life-critical) covered by battery alone, with 2 days of autonomy
[ ] System sized on DECEMBER sun, not annual average
[ ] Pure sine inverter; surge rating checked against the biggest motor
[ ] Battery sited above 5 °C
[ ] Spare charge controller, fuses, cable and connectors in stock
[ ] DC fusing correct and a main isolator fitted within reach
[ ] Transfer switch/interlock installed if a generator feeds the house
[ ] CO alarms fitted; generator siting rule written and understood by everyone
[ ] Fuel stored legally and safely, dated, with stabiliser, rotation scheduled
[ ] System diagram drawn on paper and pinned up
[ ] Existing grid-tie solar checked for blackout (EPS) capability
[ ] Headlamps + rechargeables for every person, one battery size
[ ] Blackout weekend drill completed in WINTER
```

---

**🔨 Build it:** [Power builds](../builds/02-power-builds.md) — the complete 12 V solar system with cable sizing and fusing · DC lighting circuit · insulated battery box · adjustable tilt frame · generator noise screen

**Previous:** [01 — Water](01-water.md) · **Next:** [03 — Food storage](03-food-storage.md)
