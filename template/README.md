# AWS Lambda Hexagonal Architecture Cruft Template

A cruft template for creating AWS Lambda projects using hexagonal architecture.

## Features

- **Hexagonal Architecture**: Clear separation between business logic and external dependencies
- **Model-Driven Development**: Using domain models as the foundation of application design
- **Service Adapter Pattern**: Consistent approach to external service integration
- **AWS Best Practices**: Specialized guidance for AWS services and serverless applications
- **Path Management**: Centralized path configuration using from_root
- **Lambda Factory**: Factory pattern for creating Lambda functions with consistent configuration
- **Build Process**: Automated build process for Lambda functions and layers
- **Testing**: Unit and integration tests with pytest
- **CDK Integration**: AWS CDK for infrastructure as code

## Usage

```bash
# Install cruft if not already installed
pip install cruft

# Create a new project
cruft create /path/to/this/template
```

## Template Options

- **project_name**: Name of the project
- **project_slug**: Slug for the project (auto-generated from project_name)
- **author_name**: Your name
- **author_email**: Your email
- **project_description**: Short description of the project
- **python_version**: Python version to use (e.g., 3.11)
- **include_example_function**: Whether to include an example Lambda function (yes/no)

## Project Structure

TODO

## Development

This template follows the hexagonal architecture pattern:

- **Domain Layer**: Business logic and models
- **Ports Layer**: Interfaces for external dependencies
- **Adapters Layer**: Implementation of interfaces for external systems
- **Functions Layer**: Lambda function handlers
