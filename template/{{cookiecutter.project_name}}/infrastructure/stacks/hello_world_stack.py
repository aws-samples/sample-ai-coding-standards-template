"""
Hello World CDK stack that creates a Lambda function using the Lambda factory.
"""

from aws_cdk import (
    RemovalPolicy,
    Stack,
    Tags,
)
from aws_cdk import (
    aws_apigateway as apigateway,
)
from aws_cdk import (
    aws_dynamodb as dynamodb,
)
from constructs import Construct
from lambda_factory import LambdaConfig, LambdaFactory


class HelloWorldStack(Stack):
    """
    CDK stack for the Hello World Lambda function.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """
        Initialize the Hello World stack.

        Args:
            scope: CDK app scope
            construct_id: CDK construct ID
            **kwargs: Additional arguments to pass to the Stack constructor
        """
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDB table for greetings
        greetings_table = dynamodb.Table(
            self,
            "GreetingsTable",
            partition_key=dynamodb.Attribute(
                name="name", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,  # For development only
        )

        # Add ResourceId tag to DynamoDB table
        Tags.of(greetings_table).add("ResourceId", "GreetingsTable")

        # Create Lambda factory
        lambda_factory = LambdaFactory(self)

        # Create Lambda function using the factory
        hello_function = lambda_factory.create_function(
            LambdaConfig(
                function_name="hello_world",
                handler="handler.lambda_handler",
                memory_size=256,
                environment={
                    "HELLO_WORLD_TABLE_NAME": greetings_table.table_name  # Changed from GREETINGS_TABLE_NAME
                },
            )
        )

        # Grant DynamoDB permissions to Lambda function
        greetings_table.grant_read_write_data(hello_function)

        # Create API Gateway
        api = apigateway.RestApi(
            self,
            "HelloWorldApi",
            rest_api_name="Hello World API",
            description="API for the Hello World Lambda function",
        )

        # Create API Gateway resource and method
        hello_resource = api.root.add_resource("hello")
        hello_integration = apigateway.LambdaIntegration(hello_function)
        hello_resource.add_method("GET", hello_integration)

        # Output API Gateway URL and table name
        self.api_url = api.url
        self.table_name = greetings_table.table_name
