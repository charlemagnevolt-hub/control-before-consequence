# Figure 2: Runtime Admissibility Gate MVP Architecture

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
┌────────────────────────────┐
│ Decision Space             │
│                            │
│ • ALLOW                    │
│ • BLOCK                    │
│ • REQUIRE_APPROVAL         │
└────────────────────────────┘
              │
              ▼
       Approval Queue
              │
              ▼
     Execution Decision
              │
      ┌───────┴────────┐
      ▼                ▼
 Execute           Do Not Execute
      │
      ▼
 Decision Ledger
```
