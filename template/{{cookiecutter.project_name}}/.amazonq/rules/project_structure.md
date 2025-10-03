# Project Structure Standards

## Directory Organization

- Organize projects with clear separation of concerns
- Use consistent directory naming conventions across projects
- Maintain a flat structure where possible to avoid deep nesting
- Group related files by feature or domain rather than by file type

## Reference Implementation

Study the project structure for the canonical implementation of these standards.

## Standard Project Layout

**Reference Implementation**: The template provides this exact structure:

```text
project-root/
├── README.md
├── Taskfile.yml
├── pyproject.toml
├── src/
│   ├── config_path.py       # Source-specific path configuration
│   ├── shared/              # Shared code
│   │   ├── config.py        # Configuration management
│   │   ├── domain/          # Business logic and coordination
│   │   │   ├── models/      # Pydantic models (Greeting, etc.)
│   │   │   └── services/    # Business services and coordination logic
│   │   ├── ports/           # Interfaces (GreetingPort, etc.)
│   │   └── adapters/        # AWS integrations (DynamoDB, S3, SQS)
│   ├── functions/           # Lambda functions
│   │   └── hello_world/
│   │       ├── handler.py   # Lambda entry point
│   │       └── requirements.txt
│   └── tests/               # Test code
│       ├── conftest.py      # Test fixtures and configuration
│       ├── integration/     # Integration tests with real AWS services
│       │   ├── adapters/    # Adapter integration tests
│       │   ├── functions/   # Function integration tests
│       │   ├── services/    # Service integration tests
│       │   └── test_*_model.py  # Model integration tests
│       ├── utils/           # Test utilities
│       └── payloads/        # Test data for Lambda functions
├── infrastructure/
│   ├── config_path.py       # Infrastructure-specific path configuration
│   ├── lambda_factory.py    # Lambda function factory
│   ├── scripts/             # Build and deployment scripts
│   │   └── lambda_build.py  # Lambda build script
│   ├── stacks/              # CDK stacks
│   │   └── hello_world_stack.py
│   └── tests/               # Infrastructure tests
└── dist/                    # Build artifacts
    ├── layers/              # Packaged Lambda layers
    ├── shared/              # Packaged shared code
    └── functions/           # Packaged Lambda functions
```

## Component Organization

### Domain Layer

**Reference Implementation**: See template `src/shared/domain/`

- **Models**: `src/shared/domain/models/greeting.py` - Pydantic models with validation rules
- **Services**: `src/shared/domain/services/greeting_service.py` - Business logic and coordination

### Ports Layer

**Reference Implementation**: See template `src/shared/ports/greeting_port.py`

- Define interfaces for external dependencies
- Abstract contracts for external dependencies

### Adapters Layer

**Reference Implementation**: See template `src/shared/adapters/`

- `greetings_storage.py` - DynamoDB implementation
- `hello_world_adapter.py` - Simple adapter example
- AWS service integrations

### Functions Layer

**Reference Implementation**: See template `src/functions/hello_world/handler.py`

- Lambda handlers with proper import management
- Each function should have its own requirements.txt file
- Use dependency injection at the service level

### Tests Layer

**Reference Implementation**: See template `tests/`

- `conftest.py` - Shared test fixtures
- `integration/` - Tests with real AWS services organized by component type:
  - `adapters/` - Adapter integration tests
  - `functions/` - Function integration tests
  - `services/` - Service integration tests
  - `test_*_model.py` - Model integration tests
- `utils/` - Test utilities and resource discovery
- `payloads/` - Test data for Lambda functions

### Infrastructure Layer

**Reference Implementation**: See template `infrastructure/`

- `stacks/` - CDK stack definitions
- `scripts/` - Build and deployment scripts
- `lambda_factory.py` - Consistent Lambda function creation
- `config_path.py` - Path management for infrastructure

## Path Management

### Centralized Path Configuration

**Reference Implementation**: See template files:

- `src/config_path.py` - Source-specific path configuration
- `infrastructure/config_path.py` - Infrastructure-specific path configuration

Key principles:

- Create separate `config_path.py` files in each major directory
- Use the `from_root` library to ensure paths are always relative to the project root
- Reference these path constants throughout the codebase
- Never use hardcoded paths or relative path calculations in application code

### Implementation Example

**Reference Implementation**: Study the template `config_path.py` files for:

- Project root and main directories configuration
- Lambda-specific paths
- Test paths
- Infrastructure paths
- Distribution paths

### Usage in Code

**Reference Implementation**: See how template files use path constants:

- Lambda handlers importing from shared code
- Infrastructure stacks referencing build artifacts
- Tests accessing test data and fixtures

### Benefits of Centralized Path Management

- **Consistency**: All paths are defined in one place per directory
- **Maintainability**: Path changes only need to be made in one file
- **Reliability**: Eliminates path-related errors across different environments
- **Clarity**: Makes path relationships explicit and self-documenting
- **Portability**: Works across different operating systems
- **IDE Support**: Better code completion and navigation

### Path Management Rules

- **No Hardcoded Paths**: Never use hardcoded absolute or relative paths in code
- **No Path Calculation**: Avoid manual path calculation with string concatenation
- **Use Path Objects**: Always use `pathlib.Path` objects for path manipulation
- **Import from Root**: Import path constants from the appropriate `config_path.py` module
- **Path Constants**: Define all paths as uppercase constants
- **Path Documentation**: Document the purpose of each path constant

### Integration with Build Process

**Reference Implementation**: See template `infrastructure/scripts/lambda_build.py` for:

- Using path constants in build scripts and Taskfiles
- CI/CD pipelines referencing the same path constants
- Path existence validation as part of the build process

### Domain Layer

- **Models**: Place all Pydantic models in `src/shared/domain/models/`
  - Business data structures with validation rules
  - Domain events and value objects
  - Example: User, Order, Product models

- **Services**: Place business services in `src/shared/domain/services/`
  - Business logic classes and methods (`UserService`, `OrderService`)
  - Business rules like `calculate_total()`, `validate_email()`, `apply_discount()`
  - Coordination logic for workflows and business processes
  - Use dependency injection for adapters

### Ports Layer

- Define interfaces for external dependencies in `src/shared/ports/`
- Examples:
  - `UserRepository` interface with methods like `save()`, `find_by_email()`
  - `EmailService` interface with `send_welcome_email()`, `send_receipt()`
  - Abstract contracts for external dependencies

### Adapters Layer

- Implement interfaces for external systems in `src/shared/adapters/`
- Examples:
  - DynamoDB implementation of UserRepository
  - SES email implementation of EmailService
  - EventBridge publisher for domain events
  - AWS service integrations

### Functions Layer

- Lambda handlers in `src/functions/{function_name}/`
- Each function should:
  - Convert between API formats and domain Pydantic models
  - Handle incoming requests and orchestrate business operations
  - Have its own requirements.txt file
  - Use dependency injection at the service level, not in handlers

### Tests Layer

- Place all tests in `tests/`
- Organize by test type and component:
  - `integration/`: Tests with real AWS services organized by component type:
    - `adapters/`: Adapter integration tests
    - `functions/`: Function integration tests
    - `services/`: Service integration tests
    - `test_*_model.py`: Model integration tests
  - `payloads/`: Test data for Lambda functions

### Infrastructure Layer

- Place all infrastructure code in `infrastructure/`
- Organize by component type:
  - `stacks/`: CDK or CloudFormation stacks
  - `scripts/`: Build and deployment scripts
  - `tests/`: Tests for infrastructure code

## Path Management

### Centralized Path Configuration

- Create separate `config_path.py` files in each major directory (src/, infrastructure/)
- Use the `from_root` library to ensure paths are always relative to the project root
- Reference these path constants throughout the codebase
- Never use hardcoded paths or relative path calculations in application code

### Implementation Example

```python
# src/config_path.py
from pathlib import Path
from from_root import from_root

# Project root and main directories
PROJECT_ROOT = from_root()
SRC_ROOT = PROJECT_ROOT / "src"

# Lambda-specific paths
LAMBDA_ROOT = SRC_ROOT / "functions"
LAMBDA_SHARED = SRC_ROOT / "shared"
LAMBDA_LAYERS = SRC_ROOT / "layers"

# Test paths
TESTS_ROOT = SRC_ROOT / "tests"
UNIT_TESTS = TESTS_ROOT / "unit"
INTEGRATION_TESTS = TESTS_ROOT / "integration"
TEST_DATA = TESTS_ROOT / "payloads"
```

```python
# infrastructure/config_path.py
from pathlib import Path
from from_root import from_root

# Project root and main directories
PROJECT_ROOT = from_root()
INFRASTRUCTURE_ROOT = PROJECT_ROOT / "infrastructure"
SRC_ROOT = PROJECT_ROOT / "src"
DIST_ROOT = PROJECT_ROOT / "dist"

# Infrastructure paths
CDK_STACKS = INFRASTRUCTURE_ROOT / "stacks"
CDK_CONSTRUCTS = INFRASTRUCTURE_ROOT / "constructs"
SCRIPTS_ROOT = INFRASTRUCTURE_ROOT / "scripts"

# Distribution paths
LAMBDA_DIST = DIST_ROOT / "functions"
LAMBDA_DIST_LAYERS = DIST_ROOT / "layers"
LAMBDA_DIST_SHARED = DIST_ROOT / "shared"
```

### Usage in Code

```python
# In src/functions/example/handler.py
from src.config_path import LAMBDA_SHARED
import sys
sys.path.append(str(LAMBDA_SHARED))

# In infrastructure/stacks/example_stack.py
from infrastructure.config_path import LAMBDA_DIST, LAMBDA_DIST_LAYERS
lambda_code = aws_lambda.Code.from_asset(str(LAMBDA_DIST / "example_function"))
lambda_layer = aws_lambda.LayerVersion.from_asset(str(LAMBDA_DIST_LAYERS / "common"))

# In tests/integration/functions/test_example.py
from src.config_path import TEST_DATA
test_payload = json.loads((TEST_DATA / "example_payload.json").read_text())
```

### Benefits of Centralized Path Management

- **Consistency**: All paths are defined in one place per directory
- **Maintainability**: Path changes only need to be made in one file
- **Reliability**: Eliminates path-related errors across different environments
- **Clarity**: Makes path relationships explicit and self-documenting
- **Portability**: Works across different operating systems
- **IDE Support**: Better code completion and navigation

### Path Management Rules

- **No Hardcoded Paths**: Never use hardcoded absolute or relative paths in code
- **No Path Calculation**: Avoid manual path calculation with string concatenation
- **Use Path Objects**: Always use `pathlib.Path` objects for path manipulation
- **Import from Root**: Import path constants from the appropriate `config_path.py` module
- **Path Constants**: Define all paths as uppercase constants
- **Path Documentation**: Document the purpose of each path constant

### Integration with Build Process

- Use path constants in build scripts and Taskfiles
- Ensure CI/CD pipelines reference the same path constants
- Validate path existence as part of the build process
