"""
Port interface for hello world operations.
"""

from abc import ABC, abstractmethod

from models.hello_world_model import HelloWorld


class HelloWorldPort(ABC):
    """
    Port interface for hello world operations.
    """

    @abstractmethod
    def get_saved_greeting(self, name: str) -> HelloWorld:
        """
        Get a greeting for a name.

        Args:
            name: The name to greet

        Returns:
            HelloWorld model with greeting data
        """
        pass

    @abstractmethod
    def save_greeting(self, greeting: HelloWorld) -> None:
        """
        Save a greeting.

        Args:
            greeting: HelloWorld model to save
        """
        pass
