"""
Test configuration and fixtures.
"""

from unittest.mock import MagicMock

import pytest


@pytest.fixture
def lambda_event():
    """Fixture providing a mock Lambda event for testing."""
    return {
        "queryStringParameters": {"name": "TestUser"},
        "httpMethod": "GET",
        "headers": {"Content-Type": "application/json"},
        "body": None,
        "isBase64Encoded": False,
        "pathParameters": None,
        "requestContext": {
            "requestId": "test-request-id",
            "stage": "test",
            "httpMethod": "GET",
        },
    }


@pytest.fixture
def lambda_context():
    """Fixture providing a mock Lambda context for testing."""
    context = MagicMock()
    context.function_name = "test-function"
    context.function_version = "$LATEST"
    context.invoked_function_arn = (
        "arn:aws:lambda:us-east-1:123456789012:function:test-function"
    )
    context.memory_limit_in_mb = "256"
    context.remaining_time_in_millis = lambda: 30000
    context.aws_request_id = "test-request-id"
    context.log_group_name = "/aws/lambda/test-function"
    context.log_stream_name = "2023/01/01/[$LATEST]test-stream"
    return context
