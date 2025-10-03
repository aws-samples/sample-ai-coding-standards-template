# Project template for AI-Driven Development Standards with AWS Architecture Patterns

A comprehensive project template implementing [hexagonal architecture pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html) for AWS applications, with integrated AI coding assistant configuration and enterprise-grade development standards.

## Why This Template

Development teams increasingly adopt AI coding assistants but struggle with maintaining consistent standards between AI assistants and human developers across projects. Teams face challenges with varying coding standards, undocumented architectural decisions, and complex knowledge transfer processes as they scale.

Many developers find that current approaches to agentic development can break as projects increase in complexity. They end up spending as much time guiding agents and fixing problems as they would writing code from scratch. Teams need ways to provide more precise and comprehensive project context to decrease task ambiguity and ensure AI-generated work meets quality standards.

This template addresses these collaboration challenges by establishing standardized development practices, implementing proven architecture patterns, and integrating AI coding assistant configuration to ensure consistent practices between AI assistants and development teams.

## Overview

This repository provides a comprehensive project template and standardized configurations for AI-driven development with:

- Amazon Q Developer
- Cursor AI
- Cline (Claude Dev)
- Roo Cline
- Kiro AI
- Amazon Bedrock Client

## Features

- **Project-Level MCP Configuration**: Pre-configured Model Context Protocol servers for AWS services at the project level
- **Development Rules**: Comprehensive coding standards and best practices
- **Multi-Tool Support**: Compatible with multiple AI coding assistants
- **Template-Based Setup**: One-command template configuration management
- **Cookiecutter Integration**: Automated project generation with all configurations included

## Development Rules

The rules are stored in [`rules/`](rules/) have been organized to eliminate duplication and provide clear guidance:

**Core Architecture and Implementation:**

- **architecture.md**: General architectural principles and hexagonal architecture patterns
- **python.md**: Python-specific implementation guidelines and patterns
- **aws.md**: AWS-specific implementation details and best practices
- **project_structure.md**: Standardized project layout and path management

**Development Process and Tools:**

- **general.md**: General development standards and implementation approach
- **cdk.md**: AWS CDK resource management and deployment standards
- **taskfile.md**: Taskfile.dev automation and command management
- **test.md**: Integration testing strategy with real AWS resources

**Documentation and Specifications:**

- **doc.md**: Documentation standards and formatting guidelines
- **adr.md**: Architecture Decision Records structure and best practices
- **spec.md**: Specification standards and templates
- **blog.md**: AWS blog writing standards and guidelines

**Specialized Frameworks:**

- **strandsagent.md**: Multi-agent development with Bedrock integration

## MCP Server Configuration

Model Context Protocol (MCP) servers configuration is stored in [`mcp/mcp.json`](mcp/mcp.json). MCP servers extend AI coding assistant capabilities:

**AWS Development Servers:**

- **awslabs.core-mcp-server**: Core AWS functionality with CDK guidance and best practices
- **awslabs.cdk-mcp-server**: AWS CDK constructs, patterns, and deployment automation
- **awslabs.aws-documentation-mcp-server**: Real-time AWS documentation search and retrieval
- **awslabs.aws-api-mcp-server**: Direct AWS API interactions and resource management
- **awslabs.dynamodb-mcp-server**: DynamoDB operations and data modeling assistance

**Documentation and Visualization:**

- **awslabs.code-doc-gen-mcp-server**: Automated code documentation generation
- **awslabs.aws-diagram-mcp-server**: AWS architecture diagram creation and visualization
- **mermaid-doc-mcp-server**: Mermaid diagram documentation and examples

**Development Tools:**

- **playwright**: Browser automation and testing capabilities
- **strands**: Multi-agent development with Bedrock integration

These MCP servers provide AI coding assistants with specialized knowledge and tools for AWS development, enabling more accurate and context-aware assistance.

## Template Configuration Management

The project uses Taskfile.dev to manage template configurations and synchronize changes across multiple AI coding assistants.

### Updating Template Configurations

```bash
task install
```

This command performs a complete installation and synchronization process:

**What `task install` does:**

1. **Installs MCP Configurations** (`task install:template:mcp`):
2. **Installs Development Rules** (`task install:template:rules`):
3. **Installs Hooks** (`task install:template:hooks`):
4. **Sets Up Pre-commit Hooks** (`task install:pre-commit`):

### When to Run `task install`

- After modifying any files in `rules/` directory
- After updating `mcp/mcp.json` configuration

This ensures all AI coding assistants have consistent, up-to-date configurations and development standards.

## Cruft usage

The repository includes a [cruft template](https://cruft.github.io/cruft/) that implements all the development rules and best practices:

```bash
cruft create https://github.com/aws-samples/sample-ai-coding-standards-template.git --directory template/
```

The template provides:

1. **Hexagonal Architecture**: Clean separation between business logic and external dependencies
2. **AWS CDK Infrastructure**: Infrastructure as code with AWS CDK
3. **Integration Testing**: Tests with real AWS resources using resource discovery
4. **Configuration Management**: Centralized configuration with validation
5. **Build Process**: Automated build and deployment process
6. **Clean Imports**: No src/shared prefixes, clean import structure
7. **Automated Cruft Updates**: Seamless template synchronization with conflict resolution
8. **Project-Level MCP Configuration**: Each generated project includes MCP configurations for:
   - **Roo Cline**: `.roocode/mcp.json`
   - **Amazon Q Developer**: `.amazonq/mcp.json`
   - **Kiro Dev**: `.kiro/settings/mcp.json`

### Template Features

- **Domain Layer**: Pure business logic with Pydantic models
- **Ports Layer**: Technology-agnostic interfaces
- **Adapters Layer**: AWS service implementations
- **Infrastructure Layer**: CDK stacks and build scripts
- **Testing Layer**: Integration tests with AWS resources

### How to use

1. Install [Task](https://taskfile.dev/)

2. Install cruft:

   ```bash
   pip install cruft
   ```

3. Create a new project:

   ```bash
   cruft create https://github.com/aws-samples/sample-ai-coding-standards-template.git --directory template/
   ```

4. Read the generated project's README.md

### Template Updates

Every project generated from this template includes **automated cruft update capabilities** that eliminate the common issues with template synchronization:

#### **Automated Cruft Updates**

```bash
# One command for seamless template updates
task cruft:update
```

**What this automation provides:**

- **Automatic Conflict Resolution**: Uses `patch` command with multiple strategies to auto-resolve conflicts
- **No User Interaction**: Fully automated with no prompts or manual intervention required
- **Clean Workspace**: Automatically removes `.rej` and `.orig` files
- **Always Succeeds**: Never blocks your workflow - applies what it can, ignores what it can't

## Architectural Approach

This project implements a comprehensive set of development standards focused on:

### 1. Hexagonal Architecture

- **Domain Layer**: Pure business logic, independent of infrastructure
- **Ports Layer**: Interface contracts for external dependencies
- **Adapters Layer**: AWS service implementations
- **Benefits**:
  - Technology independence
  - Improved testability
  - Clear boundaries
  - Consistent patterns

### 2. Model-Driven Development

- **Domain Models**: Foundation of application design
- **Validation**: Strong validation with Pydantic
- **Type Safety**: Comprehensive type hints
- **Benefits**:
  - Data integrity
  - Clear contracts
  - IDE support
  - Documentation

### 3. Configuration Management

- **Centralized Config**: Single source of truth
- **Strong Validation**: No fallbacks
- **Benefits**:
  - Consistent configuration
  - Clear error messages
  - Easy environment switching

### 4. Resource Discovery

- **Tag-Based**: Resources found by tags
- **Real Testing**: No mocks needed
- **Clean Setup**: Automatic resource lookup
- **Benefits**:
  - Integration testing
  - Real AWS resources
  - Clean test code

### 5. Clean Imports

- **No Prefixes**: No src/shared in imports
- **IDE Support**: Full autocomplete
- **Build Process**: Proper packaging
- **Benefits**:
  - Clean code
  - Better maintainability
  - IDE integration

## Project Goals

1. **Standardize Development**: Consistent coding standards and patterns
2. **Enhance AI Assistants**: Comprehensive knowledge of best practices
3. **Accelerate Development**: Reduce configuration and decision time
4. **Ensure Quality**: High standards for code and security
5. **Share Knowledge**: Central repository of development wisdom
6. **Streamline Onboarding**: Quick project standards understanding

## License

This configuration is provided as-is for development use.
