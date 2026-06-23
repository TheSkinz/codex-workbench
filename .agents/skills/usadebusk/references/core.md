
# USADeBusk — Core Context

## Company Identity
- **Name:** USADeBusk (also: USA DeBusk, DeBusk Services Group on some accounts)
- **Primary service:** Furnace Decoking > Furnace Pigging/Decoking > Furnace Pigging (preferred order)
- **Base:** Deer Park, TX
- **Markets:** Refineries and chemical/petrochemical plants
- **Key roles:** Jesse (technical sales, PM, proposals, estimation); Jason VP (named on some customer-facing docs)
- **Contract type:** T&M on most jobs. Mob/Demob lump sum on ~95%.
- **Third-party markup:** 10% baseline; contract-dependent.

## Brand Standards
*Canonical authority for all USADeBusk brand, font, type-scale, and color specs. Other surfaces defer here.*

| Element | Spec |
|---|---|
| Font | Helvetica (Arial acceptable as fallback for DOCX generation) |
| H1 | 13pt bold `#222222`, gold `#FCC30A` bottom border |
| H2 | 11pt bold `#FCC30A` |
| Body | 10pt `#555555` |
| Footer/header | 8.5pt `#888888` |
| Table header | `#222222` fill |
| Alt row BG | `#F7F7F7` |
| Callout BG | `#FFFBE6` with `#FCC30A` accent |

## Document Numbering
- **DSP#** — Quote number. Format: YYNNN (e.g., DSP26001). Assigned at proposal stage.
- **USA#** — Job number. Format: USAYYNNN (e.g., USA26001). Assigned on award.

---

## What Furnace Decoking Is
Fired heater tubes accumulate petroleum coke (carbon-rich thermal cracking byproduct) on tube walls over time. Buildup reduces heat transfer, raises tube skin temps, increases pressure drop, and causes tube failure or unplanned shutdowns if untreated. Furnace pigging is mechanical removal of coke by propelling progressively sized pigs through the coil using water pressure.

## Core Terminology
| Term | Definition |
|---|---|
| Fired Heater / Furnace | Process vessel containing the tube coil. Interchangeable. |
| Coil | Complete tube assembly — multiple tubes connected by U-bends/return bends |
| Pass / Circuit | One continuous tube circuit. A heater may have multiple passes. |
| Tube | Individual straight pipe section within a coil |
| U-bend / Return bend | 180° fitting connecting adjacent tubes |
| Convection section | Upper section — indirect flue gas heat. Lower skin temps. Smaller or equal tube ID vs. radiant. |
| Radiant section | Lower/inner section — direct flame radiation. Highest heat flux. Hardest fouling. |
| Cross-over | External piping connecting convection outlet to radiant inlet. Contains size reducer when tube IDs differ. |
| Pig | Mechanical cleaning device propelled by water pressure |
| Rig-in | Setup of all surface equipment before pigging |
| Rig-out | Removal of all surface equipment after cleaning |
| Rig-over | Moving equipment between passes or heaters mid-job |
| Stand-by | On-site time, not actively pigging. May be billable. |
| PDT (Plant Down Time) | Facility-caused downtime — generally billable as stand-by |
| Smart pig / ILI | Intelligent inspection pig — UT transducers measure tube wall thickness post-cleaning |
| Flow test | Before/after RPM vs PSI vs GPM pump curve — verifies cleaning effectiveness |
| Effluent | Return water from receiver — clarity indicates fouling removal progress |
| Jumper spool | Temporary 180° spool connecting two radiant outlet flanges to loop two passes |
| SIMOPS | Simultaneous operations on multi-heater jobs — resource overlap must be managed |
| Pitch | Heavy viscous fouling — harder to remove; common in coker/crude units |
| Kicksolve | Chemical additive for mobilizing hardened residual product/pitch |
| Ticket Breakdown | Per-job Excel file: all billable resources, durations, rates |
| Service Receipt | Handwritten daily field doc completed by PM per 12-hour shift |
| TriMax (Triple) / second TriMax / double pumper | Naming lock. The standard pumper unit is a "Triple" (3 independent assemblies); a 2× deployment is a "second TriMax." The "double pumper" is a distinct, rare unit — single trailer, 2 assemblies, no center. Never "dual-pumper." Dead string: 'dual-pumper' / 'dual pumper' / 'Dual pumper' — flag and correct on sight. Equipment specs live in usadebusk-equipment. |

⚠️ TERMINOLOGY FLAG: "Triple" and "second TriMax" are canonical. "Double pumper" is accepted ONLY for the specific 2-assembly single-trailer unit (see usadebusk-equipment) — never as a synonym for the TriMax. Never write "dual-pumper" in any document, internal or customer-facing — customers misread it as a pumper limited to two circuits. The near-homophone collision is deliberate to guard against: double pumper (real, rare) ≠ dual-pumper (banned). Flag and correct on sight.

---

## Fired Heater & Tube Knowledge

### Heater Types
- **Cabin / Box** — rectangular; burners floor/sides; common in crude/VDU
- **Vertical Cylindrical (VC)** — cylindrical shell; burners floor; circular coil pattern
- **Arbor / Wicket** — coil hangs in loops; less common

### Coil Sections
**Convection:** Upper. Horizontal rows. Flue gas convection only. Lower skin temps. Tube ID same size or smaller than radiant — true on 99%+ of heaters. ⚠️ FLAG: If convection ID is larger than radiant ID, stop and confirm with Jesse before proceeding.

**Radiant:** Lower/inner. Direct flame radiation. Highest heat flux. Hardest fouling at radiant outlet. Radiant outlet is most fouling-prone location.

**Cross-over:** External. Convection outlet → radiant inlet. Reducer lives here when tube IDs differ. ⚠️ Known obstruction point when transitioning pig sizes (e.g., 5" conv → 6" rad).

### Tube Geometry
- **Serpentine (standard conv):** Horizontal parallel rows, U-bends alternate ends. Pig reverses direction each tube.
- **Helical (radiant, VC heaters):** Coil wraps around circumference.
- **Return bend:** Cast 180° fitting. Common.
- **Plug header:** Box header with removable plugs at tube ends. Older design.

When reasoning about coil topology — serpentine reversal, conv → crossover → rad order, or where an ID transition can occur — see `references/core-coil-template.md` (Diagram 2). It is a template: tube count is per-job and ID transitions can occur mid-pass between any tubes, not only at the crossover.

### Common Tube Dimensions
| Size | OD | ID |
|---|---|---|
| 4" Sch 40 | 4.500" | 4.026" |
| 5" | — | ~5.047" |
| 6" Sch 40 | 6.625" | 6.065" |

### Metallurgy
- **Carbon steel:** Standard — no modification
- **Stainless steel:** Requires soda ash passivation after mechanical cleaning — passivation and soda ash mixing are customer-performed. Customer typically provides the soda ash. pH target ≥ 10.0 throughout circulation; final flush to neutral. Firewater is avoided by default due to chloride content, but may be permitted if the facility has tested its hydrant supply and confirmed acceptable chloride levels.

### Key Job Variables
Pass/circuit count · Tube ID (conv and rad) · Flange size & rating · Total footage per pass · Tube arrangement (H vs V) · Fouling type · Metallurgy · Loop configuration

---

## Heater Card Schema

The heater card is the canonical structured record for one fired heater and the single source of truth for heater facts. Downstream workflows read these as fields rather than inferring them: estimating and SOP work defer to this schema for what fields mean and which behavior they gate. Treat heater cards as user-provided documents or thread context unless the user explicitly points Codex to a file path.

### Fact / decision wall (core principle)
- **Facts** about the heater — tube geometry, metallurgy, flange details, return-bend type, water supply — live in the technical tables below. A fact is a heater property a drawing or field measurement establishes.
- **Decisions** the customer makes — filtration, smart pigging/inspection — live ONLY in the quarantined Job Options table, recorded as status (Optional / Elected / Declined / TBD), never as a spec. A decision placed in a fact table causes estimating and SOP errors downstream.
- **Pumping-unit type is NOT a card field.** It is a per-job dispatch decision, not a heater property — never recorded or inferred on the card. TriMax is the default unit for essentially all jobs; the double pumper is explicit-only (see `usadebusk-equipment`).

### Tube geometry
One table, one row per distinct pipe ID per section. Add a row only when a section contains more than one pipe ID; default is a single row per section.

| Section | OD (in) | Sched | Wall (in) | ID (in) | Tubes/Coil | Avg Length (ft) | Length/Coil (ft) | Notes |
|---|---|---|---|---|---|---|---|---|

- `ID` is what pig sizing keys off; `OD` + `Sched` are how ID is verified against a drawing. Record all three when available — never drop OD/Sched.
- `Tubes/Coil` = tube count in ONE pass of that geometry (one coil = one pass). Pass count is not a column here — the config rollup carries it.

### Config rollup (estimating reference)
| Config | Section | Coils | Pipe IDs (in) | Tubes | Total Length |
|---|---|---|---|---|---|
| 1 Pass | | 1 | | | |
| N Passes | | N | | | |

- **1 Pass** = one circuit in isolation. **N Passes** = all passes (single-pass values × pass count; Coils = N).
- Edge case: when passes sharing a pipe ID have unequal tube counts, the single-pass figure is an average, not an exact count — flag it rather than dividing blindly.
- Total Length (all passes) feeds the cleaning-rate duration estimate.

### Connection info (facts)
Launcher flange (size / rating# / type, e.g. RFWN) · Receiver flange · Return-bend type (180° U-bend / plug-type "mule ear" header — see `usadebusk-sop` for the distinction) · Water supply source · Max pig OD. Metallurgy (frontmatter + identity) gates NACE/passivation eligibility per the Metallurgy section above; election is still a customer decision recorded in Job Options.

### Job Options (quarantined decisions)
Status only, never facts. Filtration · Smart pigging / inspection. Status ∈ {Optional, Elected, Declined, TBD}. Estimating and SOP read election status here; they never read a decision from a fact table.

---

## Customer-Side Contacts (Typical)
- Maintenance / Turnaround — scheduling and execution
- Procurement / Contracts — bid intake, PO
- Process / Mechanical Engineering — technical review (common at ExxonMobil-tier)
- Operations — isolation, permitting

---

## Role Boundaries
Apply on every job regardless of which domain skill is loaded.
- **Lifting:** USADeBusk does not perform lifts. All rigging and lifting is the customer's lifting contractor's scope.
- **Adapters:** When heater flange size or rating differs from the launcher, the customer fabricates the required adapters.

---

## Customer-Facing Language
- Never expose internal billing constructs — cost basis, markup, internal rates, stand-by/idle rate logic — in any customer-facing output.
