"""
Setup script for development installation.

This allows the project to be installed in development mode with:
pip install -e .

This enables clean imports without any path manipulation.
"""

from setuptools import find_namespace_packages, setup

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.1.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    # Core dependencies are in src/shared/requirements.txt
    # Development dependencies are in requirements-dev.txt
)
