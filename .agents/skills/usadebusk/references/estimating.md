
# USADeBusk — Estimating & Proposals

> **Canonical authority:** estimating is the single source of truth for USADeBusk proposal content, section composition, and bid-intake logic across all Codex USADeBusk workflows. On conflict over proposal content/composition/intake, this reference governs. Page layout and visual formatting defer to USADeBusk brand standards in `core.md`; behavior defers to active Codex instructions.

## Primary Estimating Drivers
1. **Pass / circuit count** → equipment qty, launcher/receiver sets, job duration
2. **Tube ID** → pig sizing, launcher size, adapter requirements
3. **Total footage per pass** → primary pigging duration driver
4. **Expected fouling type** → standard coke vs. hard coke/pitch (coker/crude)
5. **Equipment profile** → 1×, 2×, or 3× TriMax (sets asset count and crew size)
6. **Travel distance** → mob/demob mileage
7. **Crew size** → labor and per diem

*Metallurgy does not significantly change the **cost estimate** (customer handles
soda ash). This does not apply to SOP, safety, or chemistry compatibility —
confirm metallurgy separately for those purposes.*

---

## Duration Model
- All projects built on **12-hour shift cycles**
- Operations run **24/7** — Day and Night shift handovers
- **Total duration = Rig-In + Pigging Hours + Rig-Out ± Rig-Over + Stand-By**
- Mob/Demob: 12-hour simultaneous Day and Night events (fixed). Costing is computed separately — see **Mob/Demob Costing** below.

**Pigging duration benchmark:** ~100 ft/hour per pass (nominal fouling)
- 3,000 ft coil = ~30 pigging hours
- **Reduce the ft/hour rate (more hours required) for:** harder fouling (coker/crude), pitch presence, tube restrictions, plug-header / mule-ear return bends (harder pig traversal — read `Return bend type` from the heater card), first-time clean with no prior data
- Adjust using: prior cleaning data for same heater, job walk observations, loop configuration

**Rig-In / Rig-Out:** Fixed events. Duration varies by pass count and access complexity. Proposal-generation defaults: Rig-In 6 hrs, Rig-Out 6 hrs, Smart Pig 4 hrs (when applicable) — adjust per pass count and access.

**SIMOPS:** Multi-heater jobs require overlapping heater timeline visibility — resource stacking and scheduling commitments visible across all heater cards simultaneously.

---

### Mob/Demob Costing

Basis: Deer Park, TX shop → facility, one-way miles per trip. Mob and Demob are
calculated separately; Demob mirrors Mob as the return trip. Presented as two
lump-sum line items (Mob separate from Demob).

1. Equipment travel — one-way miles × $3.00/mile × number of equipment pieces
   traveling. The $3.00/mile includes driver labor (drivers carry no separate
   travel-labor line). $3.00/mile is the default; confirm per job. One driver per
   piece (drivers = pieces traveling).

2. Driver per diem — drivers × drive-days × contract per-diem rate. Drive-days =
   total one-way drive time ÷ ~10 hrs/day, rounded up; any drive over 1 hour
   accrues at least one per diem, and per diem accrues per driver per drive-day
   (e.g., 2 drivers × 2-day haul = 4 per diems). Per-diem rate is the contract
   per-diem line (currently $150/day); confirm per contract.

3. Non-driver crew travel — (total crew − drivers) × hourly labor rate × actual
   travel hours (drive or air; typically 8, occasionally as low as 1). Each
   non-driver also receives exactly one day of per diem (contract rate). Non-driver
   travel never exceeds one day.

4. Travel ancillaries — rental cars, flights, and other travel rentals at the
   quoted day/unit rate + contract third-party markup.

Costing (above) is distinct from duration/scheduling. The Duration Model's
mob/demob entry governs how mob/demob occupies the schedule; it does not set price.

---

## Pricing Structure
| Category | Type | Line Items |
|---|---|---|
| Equipment | Hourly task-based | TriMax Pumper (Rig-In / Pig / Smart Pig / Stand-By rates) |
| Support equipment | Hourly fixed | 4×3 Pump, Filter Press (pumping / non-pumping), Support Units, Crew Trucks |
| Labor | 12-hr Day Rate | PM, Supervisor (Day/Night), Operator (Day/Night) |
| Per Diem | Daily per person | 1 PD per 12-hr shift |
| Materials | Unit rate | Pigs (by size/type), DEF (per shift) |
| Third Party | Cost + markup | Vac truck, light plant, compressor, rental, flights |
| Mob/Demob | Lump sum (95%) | Equipment miles + crew travel labor + driver per diem |

**Filter Press billing:** Two rates
- Pumping rate: TriMax actively pigging
- Non-pumping/stand-by rate: rig-in, rig-out, stand-by

**Stand-by applies to two rate lines only — TriMax Pumper and Filter Press.**
Triggered when the project is not actively moving forward (rig-in, rig-out,
waiting) and USADeBusk cannot rig-in, pig, or smart-pig. All other resources
(Support equipment, Labor, Per Diem, Materials, Mob/Demob) bill unchanged
regardless of stand-by status.

**Third-party markup:** 10% baseline; contract-dependent. Confirm applicable contract markup before finalizing any proposal or invoice; some facilities contract as low as 5%.

---

## Baseline Rate Table
*Generic rates for new facilities without contract rates. Replace with contract rates before finalizing.*

| Category | Description | Rate | Unit |
|---|---|---|---|
| Third Party | Cost + markup | 5–10% | Mark-up (10% baseline) |
| Mob/Equipment | TriMax Travel | $3.00 | Mile |
| Mob/Equipment | Support Travel | $3.00 | Mile |
| Mob/Equipment | Crew Truck Travel | $3.00 | Mile |
| Mob/Labor | Driver Travel | $58.00 | Hour |
| Per Diem | Per Diem | $150.00 | Day |
| Equipment | Pumper: Rigging | $500.00 | Hour |
| Equipment | Pumper: Pig | $500.00 | Hour |
| Equipment | Pumper: Smart Pig | $500.00 | Hour |
| Equipment | Pumper: Stand-by | $500.00 | Hour |
| Equipment | Support Unit | $30.00 | Hour |
| Equipment | Filtration | $200.00 | Hour |
| Equipment | Filter Stand-by | $150.00 | Hour |
| Equipment | Crew Truck | $15.00 | Hour |
| Equipment | 4×3 Trash Pump | $50.00 | Hour |
| Labor | Project Manager | $80.00 | Hour |
| Labor | Supervisor | $74.00 | Hour |
| Labor | Operator | $64.00 | Hour |
| Materials | DEF | $125.00 | Shift |
| Materials | 4" Pigs | $59.00 | Each |
| Materials | 4.25" Pigs | $64.90 | Each |
| Materials | 5" Pigs | $89.70 | Each |
| Materials | 5.25" Pigs | $94.40 | Each |
| Materials | 6" Pigs | $118.00 | Each |
| Materials | 6.25" Pigs | $129.80 | Each |
| Materials | 6.5" Pigs | $142.80 | Each |
| Materials | 8" Pigs | $230.10 | Each |
| Materials | 8.25" Pigs | $247.80 | Each |
| Materials | 10" Pigs | $483.80 | Each |
| Materials | 10.25" Pigs | $531.00 | Each |

---

## Cost Categories (Proposal Structure)
**Mobilization | Demobilization | Equipment | Labor | Materials | Per Diem**

## Heater Card Format
**Rig-In → Pig → [Rig-Over] → [additional Pig passes] → [Smart Pig] → [Stand-By] → Rig-Out**
*Rig-Over occurs between passes or heaters mid-job, not before pigging begins.*

---

## RFQ Intake — Required Inputs
Before building any proposal, confirm:
1. Facility name and customer
2. Heater tag and service name
3. Scope type (Planned / Emergency / Turnaround)
4. Pass/circuit count and coil pairing
5. Tube ID — convection and radiant (OD and schedule if available)
6. Total footage per pass
7. Inlet/outlet flange size and rating (e.g., 4" 300#, 6" 150#)
8. Tube arrangement (horizontal / vertical / helical)
9. Tube metallurgy (carbon steel or stainless)
10. Expected fouling type (standard coke, hard coke, pitch/resid)
11. Water source (BFW / fresh condensate / demineralized / firewater)
12. Launcher access and elevation constraints
13. Jumper spool requirements
14. Execution dates (or estimated window)
15. Equipment profile (1× / 2× / 3× TriMax)
16. Applicable contract rates
17. Applicable customer standards

**Drawing or data-sheet input:** extract all heater variables and populate the Section 5 Technical Data table before proceeding to the Execution Plan or Quotation.

**Incomplete-input gate:** if inputs are incomplete, list exactly what is missing and ask for it. Do not estimate or assume missing technical data.

---

## Proposal Document Structure
Every USADeBusk proposal follows a 12–16 page structure. Reproduce this section order exactly unless specified otherwise:
1. Cover Page
2. Table of Contents
3. Requested Service
4. Execution Plan
5. Technical Data
6. Verification of Pass Cleanliness
7. Quotation
8. Requested / Provided Items
9. Hourly Charge Out Rates
10. Time and Material Rate Charges
11. Terms & Conditions
12. USA DeBusk TriMax Pumper (boilerplate)
13. Additional Services (boilerplate)
14. Sample USA DeBusk Customer Profile (boilerplate)

---

## Section Templates

### Section 3 — Requested Service
- Opening paragraph: "USA DeBusk submits this proposal for mechanical decoking services at [Facility Name] during [Event/Month Year]."
- **Scope of Work** bullet list: job type (Emergency / Planned), heater tag(s), equipment mobilized
- **Commercial Terms** bullet list: Basis (T&M), Mob/Demob (Lump Sum), Duration Estimate basis
- Closing statement: "USA DeBusk will deliver a safe, flexible, and cost-effective solution in close collaboration with [Customer] to ensure [turnaround/project] success."
- TriMax Pumper photo placeholder

### Section 4 — Execution Plan
- Gantt table per heater (one table per heater card), columns: Start | End | Hours | Tasks
- Standard task rows: Rig-in hoses and launchers (6 hrs default) | Pig all [N] coils | Smart Pig (if applicable, 4 hrs) | Rig-out equipment (6 hrs default)
- Sub-total row per heater (bold); Total Hours row (bold)
- Equipment and Manpower Allocation table (two columns: Equipment left, Manpower right)
- Total Duration block (Project Hours / Days / Shifts / Project Manager name)
- Standard disclaimer: "The projected times and durations are estimated based on our extensive experience and the coil data provided. However, please be aware that the actual project duration may vary due to factors such as deposit hardness, location, composition, and thickness."

### Section 5 — Technical Data
Read heater facts from the heater card; field meanings defer to the Heater Card Schema in `usadebusk-core`. This table carries **facts only** — filtration and smart pigging are customer decisions, read from the card's Job Options (status), never reproduced as a spec row here.

One technical summary table per heater, titled `Furnace: [Heater Tag & Name]`:

| Item | Convection Section | Radiant Section |
|---|---|---|
| No. of Coils | [qty] ([tubes/pass] tubes/pass) | [qty] ([tubes/pass] tubes/pass) |
| Total Tube Footage | [ft/pass] ([total] ft total) | [ft/pass] ([total] ft total) |
| Avg. Tube + Bend Length | [length] ([finned/bare]) | [length] ([finned/bare]) |
| Tube Count | [N] total | [N] total |
| Tube I.D. | [inches]" | [inches]" |
| Material | [spec] | [spec] |
| Tube Arrangement | [Horizontal/Vertical] | [Horizontal/Vertical] |
| Inlet / Outlet | [size] [rating]# flanges | [size] [rating]# flanges |
| Launcher Elevation | [description] | [description] |
| Return Bends | [type] | [type] |
| Special Notes | access constraints, spool requirements, pig sizing logic, configuration type (combined field) ||

- Include P&ID snapshot or field photo when provided
- Annotate diagrams where applicable (e.g., "Remove Spools And Install 180's", "Install Pigging Spools")

### Section 6 — Verification of Pass Cleanliness
Boilerplate — use the standard USADeBusk 4-point verification protocol text (sensor data / effluent monitoring / pig condition tracking / final foam run with client sign-off). Reproduce verbatim unless customization is requested.

### Section 7 — Quotation
- Header block: Company address | Date | Quotation # (DSP#) | Billing Method | Valid date (90 days default) | Prepared by [name per job — confirm]
- Bill To block: customer facility name and address
- Special Instructions line: contract terms summary (e.g., "T&M | Mob & Demob are lump sum. Payment terms are 30 days")
- Line items table (Description | Line Total):
  - Mobilize [equipment list] (lump sum)
  - Mechanical Decoke: [Heater Tag] — hour breakdown: [N] Rig-in | [N] Pig | [N] Smart Pig (if applicable) | [N] Rig-out
  - Labor & Per Diem
  - Materials: DEF & Decoking Pigs
  - Demobilize [equipment list] (lump sum)
- Footer notes: "Quote includes all launchers, receivers, and PPE" | contact info | third-party markup rate per contract | standby note
- Pricing Summary box (right-aligned): Equipment | Manpower | Materials | **Total**
- **Critical:** Never apply a default third-party markup rate. Always confirm the applicable rate from the facility's contract before populating the markup field.

### Section 8 — Requested / Provided Items
Standard bilateral list. Adjust customer-provided items per job specifics (compressor size, spool requirements, etc.). USADeBusk-provided items list is largely standard — adjust for non-standard equipment.

### Section 9 — Hourly Charge Out Rates
Populate from the applicable facility contract. **Never use default rates from a prior job. Confirm before populating.** Standard rate line items: TriMax (Rigging / Pigging / Smart Pig / Stand-by) · Support Unit · Filtration / Filter Stand-by · Crew Truck · additional equipment (e.g., 4×3 Trash Pump) if mobilized · Supervisor / Operator · Per Diem (daily) · DEF (per shift) · Mark-up % (contract-specific).

### Sections 10–14
Boilerplate. Reproduce standard USADeBusk text. Do not modify unless changes are requested.

---

## Proposal Generation Guardrails
- Flag immediately if provided data is internally inconsistent (e.g., footage that doesn't match tube count × tube length).
- Show duration math explicitly before finalizing the Execution Plan so it can be verified.
- Show line-item hour × rate calculations in a working note before producing the final Quotation table.
- Never assume tube footage, pass count, or equipment profile — derive from provided data.
- "Use the same rates as [prior DSP#]" → confirm which DSP# is referenced and verify those rates against the current contract before use.

*(Prior-rate and third-party-markup cautions live in Sections 7 and 9 above — not restated here.)*

## Estimation Workup Tool
Excel workup template is a work in progress. Explain estimating logic from this skill when asked — do not attempt to replicate the workup structure until the template is documented here.

## DSP# Assignment
Assign at proposal start. Format: YYNNN (e.g., DSP26015).

## Submission Platforms
ARIBA, GED, or direct email per customer requirement.

## Customer Types
- **ExxonMobil / major operators:** High documentation requirements, pre-execution packages, engineering review, NACE/customer spec references
- **Mid-tier refineries:** Standard format, less overhead
- **Smaller/independent:** Often relationship-driven, simpler scope
