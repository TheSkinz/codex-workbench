
# USADeBusk — Field Project Management

## Overview

This workflow manages the full lifecycle of a furnace decoking field job from setup through final report. Use one Codex thread per job. All shift data, extractions, and log entries accumulate in the thread conversation history and serve as the running job record. Codex reads back through the thread to find prior setup records, extraction outputs, and log entries when compiling status or reports.

**Workflow:**
job setup → shift receipt extraction + shift log + payroll email each shift cycle → status summary on demand → final report at demob

---

## Workflows

### Job Project Initialization

**Trigger:** User asks to set up a new job or start a job project.

**Inputs required:**
- Job # (USA#)
- Facility name, full address, and location
- Customer contact name
- Site training code
- Heater tag(s) and pass count (support multiple heaters)
- Execution plan (upload or paste)
- Heater card data per heater: tube ID (conv + rad), total footage, tube length + bend, number of tubes, tube arrangement (H or V), metallurgy, flange size/rating/type, return bend type, inlet/outlet details
- Crew roster (day supervisor, night supervisor, operators by shift)
- PM name, cell, and email (for report closing block)
- Trailer #, crew truck(s), support equipment
- Service receipt starting ticket number
- Quoted hours by task (rig, pig, standby per heater)

**Output:** A structured job initialization block posted in the thread. This is the anchor record for the job; Codex reads it from thread history for subsequent field PM tasks. Format:

```
═══════════════════════════════════════════
JOB INITIALIZED — [USA#]
═══════════════════════════════════════════
JOB:       [USA#] — [Facility] — [Heater Tag(s)]
CUSTOMER:  [name] | CONTACT: [name]
LOCATION:  [full address]
TRAINING:  [site training code]

PM:        [name] | [cell] | [email]

CREW — DAY:   [supervisor] + [operators]
CREW — NIGHT: [supervisor] + [operators]

EQUIPMENT: [trailer #], [trucks], [support units]

HEATER: [tag]
  Passes:      [n]
  Footage:     [n] ft total
  Tube L+Bend: ~[n]'
  # Tubes:     [n]
  Arrangement: [Vertical / Horizontal]
  Tube ID:     Conv [n]" / Rad [n]"
  Metallurgy:  [grade]
  Flanges:     [size] [rating] [type]
  Returns:     [type]
  Inlet/Outlet:[detail]
  Notes:       [any special conditions]

[Repeat HEATER block for each additional heater]

QUOTED:    Rig [hrs] | Pig [hrs] | Standby [hrs] | Total [hrs]
RECEIPT START: Ticket #[NNNNN]
═══════════════════════════════════════════
```

---

### Service Receipt Extraction

**Trigger:** User uploads scanned service receipts and asks for extraction, structured data, or a summary.

**Inputs:** One or two scanned receipt PDFs (day shift + night shift). May be handwritten, photocopied, or photographed — handle OCR ambiguity gracefully. If a field is illegible, flag it explicitly rather than guessing.

**Behavior:**
- Extract all fields from each receipt
- Normalize times to HH:MM format
- Calculate derived fields (pigging hours from rig-in/rig-out/pig start times if not explicit)
- Summarize pig section from the "Pigs:" field and free-text lines
- Flag any inconsistencies (hours don't add up, missing ticket #, blank operator names)

**Output format:** Read `references/fieldpm-extraction-format.md` for the exact structured block format. Output one block per receipt. Label clearly: DAY SHIFT — Ticket #NNNNN and NIGHT SHIFT — Ticket #NNNNN.

**After extraction:** Tell the user: "Review for any corrections, then ask me to generate the email body when ready."

---

### Shift Note Append

**Trigger:** User sends a freeform note about anything that happened on the job — pig results, PDT events, equipment issues, observations, customer comments, stuck pig situations, anything.

**Inputs:** Freeform text, any length, any format. User may be on iPhone typing fast. Do not require structure — accept whatever comes in.

**Behavior:**
- Timestamp the entry (use date/time if provided; otherwise note "time unspecified")
- Identify the type of entry: pig result / PDT event / equipment issue / flow test / observation / customer interaction / other
- Structure it into a clean log entry
- Output the structured version and say "Logged." — only ask for correction if the input was genuinely ambiguous

**Output:** Structured log entry. No confirmation loop required on clear inputs.

**Named log entry types:**
- Pig run result: size, direction, condition on return, comments
- PDT: start time, cause (customer-side), estimated duration
- Stuck pig: location, pig type/size, resolution steps, outcome
- Equipment issue: what, when, how resolved
- Flow test: pass #, before/after, RPM/PSI/GPM readings — structure into flow test table format for the final report
- Observation: deposit concentration, tube condition, effluent notes
- Customer interaction: who, what was said, any commitments made

---

### Shift Email Body Generator

**Trigger:** User asks to generate the shift email after reviewing extracted receipt data.

**Inputs:** The most recent extracted receipt data (day + night). If not yet extracted, prompt for upload first.

**Output:** Plain text email body, ready to paste. Structure:

```
[Facility] — [Heater Tag] | [Date Range]
Tickets: [Day #] (Day) / [Night #] (Night)

DAY SHIFT — [Date], [Start]–[End]
Supervisor: [name]
Task: [Rig-in / Pigging / Stand-by / Rig-out]
Rig: [in time] → [out time] | Pigging: [hrs] | Standby: [hrs]
[Shift summary from receipt]

NIGHT SHIFT — [Date], [Start]–[End]
Supervisor: [name]
Task: [task]
Rig: [in time] → [out time] | Pigging: [hrs] | Standby: [hrs]
[Shift summary from receipt]

PAYROLL — DAY ([Date], Ticket #[N]):
[Name]: [hrs] hrs + [per diem] per diem
[Name]: [hrs] hrs + [per diem] per diem
...

PAYROLL — NIGHT ([Date], Ticket #[N]):
[Name]: [hrs] hrs + [per diem] per diem
...
```

Per diem: 1 unit per 12-hour shift per person unless noted otherwise on the receipt.

---

### Job Progress Summary

**Trigger:** User asks where the job stands, how many hours burned, pig count, or progress vs. quote.

**Inputs:** Read back through this conversation thread to find prior extraction outputs and setup data. Aggregate hours and pig counts from every extraction block in the thread.

**Output:** Clean summary block:

```
JOB STATUS — [USA#] [Facility] [Heater] — as of [date]

HOURS (vs. quoted):
  Rig-in/out:  [actual] / [quoted] hrs
  Pigging:     [actual] / [quoted] hrs
  Stand-by:    [actual] / [quoted] hrs
  TOTAL:       [actual] / [quoted] hrs

PIGS USED (to date):
  [size] TC:    [n]
  [size] HR:    [n]
  Foams:        [n]
  Swabs:        [n]
  TOTAL:        [n]

PASSES: [n of N] complete
PDT logged: [total hrs / events]
Current status: [active phase]
```

Flag any category where actual > 90% of quoted.

---

### Final Job Report Compiler

**Trigger:** User asks to generate or compile the job report.

**Inputs:** Read back through this conversation thread to find prior extraction outputs, log entries, setup data, and any flow test data logged. Additionally prompt for: flow test data (if not already logged), pig photos (user attaches).

**Behavior:**
1. Compile all structured data from thread history into report sections
2. Prompt user for the Decoking Summary / Analysis narrative: "Ready to compile the report. Give me your analysis — deposit location, what worked, cleaning result, any recommendations."
3. Assemble complete report structure (see `references/fieldpm-report-structure.md`)
4. Closing block uses PM name, cell, and email from setup data — not day supervisor
5. Call the `docx` skill to output a branded Word document

**User writes:** Decoking Summary / Analysis narrative only.
**Codex compiles:** Everything else from accumulated job data.

---

## Behavior Rules

- **Never guess illegible fields on scanned receipts.** Flag and ask.
- **Always label shifts clearly** — day vs. night, ticket number, date. Ambiguity in shift data causes payroll errors.
- **Preserve the user's own words** in shift summaries and log entries — don't rewrite observations into generic language.
- **Flag hours overruns proactively** — if extracted data pushes any task category past 90% of quoted, note it in the extraction output without waiting for a status request.
- **Don't require perfect input.** iPhone notes, half-sentences, and shorthand are expected. Parse intent, structure the output, confirm only if genuinely ambiguous.
- **Per diem default:** 1 unit per shift per person. Override only if receipt explicitly states otherwise.
- **Ticket number continuity:** Track ticket numbers across the job. Flag gaps or duplicates.
- **Cross-thread references:** Do not pull operational data from other job threads without explicit user request. If the user asks a question referencing a prior job, treat it as reference/context only.

---

## Reference Files

Load when needed — do not load both on every request:

- `references/fieldpm-extraction-format.md` — exact output format for service receipt extraction, field definitions, edge case handling
- `references/fieldpm-report-structure.md` — complete job report section structure, table schemas, formatting rules
