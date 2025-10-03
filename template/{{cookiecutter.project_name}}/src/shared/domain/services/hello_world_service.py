"""
Hello World service implementation.
"""

from adapters.hello_world_storage_adapter import HelloWorldStorageAdapter
from models.hello_world_model import HelloWorld
from ports.hello_world_port import HelloWorldPort


class HelloWorldService:
    """
    Service for managing hello world operations.
    """

    def __init__(self, hello_world_port: HelloWorldPort = None):
        """
        Initialize the service with dependency injection.

        Args:
            hello_world_port: Port for hello world operations (optional)
        """
        # Default to HelloWorldStorageAdapter if no adapter is provided
        self.hello_world_port = hello_world_port or HelloWorldStorageAdapter()

    def get_greeting(self, name: str) -> str:
        """
        Get a greeting for a name.

        Args:
            name: The name to greet

        Returns:
            A greeting message
        """
        greeting = self.hello_world_port.get_saved_greeting(name)
        return greeting.formatted_greeting

    def save_greeting(self, name: str, message: str) -> None:
        """
        Save a greeting for a name.

        Args:
            name: The name to greet
            message: The greeting message
        """
        greeting = HelloWorld(name=name, greeting=message)
        self.hello_world_port.save_greeting(greeting)
