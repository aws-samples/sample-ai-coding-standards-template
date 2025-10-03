# {{cookiecutter.project_name}}

A CDK Python Lambda project using hexagonal architecture with integration tests

## Architecture

This project implements **Hexagonal Serverless Architecture** (also known as Ports and Adapters pattern), which ensures clean separation of concerns and high testability in serverless applications.

### What is Hexagonal Serverless Architecture?

Hexagonal architecture organizes code into three main layers:

1. **Inner Layer (Domain)**: Pure business logic, independent of external systems
2. **Middle Layer (Ports)**: Interface contracts defining how the domain interacts with external systems
3. **Outer Layer (Adapters)**: Concrete implementations that connect to external systems (databases, APIs, file systems)

### Class Roles and Responsibilities

#### 1. **Port Classes** (`ports/`)

**Role**: Interface contracts that define operations without implementation

```python
# Example: GreetingPort
class GreetingPort(ABC):
    @abstractmethod
    def save_greeting(self, name: str, greeting: str) -> None:
        pass

    @abstractmethod
    def get_saved_greeting(self, name: str) -> str:
        pass
```

**Why Important**:

- ✅ **Defines contracts** - What operations are available
- ✅ **Enables dependency inversion** - Services depend on abstractions, not concrete implementations
- ✅ **Facilitates testing** - Easy to create mock implementations
- ✅ **Promotes flexibility** - Can swap different implementations without changing business logic

#### 2. **Service Classes** (`domain/services/`)

**Role**: Contains business logic and orchestrates domain operations

```python
# Example: GreetingService
class GreetingService:
    def __init__(self, greeting_port: GreetingPort = None):
        self.greeting_port = greeting_port  # Depends on PORT interface

    def get_greeting(self, name: str) -> str:
        # Business logic here
        return self.greeting_port.get_saved_greeting(name)
```

**Why Important**:

- ✅ **Pure business logic** - No external dependencies, only domain concepts
- ✅ **Testable** - Easy to unit test with mock ports
- ✅ **Reusable** - Can be used across different Lambda functions
- ✅ **Maintainable** - Changes to external systems don't affect business logic

#### 3. **Adapter Classes** (`adapters/`)

**Role**: Concrete implementations that connect to external systems

```python
# Example: GreetingsStorage (DynamoDB Adapter)
class GreetingsStorage(GreetingPort):  # IMPLEMENTS the port
    def __init__(self):
        self.table_name = config.get_required(config.HELLO_WORLD_TABLE_NAME)
        self.table = boto3.resource("dynamodb").Table(self.table_name)

    def save_greeting(self, name: str, greeting: str) -> None:
        # DynamoDB-specific implementation
        self.table.put_item(Item={"name": name, "message": greeting})

    def get_saved_greeting(self, name: str) -> str:
        # DynamoDB-specific implementation
        response = self.table.get_item(Key={"name": name})
        return response.get("Item", {}).get("message", f"Hello, {name}!")
```

**Why Important**:

- ✅ **External system integration** - Handles databases, APIs, file systems
- ✅ **Swappable implementations** - Can switch from DynamoDB to S3 to Redis
- ✅ **Error handling** - Manages external system failures
- ✅ **Technology isolation** - AWS-specific code stays in adapters

#### 4. **Model Classes** (`domain/models/`)

**Role**: Domain entities that represent core business concepts

```python
# Example: Greeting model
@dataclass
class Greeting:
    name: str
    message: str
    created_at: datetime
    updated_at: Optional[datetime] = None
```

**Why Important**:

- ✅ **Data validation** - Ensures data integrity
- ✅ **Business rules** - Encapsulates domain logic
- ✅ **Type safety** - Provides clear data contracts
- ✅ **Immutability** - Prevents accidental data modifications

### Benefits of Hexagonal Serverless Architecture

1. **Testability**: Easy to mock external dependencies
2. **Maintainability**: Changes to external systems don't affect business logic
3. **Flexibility**: Can swap implementations (DynamoDB → S3 → Redis)
4. **Scalability**: Services can be reused across multiple Lambda functions
5. **Clean Code**: Clear separation of concerns

## Configuration Management

This project uses a centralized configuration service (`config/config_service.py`) to manage all configuration values:

```python
# Example usage in adapters
from config.config_service import config

table_name = config.get_required(config.HELLO_WORLD_TABLE_NAME)
```

Benefits:

- ✅ Centralized configuration management
- ✅ Strong validation with no fallbacks
- ✅ Clear error messages for missing configuration
- ✅ Type-safe configuration access

## Resource Discovery

AWS resources are discovered using tags, making tests work with real AWS resources:

```python
# Example in tests
from tests.utils.resource_discovery import get_dynamodb_table_name

table_name = get_dynamodb_table_name("GreetingsTable")
```

Benefits:

- ✅ No mocking of AWS services
- ✅ Tests run against real infrastructure
- ✅ Resource discovery by tags
- ✅ Clean test setup with fixtures

## Quick Start

Install [taskfile.dev](https://taskfile.dev/) and [uv](https://docs.astral.sh/uv/)

1. **Set up development environment**:

   ```bash
   task setup
   ```

2. **Set up infrastructure environment and build Lambda functions**:

   ```bash
   task cdk:setup
   task cdk:build
   ```

3. **Deploy to AWS**:

   ```bash
   task cdk:deploy
   ```

4. **Set up test environment and run tests**:

   ```bash
   task test:setup
   task test:all
   ```

## Template Updates

Keep your project synchronized with template improvements:

```bash
# Automated template updates with conflict resolution
task cruft:update
```

**Features:**

- ✅ **No manual intervention** - Fully automated conflict resolution
- ✅ **Always succeeds** - Never blocks your workflow

The automation uses intelligent patching with multiple fallback strategies and always leaves your workspace clean.

## Project Structure

```bash
{{cookiecutter.project_name}}/
├── src/
│   ├── config_path.py       # Source path configuration
│   ├── shared/              # Shared code
│   │   ├── domain/          # Business logic and models
│   │   ├── ports/           # Interfaces
│   │   └── adapters/        # External system implementations
│   ├── functions/           # Lambda functions
│   └── tests/               # Tests
├── infrastructure/
│   ├── config_path.py       # Infrastructure path configuration
│   ├── scripts/             # Build and deployment scripts
│   ├── stacks/             # CDK stacks
│   └── tests/              # Infrastructure tests
├── docs/                    # Documentation system
│   ├── mkdocs.yml          # MkDocs configuration
│   ├── requirements.txt    # Documentation dependencies
│   ├── Taskfile.yml        # Documentation tasks
│   └── assets/             # Documentation assets
├── dist/                    # Build artifacts
├── Taskfile.yml            # Task definitions
└── README.md
```

## Documentation

This project includes a comprehensive documentation system built with MkDocs and mkdocstrings that automatically generates API documentation from Python docstrings, organized by hexagonal architecture layers.

### Quick Start

```bash
# Set up documentation environment
task docs:setup

# Build documentation
task docs:build

# Serve documentation locally with hot reload
task docs:serve

# Open your browser to http://127.0.0.1:8000
```

### Available Documentation Tasks

| Task | Description |
|------|-------------|
| `task docs:setup` | Set up documentation environment |
| `task docs:build` | Build static documentation |
| `task docs:serve` | Serve documentation locally with hot reload |
| `task docs:dev` | Development mode with auto-reload |
| `task docs:clean` | Clean generated documentation files |
| `task docs:validate` | Validate built documentation |
| `task docs:gitlab` | Prepare for GitLab Pages deployment |
| `task docs:all` | Complete workflow: setup, validate, build, and check |

## Development

This project uses [Taskfile](https://taskfile.dev/) for task automation:

- `task setup`: Set up development environment
- `task cdk:setup`: Set up infrastructure environment and dependencies
- `task cdk:build`: Build Lambda functions
- `task cdk:deploy`: Deploy to AWS
- `task cdk:destroy`: Destroy AWS resources
- `task cdk:synth`: Synthesize CloudFormation templates
- `task test:setup`: Set up test environment
- `task test:test`: Run all tests
- `task docs:serve`: Serve documentation locally
- `task lint`: Run linters
- `task clean`: Clean build artifacts

## Author

{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
