**Figure 2: Runtime Admissibility Gate MVP Architecture**

```text
AI Agent
    │
    ▼
Proposed Action
    │
    ▼
Runtime Admissibility Engine
    │
    ▼
┌─────────────────────────────────────┐
│ Decision Space                      │
│                                     │
│ ALLOW  ─────────────────► Execute   │
│ BLOCK  ─────────────────► Stop      │
│ REQUIRE_APPROVAL ───────► Approval  │
└─────────────────────────────────────┘
                                   │
                                   ▼
                           Human Review
                                   │
                                   ▼
                           ALLOW / BLOCK
                                   │
                                   ▼
                           Execute / Stop
                                   │
                                   ▼
                           Decision Ledger
```
