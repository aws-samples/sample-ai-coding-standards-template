# {{cookiecutter.project_name}} Documentation

Welcome to the {{cookiecutter.project_name}} documentation. This documentation is automatically generated from Python docstrings using MkDocs with mkdocstrings, organized following hexagonal architecture principles.

## Project Overview

{{cookiecutter.project_description}}

## Hexagonal Architecture

This project implements hexagonal architecture (also known as ports and adapters pattern) to create a clean, maintainable, and testable codebase. The architecture is organized into distinct layers:

### 🏗️ Infrastructure Layer

Contains AWS CDK stacks, deployment scripts, and infrastructure-as-code components. This layer handles the deployment and configuration of AWS resources.

- **Stacks**: CDK stack definitions for AWS resources
- **Scripts**: Build and deployment automation
- **Core**: Lambda factory and shared infrastructure utilities

### ⚡ Functions Layer

AWS Lambda function handlers that serve as primary adapters, handling incoming requests from API Gateway, EventBridge, or other AWS services.

- **Handlers**: Lambda entry points and request/response processing
- **Event Processing**: AWS service event handling and transformation

### 🎯 Domain Layer

The core business logic layer containing pure business rules and domain models. This layer is independent of external dependencies and frameworks.

- **Models**: Business entities with validation and business rules
- **Services**: Business logic orchestration and workflows

### 🔌 Ports Layer

Interface definitions that specify contracts for external communication. These abstractions allow the domain layer to remain independent of specific implementations.

- **Interfaces**: Abstract contracts for external dependencies
- **Specifications**: Port definitions for adapters

### 🔧 Adapters Layer

Concrete implementations of ports that handle integration with external systems like databases, APIs, and AWS services.

- **Storage**: Database and persistence adapters
- **External APIs**: Third-party service integrations
- **AWS Services**: AWS SDK implementations

### 🧪 Tests Layer

Comprehensive integration tests that verify the behavior of all layers working together with real AWS services.

- **Integration**: End-to-end tests with real AWS resources
- **Utilities**: Test helpers and resource discovery tools

## Getting Started

### Prerequisites

- Python {{cookiecutter.python_version}}+
- [uv](https://github.com/astral-sh/uv) for Python package management
- [Task](https://taskfile.dev/) for task automation

### Building Documentation

```bash
# Set up documentation environment
task docs:setup

# Build documentation
task docs:build

# Serve documentation locally with hot reload
task docs:serve

# Clean generated files
task docs:clean
```

### Local Development

The documentation server runs at `http://127.0.0.1:8000` with hot reload enabled. Any changes to Python docstrings or documentation files will automatically trigger a rebuild.

## Navigation Guide

### 📚 Architecture Sections

Navigate through the hexagonal architecture layers using the main navigation:

- **Infrastructure**: CDK stacks and deployment infrastructure
- **Functions**: Lambda handlers and event processing
- **Domain Layer**: Business models and services
- **Ports Layer**: Interface definitions
- **Adapters Layer**: External system integrations
- **Tests**: Integration tests and utilities

### 🔍 Code Reference

The complete API reference is automatically generated from Python docstrings and organized by architectural layers for easy navigation.

### 🔎 Search Functionality

Use the search bar (or press `Ctrl/Cmd + K`) to quickly find:

- Specific classes, methods, or functions
- Architecture layer components
- Business logic and domain concepts
- Integration patterns and examples

## Documentation Standards

This documentation follows these principles:

- **Automatic Generation**: All API documentation is generated from Python docstrings
- **Architecture-Driven**: Organization follows hexagonal architecture layers
- **Comprehensive Coverage**: Includes all public classes, methods, and functions
- **Cross-References**: Links between related components and layers
- **Search-Optimized**: Enhanced search functionality for quick navigation
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Contributing

When adding new code to the project:

1. **Write Clear Docstrings**: Use Google-style docstrings for all public classes and methods
2. **Follow Architecture**: Place code in the appropriate hexagonal architecture layer
3. **Update Documentation**: The documentation will automatically update from your docstrings
4. **Test Integration**: Ensure your code works with the existing architecture layers

For more information about the project structure and development guidelines, see the [Code Reference](reference/) section.
