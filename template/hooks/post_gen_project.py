#!/usr/bin/env python
"""
Post-generation script for cruft template.
"""
import os
import shutil
import subprocess
from pathlib import Path

# Get project directory
PROJECT_DIR = Path(os.getcwd())

# Initialize git repository
subprocess.run(["git", "init"], check=True)

# Add all files to git
subprocess.run(["git", "add", "."], check=True)

# Create initial commit
subprocess.run(["git", "commit", "-m", "Initial commit from cruft template"], check=True)

# Create directories
os.makedirs(PROJECT_DIR / "dist" / "functions", exist_ok=True)
os.makedirs(PROJECT_DIR / "dist" / "layers", exist_ok=True)
os.makedirs(PROJECT_DIR / "dist" / "shared", exist_ok=True)

# Remove example function if not needed
if "{{ cookiecutter.include_example_function }}" == "no":
    shutil.rmtree(PROJECT_DIR / "src" / "functions" / "hello_world")
    shutil.rmtree(PROJECT_DIR / "src" / "shared" / "adapters" / "hello_world_adapter.py")
    shutil.rmtree(PROJECT_DIR / "src" / "shared" / "domain" / "services" / "greeting_service.py")
    shutil.rmtree(PROJECT_DIR / "src" / "shared" / "ports" / "greeting_port.py")
    shutil.rmtree(PROJECT_DIR / "src" / "tests" / "integration" / "test_hello_world.py")
    shutil.rmtree(PROJECT_DIR / "src" / "tests" / "payloads" / "hello_world")

print("Project initialization complete!")
print("Next steps:")
print("Read README.md")
