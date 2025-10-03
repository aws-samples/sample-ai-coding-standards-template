"""
Configuration service for centralized application configuration.

This service provides a centralized way to access configuration values
with strict validation and no fallbacks.
"""

import logging
import os

logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    """Exception raised for configuration errors."""

    pass


class ConfigService:
    """
    Centralized configuration service.

    This service provides access to configuration values from environment
    variables with strict validation and no fallbacks.
    """

    # AWS Region
    AWS_REGION = "AWS_REGION"

    # DynamoDB Tables
    HELLO_WORLD_TABLE_NAME = (
        "HELLO_WORLD_TABLE_NAME"  # Changed from GREETINGS_TABLE_NAME
    )

    @staticmethod
    def get_required(key: str) -> str:
        """
        Get a required configuration value.

        Args:
            key: Configuration key (environment variable name)

        Returns:
            Configuration value

        Raises:
            ConfigurationError: If the configuration value is not found
        """
        value = os.environ.get(key)
        if value is None:
            error_message = f"Required configuration '{key}' not found"
            logger.error(error_message)
            raise ConfigurationError(error_message)
        return value


# Initialize singleton instance
config = ConfigService()
