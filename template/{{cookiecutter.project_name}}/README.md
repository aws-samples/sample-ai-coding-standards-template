# {{cookiecutter.project_name}}

A CDK Python Lambda project using hexagonal architecture with integration tests and AI assistant configurations.

## Architecture

This project implements **Hexagonal Architecture** (Ports and Adapters pattern) for clean separation of concerns and high testability in serverless applications.

### Architecture Layers

1. **Domain Layer**: Pure business logic with models and services
2. **Ports Layer**: Interface contracts for external dependencies
3. **Adapters Layer**: Concrete implementations for AWS services

### Key Components

#### 1. **Models** (`src/shared/models/`)

Domain entities representing core business concepts:

```python
# Example: HelloWorld model
@dataclass
class HelloWorld:
    name: str
    greeting: str
    created_at: datetime
    updated_at: Optional[datetime] = None
```

**Why Important**: Data validation, business rules, type safety, clear data contracts

#### 2. **Ports** (`src/shared/ports/`)

Interface contracts defining operations:

```python
# Example: HelloWorldPort
class HelloWorldPort(ABC):
    @abstractmethod
    def get_saved_greeting(self, name: str) -> HelloWorld:
        pass

    @abstractmethod
    def save_greeting(self, greeting: HelloWorld) -> None:
        pass
```

**Why Important**: Defines contracts, enables dependency inversion, facilitates testing, promotes flexibility

#### 3. **Services** (`src/shared/domain/services/`)

Business logic orchestration:

```python
# Example: HelloWorldService
class HelloWorldService:
    def __init__(self, hello_world_port: HelloWorldPort = None):
        self.hello_world_port = hello_world_port or HelloWorldStorageAdapter()

    def get_greeting(self, name: str) -> str:
        greeting = self.hello_world_port.get_saved_greeting(name)
        return greeting.formatted_greeting
```

**Why Important**: Pure business logic, testable, reusable, maintainable

#### 4. **Adapters** (`src/shared/adapters/`)

AWS service implementations:

```python
# Example: HelloWorldStorageAdapter (DynamoDB)
class HelloWorldStorageAdapter(HelloWorldPort):
    def __init__(self):
        self.table_name = config.get_required(config.HELLO_WORLD_TABLE_NAME)
        self.table = boto3.resource("dynamodb").Table(self.table_name)

    def get_saved_greeting(self, name: str) -> HelloWorld:
        response = self.table.get_item(Key={"name": name})
        if "Item" in response:
            return HelloWorld.from_dict(response["Item"])
        return HelloWorld(name=name, greeting=None)
```

**Why Important**: External system integration, swappable implementations, error handling, technology isolation

## Quick Start

Install [taskfile.dev](https://taskfile.dev/) and [uv](https://docs.astral.sh/uv/)

```bash
# Set up development environment
task setup

# Set up infrastructure and build Lambda functions
task cdk:setup
task cdk:build

# Deploy to AWS
task cdk:deploy

# Set up tests and run them
task test:setup
task test:all

# Serve documentation locally
task docs:serve
```

## AI Assistant Integration

This project includes pre-configured AI assistant support:

- **Amazon Q Developer** (`.amazonq/`)
- **Cursor AI** (`.cursor/`)
- **Cline** (`.cline/`)
- **Roo Cline** (`.roocode/`)
- **Kiro AI** (`.kiro/`)

Each configuration includes development rules, MCP servers, and project-specific context for better AI assistance.

## Template Updates

Keep your project synchronized with template improvements:

```bash
task cruft:update
```

## Author

{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

## Project Structure

```bash
{{cookiecutter.project_name}}/
├── src/
│   ├── shared/              # Shared code
│   │   ├── models/          # Domain models
│   │   ├── ports/           # Interface contracts
│   │   ├── adapters/        # AWS service implementations
│   │   ├── domain/services/ # Business logic
│   │   └── config/          # Configuration management
│   ├── functions/           # Lambda functions
│   └── tests/               # Integration tests
├── infrastructure/          # CDK stacks and scripts
├── docs/                    # Documentation system
├── .amazonq/               # Amazon Q configuration
├── .cursor/                # Cursor AI configuration
├── .cline/                 # Cline configuration
├── .roocode/               # Roo Cline configuration
├── .kiro/                  # Kiro AI configuration
└── Taskfile.yml            # Task automation
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
