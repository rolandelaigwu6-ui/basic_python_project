# Mystery Island — Game Flowchart

Use this as a guide while building the game in small parts. The map shows the required locations; choose and document the exact route and where the rope and lantern are found.

```mermaid
flowchart TD
    A([Start]) --> B[Show title and instructions]
    B --> C[Ask for player name]
    C --> D[Create fresh player state:<br/>location = Beach<br/>energy = 5<br/>inventory = empty]
    D --> E[Show current location, energy,<br/>inventory, and available actions]
    E --> F{Read and normalize<br/>menu choice}

    F -->|Invalid choice| G[Explain valid choices]
    G --> E
    F -->|Quit| Q[Show quit message]
    F -->|Show status or inventory| E
    F -->|Move| H{Is destination<br/>connected from here?}
    H -->|No| I[Explain that move is unavailable;<br/>leave state unchanged]
    I --> E
    H -->|Yes, but bridge and no rope| J[Explain rope is required;<br/>leave state unchanged]
    J --> E
    H -->|Yes| K[Move to destination<br/>and subtract 1 energy]
    K --> L{Energy is 0?}
    L -->|Yes| M[End game: player ran out of energy]
    L -->|No| N{At a location with<br/>an uncollected object?}
    N -->|Yes| O{Player chooses<br/>to collect it?}
    O -->|Yes| P[Add object once<br/>to inventory]
    O -->|No| E
    P --> E
    N -->|No| R{At Lighthouse and<br/>has lantern?}
    R -->|No| E
    R -->|Yes| S{Player chooses<br/>to light beacon?}
    S -->|No| E
    S -->|Yes| T[End game: beacon restored;<br/>player wins]

    M --> U{Play again?}
    T --> U
    Q --> U
    U -->|Yes| D
    U -->|No| V([Exit])
```

## Decisions to settle in your design

- Which locations connect, including any backward moves?
- Which location contains the rope, and which contains the lantern?
- Does choosing to collect an object cost energy, or only moving?
- How does the player choose to light the beacon at the Lighthouse?
- Does quitting offer replay, or exit directly? The chart currently offers replay after quit too.

Keep invalid choices and blocked moves from changing the player's state. A replay should create a new state with 5 energy, Beach as the location, and an empty inventory.
