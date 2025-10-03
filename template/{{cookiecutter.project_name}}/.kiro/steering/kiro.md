---
inclusion: fileMatch
fileMatchPattern: ".kiro/**/*.md"
---
# Specification Standards

## Guiding Principles

- Use Simplicity First (SF) principle - choose simplest viable solution
- Apply Readability Priority (RP) for human and AI understanding
- Maintain consistent naming conventions and terminology
- Align specifications with hexagonal architecture patterns
- Reference domain models as the foundation for all specifications

### Functional Specifications

- Detailed behavior
- Business logic requirements mapped to domain services
- Integration patterns with ports and adapters
- Error handling and validation requirements

### Data Model Specifications

- Model definitions
- DB table design and access patterns
- Entity relationships and business constraints

### AWS Service Integration Specifications

- Step Functions workflow definitions defined in mermaid diagram
- Lambda function signature with hexagonal architecture
- Data flow specifications

## Documentation Format

- Include Mermaid diagrams for visual clarity
- Reference hexagonal architecture layers explicitly

### Design Phase Best Practices

**Design Structure:**

- Start with high-level architecture diagram showing all components (Services, Adapters, External Services)
- Include sequence diagrams to show workflow interactions
- Use correct technology implementations (verify with MCP servers when available)
- Remove full implementation details - focus on high-level design concepts
- Use domain models instead of primitive types in method signatures

**Architecture Principles:**

- Follow hexagonal architecture with clear separation of concerns
- Design services to use domain models as parameters and return types
- Use prompt templates from txt files, not hardcoded strings
- Design for dependency injection and testability

### Tasks Phase Best Practices

**Task Organization:**

- Follow hexagonal architecture layers from inside out: Models → Adapters → Services → Lambdas → Infrastructure
- Include integration tests within each task, not as separate tasks
- Structure tasks as: Implementation + Integration Tests in same task

**Task Sequence:**

1. **Models**: Create domain models with validation
2. **Adapters + Integration Tests**: Implement adapters with real AWS service integration tests
3. **Services + Integration Tests**: Implement services with multi-agent architecture and integration tests
4. **Lambdas + Local Integration Tests**: Implement Lambda handlers with local integration tests
5. **Infrastructure + Deployed Integration Tests**: Deploy CDK stacks and run deployed integration tests
6. **Cleanup**: Remove deprecated services and files
7. **Documentation**: Update README and other documentation
8. **End-to-End Validation**: Complete system testing
