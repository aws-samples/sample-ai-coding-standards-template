# AWS AI-Driven Development Template

Enterprise-grade project template with integrated AI coding assistant configurations and AWS best practices. Generate production-ready applications with hexagonal architecture in minutes.

## 1. The Challenge and Solution

### The Challenge

AI coding assistants often produce inconsistent code because they lack project-specific context and standards. Teams spend more time fixing AI-generated code than writing it themselves.

### The Solution

This template provides comprehensive project context through:

- Standardized development rules and patterns
- Pre-configured AI assistant settings
- Production-ready architecture patterns
- Automated security and quality checks and testing

## 2. How to Use the Solution

### Quick Start

```bash
# Install dependencies
pip install cruft

# Create new project
cruft create https://github.com/aws-samples/sample-ai-coding-standards-template.git --directory template/

# Follow the prompts, then:
cd your-project-name
open README.md
```

**What you get:** A complete AWS Hello World application with Lambda functions, DynamoDB, CDK infrastructure, integration tests, and AI assistant configurations for Amazon Q, Cursor, Cline, and more.

### Generated Project Structure

```bash
your-project/
├── src/
│   ├── functions/           # Lambda functions
│   ├── shared/             # Business logic & adapters
│   └── tests/              # Integration tests
├── infrastructure/         # CDK stacks
├── .amazonq/              # Amazon Q configuration
├── .cursor/               # Cursor AI configuration
├── .cline/                # Cline configuration
└── Taskfile.yml           # Automation commands
```

### AI Assistant Configurations

Pre-configured for multiple AI coding assistants:

- **Amazon Q Developer** - AWS-native development
- **Cursor AI** - Code completion and chat
- **Cline** - Autonomous coding agent
- **Roo Cline** - Enhanced Claude integration
- **Kiro AI** - Advanced code analysis

### Architecture Patterns

- **Hexagonal Architecture** - Clean separation between domain logic, ports, and adapters
- **Domain-Driven Design** - Business logic first, independent of infrastructure
- **AWS CDK** - Infrastructure as code with enterprise-grade patterns
- **Integration Testing** - Real AWS resource testing with tag-based discovery
- **Clean Imports** - No complex path management, full IDE support

### Key Benefits

**For Development Teams:**

- **Productivity** - AI assistants understand project context without extensive guidance
- **Quality** - Standardized patterns ensure consistent, maintainable code
- **Cohérence** - Shared vocabulary between AI assistants and human developers
- **Scalability** - Enterprise-grade architecture that grows with your needs

**For AI Assistants:**

- **Better Context** - Comprehensive project knowledge and architectural patterns
- **Accurate Suggestions** - Code follows established standards from creation
- **Reduced Corrections** - Less time spent reviewing and fixing AI-generated code

## 3. How to Customize the Solution

### Update AI Assistant Rules

Modify development standards in [`rules/`](rules/):

```bash
# Edit any rule file
vim rules/aws.md

# Apply changes to all AI assistants
task install
```

### Update MCP Server Configuration

Add or modify AI assistant capabilities in [`mcp/mcp.json`](mcp/mcp.json):

```bash
# Edit MCP configuration
vim mcp/mcp.json

# Apply changes
task install
```

### Update Hooks

Modify AI assistant hooks in [`hooks/`](hooks/):

```bash
# Edit hook files
vim hooks/architecture-decision-record.hook

# Apply changes
task install
```

### Keep Projects Updated

```bash
# Update existing projects with template improvements
task cruft:update
```

## Prerequisites

- Python 3.11+
- [Task](https://taskfile.dev/) for automation
- AWS CLI configured
- Git for version control

## License

This configuration is provided as-is for development use.
