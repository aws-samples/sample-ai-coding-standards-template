"""
DynamoDB adapter for hello world storage.
"""

from datetime import UTC, datetime

import boto3
from botocore.exceptions import ClientError
from config.config_service import config
from models.hello_world_model import HelloWorld
from ports.hello_world_port import HelloWorldPort


class HelloWorldStorageAdapter(HelloWorldPort):
    """
    DynamoDB adapter for storing hello world data.
    """

    def __init__(self):
        """Initialize the DynamoDB adapter."""
        self.table_name = config.get_required(config.HELLO_WORLD_TABLE_NAME)
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)

    def get_saved_greeting(self, name: str) -> HelloWorld:
        """
        Get a greeting for a name from DynamoDB.

        Args:
            name: The name to greet

        Returns:
            HelloWorld model with greeting data
        """
        try:
            response = self.table.get_item(Key={"name": name})
            if "Item" in response:
                return HelloWorld.from_dict(response["Item"])
            return HelloWorld(name=name, greeting=None)  # Will use default greeting
        except ClientError as e:
            print(f"Error getting greeting: {e!s}")
            return HelloWorld(name=name, greeting=None)  # Will use default greeting

    def save_greeting(self, greeting: HelloWorld) -> None:
        """
        Save a greeting to DynamoDB.

        Args:
            greeting: HelloWorld model to save
        """
        try:
            # Update the updated_at timestamp
            greeting.updated_at = datetime.now(UTC)
            self.table.put_item(Item=greeting.to_dict())
        except ClientError as e:
            print(f"Error saving greeting: {e!s}")
            raise
