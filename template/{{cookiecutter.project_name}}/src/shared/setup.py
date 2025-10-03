"""
Setup script for shared package.

This allows the shared code to be installed as an editable package,
enabling clean imports without any path manipulation.
"""

from setuptools import find_packages, setup

setup(
    name="shared",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "pydantic>=2.4.0",
        "boto3>=1.28.0",
    ],
)
