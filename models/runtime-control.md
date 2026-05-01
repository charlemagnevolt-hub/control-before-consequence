# Runtime Control Model

A system under uncertainty must evaluate admissibility *at the moment of state transition*.


## Core Components

- State space
- Action space
- Constraint surface
- Admissibility function


## Flow

1. System proposes action  
2. Action mapped to affected state space  
3. Constraint surface evaluated  
4. Admissibility decision returned  
5. Execution allowed / constrained / blocked  


## Key Idea

Admissibility is not static.

It is evaluated dynamically based on:
- current system state
- potential downstream impact
- constraint definitions
