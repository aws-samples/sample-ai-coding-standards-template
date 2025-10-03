"""
AWS resource discovery utility for pytest integration tests.

This module provides functionality to discover AWS resources by tags,
enabling tests to dynamically find resource names and ARNs without
hardcoding them in test files.
"""

import sys
import time
from pathlib import Path
from typing import Any

import boto3
from botocore.exceptions import ClientError

# Use test config for path management
parent_path = Path(__file__).parent / ".."
sys.path.insert(0, str(parent_path))

from test_config import TAG_KEY, TAG_VALUE  # noqa: E402

# Constants
MIN_ARN_PARTS = 6


# Create a simple config object for compatibility
class TestConfig:
    TAG_KEY = TAG_KEY
    TAG_VALUE = TAG_VALUE


infra_config = TestConfig()


class ResourceDiscovery:
    """
    Utility class for discovering AWS resources by tags.

    This class provides methods to find DynamoDB tables, S3 buckets,
    Lambda functions, and IAM roles by filtering on specific tags.
    """

    def __init__(self):
        """
        Initialize the resource discovery utility.

        Raises:
            ValueError: If application tags are not configured
        """
        # Validate application tag configuration
        self.application_tag_key = getattr(infra_config, "TAG_KEY", None)
        self.application_tag_value = getattr(infra_config, "TAG_VALUE", None)

        if not self.application_tag_key or not self.application_tag_value:
            msg = (
                f"Application tags are not configured. Ensure TAG_KEY and TAG_VALUE are set in infra_config. "
                f"Current values: TAG_KEY='{self.application_tag_key}', TAG_VALUE='{self.application_tag_value}'"
            )
            raise ValueError(msg)

        # Initialize AWS clients - let boto3 handle region management
        self.dynamodb = boto3.client("dynamodb")
        self.s3 = boto3.client("s3")
        self.iam = boto3.client("iam")
        self.lambda_client = boto3.client("lambda")
        self.resourcegroupstaggingapi = boto3.client("resourcegroupstaggingapi")

        # Get the region from boto3 session for reference
        self.region_name = boto3.Session().region_name

    def get_dynamodb_table_name(self, resource_id: str) -> str | None:
        """
        Get DynamoDB table name by resource ID tag.

        Args:
            resource_id: The ResourceId tag value to search for

        Returns:
            Table name if found, None otherwise
        """
        try:
            # Use Resource Groups Tagging API for efficient tag-based search
            response = self.resourcegroupstaggingapi.get_resources(
                ResourceTypeFilters=["dynamodb:table"],
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                    {"Key": "ResourceId", "Values": [resource_id]},
                ],
            )

            if response["ResourceTagMappingList"]:
                # Extract table name from ARN
                table_arn = response["ResourceTagMappingList"][0]["ResourceARN"]
                return table_arn.split("/")[-1]

            return None

        except ClientError as e:
            print(f"Error discovering DynamoDB table: {e}")
            return None

    def get_s3_bucket_name(self, resource_id: str) -> str | None:
        """
        Get S3 bucket name by resource ID tag.

        Args:
            resource_id: The ResourceId tag value to search for

        Returns:
            Bucket name if found, None otherwise
        """
        try:
            # Use Resource Groups Tagging API for efficient tag-based search
            response = self.resourcegroupstaggingapi.get_resources(
                ResourceTypeFilters=["s3:bucket"],
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                    {"Key": "ResourceId", "Values": [resource_id]},
                ],
            )

            if response["ResourceTagMappingList"]:
                # Extract bucket name from ARN
                bucket_arn = response["ResourceTagMappingList"][0]["ResourceARN"]
                return bucket_arn.split(":")[-1]

            return None

        except ClientError as e:
            print(f"Error discovering S3 bucket: {e}")
            return None

    def get_iam_role_arn(self, resource_id: str) -> str | None:
        """
        Get IAM role ARN by resource ID tag.

        Args:
            resource_id: The ResourceId tag value to search for

        Returns:
            Role ARN if found, None otherwise
        """
        try:
            # Use Resource Groups Tagging API for efficient tag-based search
            response = self.resourcegroupstaggingapi.get_resources(
                ResourceTypeFilters=["iam:role"],
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                    {"Key": "ResourceId", "Values": [resource_id]},
                ],
            )

            if response["ResourceTagMappingList"]:
                return response["ResourceTagMappingList"][0]["ResourceARN"]

            return None

        except ClientError as e:
            print(f"Error discovering IAM role: {e}")
            return None

    def get_lambda_function_name(self, resource_id: str) -> str | None:
        """
        Get Lambda function name by resource ID tag.

        Args:
            resource_id: The ResourceId tag value to search for

        Returns:
            Function name if found, None otherwise
        """
        try:
            # Use Resource Groups Tagging API for efficient tag-based search
            response = self.resourcegroupstaggingapi.get_resources(
                ResourceTypeFilters=["lambda:function"],
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                    {"Key": "ResourceId", "Values": [resource_id]},
                ],
            )

            if response["ResourceTagMappingList"]:
                # Extract function name from ARN
                function_arn = response["ResourceTagMappingList"][0]["ResourceARN"]
                return function_arn.split(":")[-1]

            return None

        except ClientError as e:
            print(f"Error discovering Lambda function: {e}")
            return None

    def get_all_application_resources(self) -> dict[str, list[dict[str, Any]]]:
        """
        Get all resources tagged with the application tag.

        Returns:
            Dictionary mapping resource types to lists of resource information
        """
        try:
            response = self.resourcegroupstaggingapi.get_resources(
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                ],
            )

            resources_by_type = {}

            for resource in response["ResourceTagMappingList"]:
                resource_arn = resource["ResourceARN"]
                resource_type = self._extract_resource_type(resource_arn)

                if resource_type not in resources_by_type:
                    resources_by_type[resource_type] = []

                # Extract ResourceId tag if present
                resource_id = None
                for tag in resource["Tags"]:
                    if tag["Key"] == "ResourceId":
                        resource_id = tag["Value"]
                        break

                resources_by_type[resource_type].append(
                    {
                        "arn": resource_arn,
                        "resource_id": resource_id,
                        "tags": resource["Tags"],
                    },
                )

            return resources_by_type

        except ClientError as e:
            print(f"Error discovering application resources: {e}")
            return {}

    def get_resource_by_id(self, resource_id: str) -> dict[str, Any] | None:
        """
        Get resource information by resource ID tag.

        Args:
            resource_id: The ResourceId tag value to search for

        Returns:
            Resource information dictionary if found, None otherwise
        """
        try:
            response = self.resourcegroupstaggingapi.get_resources(
                TagFilters=[
                    {
                        "Key": self.application_tag_key,
                        "Values": [self.application_tag_value],
                    },
                    {"Key": "ResourceId", "Values": [resource_id]},
                ],
            )

            if response["ResourceTagMappingList"]:
                resource = response["ResourceTagMappingList"][0]
                resource_arn = resource["ResourceARN"]
                resource_type = self._extract_resource_type(resource_arn)

                return {
                    "arn": resource_arn,
                    "type": resource_type,
                    "name": self._extract_resource_name(resource_arn, resource_type),
                    "resource_id": resource_id,
                    "tags": resource["Tags"],
                }

            return None

        except ClientError as e:
            print(f"Error discovering resource by ID: {e}")
            return None

    def _extract_resource_type(self, resource_arn: str) -> str:
        """
        Extract resource type from ARN.

        Args:
            resource_arn: AWS resource ARN

        Returns:
            Resource type string
        """
        # ARN format: arn:aws:service:region:account:resource-type/resource-name
        parts = resource_arn.split(":")
        if len(parts) >= MIN_ARN_PARTS:
            service = parts[2]
            resource_part = parts[5]

            if "/" in resource_part:
                resource_type = resource_part.split("/")[0]
                return f"{service}:{resource_type}"
            return f"{service}:{resource_part}"

        return "unknown"

    def _extract_resource_name(self, resource_arn: str, resource_type: str) -> str:
        """
        Extract resource name from ARN based on resource type.

        Args:
            resource_arn: AWS resource ARN
            resource_type: Resource type string

        Returns:
            Resource name
        """
        if resource_type.startswith("dynamodb:"):
            return resource_arn.split("/")[-1]
        if resource_type.startswith("s3:"):
            return resource_arn.split(":")[-1]
        if resource_type.startswith("iam:"):
            return resource_arn.split("/")[-1]
        if resource_type.startswith("lambda:"):
            return resource_arn.split(":")[-1]
        # Generic extraction
        if "/" in resource_arn:
            return resource_arn.split("/")[-1]
        return resource_arn.split(":")[-1]

    def get_tenant_test_resources(self) -> dict[str, str]:
        """
        Get all tenant-related test resources in a convenient format.

        Returns:
            Dictionary mapping resource types to resource names/ARNs
        """
        resources = {}

        # Get DynamoDB table
        table_name = self.get_dynamodb_table_name("tenant-prompt-table")
        if table_name:
            resources["dynamodb_table_name"] = table_name

        # Get S3 bucket
        bucket_name = self.get_s3_bucket_name("tenant-content-bucket")
        if bucket_name:
            resources["s3_bucket_name"] = bucket_name

        # Get IAM role
        role_arn = self.get_iam_role_arn("tenant-lambda-role")
        if role_arn:
            resources["iam_role_arn"] = role_arn

        return resources

    def wait_for_resource_availability(
        self,
        resource_id: str,
        max_attempts: int = 30,
        delay: int = 2,
    ) -> bool:
        """
        Wait for a resource to become available after deployment.

        Args:
            resource_id: The ResourceId tag value to search for
            max_attempts: Maximum number of attempts to find the resource
            delay: Delay between attempts in seconds

        Returns:
            True if resource is found, False if timeout
        """
        for attempt in range(max_attempts):
            resource = self.get_resource_by_id(resource_id)
            if resource:
                return True

            if attempt < max_attempts - 1:
                time.sleep(delay)

        return False


# Convenience functions for direct use in tests
def get_lambda_function_name(resource_id: str) -> str | None:
    """
    Convenience function to get Lambda function name by resource ID.

    Args:
        resource_id: The ResourceId tag value to search for

    Returns:
        Function name if found, None otherwise
    """
    discovery = ResourceDiscovery()
    return discovery.get_lambda_function_name(resource_id)


def get_dynamodb_table_name(resource_id: str) -> str | None:
    """
    Convenience function to get DynamoDB table name by resource ID.

    Args:
        resource_id: The ResourceId tag value to search for

    Returns:
        Table name if found, None otherwise
    """
    discovery = ResourceDiscovery()
    return discovery.get_dynamodb_table_name(resource_id)


def get_s3_bucket_name(resource_id: str) -> str | None:
    """
    Convenience function to get S3 bucket name by resource ID.

    Args:
        resource_id: The ResourceId tag value to search for

    Returns:
        Bucket name if found, None otherwise
    """
    discovery = ResourceDiscovery()
    return discovery.get_s3_bucket_name(resource_id)
