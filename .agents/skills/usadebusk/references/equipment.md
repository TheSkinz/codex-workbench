
# USADeBusk — Equipment Library

## TriMax Pumper Unit
USADeBusk's proprietary trailer-mounted pigging pumper. High-volume / low-pressure system — pigs are propelled by flow, not pressure alone. Not a jetting unit.

**Unit architecture — TRIPLE:** One TriMax trailer contains 3 independent pumping assemblies. Each assembly has its own engine, gearbox, pump, and valve manifold. All three share ONE clean tank (3,000 gal) and ONE dirty tank (2,000 gal). Three operator stations in the control cab — one per assembly. Each assembly cleans one circuit independently: direction, flow state, and progress are set per assembly. Scope determines how many of the 3 assemblies are used; unused assemblies sit idle. The three pumping assemblies, left → right: **left (pump 1), center (pump 2), right (pump 3)**. Referenced as left/center/right side when identifying which assembly/circuit is in use.

**Physical layout (left → right):**
Control cab (3 operator stations) | Dirty tank (2,000 gal, shared) | Clean tank (3,000 gal, shared) | 3× pump/engine assemblies

**Internal routing:**
- Feed-side order (each assembly): clean tank → suction strainer → pump → flow meter → valve manifold → Fig. 200 port
- Return water enters via Fig. 200 RAD port at trailer rear
- Fixed pipe routes along trailer ceiling toward clean tank
- Diverter (90° plunger, operator-controlled from cab) at junction above tanks
  - Default: clean tank
  - Thrown (cloudy effluent): dirty tank
- Pump inlet: right side of clean tank
- Pump discharge: right side of pump → Fig. 200 CONV port → launcher

**Rear connections:**
- Two Fig. 200 (3") ports side by side at trailer rear — CONV and RAD
- Both serve as feed or return depending on pig travel direction
- Valve manifold controls direction from cab — no hose swapping required
- For standard conv-to-rad direction: feed exits CONV port, return enters RAD port
- For reversed direction: feed exits RAD port, return enters CONV port

**Operating pressure:** 100–400 PSI typical; 600 PSI absolute system limit. Over-pressure checklist required above 500 PSI.

**Circuit diagrams:** Flow topology, port/color identity, capacity scaling, diverter states, and feed-assembly flow states are diagrammed in `references/equipment-circuit-diagrams.md` — Master Flow Circuit (D1), Port/Direction/Color Map (D3), Circuit Capacity & Scaling (D5), Diverter State Machine (D6), and Generic Feed Assembly + 3 Flow States (D8). Consult it when reasoning about how the pumper moves water through a circuit.

---

## Filter Press
- 73 polypropylene plates
- Surface area: 1,243.4 ft²
- Operating pressure: 100 PSI
- Capacity: 400 GPM
- Non-gasketed filter cloths
- Trailer-mounted; significantly larger than 4×3 pump

---

## 4×3 Centrifugal Pump (Trash Pump)
- Standalone trailer-mounted
- 3" camlock inlet and outlet
- Drives dirty water from dirty tank through filter press
- Runs concurrently with pigging — does not affect coil pressure

---

## Pig Launchers / Receivers
- Installed at convection inlet flanges (launchers) and radiant outlet flanges (receivers)
- Same form factor — labeled by function
- Fig. 200 jetting hose connects TriMax rear port to launcher/receiver

**Inventory (standardized across all furnace pigging companies):**
- 10+ launchers of each size, 3" through 12"
- 3", 4", 6", 8": **300# connections** on barrel and valve
- 10", 12": **150# connections** on barrel and valve

**Adapter note:** When heater flange size or rating differs from launcher, customer fabricates required adapters.

---

## Pig Types
| Type | Body | Use Case |
|---|---|---|
| Foam | Soft foam, no abrasive elements | Opening passes, initial flow establishment, verification |
| TC (Tungsten Carbide Pin) | Urethane 84A Duro (78A special), TC pins cast in during molding | Primary coke removal — main workhorse |
| HR (High-Recovery) | Higher durometer, aggressive | Heavy fouling, pitch-laden tubes |
| Swab | Oversized soft urethane | Final cleanup, verification, larger tubes |

**TC pig mechanics:**
- Pins embedded in urethane body via molding (cast + chemical hardener + heat cure)
- When pig OD ≤ tube ID: pins extend, dig into coke
- When pig OD > tube ID (oversized): body compresses, pins lay back — cuts coke, deflects off harder tube wall without damage (differential hardness)

**Pig progression strategy:**
- Start: foams or undersized TCs to open path
- Increment: 1/8" per successful pass
- Line-size pig (= tube ID): removes bulk of coke
- Oversized final pig: tube ID + up to 0.250" maximum
  - 5.000" ID → 5.250" max pig
  - 6.065" ID → 6.250" standard final; 6.500" max (heavy fouling or looped circuits)
- Swabs: final verification or large tube sections

---

## Hoses & Connections
| Component | Type | Size | Notes |
|---|---|---|---|
| TriMax to launcher/receiver | Fig. 200 jetting hose | 3" | Rear TriMax ports to coil endpoints |
| Filtration circuit (all legs) | Camlock | 3" | Dirty tank → pump → filter press → clean tank |
| Dirty tank vac access | Camlock | 3" | T-branch for vac truck |

---

## Support Equipment
| Equipment | Notes |
|---|---|
| Crew Truck | Crew transport, tools, supplies |
| Support Unit | Additional equipment/supply trailer |
| DEF (Diesel Exhaust Fluid) | Equipment compliance; billed per shift |
| Vac Truck | Third-party; dirty tank residual disposal |
| Light Plant | Third-party; night ops lighting |
| Air Compressor | Third-party; pig loading or pneumatic tools |

---

## Second TriMax (2× TriMax Configuration)
- Terminology: "second TriMax" or "2× TriMax" — never "dual-pumper" (customers misread as 2-circuit-max). Use "Triple" for the unit itself.
- Each TriMax = own tanks (3,000 gal clean / 2,000 gal dirty) + own 3 pump/engine assemblies → 2× TriMax = up to 6 simultaneous circuits
- Filtration scales conditionally: 2× filter presses + 2× 4×3 pumps when customer requires it AND a 2nd press is available; otherwise 1× shared filter press + 1× shared 4×3 pump serving both TriMax units
- When shared: T-connections with valve manifolds on both sides link both dirty-tank outlets to shared pump suction; clean filtrate returns to respective clean tanks
- Each assembly runs its own circuit fully independently — direction, flow state, and progress are set per assembly. No cross-assembly direction constraint.

---

## Double Pumper

Same custom design as the TriMax on a single 48' trailer, with **two** of each major component (engine, gearbox, pump, valve manifold) instead of three. Two independent pump assemblies: **left = pump 1, right = pump 2. No center.** Cleans two circuits simultaneously. Documented by reference to the TriMax above — not a separate from-scratch spec.

**Distinguishing invariant:** assembly count (two vs. three) and the presence/absence of a center assembly. This separates the double pumper from both the TriMax (three assemblies, L/C/R = 1/2/3, one trailer) and the Second TriMax (two trailers, six assemblies total).

**Notation — two separate axes, do not conflate:**
- **L/C/R** = which pump assembly (physical trailer position). The double pumper has L and R only; no C.
- **Red/Blue** = the two ports on a given pump side, routing to the launchers at either end of that side's circuit. Blue port → blue launcher → convection + radiant closed-loop circuit → red launcher → red port → open-top clean tank → recycled; reversible via directional valves.

**Guardrail A — don't overwrite:** When a job states it uses the double pumper, do NOT substitute the TriMax. "Double pumper" is accepted terminology for this specific unit — leave it as written.

**Guardrail B — don't invent (the higher-volume risk):** NEVER infer the double pumper from heater data. Pass count, circuit count, and two-pass geometry do NOT imply a double pumper. The TriMax is the default mobilized unit for essentially all jobs INCLUDING two-pass heaters — one pump side simply goes unused. The double pumper is used only when explicitly stated for that specific job, and is so rare neither division documents it elsewhere. It is never a card field (see the Heater Card Schema in `usadebusk-core`).

**Terminology:** "double pumper" (this two-assembly unit) is accepted. "dual-pumper" remains **banned** — it mischaracterizes the three-assembly TriMax as two-assembly and customers misread it as 2-circuit-max. Adding the double pumper fills a real registry slot; it does not lift the dual-pumper ban. The three terms are distinct: **TriMax/Triple** (3 assemblies, 1 trailer) · **double pumper** (2 assemblies, 1 trailer) · **Second TriMax / 2× TriMax** (2 trailers, 6 assemblies).
