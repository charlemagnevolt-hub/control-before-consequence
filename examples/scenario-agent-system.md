# Scenario: Agent Action Under Runtime Control

## Context

An autonomous agent operates within a system and is allowed to:
- read system state
- propose actions
- execute changes

The system is subject to constraints:
- stability must be preserved
- certain state transitions are non-admissible
- side effects must remain bounded


## Situation

Current state:
s ∈ S

The agent proposes an action:
a ∈ A

Example:
→ modify a configuration
→ trigger a workflow
→ scale a subsystem


## Traditional Approach

The system executes the action.

After execution:
- logs are generated
- anomalies may be detected
- remediation may follow

Problem:
The system may already be in a non-admissible state.


## Runtime Control Approach

Before execution, the system evaluates:

s' = f(s, a)

→ What state would result if the action is executed?

Then:

Adm(s, a, C) is resolved at runtime.


## Decision

Three possible outcomes:

1. allow(a)
   → action is safe
   → execution proceeds

2. constrain(a)
   → action is modified
   → execution proceeds within bounds

3. block(a)
   → action is rejected
   → no state transition occurs


## Key Difference

The system does not rely on:
- detecting violations after execution
- adapting behavior over time

Instead, it ensures:

> Non-admissible states are never entered.


## Insight

Control is not applied to behavior after it happens.

It is applied to the **possibility of behavior**
at the moment it becomes real.


## Implication

As systems become more autonomous:

The critical capability is not:
→ generating better actions

But:
→ preventing invalid state transitions from ever materializing
