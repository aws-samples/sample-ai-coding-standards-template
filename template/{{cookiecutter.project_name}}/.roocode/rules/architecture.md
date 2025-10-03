# Architecture Standards

## Design Principles

- Follow fundamental principles: separation of concerns, single responsibility, DRY, KISS, SOLID
- Prioritize simplicity over complexity for maintainable designs
- Implement Clean Architecture with clearly separated layers
- Structure codebase to minimize dependencies and maximize testability
- Use modular design with loose coupling and high cohesion
- Perform continuous architectural refactoring to prevent technical debt
- Emphasize patterns, domain models, and integration points over detailed specifications

## Core Principles

- **Essential Architecture Only**: Focus on architectural decisions that matter, delegate implementation details to patterns
- **Framework Delegation**: Leverage AWS service defaults and built-in capabilities instead of custom implementations
- **Iterative Refinement**: Start simple and add complexity only when proven necessary
- **Clear Boundaries**: Maintain clean architectural boundaries with minimal implementation complexity

### Design Document Approach

- **Pattern Application**: List applied patterns with rationale, avoid pattern proliferation
- **Essential Information Only**: Remove detailed configuration explanations, cost-effectiveness discussions, and comprehensive error handling specifications that can be inferred from pattern application
- **Delegate Implementation Details**: Let established patterns handle specifics rather than documenting every configuration option
- **Focus on Business Value**: Emphasize what the architecture achieves rather than how every component works

### Code Implementation

- **Minimal Viable Implementation**: Implement the simplest solution that meets requirements
- **Framework Defaults**: Use AWS service defaults unless specific requirements demand customization
- **Progressive Enhancement**: Add features incrementally based on actual needs
- **Clean Architecture**: Maintain hexagonal architecture boundaries without over-abstraction

### Error Handling Strategy

- **Framework Delegation**: Use AWS Services default error handling and retry logic
- **Fail Fast**: Avoid complex error recovery logic unless proven necessary

### Testing Approach

- **Essential Tests**: Focus on core business logic and integration points
- **Happy Path Priority**: Ensure main workflows work correctly
- **Framework Trust**: Trust AWS services to handle their responsibilities

## Complexity Decision Framework

### When to Add Complexity

Only add architectural complexity when:

1. **Actual Problems Exist**: Current simple solution has measurable problems
2. **Business Value Clear**: Complexity provides clear, measurable business value
3. **Alternatives Exhausted**: Simpler solutions have been tried and proven inadequate
4. **Maintenance Acceptable**: Team can maintain the additional complexity long-term

### Complexity Budget

- **Track Complexity**: Maintain awareness of system complexity levels
- **Justify Additions**: Require clear justification for each complexity addition
- **Regular Review**: Periodically review if complexity is still needed
- **Simplification Opportunities**: Look for opportunities to remove unnecessary complexity

## Common Anti-Patterns to Avoid

### Over-Engineering

- **Premature Optimization**: Adding complexity for theoretical performance gains
- **Pattern Proliferation**: Applying multiple patterns without clear need
- **Custom Implementations**: Building custom solutions when framework capabilities exist
- **Comprehensive Upfront Design**: Detailed specifications that become outdated

### Under-Engineering

- **No Architecture**: Avoiding all patterns and structure
- **Framework Ignorance**: Not understanding framework capabilities and limitations
- **Technical Debt Accumulation**: Never refactoring simple solutions as they grow
- **Monitoring Neglect**: Not monitoring system health and performance

## Hexagonal Architecture

### Architecture Layers

**Domain Layer**: `src/shared/domain/`

- `models/greeting.py` - Core business models and rules
- `services/greeting_service.py` - Business logic orchestration

**Ports Layer**: `src/shared/ports/`

- `greeting_port.py` - Interfaces for external communication

**Adapters Layer**: `src/shared/adapters/`

- `greetings_storage.py` - DynamoDB adapter implementation
- `hello_world_adapter.py` - Simple adapter example

**Functions Layer**: `src/functions/`

- `hello_world/handler.py` - Lambda handler (primary adapter)

### Key Principles

- Organize code using ports and adapters pattern (hexagonal architecture)
- Separate core business logic from external dependencies
- Define clear boundaries between domains using explicit interfaces
- Use dependency injection for all adapters to enable testability
- Ensure business logic has no dependencies on infrastructure code
- Design for technology independence and replaceability

## Model-Driven Architecture

**Reference Implementation**: See `src/shared/domain/models/greeting.py` for:

- Starting design with domain models before implementing services or handlers
- Using models as the foundation for all data structures
- Implementing model validation at system boundaries
- Proper Pydantic v2 usage with ConfigDict
- Business logic methods within models

### Service Interface Design

**Reference Implementation**: See `src/shared/domain/services/greeting_service.py` for:

- Accepting domain models directly as parameters
- Returning domain models from service methods
- Type safety through model validation
- Consistent object-oriented design principles
- Centralized model logic

## Code Organization

**Reference Implementation**: Study the template structure for:

- Dependency Minimalism (DM) - justified library usage
- Logical file structure (components, helpers, types)
- DRY Principle implementation
- Code Smell Detection (CSD) patterns:
  - Functions under 30 lines
  - Files under 300 lines
  - Conditionals nested max 2 levels
  - Classes with max 5 public methods
- Robust Error Handling (REH) for all edge cases

## Configuration Management

**Reference Implementation**: See `src/shared/config.py` for:

- Centralized approach for configuration management
- Single source of truth for configuration values
- Flexible configuration through environment variables
- Consistent client initialization across services
- Structure files logically (components, helpers, types)
- Apply DRY Principle to eliminate duplicate code
- Implement Code Smell Detection (CSD):
  - Functions under 30 lines
  - Files under 300 lines
  - Conditionals nested max 2 levels
  - Classes with max 5 public methods
- Apply Robust Error Handling (REH) for all edge cases

## Configuration Management

- Use centralized approach for configuration management
- Maintain single source of truth for configuration values
- Enable flexible configuration through environment variables
- Ensure consistent client initialization across services
