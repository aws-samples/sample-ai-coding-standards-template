#!/usr/bin/env python
"""
Pre-generation script for cruft template.
"""
import re
import sys

# Validate project name
PROJECT_NAME = "{{ cookiecutter.project_name }}"
if not re.match(r"^[a-zA-Z][-a-zA-Z0-9_]+$", PROJECT_NAME):
    print(f"ERROR: {PROJECT_NAME} is not a valid project name!")
    print(
        "Project name should start with a letter and contain only letters, numbers, hyphens, and underscores."
    )
    sys.exit(1)

# Validate Python version
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
if not re.match(r"^\d+\.\d+$", PYTHON_VERSION):
    print(f"ERROR: {PYTHON_VERSION} is not a valid Python version!")
    print("Python version should be in the format X.Y (e.g., 3.11)")
    sys.exit(1)

print(f"Creating project {PROJECT_NAME} with Python {PYTHON_VERSION}...")
