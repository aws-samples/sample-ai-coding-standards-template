"""
Integration tests for Hello World Lambda function handler.

Tests the Lambda handler's request/response processing and integration with services.
"""

import json
import os

import pytest

from functions.hello_world.handler import lambda_handler
from tests.utils.resource_discovery import get_dynamodb_table_name

# Constants
HTTP_OK = 200
HTTP_INTERNAL_SERVER_ERROR = 500


@pytest.fixture
def lambda_event():
    """Create a sample Lambda event."""
    return {
        "resource": "/hello",
        "path": "/hello",
        "httpMethod": "GET",
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "requestContext": {},
        "body": None,
        "isBase64Encoded": False,
    }


@pytest.fixture
def lambda_context():
    """Create a sample Lambda context."""

    class MockContext:
        def __init__(self):
            self.function_name = "test-function"
            self.function_version = "$LATEST"
            self.invoked_function_arn = (
                "arn:aws:lambda:us-east-1:123456789012:function:test-function"
            )
            self.memory_limit_in_mb = 128
            self.aws_request_id = "test-request-id"
            self.log_group_name = "/aws/lambda/test-function"
            self.log_stream_name = "2021/01/01/[$LATEST]test-stream"

    return MockContext()


@pytest.fixture(autouse=True)
def dynamodb_table():
    """Get DynamoDB table name and set environment variable."""
    table_name = get_dynamodb_table_name("GreetingsTable")
    os.environ["HELLO_WORLD_TABLE_NAME"] = table_name
    return table_name


class TestLambdaHandler:
    """Test suite for Lambda handler."""

    def test_lambda_handler_success(self, lambda_event, lambda_context):
        """Test successful Lambda handler invocation."""
        # Update event with test name
        lambda_event["queryStringParameters"] = {"name": "TestUser"}

        # Invoke handler
        response = lambda_handler(lambda_event, lambda_context)

        # Check response structure
        assert response["statusCode"] == HTTP_OK
        assert "Content-Type" in response["headers"]
        assert response["headers"]["Content-Type"] == "application/json"

        # Parse response body
        body = json.loads(response["body"])
        assert "message" in body
        assert "Hello, TestUser!" in body["message"]

    def test_lambda_handler_default_name(self, lambda_event, lambda_context):
        """Test Lambda handler with default name."""
        # Remove name from query parameters
        lambda_event["queryStringParameters"] = {}

        # Invoke handler
        response = lambda_handler(lambda_event, lambda_context)

        # Check response
        assert response["statusCode"] == HTTP_OK
        body = json.loads(response["body"])
        assert "Hello, World!" in body["message"]

    def test_lambda_handler_no_query_params(self, lambda_event, lambda_context):
        """Test Lambda handler with no query parameters."""
        # Set query parameters to None
        lambda_event["queryStringParameters"] = None

        # Invoke handler
        response = lambda_handler(lambda_event, lambda_context)

        # Check response
        assert response["statusCode"] == HTTP_OK
        body = json.loads(response["body"])
        assert "Hello, World!" in body["message"]

    def test_lambda_handler_empty_name(self, lambda_event, lambda_context):
        """Test Lambda handler with empty name parameter."""
        # Set empty name
        lambda_event["queryStringParameters"] = {"name": ""}

        # Invoke handler
        response = lambda_handler(lambda_event, lambda_context)

        # Check response
        assert response["statusCode"] == HTTP_OK
        body = json.loads(response["body"])
        assert "Hello, World!" in body["message"]

    def test_lambda_handler_multiple_names(self, lambda_event, lambda_context):
        """Test Lambda handler with multiple different names."""
        names = ["Alice", "Bob", "Charlie", "Diana"]

        for name in names:
            # Update event with test name
            lambda_event["queryStringParameters"] = {"name": name}

            # Invoke handler
            response = lambda_handler(lambda_event, lambda_context)

            # Check response
            assert response["statusCode"] == HTTP_OK
            body = json.loads(response["body"])
            assert f"Hello, {name}!" in body["message"]

    def test_lambda_handler_response_format(self, lambda_event, lambda_context):
        """Test Lambda handler response format compliance."""
        lambda_event["queryStringParameters"] = {"name": "FormatTest"}

        # Invoke handler
        response = lambda_handler(lambda_event, lambda_context)

        # Verify response structure
        assert isinstance(response, dict)
        assert "statusCode" in response
        assert "headers" in response
        assert "body" in response

        # Verify headers
        assert isinstance(response["headers"], dict)
        assert "Content-Type" in response["headers"]

        # Verify body is valid JSON
        body = json.loads(response["body"])
        assert isinstance(body, dict)
        assert "message" in body

    def test_lambda_handler_special_characters(self, lambda_event, lambda_context):
        """Test Lambda handler with special characters in name."""
        special_names = ["José", "François", "李明", "محمد"]

        for name in special_names:
            lambda_event["queryStringParameters"] = {"name": name}
            response = lambda_handler(lambda_event, lambda_context)

            assert response["statusCode"] == HTTP_OK
            body = json.loads(response["body"])
            assert f"Hello, {name}!" in body["message"]
