---
title: SOP Pigging Diagrams — Looped Circuit & Pig Progression
source: B1-USADeBusk_Mermaid_Knowledge_Diagrams.md (06-insights), Diagrams 4 and 7. Extracted verbatim — do not edit Mermaid here; B1 is the master.
scope: Two pigging-procedure diagrams — the looped jumper-spool circuit (D4) and the smallest-ID-first pig progression with the larger-ID reversal procedure (D7). Tube counts, pig sizes, transit times, and circuit pairing are per-job variables; these diagrams show invariant strategy/topology, not fixed specs.
parent_skill: usadebusk-sop
status: D7 reversal control-action sequence is field-unconfirmed (draft) — all other content canonical
---

# SOP Pigging Diagrams

Two pigging-procedure diagrams, extracted verbatim from B1 with their scope notes. D4 is clean canon.
In D7, only the reversal **control-action sequence** (the S1–S5 throttle/switch/re-throttle order) is
draft pending field confirmation — see the field-verification note below. Everything else in D7 is canon.

---

## Diagram 4 — Looped Circuit (Jumper Spool)

**Scope:** A 180° jumper spool bonds the radiant outlets of two passes into one continuous circuit. Pass 2 runs reversed. Color stays bonded to port identity (both conv ends are Blue). Combined length extends transit and the blind period; final pig may size up for wall contact.

```mermaid
flowchart LR
    BL([BLUE port / feed]):::blue -->|3in hose| L1[Blue Launcher<br/>P1 Conv. Inlet]:::blue
    L1 --> P1[[Pass 1 Coil<br/>conv → crossover → rad]]
    P1 --> RO1[P1 Rad. Outlet]:::red
    RO1 -->|"180° jumper spool"| RO2[P2 Rad. Outlet]:::red
    RO2 --> P2[[Pass 2 Coil<br/>rad → crossover → conv<br/>REVERSED]]
    P2 --> L2[Blue Receiver<br/>P2 Conv. Inlet]:::blue
    L2 -->|3in hose| RD([BLUE / return port]):::blue

    NOTE["Two passes become one continuous circuit.<br/>Transit 10–20+ min · long blind period between launches.<br/>Final pig may size up (e.g. 6.5 vs 6.25) for wall contact over combined length."]

    classDef blue fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef red fill:#f8d7da,stroke:#842029,color:#842029;
```

---

## Diagram 7 — Pig Progression + Larger-ID Reversal Procedure

**Scope:** Smallest-ID-first strategy with progressive 1/8" sizing. Encodes the SINGLE reversal procedure triggered when a pig crosses into a larger ID (pressure drop + flow increase — same signature as entering a spool). The subsequent pressure rise is the EXPECTED confirmation that the pig is back in the smaller ID (line-size pig in smaller pipe needs more pressure), not a separate fault.

> **Field-verification note:** the reversal control sequence (throttle / directional switch / re-throttle) was built from Jesse's description. Confirm exact control-action order with a field operator before treating as canonical — procedural muscle-memory sequences are where paraphrase can drift.

```mermaid
flowchart TD
    START([Start: foam / undersized TC]) --> LAUNCH[Launch pig<br/>smallest ID first]
    LAUNCH --> TRAVEL{Pig in transit<br/>monitor pressure & flow}

    TRAVEL -->|"pressure DROP + flow INCREASE<br/>(pig crossed into LARGER ID —<br/>same signature as entering a spool)"| REV

    subgraph REV["Larger-ID Reversal Procedure"]
        direction TB
        S1[1 · Throttle engine to IDLE<br/>once pig fully in larger pipe]
        S2[2 · Set Directional Switch<br/>to opposite direction]
        S3[3 · Valves turn ~3 sec]
        S4[4 · Throttle back up to<br/>target velocity / RPM / flow<br/>→ drives pig back to smaller ID]
        S5[5 · Pressure INCREASES on monitor<br/>EXPECTED — line-size pig in smaller pipe<br/>needs more pressure than in larger pipe]
        S1 --> S2 --> S3 --> S4 --> S5
    end

    REV --> TRAVEL

    TRAVEL -->|"clean pass · effluent ≤ 3–5s & clear"| OK{Pass successful}
    OK -->|not yet line size| UP[Size up 1/8 in] --> LAUNCH
    OK -->|line size reached| OVER[Oversized final pig<br/>tube ID + up to 0.250 in]
    OVER --> DONE([Complete — run AFTER flow test])

    classDef proc fill:#cfe2ff,stroke:#084298;
    class S1,S2,S3,S4,S5 proc;
```
