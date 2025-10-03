# Taskfile.dev Rules

## Overview

These rules define how to use [Taskfile.dev](https://taskfile.dev/) for managing recurring commands in terminal environments.

## Rules

1. **Use Taskfile.dev for project automation**
   - Create a `Taskfile.yml` in the root of each project
   - Use version '3' syntax for all Taskfiles

2. **Task naming conventions**
   - Use kebab-case for task names (e.g., `build-app`, `run-tests`)
   - Group related tasks with namespaces (e.g., `db:migrate`, `db:seed`)
   - Use descriptive names that clearly indicate the task's purpose

3. **Task documentation**
   - Add a `desc:` field to every task with a clear description
   - Document required environment variables in task descriptions
   - Include example usage in complex tasks

4. **Task organization**
   - Group related tasks using namespaces
   - Use `deps:` to define task dependencies
   - Create composite tasks for common workflows

5. **Environment variables**
   - Define project-specific variables in the `env:` section
   - Use `.env` files for sensitive or user-specific variables
   - Reference environment variables with `{% raw %}{{.ENV_VAR}}{% endraw %}`

6. **Task output**
   - Set appropriate `silent:` values based on verbosity needs
   - Use `prefix:` for multi-command tasks to improve output readability
   - Consider using `set: [pipefail]` for safer command chaining

7. **Includes and imports**
   - Break large Taskfiles into smaller files using `includes:`
   - Store reusable task templates in a central location
   - Import common tasks across multiple projects

8. **Error handling**
   - Use `ignore_error:` only when appropriate
   - Add validation steps for critical tasks
   - Implement proper exit codes for task failures

9. **Python project requirements**
   - Always include a task to set up a Python virtual environment using uv
   - Create tasks for managing dependencies with uv
   - Include tasks for common Python development workflows

10. **Path management**
    - Use consistent path variables in Taskfile commands
    - Define path variables at the top of your Taskfile:

      ```yaml
      vars:
        DIST_DIR: ./dist
        SRC_DIR: ./src
        LAMBDA_DIR: '{% raw %}{{.SRC_DIR}}{% endraw %}/functions'
      ```

    - Reference these variables in tasks:

      ```yaml
      tasks:
        build:
          cmds:
            - mkdir -p {% raw %}{{.DIST_DIR}}{% endraw %}
            - cp -r {% raw %}{{.LAMBDA_DIR}}{% endraw %}/* {% raw %}{{.DIST_DIR}}{% endraw %}/
      ```

## Best Practices

1. Always run `task --list` to see available tasks in a new project
2. Keep tasks focused on a single responsibility
3. Use variables to make tasks configurable
4. Leverage OS-specific variations with `platforms:` when needed
5. Consider using `interval:` for tasks that should run periodically
6. Add `status:` checks to avoid unnecessary task execution
