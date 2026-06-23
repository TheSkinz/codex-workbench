---
title: Equipment Circuit Diagrams — TriMax Water Movement
source: B1-USADeBusk_Mermaid_Knowledge_Diagrams.md (06-insights). Diagrams extracted verbatim — do not edit Mermaid here; B1 is the master.
scope: How the TriMax pumper moves water through a circuit — flow topology, port/color identity, capacity scaling, diverter states, and feed-assembly flow states. Tube counts, valve positions, and circuit counts are per-job variables; these diagrams show invariant topology, not fixed specs.
parent_skill: usadebusk-equipment
---

# Equipment Circuit Diagrams

One logical group: how the pumper moves water. Each diagram carries its scope
note from the source, stating what it asserts and what it leaves variable.
Diagrams 2, 4, and 7 live with core/sop and are not duplicated here.

---

## Diagram 1 — Master Flow Circuit

**Scope:** Full closed-loop circuit for one assembly, standard Blue→Red feed direction. Color is bonded to port/endpoint identity (Blue=CONV, Red=RAD), not to feed/return. Filtration shown as an independent concurrent sub-loop. One assembly drawn; TriMax carries 3 identical ones sharing both tanks. Diverter logic detailed separately in Diagram 6.

```mermaid
flowchart LR
    subgraph TRIMAX["TriMax — Triple unit (1 of 3 identical assemblies shown)"]
        CT["Clean Tank<br/>3,000 gal (shared)"]
        DT["Dirty Tank<br/>2,000 gal (shared)"]
        STR[Suction Strainer]
        FM[Flow Meter]
        PUMP[Pump + Engine/Gearbox Drive]
        DIV{Diverter}
        MAN[Valve Manifold<br/>+ bleeder + bypass branch]
        BLUE([BLUE port / CONV]):::blue
        RED([RED port / RAD]):::red
    end

    CT --> STR --> PUMP --> FM --> MAN
    MAN -->|feed: manifold selects port| BLUE
    BLUE -->|3in jetting hose| LAU[Blue Launcher<br/>Conv. Inlet]:::blue
    LAU --> COIL[[Heater Coil — see Diagram 2]]
    COIL --> REC[Red Receiver<br/>Rad. Outlet]:::red
    REC -->|3in jetting hose| RED
    RED --> CEIL[Effluent / Ceiling Pipe] --> DIV
    DIV -->|steady-state| CT
    DIV -->|pig caught / flush| DT

    subgraph FILT["Filtration (concurrent, independent)"]
        DT -. 3in camlock .-> P43[4x3 Pump] -. 3in camlock .-> FP[Filter Press] -. 3in camlock .-> CT
    end

    NOTE["TriMax = 3 of these assemblies on one trailer, sharing both tanks.<br/>Each assembly = independent circuit, own operator station.<br/>Diverter logic detailed in Diagram 6."]

    classDef blue fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef red fill:#f8d7da,stroke:#842029,color:#842029;
```

---

## Diagram 3 — Port / Direction / Color Map

**Scope:** Color is bonded to PORT IDENTITY (Blue=CONV, Red=RAD), fixed. The valve manifold selects which port feeds — no hose swapping. Blue and Red never move; only the feed/return assignment flips. Blue→Red is the standard direction.

```mermaid
flowchart TB
    NOTE["Color is bonded to PORT IDENTITY, not flow direction.<br/>Valve manifold selects feed port — no hose swapping.<br/>Blue = CONV (conv-inlet end) · Red = RAD (radiant-outlet end)."]

    subgraph D1["Blue → Red (STANDARD)"]
        direction LR
        b1[BLUE / CONV port]:::blue -->|FEED| coilA[[Coil: conv → crossover → rad]] -->|RETURN| r1[RED / RAD port]:::red
    end

    subgraph D2["Red → Blue (reversed)"]
        direction LR
        r2[RED / RAD port]:::red -->|FEED| coilB[[Coil: rad → crossover → conv]] -->|RETURN| b2[BLUE / CONV port]:::blue
    end

    classDef blue fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef red fill:#f8d7da,stroke:#842029,color:#842029;
```

---

## Diagram 5 — Circuit Capacity & Scaling

**Scope:** How circuit count maps to equipment. One TriMax handles up to 3 simultaneous circuits. Beyond 3, either mobilize a second TriMax (urgent, all-at-once) or change over (clean 3, rig-over, clean next 3 — roughly doubles decoke duration). Terminology: "second TriMax," never "dual-pumper."

```mermaid
flowchart TD
    Q{Heater circuit count?}
    Q -->|1–3 circuits| ONE[One TriMax<br/>up to 3 simultaneous<br/>unused pumps idle]
    Q -->|"> 3 circuits"| URG{Customer urgency?}

    URG -->|urgent · all at once| TWO[Two TriMax trailers<br/>6 circuits simultaneous]
    URG -->|standard| CO[One TriMax + change-over<br/>clean 3 → rig-over → clean next 3]

    CO --> CONOTE["Roughly doubles decoke duration<br/>(e.g. 6 circuits = 3 @ 24h + 3 @ 24h = 48h)"]:::note
    ONE --> ONENOTE["TriMax = 3 independent assemblies,<br/>3 operator stations, shared tanks"]:::note
    TWO --> TWONOTE["Each TriMax: own tanks + 3 assemblies.<br/>Term: 'second TriMax' — never 'dual-pumper'"]:::note

    classDef note fill:#fff3cd,stroke:#997404;
```

---

## Diagram 6 — Diverter State Machine

**Scope:** Corrects the passive-clarity model. The diverter is operator-driven on a per-pig-run phase trigger, not a continuous clarity sensor. Rests on clean tank during steady-state recirculation; thrown to dirty on the capture→black-confirm sequence and during initial flush.

```mermaid
stateDiagram-v2
    [*] --> Circulating
    Circulating: Diverter on CLEAN TANK<br/>(recirculate pigging water to pump)
    Circulating --> PigCaptured: pressure drop /<br/>flow increase<br/>(pig enters receiver cage)
    PigCaptured: Effluent inbound<br/>(dirty water bypasses caught pig)
    PigCaptured --> BlackConfirmed: visual — clean water turns black<br/>(coke fines arrive at diverter)
    BlackConfirmed --> ToDirty: operator pushes plunger
    ToDirty: Diverter on DIRTY TANK<br/>(dump effluent · removes water from loop)
    ToDirty --> Replenish: makeup water from source
    Replenish --> Circulating: plunger back to clean<br/>(resume steady-state)

    note right of ToDirty
        Also triggered during INITIAL FLUSH.
        Dirty tank to 4x3 to filter press to clean (concurrent).
    end note
```

---

## Diagram 8 — Generic Feed Assembly + 3 Flow States

**Scope:** Invariant feed-side assembly order with the three routable, mutually-exclusive states (Blue→Red, Red→Blue, Bypass). Exact valve open/closed patterns are deliberately NOT encoded — bleeder and valve placement vary between TriMax units, so a canonical valve-state table would be wrong for some units. Bypass recirculates to the clean tank with no port feeding the coil (idle/flush state).

```mermaid
flowchart LR
    CT[Clean Tank] --> STR[Strainer] --> PUMP[Pump<br/>engine/gearbox driven] --> FM[Flow Meter]:::aux --> MAN{Manifold<br/>routes one of 3 states}
    BLEED[Bleeder Valve<br/>position varies per unit]:::aux -.-> MAN

    MAN ==>|"STATE 1 · Blue→Red"| B1[BLUE port → coil → RED port → return]:::blue
    MAN ==>|"STATE 2 · Red→Blue"| R1[RED port → coil → BLUE port → return]:::red
    MAN ==>|"STATE 3 · Bypass"| BP[Recirculate to Clean Tank<br/>no port feeds coil — idle/flush]:::byp

    NOTE["Invariant: tank → strainer → pump → flow meter → manifold → ports.<br/>Three states are mutually exclusive on a given assembly.<br/>Exact valve open/closed pattern NOT canonical — bleeder/valve<br/>placement differs between TriMax units."]

    classDef blue fill:#cfe2ff,stroke:#084298,color:#084298;
    classDef red fill:#f8d7da,stroke:#842029,color:#842029;
    classDef byp fill:#e2e3e5,stroke:#41464b;
    classDef aux fill:#fff,stroke:#999,stroke-dasharray:3 3;
```
