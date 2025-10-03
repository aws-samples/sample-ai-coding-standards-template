---
inclusion: fileMatch
fileMatchPattern: "**/*.py"
---

# Python Development Standards

## Environment Management

- Always use uv in place of pip, pyenv, and virtualenv for all Python environment management
- Use uv for package installation, virtual environment creation, and dependency management
- Standardize on uv for consistent Python version management across projects

## Code Style

- Use English for all code and documentation
- Follow PEP8 style guide consistently
- Use type hints for all variables and functions
- Group imports logically: standard library, third-party, local

## Path Management

- Use `pathlib.Path` for all path operations
- Import path constants from `config_path.py` when working with files
- Never use hardcoded paths in code
- **Reference Implementation**: See `infrastructure/config_path.py` and `src/config_path.py` in template

## Model-Driven Development

- Define domain models as the foundation of application design
- Use Pydantic models for all data structures with validation
- Implement model inheritance hierarchies for related concepts
- **Reference Implementation**: See `src/shared/domain/models/greeting.py` for proper model pattern:
  - Modern Pydantic v2 syntax with `ConfigDict`
  - Proper datetime handling with timezone awareness
  - Field validation and descriptions
  - Business logic methods within models
- Validate models at system boundaries
- Transform external data to domain models in adapters

## Class Design Principles

- Apply Single Responsibility Principle - each class should have only one reason to change
- Implement SOLID principles throughout your class hierarchy
- Use Dependency Injection for easier testing and component replacement
- Favor composition over inheritance for more flexible designs
- Create thin wrappers around external service clients for better abstraction
- Design for idempotency, especially when integrating with external services
- Implement proper logging and observability within class methods

## Service Adapter Pattern

**Reference Implementation**: Study these template files:

- `src/shared/adapters/greetings_storage.py` - DynamoDB adapter implementation
- `src/shared/adapters/hello_world_adapter.py` - Simple adapter example
- `src/shared/ports/greeting_port.py` - Port interface definition

Key principles:

- Implement adapters for all external service interactions
- Use dependency injection for all adapters
- Handle errors consistently within adapters
- Transform external responses to domain models
- Use centralized configuration for all configuration values
- Test adapters with mock clients

## Function Design

- Keep functions short and single-purpose (under 20 lines)
- Use descriptive function and variable names
- Implement proper error handling for external interactions
- Create specific exception classes for different error scenarios
- Consider asynchronous patterns for I/O-bound operations

## Data Management

- Use Pydantic or similar libraries for input validation
- Implement Input Validation (IV) for all external data
- Use Constants Over Magic Values (CMV) - avoid magic strings/numbers

## Implementation Guidelines

- Use duck typing rather than explicit interface checking
- Apply functional programming concepts where appropriate
- Leverage Python's built-in features (context managers, decorators)
- Implement design patterns appropriate to the problem:
  - Factory Method for flexible object creation
  - Strategy pattern using first-class functions
  - Decorator pattern for extending functionality
  - Context Managers for resource handling
- Design service integration classes with clear boundaries and responsibilities

## Import Management

**Reference Implementation**: The template uses Python's native packaging features through `setup.py` and `pyproject.toml` to manage imports cleanly across all deployment scenarios.

**Project Setup**: See template packaging files:

- `setup.py` - Project root setup with namespace packages
- `src/shared/setup.py` - Shared package setup with dependencies
- `pyproject.toml` - Tool configuration with Python paths

**Usage Pattern**: See `src/functions/hello_world/handler.py` for correct import pattern:

```python
# Clean imports that work in all environments
from domain.services.hello_world_service import HelloWorldService
```

**Key Benefits**:

- Native Python packaging without custom import logic
- Full IDE support with autocomplete and static analysis
- Clean import statements without path manipulation
- Consistent behavior across development and deployment

**Build Process**: See `infrastructure/scripts/lambda_build.py` for:

- Inline deployment copies shared code directly to function root
- No `shared/` prefix needed in imports
- Standard Python packaging for layers

## Documentation

- Add docstrings for all public classes and methods
- Document complex algorithms and business logic
- Update documentation when implementing changes

- Use duck typing rather than explicit interface checking
- Apply functional programming concepts where appropriate
- Leverage Python's built-in features (context managers, decorators)
- Implement design patterns appropriate to the problem:
  - Factory Method for flexible object creation
  - Strategy pattern using first-class functions
  - Decorator pattern for extending functionality
  - Context Managers for resource handling
- Design service integration classes with clear boundaries and responsibilities

## Documentation

- Add docstrings for all public classes and methods
- Document complex algorithms and business logic
- Update documentation when implementing changes
