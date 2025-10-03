"""
CDK app for the {{ cookiecutter.project_slug }} application.
"""

import os

import aws_cdk as cdk
from config import STACK_PREFIX
from stacks.hello_world_stack import HelloWorldStack

app = cdk.App()
# Add project-level tags to all resources
cdk.Tags.of(app).add("Project", STACK_PREFIX)
cdk.Tags.of(app).add("ManagedBy", "CDK")

# Get environment configuration from environment variables
env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION", "eu-west-1"),
)

# Create Hello World stack with prefix
hello_world_stack = HelloWorldStack(app, f"{STACK_PREFIX}-HelloWorldStack", env=env)

app.synth()
