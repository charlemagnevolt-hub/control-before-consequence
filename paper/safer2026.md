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

[TBD]

### 4.2 Policy Engine

[TBD]

### 4.3 Approval Queue

[TBD]

### 4.4 Reference Applications

[TBD]

## 5. Runtime Admissibility Threat Model

[TBD]

## 6. Implications for a Trustworthy Agentic AI Roadmap

[TBD]

## 7. Discussion and Limitations

[TBD]

## 8. Conclusion

[TBD]

## References

