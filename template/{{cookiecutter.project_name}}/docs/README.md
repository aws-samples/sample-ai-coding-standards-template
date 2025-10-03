# {{cookiecutter.project_name}} Documentation

This directory contains the documentation system for {{cookiecutter.project_name}}, built with MkDocs and mkdocstrings to automatically generate comprehensive API documentation from Python docstrings.

## 🏗️ Architecture

The documentation system follows the project's hexagonal architecture organization:

- **Infrastructure Layer**: CDK stacks, deployment scripts, and infrastructure utilities
- **Functions Layer**: AWS Lambda handlers and event processing
- **Domain Layer**: Business models and services with core logic
- **Ports Layer**: Interface definitions and abstract contracts
- **Adapters Layer**: External system integrations and AWS service implementations
- **Tests Layer**: Integration tests and testing utilities

## 🚀 Quick Start

### Local Development

1. **Set up the documentation environment:**

   ```bash
   task docs:setup
   ```

2. **Start the development server:**

   ```bash
   task docs:serve
   ```

3. **Open your browser to:** <http://localhost:8000>

### Configuration

The documentation system supports environment-based configuration for deployment customization.

#### Environment Configuration (.env.example)

The template includes a `.env.example` file with all available configuration options. For deployment, copy this file to `.env` and customize:

```bash
cp .env.example .env
```

**Available Environment Variables:**

- `DOCS_SITE_URL`: URL where documentation will be deployed (default: <http://localhost:8000>)
- `DOCS_REPO_URL`: Repository URL for source code links and "Edit this page" functionality
- `DOCS_REPO_NAME`: Display name for the repository
- `DOCS_EDIT_URI`: Path for "Edit this page" links (default: edit/main/)

#### Platform-Specific Examples

The `.env.example` file includes ready-to-use configurations for popular platforms:

**GitHub Pages:**

```bash
DOCS_SITE_URL=https://username.github.io/{{cookiecutter.project_name}}
DOCS_REPO_URL=https://github.com/username/{{cookiecutter.project_name}}
DOCS_EDIT_URI=edit/main/
```

**GitLab Pages:**

```bash
DOCS_SITE_URL=https://username.gitlab.io/{{cookiecutter.project_name}}
DOCS_REPO_URL=https://gitlab.com/username/{{cookiecutter.project_name}}
DOCS_EDIT_URI=edit/main/
```

**Custom Domain:**

```bash
DOCS_SITE_URL=https://docs.yourcompany.com
DOCS_REPO_URL=https://github.com/yourcompany/{{cookiecutter.project_name}}
DOCS_EDIT_URI=edit/main/
```

#### Local Development

For local development, no configuration is needed - the system uses sensible defaults. The `.env` file is optional and only required for deployment customization.

## 📁 Directory Structure

```text
docs/
├── README.md              # This file
├── .env.example           # Environment configuration template
├── mkdocs.yml            # MkDocs configuration
├── requirements.txt      # Documentation dependencies
├── Taskfile.yml         # Documentation tasks
├── validate_setup.py    # Setup validation script
├── index.md             # Documentation homepage
├── assets/              # Custom CSS and JavaScript
│   ├── css/custom.css
│   └── js/custom.js
└── reference/           # API reference documentation
    ├── infrastructure.md  # All infrastructure components
    ├── functions/         # Lambda handlers
    ├── shared/           # Domain, ports, and adapters
    └── tests/            # Testing utilities
```

## 🛠️ Available Tasks

Use the Taskfile to manage documentation:

```bash
# Set up documentation environment
task docs:setup

# Build documentation
task docs:build

# Serve documentation locally with hot reload
task docs:serve

# Clean generated files
task docs:clean

# Validate documentation setup
task docs:check

# Complete workflow (setup, build, validate)
task docs:all
```

## 🔧 Customization

### Theme and Styling

- **Custom CSS**: Edit `assets/css/custom.css`
- **Custom JavaScript**: Edit `assets/js/custom.js`
- **Theme configuration**: Modify the `theme` section in `mkdocs.yml`

### Navigation

Update the `nav` section in `mkdocs.yml` to customize the documentation structure.

### Plugins

The documentation system includes:

- **mkdocstrings**: Automatic API documentation from docstrings
- **search**: Full-text search functionality
- **Material theme**: Modern, responsive design

## 📝 Writing Documentation

### API Documentation

API documentation is automatically generated from Python docstrings using the Google docstring format:

```python
def example_function(param1: str, param2: int) -> bool:
    """Brief description of the function.

    Longer description with more details about what the function does,
    its behavior, and any important notes.

    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter.

    Returns:
        Description of the return value.

    Raises:
        ValueError: Description of when this exception is raised.

    Example:
        >>> result = example_function("hello", 42)
        >>> print(result)
        True
    """
    return True
```

### Manual Documentation

Add manual documentation pages in the `reference/` directory following the existing structure.

## 🚀 Deployment

### Environment-Aware Configuration

The documentation system automatically adapts to different environments:

- **Local Development**: Uses localhost URLs and minimal configuration
- **Deployment**: Uses environment variables for site URLs, repository links, and edit URIs

### CI/CD Integration

Set environment variables in your CI/CD pipeline:

```yaml
# Example for GitLab CI
variables:
  DOCS_SITE_URL: "https://$CI_PROJECT_NAMESPACE.gitlab.io/$CI_PROJECT_NAME"
  DOCS_REPO_URL: "$CI_PROJECT_URL"
  DOCS_REPO_NAME: "$CI_PROJECT_NAME"
  DOCS_EDIT_URI: "edit/main/"
```

Then build and deploy:

```bash
task docs:build-gitlab  # or task docs:build for generic deployment
```

## 🔍 Troubleshooting

### Common Issues

1. **Missing dependencies**: Run `task docs:setup` to install all required packages
2. **Build errors**: Run `task docs:check` to validate configuration
3. **Import errors**: Ensure your Python code is properly structured and importable

### Validation

Use the validation script to check your setup:

```bash
task docs:test-setup
```

This will verify:

- All dependencies are installed
- MkDocs configuration is valid
- Python paths are correctly configured
- Documentation can be built successfully

## 📚 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings](https://mkdocstrings.github.io/)
- [Google Docstring Format](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

## 🚀 Quick Start

### Prerequisites

- Python {{cookiecutter.python_version}}+
- [uv](https://github.com/astral-sh/uv) for Python package management
- [Task](https://taskfile.dev/) for task automation

### Setup and Build

```bash
# Set up documentation environment
task docs:setup

# Build documentation
task docs:build

# Serve documentation locally with hot reload
task docs:serve

# Open your browser to http://127.0.0.1:8000
```

### Development Workflow

```bash
# Check configuration and setup
task docs:check

# Test the documentation setup
task docs:test-setup

# Development mode with auto-reload
task docs:dev

# Validate the built documentation
task docs:validate

# Complete workflow (setup, build, validate)
task docs:all

# Clean generated files
task docs:clean
```

## 📖 Available Tasks

| Task | Description |
|------|-------------|
| `task docs:setup` | Set up documentation environment and install dependencies |
| `task docs:build` | Build static documentation |
| `task docs:serve` | Serve documentation locally with hot reload |
| `task docs:dev` | Development mode with auto-reload |
| `task docs:clean` | Clean generated documentation files |
| `task docs:check` | Check documentation configuration |
| `task docs:test-setup` | Test documentation setup and configuration |
| `task docs:validate` | Validate built documentation and check for issues |
| `task docs:gitlab` | Prepare documentation for GitLab Pages deployment |
| `task docs:all` | Complete workflow: setup, validate, build, and check |

## 🔧 Configuration

### MkDocs Configuration (`mkdocs.yml`)

The MkDocs configuration includes:

- **Material Theme**: Modern, responsive design with dark/light mode
- **mkdocstrings Plugin**: Automatic API documentation from docstrings
- **Navigation**: Organized by hexagonal architecture layers
- **Search**: Enhanced search functionality with suggestions
- **Code Highlighting**: Syntax highlighting for code examples
- **Mermaid Diagrams**: Support for architectural diagrams

### Dependencies (`requirements.txt`)

Core documentation dependencies:

- `mkdocs>=1.5.0` - Static site generator
- `mkdocs-material>=9.4.0` - Material Design theme
- `mkdocstrings[python]>=0.24.0` - Python docstring extraction
- `mkdocs-gen-files>=0.5.0` - Dynamic file generation
- `mkdocs-literate-nav>=0.6.0` - Navigation from markdown
- `mkdocs-section-index>=0.3.0` - Section index pages

## 📝 Writing Documentation

### Docstring Standards

Use Google-style docstrings for all public classes and methods:

```python
class ExampleService:
    """Service for handling example operations.

    This service demonstrates proper docstring formatting for
    automatic documentation generation.
    """

    def process_data(self, data: str, options: dict = None) -> str:
        """Process input data with optional configuration.

        Args:
            data: The input data to process
            options: Optional configuration parameters

        Returns:
            Processed data as a string

        Raises:
            ValueError: If data is empty or invalid

        Example:
            ```python
            service = ExampleService()
            result = service.process_data("input", {"format": "json"})
            ```
        """
        # Implementation here
        pass
```

### Architecture Layer Organization

Place your code in the appropriate hexagonal architecture layer:

- **Domain Models**: `src/shared/domain/models/`
- **Domain Services**: `src/shared/domain/services/`
- **Ports**: `src/shared/ports/`
- **Adapters**: `src/shared/adapters/`
- **Functions**: `src/functions/`
- **Infrastructure**: `infrastructure/`
- **Tests**: `src/tests/`

The documentation will automatically organize your code by these layers.

## 🎨 Customization

### Custom Styling (`assets/css/custom.css`)

Add custom CSS to enhance the documentation appearance:

- Architecture layer indicators
- Improved code block styling
- Enhanced navigation
- Responsive design improvements

### Custom JavaScript (`assets/js/custom.js`)

Enhance functionality with custom JavaScript:

- Copy button for code blocks
- Smooth scrolling for anchor links
- Architecture layer indicators
- Enhanced search functionality
- Keyboard shortcuts (Ctrl/Cmd + K for search)

## 🔍 Validation and Testing

### Setup Validation

Run the validation script to check your documentation setup:

```bash
task docs:test-setup
```

This validates:

- Required files and directories exist
- Python modules have proper docstrings
- MkDocs configuration is valid
- Documentation generation works correctly

### Build Validation

After building documentation:

```bash
task docs:validate
```

This checks:

- Main index page exists
- Reference documentation generated
- No obvious broken links
- Build artifacts are complete

## 🚀 Deployment

### GitLab Pages

The documentation is configured for automatic deployment to GitLab Pages:

```bash
# Prepare for GitLab Pages deployment
task docs:gitlab
```

This will:

- Build the documentation
- Validate the build
- Prepare artifacts for GitLab CI/CD
- Display deployment information

### Local Preview

For local development and preview:

```bash
# Start development server
task docs:dev

# Or use the standard serve command
task docs:serve
```

The documentation will be available at `http://127.0.0.1:8000` with hot reload enabled.

## 🐛 Troubleshooting

### Common Issues

1. **Module Import Errors**
   - Ensure your Python modules are in the correct directories
   - Check that `src` and `infrastructure` are in the mkdocstrings paths
   - Verify your module structure follows the expected layout

2. **Missing Documentation**
   - Check that your Python files have proper docstrings
   - Ensure files are not excluded by the generation script
   - Verify the gen_ref_pages.py script can find your modules

3. **Build Failures**
   - Run `task docs:check` to validate configuration
   - Check the MkDocs configuration syntax
   - Ensure all dependencies are installed

4. **Styling Issues**
   - Check custom CSS in `assets/css/custom.css`
   - Verify Material theme configuration
   - Test in different browsers and screen sizes

### Getting Help

1. Run the validation script: `task docs:test-setup`
2. Check the configuration: `task docs:check`
3. Review the build output for error messages
4. Ensure your docstrings follow Google style format

## 📚 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings Documentation](https://mkdocstrings.github.io/)
- [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
