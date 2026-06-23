
# USADeBusk — Operations & Field Admin

## Service Receipt
Handwritten daily document completed by PM for each 12-hour shift. Canonical field structure (this is the receipt's field map; the Step 1 table below is the extraction map):

**Header:**
- Customer name + contact
- Date · Shift (Day/Night)
- Location
- Job # / PO
- Unit # / Pass #
- Clean ID — largest pig size that passed through the full circuit without obstruction. Max pig size = tube ID + 0.250".
- Total Length — footage pigged this shift, if recorded

**Equipment hours:**
- **Pumper — hours.** (L/C/R is preprinted on the form — legacy circling convention, no longer used.) Which pump/side/circuit is operated/cleaned is recorded in the **Shift Summary** narrative, not by marking L/C/R. See `usadebusk-equipment` for left/center/right assembly identity.
- Support # — hours
- Crew Truck(s) — ID + hours
- Materials/Equipment — freeform (e.g., 4×3 diesel pump — hours)
- Filtration/Filters — hours
- Pigs — types + quantities

**Labor hours:**
- DS Supervisor — name + hours
- NS Supervisor — name + hours
- Operators — name + hours (up to 6 slots)

**Task hours:**
- Rig In
- Rig Out
- Rig Over
- Pigging
- Plant Down Time
- Third Party Services — description + hours

**Consumables:**
- Per Diem — count (people × shifts)
- DEF — count (shifts)

**Shift Summary** — freeform chronological narrative of shift activity, **including which pump/side/circuit(s) were operated/cleaned this shift**. Example: "7am–9am: Pig (2 hrs) Polish 30 passes. 9am–12pm: Smart Pig (3 hrs). 12pm–2pm: Stand-by (2 hrs) wait for approval. 2pm–7pm: Rig-out (5 hrs)."

**Sign-off:**
- Customer name + signature
- Supervisor name + signature
- Date

⚠️ **Unsigned receipts = dispute risk. Flag immediately.**

---

## Ticket Breakdown File
Most important per-job operational document.

**Naming:** `USA[YYNNN] [Facility Name] [Scope] TriMax Ticket Breakdown`

**Contents:** All billable resources mobilized, durations, billing rates, running totals.

**Purpose:** Source for invoice generation. All service receipt data feeds here.

---

## Receipt Extraction Process
When processing service receipts for a job:

**Step 1 — Extract all billable fields**

| Line Item | Category | Hours/Qty | Rate Basis |
|---|---|---|---|
| TriMax Pumper | Equipment | N hrs | Hourly task-based |
| Filter Press | Equipment | N hrs | Pumping / non-pumping (pumping = pigging/smart pigging; non-pumping = rigging/stand-by) |
| 4×3 Pump | Equipment | N hrs | Hourly |
| Support Unit | Equipment | N hrs | Hourly |
| Crew Truck | Equipment | N hrs | Hourly |
| DS Supervisor | Labor | N hrs | Hourly |
| NS Supervisor | Labor | N hrs | Hourly |
| Operator | Labor | N hrs | Hourly |
| Per Diem | Labor | N count | Daily |
| DEF | Materials | N shifts | Per shift |
| Pigs | Materials | qty/type | Unit rate |
| Third Party | Third Party | N hrs | Cost + markup |
| Plant Down Time | Stand-by | N hrs | Stand-by rate |

**Step 2 — Cross-check against proposal**
- Resources on receipt consistent with proposal scope?
- Task hours (Rig-In, Pig, Rig-Out, Stand-by) align with execution plan?
- Any resources appearing that weren't in the original proposal? → Flag for billing review
- PDT present? → Flag as potentially billable stand-by
- Third-party services captured with enough detail for invoicing?

**Step 3 — Variance flags — call out explicitly:**
- Hours exceeding proposal estimate for any task category
- Resources billed not in original proposal scope
- Missing signatures (customer or supervisor)
- Missing Clean ID
- Incomplete or missing shift summary
- Per diem count not matching headcount

**Step 4 — Import-ready table**
Produce clean structured table formatted for Ticket Breakdown Excel entry.

---

## Plant Down Time (PDT)
- Facility-caused downtime — not USADeBusk-caused
- Always flag as potentially billable at stand-by rate
- Distinguish clearly from USADeBusk-caused delays in shift summary narrative

---

## Invoice Readiness Check
Before generating invoice:
1. All receipts collected — no gaps in shift sequence
2. All receipts have customer signature
3. Third-party items described sufficiently for invoicing
4. Total hours reconciled against proposal — flag significant overruns or underruns
5. PDT hours confirmed billable with customer

---

## Job Filing
- All documents under USA# in Pigging Jobs folder on SharePoint
- Ticket Breakdown is the anchor document
- Service receipts (scanned) attached to job folder
