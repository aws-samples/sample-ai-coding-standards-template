"""
Lambda utilities for integration tests - KISS approach.

Simple functions to find and invoke Lambda functions using Name tags.
"""

import json
import logging
from typing import Any

import boto3

logger = logging.getLogger(__name__)


def find_lambda_by_name(construct_id: str) -> str | None:
    """
    Find a Lambda function by its Name tag using Resource Groups Tagging API.

    Args:
        construct_id: The construct ID used when creating the Lambda in CDK

    Returns:
        Lambda function name or None if not found
    """
    try:
        # Use Resource Groups Tagging API for efficient tag-based filtering
        tagging_client = boto3.client("resourcegroupstaggingapi")

        response = tagging_client.get_resources(
            ResourceTypeFilters=["lambda:function"],
            TagFilters=[
                {
                    "Key": "Project",
                    "Values": ["hexagonal-architecture-serverless-python-cdk-project"],
                },
                {"Key": "Name", "Values": [construct_id]},
            ],
        )

        for resource in response.get("ResourceTagMappingList", []):
            function_arn = resource["ResourceARN"]
            # Extract function name from ARN (format: arn:aws:lambda:region:account:function:function-name)
            return function_arn.split(":")[-1]

        logger.warning("Lambda function with Name '%s' not found", construct_id)
        return None

    except Exception:
        logger.exception("Error finding Lambda function with Name '%s'", construct_id)
        raise


def invoke_lambda_by_name(construct_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """
    Find and invoke a Lambda function by its Name tag.

    Args:
        construct_id: The construct ID used when creating the Lambda in CDK
        payload: Function payload

    Returns:
        Function response
    """
    function_name = find_lambda_by_name(construct_id)
    if not function_name:
        msg = f"Lambda function with Name '{construct_id}' not found"
        raise ValueError(msg)

    lambda_client = boto3.client("lambda")

    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload),
        )

        return json.loads(response["Payload"].read())

    except Exception:
        logger.exception("Error invoking function %s", function_name)
        raise
