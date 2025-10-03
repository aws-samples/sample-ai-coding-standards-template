# Architecture Decision Records (ADR) Standards

## Purpose

- Document architectural decisions using structured ADR format
- Capture context, decision rationale, and consequences
- Align with Industry Standards Adherence (ISA)

## ADR Structure

- Title: Concise description of the architectural decision
- Status: Proposed, Accepted, Deprecated, or Superseded
- Context: Background information and constraints
- Decision: The architectural choice made and its justification
- Consequences: Positive and negative outcomes
- Alternatives Considered: Other options evaluated and why rejected

## File Naming and Organization

- Store ADRs in `/docs/adr/` directory
- Name files using the format: `NNNN-title-with-hyphens.md` (e.g., `0001-use-postgresql-database.md`)
- Number ADRs sequentially starting from 0001

## Best Practices

- Maintain ADRs as living documents that evolve with architecture
- Use Atomic Changes (AC) when updating ADRs to improve traceability
- Link related ADRs to show decision dependencies and evolution
- Do not implement code inside ADR, only class and method signature with comments
- Use Mermaid diagrams if needed, you have MCP Server to help you
- Do not hallucinate and only create content following giving informations
- Each ADR has to be generic and usable in other projects, so do not include project specificity, you have to generalize
