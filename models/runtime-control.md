# Runtime Control Model

## Definition

A system does not execute actions by default.

Every proposed action must first pass an admissibility decision
at the moment it becomes real.



## Model

Let:

- S = state space  
- A = action space  
- C = constraint set  
- s ∈ S = current state  
- a ∈ A = proposed action  

The key challenge is not defining S, A, or C in isolation.

It is evaluating the effect of a ∈ A on S
and enforcing constraints C exactly at the point of state transition.


## Core Mapping
(s, a, C) → Adm(s, a, C) → execution


## Admissibility
Adm(s, a, C) ∈ {allow, constrain, block}


## Execution Rule
execute(a) ⇔ Adm(s, a, C) ∈ {allow, constrain}


## Interpretation
Traditional systems assume execution and validate afterward.

This model inverts that assumption:

An action does not become real unless it is admissible.

This shift control from:
- observing behavior
to
- constraining state transitions


## Decision Function
D(s, a, C) =
allow if no constraint is violated
constrain if violations are controllable
block otherwise


## Operational Flow

1. propose action a  
2. compute next state s' = f(s, a)  
3. evaluate constraints C(s', a)  
4. compute Adm(s, a, C)  
5. execute based on decision  


## Pseudocode

```pseudo
function runtime_control(s, a, C):

    s_prime = f(s, a)

    violations = evaluate_constraints(s_prime, a, C)

    if violations == ∅:
        return allow(a)

    if can_mitigate(violations):
        return constrain(apply_constraints(a, violations))

    return block(a)
