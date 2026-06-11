# Control Before Consequence:

## Runtime Admissibility for Safe Agentic AI Systems

### Abstract

[TBD]

## 1. Introduction

[TBD]

## 2. Limitations of Current Governance Paradigms

[TBD]

## 3. Control Before Consequence

### 3.1 From Observation to Intervention

The governance of AI systems has traditionally focused on observation, monitoring, auditing, and post-hoc accountability. These mechanisms remain essential, but they are increasingly insufficient for agentic systems capable of initiating externally consequential actions.

As AI systems evolve from information-processing systems into action-producing systems, governance must extend beyond observing outcomes and toward controlling execution. The critical challenge is no longer limited to understanding what an AI system generated, but determining whether a proposed action should be permitted to affect the external world.

This shift represents a transition from observational governance toward intervention-oriented governance. Rather than evaluating actions after consequences occur, safe agentic systems require mechanisms capable of evaluating admissibility before execution.

The central question therefore becomes:

> Under what conditions should an AI-generated action be allowed to become consequential?

This question defines a new control problem for agentic AI systems.

### 3.2 Runtime Admissibility

We introduce Runtime Admissibility as the decision process that determines whether a proposed action may become externally consequential under the current constraints.

Runtime admissibility operates at the boundary between agent reasoning and action execution. It evaluates a proposed action against the current system state and the applicable constraints before execution is permitted.

Unlike traditional guardrails, which primarily focus on inputs, outputs, or generated content, runtime admissibility focuses on execution itself. The objective is not to determine whether generated content is acceptable, but whether a proposed action should be allowed to cause a state transition in the external environment.

Runtime admissibility therefore introduces an explicit execution-control boundary between agent cognition and consequential action.

Within the Control Before Consequence framework, no externally consequential action should execute before admissibility has been resolved.

This principle establishes runtime admissibility as a foundational capability for safe and trustworthy agentic AI systems.

### 3.3 Formal Model

Runtime admissibility can be represented as a decision function operating over system state, proposed actions, and applicable constraints.

Let:

```text
s ∈ S
```

denote the current system state,

```text
a ∈ A
```

denote a proposed action,

and

```text
C
```

denote the applicable constraint set.

Runtime admissibility is defined as:

```text
Adm : S × A × C → D
```

where:

```text
D = {ALLOW, BLOCK, REQUIRE_APPROVAL}
```

The admissibility function evaluates whether a proposed action may become externally consequential under the current constraints.

Execution is permitted only if admissibility evaluates to ALLOW:

```text
execute(a) ⇔ Adm(s,a,C) = ALLOW
```

Consequently:

```text
Adm(s,a,C) ≠ ALLOW
```

implies:

```text
¬execute(a)
```

This formulation establishes a formal execution-control boundary between agent reasoning and externally consequential actions.

### 3.4 Decision Space

The admissibility decision space consists of three possible outcomes.

#### ALLOW

The proposed action satisfies the applicable constraints and may execute immediately.

#### BLOCK

The proposed action violates one or more constraints and must not execute.

#### REQUIRE_APPROVAL

The proposed action cannot be automatically admitted and requires human or supervisory review before execution.

The decision space can therefore be represented as:

```text
D = {ALLOW, BLOCK, REQUIRE_APPROVAL}
```

This structure separates admissibility evaluation from execution and creates an explicit control layer between agent cognition and consequential action.

The Control Before Consequence principle can therefore be expressed as:

```text
∀a : execute(a) ⇒ Adm(s,a,C) = ALLOW
```

In other words:

> No externally consequential action should execute unless admissibility has been explicitly resolved.

## 4. Runtime Admissibility Gate MVP

### 4.1 Architecture

To demonstrate the practical applicability of runtime admissibility, we implemented a lightweight Runtime Admissibility Gate MVP.

The prototype introduces an execution-control boundary between an AI agent and externally consequential actions.

The architecture consists of four primary components:

1. Proposed Action
2. Policy Engine
3. Execution Decision
4. Decision Ledger

The execution flow is illustrated below:

```text
AI Agent
      ↓
Proposed Action
      ↓
Admissibility Evaluation
      ↓
ALLOW / BLOCK / REQUIRE_APPROVAL
      ↓
Execution Decision
      ↓
Ledger Record
```

The gate evaluates admissibility before execution occurs.

Only actions that satisfy admissibility requirements may proceed to execution.

Actions that violate constraints are blocked, while actions requiring additional review are suspended pending approval.

The objective of the MVP is not to provide a complete governance platform but to demonstrate the execution-control boundary proposed by the Control Before Consequence framework.

### 4.2 Policy Engine

The policy engine represents the decision-making component of the Runtime Admissibility Gate.

It evaluates proposed actions against applicable constraints and produces one of three admissibility decisions:

* ALLOW
* BLOCK
* REQUIRE_APPROVAL

The policy engine serves as the implementation layer of the runtime admissibility function:

```text
Adm(s,a,C)
```

Within the MVP, policy evaluation is intentionally simple and transparent.

The purpose is not to optimize policy complexity but to demonstrate how admissibility decisions can be enforced before execution.

Different action types may be evaluated using different policies while sharing the same admissibility decision space.

This design allows the framework to scale across heterogeneous actions while maintaining a consistent execution-control model.

### 4.3 Approval Queue

The Runtime Admissibility Gate may return a decision of REQUIRE_APPROVAL.

In the current MVP, actions requiring approval are suspended and not executed.

Conceptually, a future approval queue would store pending actions until a human or supervisory process resolves the admissibility decision.

The approval flow can be represented as:

```text
Proposed Action
      ↓
Admissibility Evaluation
      ↓
REQUIRE_APPROVAL
      ↓
Approval Queue
      ↓
Human Review
      ↓
ALLOW / BLOCK
      ↓
Execution Decision
      ↓
Execute / Stop
      ↓
Ledger Record
```

The approval queue does not replace runtime admissibility.

Instead, it extends the REQUIRE_APPROVAL branch of the admissibility decision space.

Actions that cannot be automatically admitted are temporarily suspended until additional review is completed.

This mechanism allows governance controls to intervene before externally consequential actions occur.

### 4.4 Reference Applications

The MVP currently implements three reference applications that demonstrate runtime admissibility across different classes of consequential actions.

#### Email Actions

The first reference application evaluates email actions.

Examples include:

* internal communication
* external communication
* sensitive information transfer

Depending on the context, the admissibility gate may allow, block, or require approval before execution.

#### Record Updates

The second reference application evaluates record modification actions.

Examples include:

* customer record updates
* operational data modifications
* workflow state changes

Higher-risk modifications may require approval before execution.

#### API Calls

The third reference application evaluates API invocation requests.

Examples include:

* service integrations
* workflow orchestration
* external system interactions

Risk-sensitive API calls may require approval before execution.

Together, these examples demonstrate that runtime admissibility is not limited to a single action type but can be applied consistently across heterogeneous consequential actions.

The purpose of these reference applications is not to provide production functionality but to make the execution-control boundary observable and testable in code.

## 5. Runtime Admissibility Threat Model

[TBD]

## 6. Implications for a Trustworthy Agentic AI Roadmap

[TBD]

## 7. Discussion and Limitations

[TBD]

## 8. Conclusion

[TBD]

## References

