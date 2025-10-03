"""
Hello World Lambda function handler.
"""

import json
from typing import Any

from domain.services.hello_world_service import HelloWorldService


def lambda_handler(event: dict[str, Any], _context: Any) -> dict[str, Any]:
    """
    Hello World Lambda function handler.

    Args:
        event: Lambda event
        _context: Lambda context (unused)

    Returns:
        API Gateway response
    """
    try:
        # Parse name from event
        query_params = event.get("queryStringParameters") or {}
        name = query_params.get("name", "World")

        # Handle empty string names
        if not name or name.strip() == "":
            name = "World"

        # Initialize service (adapter is injected by default)
        service = HelloWorldService()

        # Get greeting
        greeting = service.get_greeting(name)

        # Return response
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": greeting}),
        }
    except Exception as e:
        # Log error
        print(f"Error getting greeting: {e!s}")

        # Return error response
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": f"Error: {e!s}"}),
        }
