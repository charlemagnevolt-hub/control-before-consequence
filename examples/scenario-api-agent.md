# Scenario: LLM Agent Calling an External API

## Context

An LLM-based agent is connected to external tools.

It can:
- read user intent
- call APIs
- modify records
- trigger workflows
- send requests to external systems

The system is no longer only generating text.

It is causing state transitions.


## Situation

A user asks the agent:

> "Update the customer account and notify the operations team."

The agent proposes an action:

a ∈ A

Example:
→ update customer status  
→ write to CRM  
→ trigger notification  
→ create downstream workflow  


## Traditional Approach

The agent executes the API call.

After execution:
- logs record what happened
- monitoring may detect anomalies
- humans may review the outcome
- remediation may follow

Problem:

The state transition already happened.

If the action was incorrect, unauthorized, or high-impact,
the system has already entered a potentially non-admissible state.


## Runtime Control Approach

Before the API call is committed, the system evaluates:

- What object will be changed?
- Which permissions apply?
- What downstream workflows will be triggered?
- Is the action reversible?
- Does the action violate any constraint?

The proposed action is mapped against the current system state and constraint set:

Adm(s, a, C)


## Decision

Three outcomes are possible:

### 1. allow(a)

The action is admissible.

The API call is executed.

### 2. constrain(a)

The action is partially admissible.

The system modifies the action before execution.

Example:
- update internal status
- but do not notify external parties
- require human confirmation for high-impact changes

### 3. block(a)

The action is non-admissible.

No API call is executed.

The state transition never occurs.


## Key Difference

The critical control point is not after the API call.

It is before the action becomes real.

Runtime control turns execution into a conditional process:

> No action is committed unless it is admissible.


## Insight

For agentic systems, API access is not just integration.

It is a control boundary.

Every external call is a potential state transition.

And every state transition needs an admissibility decision before it happens.


## Implication

As LLM agents gain access to tools, databases, workflows, and infrastructure,
the central question becomes:

> What is the system allowed to change?

Not in theory.

At runtime.
