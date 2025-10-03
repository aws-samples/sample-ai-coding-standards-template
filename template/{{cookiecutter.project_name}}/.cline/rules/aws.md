# AWS Best Practices

## CLI Configuration

Disable the pager feature in AWS CLI v2, using the `--no-cli-pager` option.

## Hexagonal Architecture for AWS Services

### AWS-Specific Implementation

Apply hexagonal architecture (ports and adapters pattern) to create loosely coupled AWS applications where:

- Business logic is isolated from AWS infrastructure concerns
- Components can be tested independently without dependencies on AWS services
- Technology stack can be changed with minimal impact to domain logic
- Application communicates with external components through well-defined interfaces (ports)
- Adapters translate technical exchanges with AWS services

### Reference Implementation

The project provides a complete reference implementation of hexagonal architecture for AWS Lambda applications. Study these key files:

**Domain Layer:**

- `src/shared/domain/models/greeting.py` - Domain model with business rules and validation
- `src/shared/domain/services/greeting_service.py` - Business logic and coordination

**Ports Layer:**

- `src/shared/ports/greeting_port.py` - Interface defining what the application needs

**Adapters Layer:**

- `src/shared/adapters/greetings_storage.py` - DynamoDB implementation
- `src/shared/adapters/hello_world_adapter.py` - Simple adapter example

**Functions Layer:**

- `src/functions/hello_world/handler.py` - Lambda handler with proper import management

**Infrastructure Layer:**

- `infrastructure/stacks/hello_world_stack.py` - CDK stack definition
- `infrastructure/lambda_factory.py` - Consistent Lambda function creation

### Domain-Driven Design Integration

Structure AWS applications using simplified domain-driven design principles:

- Each Lambda function represents a bounded context or subdomain
- Business logic and coordination are combined in the domain layer
- Domain models contain both core business rules and workflow coordination
- Use simple aggregates to maintain consistency boundaries within Lambda functions

### AWS Ports and Adapters Structure

Organize AWS services using simplified ports and adapters pattern:

- **Ports**: Define technology-agnostic interfaces for external communication
- **Primary Adapters**: Handle incoming requests (API Gateway, EventBridge, SQS) - implemented in Lambda functions
- **Secondary Adapters**: Manage outgoing communications (DynamoDB, S3, external APIs)
- **Domain Layer**: Contains both pure business logic and coordination logic without infrastructure dependencies

### AWS Shared Components Architecture

Design shared components following hexagonal principles. See template examples:

**AWS Domain Models:**

- Reference: `src/shared/domain/models/greeting.py`
- Business objects that contain only business rules
- No AWS SDK imports, no database queries, no API calls - just business logic
- Can be tested without any AWS services running

**AWS Port Interfaces:**

- Reference: `src/shared/ports/greeting_port.py`
- Define what your application needs without specifying how it gets it
- Example: Repository interfaces with methods like `save()`, `find_by_id()`
- Your business logic uses these interfaces, not specific AWS implementations

**AWS Configuration Management:**

- Reference: `src/shared/config.py`
- Settings that change between environments (dev/staging/prod) without code changes
- Example: Database table names, API endpoints, feature flags
- Business logic doesn't know if it's running in AWS Lambda or locally
- Configuration is injected, not hardcoded

**AWS Validation Logic:**

- Reference: Domain models in `src/shared/domain/models/`
- Business rules for what makes valid data, separate from AWS API Gateway validation
- Can validate data whether it comes from API Gateway, EventBridge, or Step Functions
- Reusable across different input sources

**AWS Event Models:**

- Business events that matter to your domain, not AWS-specific events
- These events can be published to EventBridge, SQS, or any other system
- Business logic creates these events, adapters decide where to send them

### Hexagonal Architecture Integration Pattern for Step Functions

Apply the comprehensive Hexagonal Architecture Integration Pattern for Step Functions workflows, combining multiple established patterns while maintaining strict architectural boundaries:

#### Core Integration Principles

**Domain-Driven Step Functions Design:**

- Design Step Functions workflows around business domains rather than technical concerns
- Maintain strict separation between orchestration logic and business logic
- Use Step Functions as primary adapters that orchestrate business operations
- Treat Step Functions state machines as workflow coordinators, not business logic containers

**Clean Architecture Boundaries:**

- **Workflow Design**: Step Functions orchestrate business operations without containing business logic
- **Lambda Function Architecture**: Structure each Lambda using hexagonal architecture with clear ports and adapters
- **Data Flow Management**: Use structured data models (Pydantic) for all data flowing through workflows
- **Service Integration**: Integrate domain services through well-defined ports and adapters

#### Multi-Pattern Composition Strategy

**Sequential Pipeline Integration:**

- Use Sequential Pipeline Pattern within Step Functions for stage-based processing
- Each pipeline stage represents a distinct business operation
- Maintain clear input/output contracts between pipeline stages
- Enable independent testing and deployment of pipeline stages

**Map-Reduce Integration:**

- Apply Map-Reduce Pattern for collection processing within pipeline stages
- Use Step Functions Map state for parallel processing of collections
- Maintain data consistency across map-reduce operations

**Functional Cohesion Integration:**

- Organize related Lambda functions using Functional Cohesion Pattern
- Group functions by business capability rather than technical similarity
- Share domain services and adapters across functionally cohesive functions
- Enable reusability of business logic across different workflow contexts

#### EventBridge Integration

**Event-Driven Architecture:**

- Domain events are separate from EventBridge event format
- Primary Adapters: EventBridge event handlers that translate events to domain operations
- Secondary Adapters: Publish domain events back to EventBridge in proper format
- Multiple Event Sources: Same business logic can handle events from different sources
- Loose Coupling: Publishers and subscribers are decoupled through port interfaces

#### Benefits for Event-Driven Serverless

- **Clean Architecture**: Maintains strict separation between orchestration and business logic
- **Pattern Consistency**: Systematic application of architectural patterns across entire workflows
- **Enhanced Testability**: Business logic can be tested independently from Step Functions orchestration
- **Improved Maintainability**: Changes to business logic don't require orchestration changes and vice versa
- **Better Observability**: Clear separation enables monitoring at both orchestration and business levels
- **Flexible Evolution**: Individual patterns can evolve independently while maintaining integration consistency
- **Domain Clarity**: Business domains are clearly represented in both orchestration and implementation
- **Reusable Components**: Domain services and adapters can be reused across different workflows
- **Technology Independence**: Business logic doesn't depend on Step Functions or EventBridge specifics
- **Event Schema Evolution**: Can change event formats in adapters without affecting domain logic
- **Multiple Triggers**: Same business logic works with API Gateway, EventBridge, or Step Functions
- **Error Handling**: Domain-level error handling separate from Step Function error states
- **Testing**: Can test complete workflows without actual AWS services

### AWS Pydantic Models

**Location**: Place all Pydantic models in the `src/shared/domain/models/` folder

**Reference Implementation**: See `src/shared/domain/models/greeting.py` for:

- Data validation with business rules
- Serialization between JSON and Python objects
- Type safety throughout the application
- Auto-generated API schemas

**Integration Pattern**:

- Lambda functions receive raw JSON
- Convert to Pydantic models for validation
- Pass validated models to domain services
- Domain services use models for business logic
- Return Pydantic models serialized as JSON

### AWS Domain Services Organization

**Location**: Place business services in the `src/shared/domain/services/` folder

**Reference Implementation**: See `src/shared/domain/services/greeting_service.py` for:

- Business logic encapsulation
- Coordination of operations across multiple domain models
- Reusability across multiple Lambda functions
- Testability independent of AWS infrastructure

### AWS Service Layer Integration Principles

- **Single Responsibility**: Each service handles one domain area
- **Dependency Injection**: Use constructor injection for AWS clients
- **Configuration Management**: Centralized, environment-aware configuration
- **Error Handling**: Consistent error handling across all services

## Lambda Build Process and Deployment

### Source Code Organization

Reference the template structure for organizing Lambda functions and shared code:

- `src/shared/` - Unified shared folder structure for all Lambda-based projects
- `src/functions/` - Individual Lambda function directories
- `infrastructure/scripts/lambda_build.py` - Build script for packaging automation
- `infrastructure/config_path.py` - Path constants for all file operations

### Build Process Implementation

**Reference Implementation**: See `infrastructure/scripts/lambda_build.py` for:

- Packaging functions individually with specific dependencies
- Creating shared layers with common code accessible to all functions
- Handling import resolution between local development and Lambda runtime
- Managing dependencies appropriately

### Import Resolution Strategy

**Reference Implementation**: The template uses Python's native packaging features through `setup.py` and `pyproject.toml` to handle differences between local development and Lambda runtime environments:

- Clean imports without custom import logic
- IDE-compatible development with full autocomplete support
- Consistent behavior across all deployment scenarios

### Lambda Factory Pattern

**Reference Implementation**: See `infrastructure/lambda_factory.py` for:

- Creating AWS Lambda functions with unified configuration
- Type safety and validation throughout
- Consistent configuration settings across all Lambda functions
- Automatic IAM role creation with common permissions

### AWS Resource Discovery for Testing

**Reference Implementation**: See `tests/utils/resource_discovery.py` for:

- Tag-based resource discovery to enable dynamic resource identification in tests
- CDK resource tagging strategy for test resource discovery
- Automated resource identification in testing scenarios

## Event-Driven Architecture

### EventBridge Integration

- **Consistent Event Structure**: Use standardized event schemas across all services
- **Event Validation**: Implement validation for all event payloads
- **Dead Letter Queues**: Configure DLQs for failed event processing
- **Event Replay**: Design events to support replay for disaster recovery

## Security Best Practices

### Authentication and Authorization

- **Principle of Least Privilege**: Grant minimal necessary permissions

### Data Protection

- **Encryption at Rest**: Encrypt all sensitive data in DynamoDB and S3
- **Encryption in Transit**: Use TLS for all API communications
- **Secrets Management**: Store all secrets in AWS Secrets Manager
- **Data Sanitization**: Validate and sanitize all input data

## Lambda Import Management Strategy

### Import Management Overview

**Reference Implementation**: The template uses Python's native packaging features through `setup.py` and `pyproject.toml` to manage imports cleanly across all deployment scenarios.

### Deployment Scenarios

Lambda functions work consistently across deployment scenarios using Python's native packaging:

1. **Local Development**: Uses `setup.py` with editable installs (`pip install -e .`)
2. **Lambda Inline Deployment**: Shared code copied directly to function root without `shared/` prefix
3. **Lambda Layer Deployment**: Shared code deployed as a layer with proper Python packaging

### Core Principles

- **Native Python Packaging**: Uses `setup.py` and `pyproject.toml` for clean imports
- **No Custom Import Logic**: Eliminates custom import managers completely
- **IDE Compatible**: Full IDE support with autocomplete and static analysis
- **Clean Import Statements**: Direct imports without path manipulation

### Standard Import Pattern for Lambda Functions

**Reference Implementation**: See `src/functions/hello_world/handler.py` for the correct pattern:

```python
# Clean imports that work in all environments
from domain.services.hello_world_service import HelloWorldService
```

### Python Packaging Configuration

**Reference Implementation**: See template packaging files:

**Project Root Setup** (`setup.py`):

```python
setup(
    name="project-name",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
)
```

**Shared Package Setup** (`src/shared/setup.py`):

```python
setup(
    name="shared",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=["pydantic>=2.4.0", "boto3>=1.28.0"],
)
```

**PyProject Configuration** (`pyproject.toml`):

```toml
[tool.pytest.ini_options]
pythonpath = [
    "src/shared",  # For domain, adapters, models, etc.
    "src",         # For functions, tests
]

[tool.mypy]
mypy_path = [
    "src/shared",
    "src"
]
```

### Build Process Integration

**Reference Implementation**: See `infrastructure/scripts/lambda_build.py` for:

- **Development Environment**: Uses editable installs with `pip install -e .`
- **Inline Packaging**: Copies shared code contents directly to function root (no `shared/` prefix)
- **Dependency Management**: Installs requirements using `uv pip install`

## Data Management

### Data Modeling

- **Single Table Design**: Consider single table design for DynamoDB
- **Access Patterns**: Design data models based on access patterns
- **Data Normalization**: Balance between normalization and performance
- **Schema Evolution**: Plan for schema changes and backwards compatibility

## Serverless Development Standards

### Lambda Function Structure

**Reference Implementation**: Study the template structure:

- `src/functions/hello_world/handler.py` - Handler layer (entry point, request/response transformation)
- `src/shared/domain/services/greeting_service.py` - Service layer (business logic orchestration)
- `src/shared/adapters/` - Adapter layer (external system interactions)
- `src/shared/domain/models/` - Domain layer (core business models and rules)

### Handler Design

**Reference Implementation**: See `src/functions/hello_world/handler.py` for proper handler pattern:

- Request validation and input transformation to domain models
- Service orchestration
- Response formatting
- Error handling with domain-specific exceptions

### Performance Optimization

- Minimize cold start times
- Use global scope for initialization code
- Implement connection pooling for database connections
- Cache expensive operations outside the handler
- Use async patterns for I/O-bound operations

### Error Handling

- Implement consistent error handling across all functions
- Use domain-specific exceptions
- Transform exceptions to appropriate HTTP responses
- Log errors with context information
- Implement retry mechanisms for transient failures
- Example: `UserRepository` interface with methods like `save_user()` and `find_user_by_email()`
- Example: `PaymentProcessor` interface with `process_payment()` method
- Your business logic uses these interfaces, not specific AWS implementations

**AWS Configuration Management:**

- Settings that change between environments (dev/staging/prod) without code changes
- Example: Database table names, API endpoints, feature flags
- Business logic doesn't know if it's running in AWS Lambda or locally
- Configuration is injected, not hardcoded

**AWS Validation Logic:**

- Business rules for what makes valid data, separate from AWS API Gateway validation
- Example: Email format validation, business rule that orders must have at least one item
- Can validate data whether it comes from API Gateway, EventBridge, or Step Functions
- Reusable across different input sources

**AWS Event Models:**

- Business events that matter to your domain, not AWS-specific events
- Example: `UserRegistered`, `OrderPlaced`, `PaymentProcessed` events
- These events can be published to EventBridge, SQS, or any other system
- Business logic creates these events, adapters decide where to send them

### AWS Pydantic Models

**Location**: Place all Pydantic models in the `src/shared/domain/models/` folder

**Purpose**:

- **Data Validation**: Ensure incoming data meets business rules
- **Serialization**: Convert between JSON and Python objects
- **Type Safety**: Provide strong typing throughout the application
- **Documentation**: Auto-generate API schemas

**Benefits in Lambda Functions**:

- Validate API Gateway requests before processing
- Ensure EventBridge events have correct structure
- Serialize responses consistently
- Enable easy testing with typed data

**Integration Pattern**:

- Lambda functions receive raw JSON
- Convert to Pydantic models for validation
- Pass validated models to domain services
- Domain services use models for business logic
- Return Pydantic models serialized as JSON

### AWS Domain Services Organization

**Location**: Place business services in the `src/shared/domain/services/` folder

**Purpose**:

- **Business Logic**: Encapsulate complex business rules and workflows
- **Coordination**: Orchestrate operations across multiple domain models
- **Reusability**: Share business logic across multiple Lambda functions
- **Testability**: Test business logic independently of AWS infrastructure

**Examples**:

- `UserService` with methods like `create_user()`, `update_profile()`, `deactivate_account()`
- `OrderService` with methods like `process_order()`, `calculate_shipping()`, `apply_discounts()`
- `PaymentService` with methods like `validate_payment()`, `process_refund()`

### AWS Service Layer Integration Principles

- **Single Responsibility**: Each service handles one domain area
- **Dependency Injection**: Use constructor injection for AWS clients
- **Configuration Management**: Centralized, environment-aware configuration
- **Error Handling**: Consistent error handling across all services

### AWS Configuration Management Best Practices

- **Environment-based Configuration**: Separate configs for dev/staging/prod
- **Secrets Management**: Store sensitive data in AWS Secrets Manager
- **Configuration Caching**: Lazy loading and caching for performance
- **Type Safety**: Use Pydantic models for configuration

## Lambda Build Process and Deployment

### Source Code Organization

Organize Lambda functions and shared code consistently across all projects:

- Create unified shared folder structure for all Lambda-based projects
- Separate shared code from individual Lambda function directories
- Use layers for custom reusable components
- Maintain build scripts for packaging automation
- Use path constants from `config_path.py` for all file operations

### Build Process Implementation

Implement a consistent build process that:

- **Packages Functions Individually**: Each Lambda function is packaged with its specific dependencies
- **Creates Shared Layers**: Common code becomes a Lambda layer accessible to all functions
- **Handles Import Resolution**: Bridges differences between local development and Lambda runtime
- **Manages Dependencies**: Installs and packages dependencies appropriately
- **Uses Path Constants**: References paths from `config_path.py` for consistency

### Import Resolution Strategy

Handle differences between local development and Lambda runtime environments:

- Configure Lambda runtime imports to access layer code directly
- Set up local development with proper package mapping
- Implement import redirection patterns for development consistency

### Dependency Management Best Practices

- **Function-Specific Dependencies**: Each Lambda has its own requirements file
- **Shared Dependencies**: Common libraries in shared layer requirements
- **Dependency Isolation**: Avoid dependency conflicts between functions
- **Version Pinning**: Pin dependency versions for reproducible builds

### Build Automation

Create automated build scripts with comprehensive CLI interface:

- **Command Grouping**: Use organized command structure for build operations
- **Granular Commands**: Support building all, individual functions, or specific layers
- **Clear Feedback**: Provide visual feedback and clear messages
- **Error Handling**: Validate inputs and provide helpful error messages
- **Flexible Configuration**: Allow customization through command-line options

### Build Tool Best Practices

**File Management Best Practices:**

- **Selective File Copying**: Only copy relevant files (.py, .json, .jschema)
- **Directory Filtering**: Skip hidden directories (starting with ".")
- **Clean Builds**: Always remove previous artifacts before building
- **Target Directory Management**: Handle directory overwrites safely

**Dependency Installation Best Practices:**

- **Isolated Installation**: Use target directories for specific installations
- **No Cache**: Use no-cache options for consistent builds
- **Quiet Mode**: Use quiet mode to reduce build noise
- **Error Checking**: Implement proper error checking in build processes

**Build Process Architecture:**

- **Layer-First Strategy**: Always build shared layers before functions
- **Incremental Building**: Support building individual components
- **Validation Checks**: Verify directory existence before operations
- **Build Status Tracking**: Return success/failure status for operations

### Local Development Environment

Set up local development to mirror Lambda runtime:

- **Python Path Management**: Ensure imports work consistently
- **Environment Variables**: Use same environment variables as Lambda
- **Testing Setup**: Test with the same directory structure as production
- **Dependency Resolution**: Use same dependency versions as Lambda

### Deployment Considerations

- **Layer Size Limits**: AWS Lambda layers have size restrictions
- **Package Size Optimization**: Minimize package sizes for faster cold starts
- **Selective File Copying**: Only include necessary files
- **Build Validation**: Validate packages before deployment

### Development Workflow

Follow structured development workflow:

1. **Code Development**: Write code using local development setup
2. **Local Testing**: Test with local Lambda simulation
3. **Build Process**: Run automated build to create packages
4. **Package Validation**: Verify packages work correctly
5. **Deployment**: Deploy functions and layers to AWS
6. **Integration Testing**: Test in AWS environment

## Lambda Factory Pattern

### Factory Pattern Implementation

Implement a consistent Lambda Factory pattern for creating AWS Lambda functions:

- Create core factory class with unified configuration
- Define configuration properties using dataclasses
- Implement type safety and validation throughout

### Factory Pattern Best Practices

**Type Safety and Validation:**

- **Strong Type Hints**: Use comprehensive type hints for all parameters and return values
- **Dataclass Configuration**: Use dataclasses for configuration properties with validation
- **Custom Error Classes**: Implement custom exception classes for factory-specific errors
- **Handler Validation**: Parse and validate handler strings before function creation

**Consistent Configuration:**

- **Common Configuration**: Provide unified configuration settings across all Lambda functions
- **Runtime Standardization**: Use consistent runtime versions and architecture settings
- **Environment Variables**: Standardize environment variable patterns across functions
- **Tracing Enabled**: Enable AWS X-Ray tracing by default for all functions

**IAM Role Management:**

- **Automatic Role Creation**: Create IAM roles automatically with common permissions
- **Basic Execution Permissions**: Include Lambda basic execution role and X-Ray permissions by default
- **Additional Policies**: Support additional policy statements for specific function needs
- **Permission Segregation**: Create function-specific roles with minimal necessary permissions

**Resource Tagging:**

- **Essential Tags**: Add Name tag by default for all Lambda functions
- **Custom Tags**: Support custom tags for resource organization and cost allocation
- **Discovery Tags**: Use consistent tagging for Lambda function discovery in tests and automation

**Error Handling and Validation:**

- **Directory Validation**: Validate Lambda source directory existence before creation
- **Handler Format Validation**: Ensure handler format follows expected patterns
- **Resource Existence Checks**: Verify required resources exist before granting permissions
- **Descriptive Error Messages**: Provide clear error messages for debugging

### AWS Resource Discovery for Testing

Implement tag-based resource discovery to enable dynamic resource identification in tests:

- Use CDK resource tagging strategy for test resource discovery
- Apply consistent tagging patterns across all AWS resources
- Enable automated resource identification in testing scenarios

## Event-Driven Architecture

### EventBridge Integration

- **Consistent Event Structure**: Use standardized event schemas across all services
- **Event Validation**: Implement validation for all event payloads
- **Dead Letter Queues**: Configure DLQs for failed event processing
- **Event Replay**: Design events to support replay for disaster recovery

## Security Best Practices

### Authentication and Authorization

- **Principle of Least Privilege**: Grant minimal necessary permissions

### Data Protection

- **Encryption at Rest**: Encrypt all sensitive data in DynamoDB and S3
- **Encryption in Transit**: Use TLS for all API communications
- **Secrets Management**: Store all secrets in AWS Secrets Manager
- **Data Sanitization**: Validate and sanitize all input data

## Lambda Import Management Strategy

### Import Management Overview

**Reference Implementation**: The template uses Python's native packaging features through `setup.py` and `pyproject.toml` to manage imports cleanly across all deployment scenarios.

### Deployment Scenarios

Lambda functions work consistently across deployment scenarios using Python's native packaging:

1. **Local Development**: Uses `setup.py` with editable installs (`pip install -e .`)
2. **Lambda Inline Deployment**: Shared code copied directly to function root without `shared/` prefix
3. **Lambda Layer Deployment**: Shared code deployed as a layer with proper Python packaging

### Core Principles

- **Native Python Packaging**: Uses `setup.py` and `pyproject.toml` for clean imports
- **No Custom Import Logic**: Eliminates custom import managers completely
- **IDE Compatible**: Full IDE support with autocomplete and static analysis
- **Clean Import Statements**: Direct imports without path manipulation

### Standard Import Pattern for Lambda Functions

**Reference Implementation**: See `src/functions/hello_world/handler.py` for the correct pattern:

```python
# Clean imports that work in all environments
from domain.services.hello_world_service import HelloWorldService
```

### Python Packaging Configuration

**Reference Implementation**: See template packaging files:

**Project Root Setup** (`setup.py`):

```python
setup(
    name="project-name",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
)
```

**Shared Package Setup** (`src/shared/setup.py`):

```python
setup(
    name="shared",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=["pydantic>=2.4.0", "boto3>=1.28.0"],
)
```

**PyProject Configuration** (`pyproject.toml`):

```toml
[tool.pytest.ini_options]
pythonpath = [
    "src/shared",  # For domain, adapters, models, etc.
    "src",         # For functions, tests
]

[tool.mypy]
mypy_path = [
    "src/shared",
    "src"
]
```

### Build Process Integration

**Reference Implementation**: See `infrastructure/scripts/lambda_build.py` for:

- **Development Environment**: Uses editable installs with `pip install -e .`)
- **Inline Packaging**: Copies shared code contents directly to function root (no `shared/` prefix)
- **Dependency Management**: Installs requirements using `uv pip install`

### Import Management Benefits

- **Clean Code**: No import setup code needed in Lambda functions
- **IDE Support**: Full autocomplete and navigation support
- **Type Safety**: Static analysis works correctly
- **Maintainable**: Standard Python packaging patterns
- **Testable**: Same imports work in tests and production

## Data Management

### Data Modeling

- **Single Table Design**: Consider single table design for DynamoDB
- **Access Patterns**: Design data models based on access patterns
- **Data Normalization**: Balance between normalization and performance
- **Schema Evolution**: Plan for schema changes and backwards compatibility

## Serverless Development Standards

### Lambda Function Structure

- Organize Lambda functions using hexagonal architecture principles
- Separate handler logic from business logic
- Structure Lambda functions with these layers:
  - **Handler Layer**: Entry point, request/response transformation
  - **Service Layer**: Business logic orchestration
  - **Adapter Layer**: External system interactions
  - **Domain Layer**: Core business models and rules

### Handler Design

- Keep handlers thin and focused on:
  - Request validation
  - Input transformation to domain models
  - Service orchestration
  - Response formatting
- Example handler pattern:

  ```python
  def handler(event, context):
      # 1. Parse and validate input
      try:
          input_model = InputModel.parse_obj(event)
      except ValidationError as e:
          return format_error_response(e)

      # 2. Initialize services with adapters
      service = DomainService()

      # 3. Execute business logic
      try:
          result = service.process(input_model)
          return format_success_response(result)
      except DomainError as e:
          return format_error_response(e)
  ```

### Performance Optimization

- Minimize cold start times
- Use global scope for initialization code
- Implement connection pooling for database connections
- Cache expensive operations outside the handler
- Use async patterns for I/O-bound operations

### Error Handling

- Implement consistent error handling across all functions
- Use domain-specific exceptions
- Transform exceptions to appropriate HTTP responses
- Log errors with context information
- Implement retry mechanisms for transient failures
