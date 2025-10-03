# Infrastructure

This section contains all infrastructure components including CDK stacks, deployment scripts, and infrastructure utilities.

## Overview

The infrastructure is organized using AWS CDK (Cloud Development Kit) with the following structure:

### Directory Structure

```text
infrastructure/
├── __init__.py              # Package initialization
├── app.py                   # CDK app entry point
├── cdk.json                 # CDK configuration
├── config.py                # Infrastructure configuration
├── lambda_factory.py        # Lambda function factory
├── scripts/                 # Build and deployment scripts
│   └── lambda_build.py      # Lambda build automation
└── stacks/                  # CDK stack definitions
    └── hello_world_stack.py # Example stack
```

## Key Components

### CDK Application

The main CDK application is defined in `app.py` and serves as the entry point for all infrastructure deployment.

### Lambda Factory

The `lambda_factory.py` module provides a consistent pattern for creating Lambda functions with:

- Standardized configuration
- Automatic IAM role creation
- Built-in observability (X-Ray tracing)
- Resource tagging

### Build Scripts

The `scripts/lambda_build.py` provides automated build processes for:

- Lambda function packaging
- Shared layer creation
- Dependency management
- Clean build artifacts

### Stack Organization

CDK stacks are organized by feature or service, with each stack containing related resources and following infrastructure as code best practices.
