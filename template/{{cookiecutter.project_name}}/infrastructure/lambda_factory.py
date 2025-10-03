"""
Lambda Factory for creating AWS Lambda functions with consistent configuration.
"""

import uuid
from dataclasses import dataclass, field

import aws_cdk as cdk
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_

# Import path constants
from config_path import LAMBDA_DIST
from constructs import Construct

# Constants
DEFAULT_TIMEOUT_SECONDS = 30


def _default_timeout() -> cdk.Duration:
    """Create default timeout duration."""
    return cdk.Duration.seconds(DEFAULT_TIMEOUT_SECONDS)


@dataclass
class LambdaConfig:
    """Configuration for Lambda function creation."""

    # Required parameters
    function_name: str
    handler: str

    # Optional parameters with defaults
    memory_size: int = 128
    timeout: cdk.Duration = field(default_factory=_default_timeout)
    runtime: lambda_.Runtime = lambda_.Runtime.PYTHON_3_11
    architecture: lambda_.Architecture = lambda_.Architecture.X86_64
    environment: dict[str, str] = field(default_factory=dict)
    layers: list[lambda_.ILayerVersion] = field(default_factory=list)
    tracing: lambda_.Tracing = lambda_.Tracing.ACTIVE
    description: str | None = None
    reserved_concurrent_executions: int | None = None
    role: iam.IRole | None = None
    tags: dict[str, str] = field(default_factory=dict)


class LambdaFactory:
    """Factory for creating AWS Lambda functions with consistent configuration."""

    def __init__(self, scope: Construct):
        """
        Initialize the Lambda factory.

        Args:
            scope: CDK construct scope
        """
        self.scope = scope

    def create_function(self, config: LambdaConfig) -> lambda_.Function:
        """
        Create a Lambda function with consistent configuration.

        Args:
            config: Lambda function configuration

        Returns:
            The created Lambda function
        """
        # Validate function path
        function_path = LAMBDA_DIST / config.function_name
        if not function_path.exists():
            msg = f"Function path does not exist: {function_path}"
            raise ValueError(msg)

        # Create role if not provided
        role = config.role or self._create_default_role(config.function_name)

        # Create function
        function = lambda_.Function(
            self.scope,
            id=f"{config.function_name}Function",
            handler=config.handler,
            runtime=config.runtime,
            architecture=config.architecture,
            memory_size=config.memory_size,
            timeout=config.timeout,
            environment=config.environment,
            layers=config.layers,
            tracing=config.tracing,
            description=config.description
            or f"Lambda function for {config.function_name}",
            reserved_concurrent_executions=config.reserved_concurrent_executions,
            role=role,
            code=lambda_.Code.from_asset(str(function_path)),
        )

        # Add tags
        resource_id = str(uuid.uuid4())
        tags = {
            "Name": config.function_name,
            "ResourceId": resource_id,
            **config.tags,
        }

        for key, value in tags.items():
            cdk.Tags.of(function).add(key, value)

        return function

    def _create_default_role(self, function_name: str) -> iam.Role:
        """
        Create a default IAM role for a Lambda function.

        Args:
            function_name: Name of the Lambda function

        Returns:
            The created IAM role
        """
        # Create role with basic Lambda execution permissions
        return iam.Role(
            self.scope,
            f"{function_name}Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSXRayDaemonWriteAccess"
                ),
            ],
        )
