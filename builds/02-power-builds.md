# 02 — Power Builds

*Read [Chapter 02](../docs/02-electricity.md) first — especially the load audit.
**Never size a system before you have measured your loads.** These builds assume
you have done that and know your Wh/day figure.*

**Contents:** [12 V solar system](#1-the-12-v-solar-system--complete-build) ·
[Cable sizing](#13-cable-sizing--the-table-that-prevents-fires) ·
[Fusing](#14-fusing--non-negotiable) ·
[DC lighting circuit](#2-12-v-dc-lighting-and-usb-circuit) ·
[Battery box](#3-insulated-battery-box) ·
[Panel tilt frame](#4-adjustable-panel-tilt-frame) ·
[Generator noise screen](#5-generator-noise-screen)

> ⚠️ **The line you must not cross.** Everything in this file is
> **extra-low-voltage DC, isolated from your house wiring.** That is legal,
> safe and DIY-able everywhere. **Anything that connects to your mains wiring —
> a transfer switch, an interlock, a hybrid inverter feeding house circuits —
> must be done by a qualified electrician.** Not because of bureaucracy: a
> backfed generator kills line workers, and a badly earthed inverter kills you.

---

# 1. The 12 V solar system — complete build

**1 day** · **€400–1,200 depending on size** · Skill ⬤⬤○

This is the **P1 "Essentials"** system from Chapter 02: lights, phones, laptop,
radio, and a fridge if you size it up. It is the system every household should
have, and it is genuinely a one-day job.

## 1.1 The wiring diagram

```
  ┌────────────┐
  │   PANELS   │  400–600 W, wired in SERIES for MPPT
  │ ▒▒▒▒ ▒▒▒▒  │  (higher voltage = thinner cable, better dull-day harvest)
  └─────╥──────┘
        ║  PV cable (4 or 6 mm², MC4 connectors)
   ┌────╨────┐
   │ PV DC   │ ← isolator switch: turn the array off before touching anything
   │ ISOLATOR│
   └────╥────┘
   ┌────╨─────────┐
   │ MPPT CHARGE  │  30–50 A. Buy a SPARE — this is the most likely failure.
   │  CONTROLLER  │
   └──╥────────╥──┘
      ║        ║
      ║   ┌────╨─────────────────────────────────┐
      ║   │  ⚡ MAIN FUSE — within 300 mm of the │
      ║   │     battery POSITIVE terminal        │
      ║   └────╥─────────────────────────────────┘
      ║   ┌────╨────┐
      ╚═══╡ BATTERY │  100–200 Ah LiFePO₄ (1.2–2.4 kWh)
          │  12 V   │  with an integrated BMS
          └────╥────┘
       ┌───────╨────────┐
       │  BATTERY       │ ← main isolator switch you can reach IN THE DARK
       │  ISOLATOR      │
       └───┬────────┬───┘
           │        │
    ┌──────┴──┐  ┌──┴──────────┐
    │ DC FUSE │  │ ⚡fuse      │
    │  BLOCK  │  │  INVERTER   │ 1000–1500 W pure sine
    └──┬───┬──┘  │  (switch it │ ⚠️ modified sine damages motors,
       │   │     │   OFF when  │    chargers and medical devices
       │   │     │   not used) │
       │   │     └──────╥──────┘
       │   │            ║
   lights USB      230 V AC sockets (STANDALONE — not wired to the house)
```

## 1.2 Parts list (a 600 W / 1.2 kWh example)

| Item | Spec | ~€ |
|---|---|---|
| Solar panels | 2 × 300 W mono, wired in series | 220 |
| Mounting rails / frame | see §4 | 80 |
| PV cable + MC4 connectors | 6 mm², 20 m + 4 pairs | 45 |
| **MPPT charge controller** | 30 A, 12/24 V auto | 110 |
| **Spare MPPT controller** | same | 110 |
| PV DC isolator | 600 V, 25 A | 20 |
| **LiFePO₄ battery** | 12 V 100 Ah with BMS | 320 |
| **Main fuse + holder** | 125 A Class T or MEGA | 25 |
| Battery isolator switch | 300 A marine type | 20 |
| Battery cable | 25 mm², lugs, heat shrink | 40 |
| DC fuse block | 6-way, blade fuses | 15 |
| Pure sine inverter | 1000 W, 12 V | 130 |
| Cable, crimps, glands, trunking, labels | — | 60 |
| Battery monitor (shunt-based) | optional but excellent | 60 |
| **Total** | | **~€1,255** |

*Halve this for a 300 W / 50 Ah starter system (~€500), or scale up to 24 V for
anything over 1.5 kW of load.*

## 1.3 Cable sizing — the table that prevents fires

**Undersized DC cable is the classic off-grid fire cause.** At 12 V the currents
are large and the voltage drop is brutal. Size for **both** voltage drop *and*
current-carrying capacity, and **use whichever is bigger.**

**Minimum cable size (mm²) for 12 V, 3% voltage drop, for the ONE-WAY run length:**

| Current | 1 m | 2 m | 3 m | 5 m | 8 m |
|---|---|---|---|---|---|
| 5 A | 1.5 | 1.5 | 1.5 | 2.5 | 4 |
| 10 A | 1.5 | 2.5 | 4 | 6 | 10 |
| 20 A | 2.5 | 4 | 6 | 10 | 16 |
| 30 A | 4 | 6 | 10 | 16 | 25 |
| 50 A | **10** | 10 | 16 | 25 | 50 |
| 100 A | **25** | 25 | 35 | 50 | 95 |

*(Values in bold are set by ampacity, not voltage drop.)*

**Rules:**
- **At 24 V you can use half the area** for the same power; at 48 V, a quarter.
  This is the main reason to go to a higher voltage as systems grow.
- **Keep the battery-to-inverter run as short as physically possible.** 
  Under 1.5 m, ideally under 1 m.
- Use **flexible fine-strand cable** (welding or marine cable), not solid house
  wire — it survives vibration and tight bends.
- **Crimp lugs properly** with a proper crimping tool, then heat-shrink. A bad
  crimp is a resistance heater. Do not twist-and-tape anything on the DC side.
- Colour code red positive / black negative and **label every cable at both ends.**

## 1.4 Fusing — non-negotiable

**A fuse protects the CABLE, not the device.** Its job is to blow before the wire
melts.

| Location | Fuse | Why |
|---|---|---|
| **Within 300 mm of the battery positive** | 100–150 A Class T or MEGA | ⚠️ **The most important fuse in the system.** A shorted battery cable delivers thousands of amps and will start a fire in seconds. Class T has the high interrupt rating lithium needs. |
| Inverter feed | Sized to the inverter | 1000 W ÷ (12 V × 0.85) ≈ 98 A → **125 A fuse, 25 mm² cable** |
| Each DC branch circuit | 5–20 A blade fuse | Lights, USB, pumps, fridge |
| PV array to controller | DC isolator + controller's own protection | Fit the isolator so you can safely work on the system |

**Sizing a fuse:** rate it at roughly **125% of the expected continuous current**,
and **never above the cable's ampacity**.

## 1.5 Build sequence

1. **Plan the layout on paper first.** Battery, controller and inverter close
   together; panels as far away as necessary. Draw it, label it, keep the drawing.
2. **Mount the panels** (§4). Wire them in **series** for an MPPT controller —
   higher voltage means thinner cable and better output in dull conditions.
   **Check the controller's maximum PV voltage** and remember open-circuit
   voltage *rises* in the cold: allow 25% headroom.
3. **Run the PV cable** into the building through a proper gland or a drip loop,
   with the DC isolator at the entry point.
4. **Mount the controller** on a non-combustible surface with 100 mm of clear air
   all round (they get hot).
5. **Connect in this order — it matters:**
   ```
   BATTERY first  →  then the CONTROLLER  →  then the PANELS  →  then the LOADS
   ```
   Most MPPT controllers need to see the battery voltage first to detect the
   system voltage. Connecting panels first can damage them.
6. **Fit the main fuse and the isolator** as you connect the battery, not
   afterwards.
7. **Set the controller** to the right battery chemistry — **LiFePO₄, not "lithium"
   generically, and definitely not the lead-acid default.** Wrong charge profile
   is the fastest way to kill a €320 battery.
8. **Wire the DC fuse block** off the isolator, and run the lighting and USB
   circuits from it (§2).
9. **Mount the inverter** on its own short heavy cable with its own fuse. Put it
   on a **switched** circuit — idle draw of 10–30 W is 240–700 Wh/day wasted on
   nothing.
10. **Label everything**, pin the diagram on the wall beside the equipment, and
    **write the operating notes** — how to check state of charge, what the alarms
    mean, what to do if it stops. Chapter 11's single-point-of-failure rule
    applies: someone else must be able to run this.
11. **Test under load.** Run the fridge off it for 48 hours and watch the numbers
    before you trust it.

## 1.6 Common mistakes

```
❌ Cable too thin                     → voltage drop, heat, fire
❌ No main battery fuse               → the one that burns houses down
❌ Modified sine inverter             → damages motors, chargers, medical devices
❌ Inverter left on 24/7              → 240–700 Wh/day of pure waste
❌ Battery in an unheated garage      → LiFePO₄ refuses to charge below 0 °C
❌ Controller set to the wrong chemistry → a dead battery in months
❌ Sized on annual average sun        → works in June, fails in December
❌ Shading "only a little"            → one shaded cell can halve a string
❌ No spare charge controller         → €60 part strands a €1,200 system
❌ Only one person understands it     → they get ill, the house goes dark
```

---

# 2. 12 V DC lighting and USB circuit

**2 h** · **€40** · Skill ⬤○○ · **Do this even on the smallest system**

Running lights and charging directly from the battery at 12 V **avoids the
inverter entirely** — which saves the 10–15% conversion loss *and*, far more
importantly, lets you switch the inverter off and stop its idle drain.

**Materials:** 12 V LED strip (warm white, 4.8–9 W/m) or 12 V LED bulbs with
fittings · 12 V USB charging sockets (dual, 3 A) · 12 V cigarette sockets for
accessories · switches · 1.5–2.5 mm² twin cable · blade fuses.

**Build**
1. Run a 2.5 mm² pair from the DC fuse block to each room.
2. **Lights:** LED strip along a ceiling cornice or under a shelf, on a switch.
   5 W lights a room adequately; 10 W lights it well.
3. **USB points:** one per room, plus two at the "charging station" where phones,
   headlamps, radios and battery packs live.
4. **Fuse each circuit** at the block (5 A for lights, 10 A for USB/accessories).
5. Keep polarity consistent everywhere — reversed polarity destroys most 12 V
   devices instantly.

**Energy reality:** a whole house on 12 V LED is **30–60 Wh per evening**. Your
phone is 15 Wh. **You can light and communicate for weeks on a 1 kWh battery.**
This is why the P0 tier removes the panic from a blackout for €200.

---

# 3. Insulated battery box

**2 h** · **€50** · Skill ⬤○○

LiFePO₄ **must not be charged below 0 °C** — the BMS will simply refuse, and you
will think the system is broken. In a Central European winter an outbuilding
regularly sits below freezing.

```
        ┌─────────────────────────────────────┐
        │ ░░░ 50 mm insulation, lid ░░░░░░░░░ │
        ├─────────────────────────────────────┤
        │ ░│                             │░   │
        │ ░│      BATTERY                │░   │  Cable exits through a
        │ ░│                             │░   │  sealed gland, LOW down
        │ ░│                             │░─────►
        │ ░└─────────────────────────────┘░   │
        │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
        └─────────────────────────────────────┘
          18 mm ply box · 50 mm PIR/foam lining · battery strapped down
```

**Build:** an 18 mm ply box, 50 mm larger than the battery all round, lined with
50 mm PIR foam board (taped joints), with a lifting lid. Strap the battery down
so it cannot move. Take the cable out through a **cable gland at low level** and
seal it.

**Details:**
- **LiFePO₄:** seal it up. The battery's own charge/discharge losses keep it
  a few degrees above ambient inside an insulated box. Add a **thermostatically
  controlled 10–20 W heat pad** for a cold shed (that is 240–480 Wh/day — budget
  for it, or just keep the battery indoors, which is free).
- ⚠️ **Lead-acid: NEVER seal it.** Flooded and AGM batteries vent hydrogen, which
  is explosive. Vent the box to the outside at the top, and keep all sparks and
  switches outside the box.
- Put a thermometer inside and check it on the coldest nights.
- **Best answer of all: put the battery inside the heated envelope of the house.**
  LiFePO₄ is safe indoors and it needs no ventilation. This costs nothing.

---

# 4. Adjustable panel tilt frame

**4 h** · **€80** · Skill ⬤⬤○ · **Gains 20–30% in December**

At 46 °N, panels at a fixed 35° lose a lot in winter. A frame you can re-tilt
twice a year to **latitude + 15° in winter** (≈ 60°) and **latitude − 10° in
summer** (≈ 35°) gains 20–30% in the months that matter — and a steep winter
angle **sheds snow**, which is worth more than the angle itself.

```
    SUMMER ~35°                  WINTER ~60°
         ╱▒▒▒▒▒▒▒                    ╱▒
       ╱▒▒▒▒▒▒▒▒                   ╱▒▒
     ╱▒▒▒▒▒▒▒▒                   ╱▒▒▒
   ╱─────○────                 ╱──○         ○ = pivot bolt (M10) at the
  ╱  strut in   ╲             ╱ strut in        bottom rail
 ╱   hole A      ╲           ╱  hole B
═╧════════════════╧═════════╧═══════════   base frame, weighted or anchored
```

**Materials:** 45 × 95 treated timber or 40 × 40 steel angle · M10 bolts and
washers · panel clamps or 45 × 45 rails · ground anchors, or concrete blocks as
ballast.

**Build:** a rectangular base frame sized to the panels · a hinged panel frame
bolted to the base at the front edge with M10 pivot bolts · a rear strut with
**two or three drilled holes** for the seasonal angles.

**Critical details:**
- ⚠️ **Wind load is the killer.** A 2 m² panel at 60° in an 80 km/h gust carries a
  load of several hundred kilos. **Anchor the frame to the ground or ballast it
  with 80–150 kg of concrete blocks.** Panels that fly are lethal and they take
  the roof with them.
- Keep the bottom edge **at least 300 mm above ground/snow level** or winter drifts
  bury the array exactly when you need it.
- Leave **100 mm of air behind the panels** — they lose about 0.4%/°C of output as
  they heat, so ventilation matters in summer.
- Survey the **winter** sun path before siting. The sun is very low from November
  to February; trees and buildings that cast no shadow in June will shade you
  completely in December.
- Ground mounting beats roof mounting for anyone who can: you can clean it, clear
  snow, re-tilt it, and repair it without a ladder.

---

# 5. Generator noise screen

**4 h** · **€100** · Skill ⬤⬤○

A generator is audible for hundreds of metres and announces that your house has
fuel and things worth powering ([Chapter 10](../docs/10-security-community-communications.md)).
You can cut that substantially — **but not by putting it in a box.**

> ⚠️⚠️ **NEVER enclose a running generator.** Enclosure causes overheating,
> engine fire, and — above all — **carbon monoxide accumulation that kills.**
> Generators need enormous airflow for cooling and combustion. Every year people
> die building "generator sheds". **Do not build one.**

**What actually works, safely:**

1. **Distance and position first.** Every doubling of distance cuts perceived
   noise. Site it **≥ 5 m from any door, window or vent**, downwind, with the
   exhaust pointed away from the house and away from neighbours.
2. **A three-sided screen, open at the top and open at the exhaust end.**
   A mass barrier between the generator and the listener: 18 mm ply or two
   layers of board, with a dense core (mineral wool, or a rubber/mass-loaded
   vinyl layer). **Mass blocks sound; foam does not.**
   - Three panels, 1.2 m high, forming a U around the sides and back
   - **Completely open above and at the front** for airflow
   - **At least 1 m of clear space** on all open sides
3. **Line the inside faces** of the screen with 50 mm mineral wool behind a
   perforated board — this absorbs the reflections rather than bouncing them.
4. **Put it on a rubber mat or paving slabs on sand**, not on a hollow wooden
   deck (which acts as a soundboard) and not on bare resonant ground.
5. **Exhaust extension:** a flexible steel exhaust pipe routed away from the house
   and screened separately makes a big difference — most of the noise is exhaust.
   ⚠️ Keep it clear of anything combustible; it glows.
6. **The bigger win is operational:** run it **in batch-charging mode** (Chapter 02
   §5) — 1–2 hours in daylight, at 60–80% load, while other noise exists, instead
   of all day. That cuts noise exposure, fuel and engine wear together.

**CO rules, every time, no exceptions:**
```
⚠️ Outdoors only. Never in a garage, shed, porch, cellar or under an overhang.
⚠️ ≥ 5 m from any opening, exhaust pointing away.
⚠️ CO alarms in every sleeping room and on the nearest wall.
⚠️ Never refuel a hot engine.
⚠️ Never backfeed into a socket — use a transfer switch fitted by an electrician.
```

---

**Related:** [Chapter 02 — Electricity](../docs/02-electricity.md) ·
[Apartment builds](08-apartment-builds.md) · [Build index](README.md)
