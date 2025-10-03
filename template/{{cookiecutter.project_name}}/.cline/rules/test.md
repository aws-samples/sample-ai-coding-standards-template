# Testing Strategy

## Testing Approach

- Follow Test-Driven Thinking (TDT)
- Design all code to be easily testable from inception
- Implement comprehensive test coverage:
  - Integration Tests: Verify component interactions
  - End-to-End Tests: Validate complete user workflows
- Do not mock AWS Services in tests

## Testing with Python

- Use pytest for integration and end-to-end tests
- Do not create unit tests, focus on integration tests with AWS Services
- Do not mock AWS services in tests
- **Reference Implementation**: See `tests/conftest.py` for fixtures implementation
- To add new integration tests, create a new file in the appropriate `tests/integration/` subdirectory with the naming convention `test_*.py`
- Use the fixtures to interact with AWS services
- Add assertions to verify the expected behavior

## Reference Implementation

Study the template test structure for best practices:

**Test Configuration**: `tests/conftest.py`

- Lambda event and context fixtures
- Import manager setup for tests
- Test utilities path configuration

**Integration Tests**: `tests/integration/`

- **Adapters**: `tests/integration/adapters/` - Tests for adapter implementations
- **Functions**: `tests/integration/functions/` - Tests for Lambda function handlers
- **Services**: `tests/integration/services/` - Tests for domain services
- **Models**: `tests/integration/test_*_model.py` - Tests for domain models

**Test Utilities**: `tests/utils/`

- `lambda_utils.py` - Lambda invocation utilities
- `resource_discovery.py` - AWS resource discovery for tests

**Test Configuration**: `pyproject.toml`

- Pytest configuration with integration markers
- Test path configuration

## Best Practices

1. **Clean Up Resources**: Make sure tests clean up any resources they create
2. **Use Unique Names**: Use unique names for test resources to avoid conflicts
3. **Handle Failures Gracefully**: Use try/except blocks to handle failures
4. **Print Useful Information**: Print useful information for debugging
5. **Check CloudWatch Logs**: Use the `get_logs` fixture to check CloudWatch logs
6. **Wait for Asynchronous Operations**: Use appropriate wait times for asynchronous operations
7. Use CloudFormation Output to get AWS resource name or ARN

### Testing Directory Structure

**Reference Implementation**: The template provides this exact structure in `tests/`:

```bash
tests/                               # All test code
├── conftest.py                      # Shared test fixtures and lambda_runner
├── __init__.py                      # Test package marker
├── integration/                     # Integration tests with real AWS services
│   ├── __init__.py                  # Integration package marker
│   ├── adapters/                    # Adapter integration tests
│   │   ├── __init__.py              # Adapters package marker
│   │   └── test_hello_world_storage_adapter.py  # Storage adapter tests
│   ├── functions/                   # Function integration tests
│   │   ├── __init__.py              # Functions package marker
│   │   └── test_hello_world_handler.py  # Lambda handler tests
│   ├── services/                    # Service integration tests
│   │   ├── __init__.py              # Services package marker
│   │   └── test_hello_world_service.py  # Domain service tests
│   └── test_hello_world_model.py    # Domain model tests
├── utils/                           # Test utilities
│   ├── __init__.py                  # Utils package marker
│   ├── lambda_utils.py              # Lambda invocation utilities
│   └── resource_discovery.py       # AWS resource discovery
└── payloads/                        # Test payloads for Lambda functions
    └── hello_world/
        └── event.json               # Sample Lambda event
```

## Test Organization by Component Type

### Adapter Tests

**Location**: `tests/integration/adapters/`
**Purpose**: Test adapter implementations and their interaction with AWS services
**Example**: `test_hello_world_storage_adapter.py`

- Test direct adapter functionality
- Test data persistence and retrieval
- Test adapter initialization
- Test error handling in adapters

### Function Tests

**Location**: `tests/integration/functions/`
**Purpose**: Test Lambda function handlers and their request/response processing
**Example**: `test_hello_world_handler.py`

- Test Lambda handler invocation
- Test request parameter parsing
- Test response format compliance
- Test error handling in handlers

### Service Tests

**Location**: `tests/integration/services/`
**Purpose**: Test domain services and their business logic coordination
**Example**: `test_hello_world_service.py`

- Test service business logic
- Test service integration with adapters
- Test service consistency
- Test dependency injection patterns

### Model Tests

**Location**: `tests/integration/`
**Purpose**: Test domain models and their validation, serialization, and business logic
**Example**: `test_hello_world_model.py`

- Test model creation and validation
- Test serialization and deserialization
- Test business logic methods
- Test model behavior with edge cases

## Test Fixtures

**Reference Implementation**: See `tests/conftest.py` for:

- `dynamodb_table()` - DynamoDB table fixture using resource discovery
- Path configuration for test utilities

## Integration Testing Patterns

**Lambda Function Testing**: See `tests/integration/functions/test_hello_world_handler.py` for:

- Direct Lambda handler testing
- AWS Lambda invoke testing
- API Gateway endpoint testing
- Resource discovery testing
- DynamoDB integration testing

**Adapter Testing**: See `tests/integration/adapters/test_hello_world_storage_adapter.py` for:

- Direct adapter testing
- Data persistence testing
- AWS service integration testing
- Error handling testing

**Service Testing**: See `tests/integration/services/test_hello_world_service.py` for:

- Business logic testing
- Service coordination testing
- Dependency injection testing
- Integration with multiple adapters

## Path Management in Tests

**Reference Implementation**: See `tests/conftest.py` for:

- Import path constants from `config_path.py` for accessing test data and fixtures
- Consistent file access across tests
- Pytest configuration to add the project root to sys.path
