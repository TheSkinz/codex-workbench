# Job Report Structure

## Overview

The job report is a branded, customer-facing document delivered at project completion. It goes to: (1) the customer contact, (2) internal SharePoint for future reference on similar bids.

Output format: Word document (.docx) via the `docx` skill. Use DeBusk brand standards from `usadebusk-core`.

---

## Section Sequence

### 1. Cover Page
- DeBusk logo (centered, large)
- Tagline: "Re-imagining The Industrial Cleaning Business"
- Body text: "USA DeBusk is driving innovation for a full range of industrial services… delivering maintenance projects that are safe, reliable, and cost-efficient."
- Bottom right block:
  - **[Facility Name]:** [scope description]
  - **Equipment:** [list of primary equipment]
  - **Execution Date:** [rig-in date]

---

### 2. Job Summary Page

**CUSTOMER DETAILS** table
| Field | Value |
|---|---|
| FACILITY | [facility name] |
| ADDRESS | [full address] |
| JOB & PO# | [USA#] / [PO number] |
| CONTACT | [customer contact name] |

**PROJECT DETAILS** table
| Field | Value |
|---|---|
| SCOPE | [scope description] |
| EXECUTION | [rig-in date] |
| SITE TRAINING | [training code] |
| EQUIPMENT | [comma-separated equipment list] |

**CREW DETAILS** table
| Field | Value |
|---|---|
| SHIFT LEAD | Day: [name] \| Night: [name] |
| DAYSHIFT | [name, name, name, ...] |
| NIGHTSHIFT | [name, name, name, ...] |

**PROJECT DURATION** table — one row per heater/scope item
| SCOPE | RIGGING | PIG | SMART PIG | STAND-BY | TOTAL |
|---|---|---|---|---|---|
| [heater tag] | [hrs] | [hrs] | [hrs or 0] | [hrs] | [sum] |

**PIGS USED** table — aggregated across all shifts
| SIZE | TC | HR | FOAMS | SWABS | TOTAL |
|---|---|---|---|---|---|
| [size] | [n] | [n] | [n] | [n] | [sum] |
| TOTAL | [sum] | [sum] | [sum] | [sum] | [grand total] |

---

### 3. Heater Card + Timeline Page

**Heater card** — one table per heater
| Field | Value |
|---|---|
| Furnace | [heater name — ALL CAPS] |
| Section | [Radiant / Convection + Radiant / etc.] |
| Number of Coils | [n Pass(es)] |
| Total Footage | [n]' Total |
| Tube Length + Bend | Approximately [n]' |
| # of Tubes | [n] Tubes Total |
| Tube ID's | [OD] Sch [n] / [OD]" O.D. X [wall] ([ID] I.D.) |
| Metallurgy | [A-xxx grade] |
| Tube Arrangement | [Vertical / Horizontal] |
| Inlet/Outlet Details | [flange size] [rating] [type] |
| Return Bends | [type] |
| Notes | [any special conditions — use orange/amber text for critical notes] |

**TIMELINE** table — one row per service receipt ticket
| TICKET | START | FINISH | TASK | HOURS | DETAIL |
|---|---|---|---|---|---|
| [#] | [date time] | [date time] | [Mobilization / Rig-in / Stand-by / Pigging / Rig-out / Demobilization] | [hrs] | [1–2 sentence detail] |

Timeline detail field guidance:
- Mobilization: "Equipment transport; site badging."
- Rig-in: "Rigging hoses and launchers to [pass description]."
- Stand-by: Specific cause — "Awaiting tube cuts and launcher installation." Never write generic "standby."
- Pigging: Specific activity — "Flow test; [pig size] pin pigging runs; dewatered."
- Rig-out: "Dewatered coil; rigged out equipment; demobilized from facility."

---

### 4. Flow Tests + Analysis Page

**FLOW TESTS** — one table pair per pass
Left table: BEFORE: PASS [n]
Right table: AFTER: PASS [n]

| RPM | PSI | GPM |
|---|---|---|
| [n] | [n] | [n] |
| [n] | [n] | [n] |
| [n] | [n] | [n] |
| [n] | [n] | [n] |

Note: Flow test data comes from the Decoking Data Sheet (separate from service receipts). User provides this data at report time if not already logged.

---

**DECOKING SUMMARY / ANALYSIS** section header

Sub-header: [Heater Tag] Heater

**Deposit Localization and Concentration:** [User-written narrative — where deposits were concentrated, severity, distribution across coil sections]

**Decoking Analysis:** [User-written narrative — what pig progression was used, what worked, how cleaning progressed, key observations]

**Cleaning Results:** [heading only — photos follow]

Photos: Insert pig progression photos and deposit photos here. User attaches images at report generation time.

---

### 5. Closing Block (bottom of final page)

```
[PM Name]
USADebusk
Cell: [PM cell — from /setup data]
[PM email — from /setup data]
[DeBusk logo]
```

---

## Data Sources for Each Section

| Section | Source |
|---|---|
| Cover | /setup data |
| Customer / Project / Crew Details | /setup data |
| Project Duration | Aggregated from all /extract outputs |
| Pigs Used | Aggregated from all /extract outputs |
| Heater Card | /setup data + heater card upload |
| Timeline | One row per /extract ticket, detail from shift summaries |
| Flow Tests | Decoking Data Sheet — user provides |
| Decoking Summary | User-written at /report time |
| Photos | User attaches at /report time |
| Closing | PM name/cell/email from /setup data |

---

## Aggregation Rules

**Project Duration hours:**
- Pull Rig-in/out hours, Pigging hours, Stand-by hours from each receipt extraction
- Sum by task category across all tickets for each heater
- Smart Pig = 0 unless explicitly logged

**Pigs Used totals:**
- Parse PIGS USED from each receipt extraction
- Aggregate by size and type across all shifts
- Foams = gauge foams + pusher foams combined
- Swabs = dewatering swabs

**Timeline detail:**
- One row per ticket number
- If two passes on one ticket, combine into one row with combined task label
- Start/Finish times pulled from rig-in/rig-out fields on receipt
- Hours = total shift hours for that ticket

---

## Formatting Rules (docx skill)

- Table headers: `#222222` fill, white text, bold
- Alternating row fill: `#F7F7F7`
- Heater card critical notes: orange/amber text
- All tables: Arial 10pt body
- Section headers: Arial 13pt bold, `#FCC30A` bottom border
- Confidentiality footer on every page: "CONFIDENTIAL AND PROPRIETARY"
- Page numbers: bottom right
