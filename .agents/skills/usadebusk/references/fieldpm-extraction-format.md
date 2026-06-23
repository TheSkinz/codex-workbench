# Service Receipt Extraction Format

## Overview

Handwritten service receipts are the source documents for all shift data. They are frequently messy, partially filled, or photocopied at low quality. Extract what's there, flag what's missing or ambiguous, never fabricate.

**Cross-reference with job initialization data:** The `/setup` block in this thread is the authoritative reference for all static job data. It does not change until the job is over. Before finalizing any extraction, cross-reference the following against the setup block and correct plausible OCR errors or handwriting misreads:

- **Crew names** — supervisors and all operators. If "Jese Utey" is extracted and "Jesse Utsey" is in the crew roster, correct it.
- **Equipment numbers** — trailer #, pumper #, support #, crew truck numbers
- **Job identifiers** — USA#, PO#, heater tag, pass label, facility name, location
- **Shift structure** — day/night designation, supervisor assignment per shift

Correction format in FLAGS: `[Field corrected: "[extracted]" → "[corrected]" — matched /setup data]`
Do not silently correct. Always note it in FLAGS even if confidence is high.

---

## Field Reference — Service Receipt

### Left Column
| Field | Notes |
|---|---|
| Customer | Facility name (not company name) |
| Contact | Customer rep name on-site |
| Pumper # | Trimax unit number. L/C/R = Left/Center/Right pump — note if circled, skip if not |
| Support # | Support unit number (crew truck or support trailer) |
| DS Supervisor | Day shift supervisor name — always extract even on a night receipt |
| DS Hours | Day supervisor hours worked this ticket |
| NS Supervisor | Night shift supervisor name — always extract even on a day receipt |
| NS Hours | Night supervisor hours worked this ticket |
| Rig In | Time rig-in started (HH:MM) |
| Rig Out | Time rig-out completed (HH:MM) |
| Rig Over | Time rig-over completed if applicable (HH:MM) |
| Pigging Hours | Total active pigging hours this shift |
| Plant Down Time | PDT hours — facility-caused downtime, typically billable as standby |
| Third Party Services | Any subcontractors or rented equipment on-site |
| PPE | PPE cost if applicable |
| Per Diem | Per diem units claimed — 1 per person per 12-hr shift standard |
| DEF | Diesel exhaust fluid — $125/shift standard |
| Trailer # | Trimax trailer number |
| Crew Truck(s) | Crew truck number(s) |
| Materials/Equipment | Any consumables or additional equipment |
| Shift Summary | Free-text narrative — preserve verbatim |

### Right Column
| Field | Notes |
|---|---|
| Date | Shift date |
| Day / Night | Check box — note which is marked |
| Location | Facility location (city or unit area) |
| Job # / PO | USA# and customer PO number |
| Unit # & Pass # | Heater unit tag and pass label (e.g., H-19 Pass 1+2 Conv) |
| Clean ID | Maximum pig size run — indicates cleaning endpoint achieved |
| Total Length | Total footage of coil cleaned this shift |
| Operators (x6) | Operator names and hours — up to 6 slots |
| Filtration/Filters | Filter type and count used |
| Pigs | Pig inventory used — size, type, count. Often shorthand (e.g., "4" TC x3, 4.125 PPS x2, 4" foam x1") |
| Free lines | Additional pig notes, deposit observations, effluent notes |

---

## Output Block Format

Use this exact structure for each extracted receipt. One block per receipt.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[DAY / NIGHT] SHIFT — Ticket #[NNNNN]
Date: [Day, Month DD, YYYY]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

JOB INFO
  Facility:       [name]
  Location:       [city/unit]
  Job # / PO:     [USA#] / [PO#]
  Unit & Pass:    [heater tag] — [pass label]

CREW
  DS Supervisor:  [name] — [hrs] hrs
  NS Supervisor:  [name] — [hrs] hrs
  Operators:
    [name] — [hrs] hrs
    [name] — [hrs] hrs
    [name] — [hrs] hrs
    [name] — [hrs] hrs

EQUIPMENT
  Pumper:        #[n] ([L/C/R if noted])
  Support:       #[n]
  Trailer:       #[n]
  Crew Truck(s): #[n]

TASK HOURS
  Rig-in:        [HH:MM] → [HH:MM]
  Rig-out:       [HH:MM] → [HH:MM] [if applicable]
  Rig-over:      [HH:MM] [if applicable]
  Pigging:       [hrs]
  Plant Down:    [hrs] [reason if noted]

MATERIALS
  Per Diem:      [n] units
  DEF:           [yes/no]
  PPE:           [amount if noted]
  Filtration:    [type/count]
  Third Party:   [description if any]
  Other:         [materials/equipment if noted]

PIGS USED
  [size] [type]:  [n]
  [size] [type]:  [n]
  Clean ID:       [max pig size run]
  Total Footage:  [n] ft

SHIFT SUMMARY
  [verbatim from receipt]

FLAGS: [list any illegible fields, missing data, or inconsistencies]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Pig Type and Size Validation

Pig entries must conform to known valid types and sizes. Apply autocorrection where the intent is clear; flag where it is not.

### Valid Pig Types
| Code | Full Name | Notes |
|---|---|---|
| TC | TrueCut | Aggressive carbide-studded |
| PPS | Pin Poly Soft | Medium aggressiveness — also written HR |
| HR | High Recovery | Same category as PPS |
| BLT | Bolt | Very aggressive — also written "Bolted" |
| Foam | Foam pig | Gauge or pusher — soft, diagnostic |
| Swab | Swab pig | Dewatering only |
| Wire Brush | Wire brush | Mechanical scrubbing |
| Bald | Bald urethane | Softest cleaning pig |
| Gauge | Gauge pig | Assesses restriction or obstruction |

Any pig type not in this list: flag it and attempt to match to the nearest valid type. Format: `FLAGS: [Pig type "PPC" unrecognized — possible PPS? Confirm.]`

### Valid Pig Sizes
Sizes are based on tube ID for the job — read the pipe ID from the `/setup` block. Valid pig sizes are standard increments for that tube ID:

**Common size increments per tube ID:**
- 4" tube (4.026" ID): 3.5", 3.75", 4", 4.125", 4.25"
- 5" tube (~5.047" ID): 4.5", 4.75", 5", 5.125", 5.25"
- 6" tube (6.065" ID): 5.5", 5.75", 6", 6.125", 6.25", 6.5"
- 8" tube (7.981" ID): 7", 7.25", 7.5", 7.75", 8", 8.125", 8.25"
- 10" tube (10.020" ID): 9", 9.25", 9.5", 9.75", 10", 10.125", 10.25"

Max pig OD = tube ID + 0.250" (hard limit — flag any size exceeding this).

If an extracted pig size is not a standard increment but is close to one (e.g., "4.1"" likely means "4.125""), autocorrect and note in FLAGS. If it could be multiple sizes, flag for confirmation.

Direction notation: B-R = Blue to Red, R-B = Red to Blue (per job surface equipment labeling)

---

## Edge Case Handling

**Illegible handwriting:** Write `[ILLEGIBLE]` in the field. Do not guess. List in FLAGS.

**Partially filled receipt:** Extract what's present. List blank fields in FLAGS only if they are operationally significant (supervisor name, ticket #, pig count). Skip cosmetic blanks silently.

**Two passes on one receipt:** Split into separate pass sections under the same ticket block. Label clearly: PASS 1 / PASS 2.

**Pig count in free text:** Parse shorthand pig notation into the structured PIGS USED table. If notation is ambiguous (e.g., "4" x3 TC/PPS mixed") note the ambiguity in FLAGS.

**Times in 12-hr format:** Convert to 24-hr (HH:MM) for consistency.

**Hours that don't add up:** If rig + pig + standby hours don't reconcile with shift duration, flag it. Show the math.

**Multiple receipts — one upload:** Process each separately, output sequentially.

**Mobilization / Demobilization receipt:** Travel-only tickets with no rig times, no pig data, and no pigging hours. Expected — do not flag missing rig/pig fields. Extract: date, shift, supervisor names and hours, operator names and hours, per diem, trailer #, crew trucks, any third-party transport or equipment. Task Hours block should show: Travel: [hrs] only. PIGS USED block: N/A — Mob/Demob ticket.
