---
title: Coil Template — Tube-Level Topology (multi-size)
source: B1-USADeBusk_Mermaid_Knowledge_Diagrams.md (06-insights), Diagram 2. Extracted verbatim — do not edit Mermaid here; B1 is the master.
scope: Invariant coil topology for a single pass — serpentine reversal, conv → crossover → rad order. Tube count and ID-transition points are per-job variables; this is a template, not a fixed spec.
parent_skill: usadebusk-core
---

# Coil Template — Tube-Level Topology

Invariant coil topology only. Tube counts, crossover form, and ID-transition
points are per-job variables — read this as a template, not a spec.

---

## Diagram 2 — Tube-Level Coil Template (multi-size)

**Scope:** Invariant coil topology — serpentine reversal at each bend, conv → crossover → rad order. Tube count is a per-job variable (avg ~10 conv tubes). The crossover is a single abstracted node carrying all real-world variants (external flanged / internal welded / none; reducer present or absent). ID transitions via reducer/expander can occur **mid-pass between any tubes**, not only at the crossover. This is a TEMPLATE, not a spec.

```mermaid
flowchart LR
    IN([Conv. Inlet · BLUE]):::blue --> C1[Conv Tube 1 →]
    C1 -->|U-bend| C2[Conv Tube 2 ←]
    C2 -. "ID transition possible<br/>(reducer/expander, mid-pass)" .-> C3[Conv Tube 3 / outlet →]
    C3 -.->|"… N conv tubes per job (avg ~10) …"| XO
    XO{{Cross-over<br/>external flanged / internal welded / none ·<br/>reducer here OR mid-coil OR absent}}
    XO --> R1[Rad Tube 1 / inlet →]
    R1 -->|return bend| R2[Rad Tube 2 ←]
    R2 -->|return bend| R3[Rad Tube 3 / outlet →]:::hot
    R3 -.->|"… M rad tubes per job …"| OUT([Rad. Outlet · RED]):::red

    NOTE["TEMPLATE — tube count varies per job.<br/>ID transitions can occur mid-pass between ANY tubes, not only at crossover.<br/>Pigging targets smallest ID first (see Diagram 7).<br/>Radiant outlet = hottest, most fouling-prone."]

    classDef blue fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef red fill:#f8d7da,stroke:#842029,color:#842029;
    classDef hot fill:#ffe0b2,stroke:#c43e00;
```
