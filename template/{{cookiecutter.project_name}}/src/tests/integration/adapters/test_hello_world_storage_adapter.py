"""
Integration tests for HelloWorldStorageAdapter.

Tests the adapter's interaction with DynamoDB and data persistence.
"""

import os

import pytest

# Clean imports without src/shared prefixes
from adapters.hello_world_storage_adapter import HelloWorldStorageAdapter
from models.hello_world_model import HelloWorld

# Import test utilities
from tests.utils.resource_discovery import get_dynamodb_table_name


@pytest.fixture(autouse=True)
def dynamodb_table():
    """Get DynamoDB table name and set environment variable."""
    table_name = get_dynamodb_table_name("GreetingsTable")
    os.environ["HELLO_WORLD_TABLE_NAME"] = table_name
    return table_name


class TestHelloWorldStorageAdapter:
    """Test suite for HelloWorldStorageAdapter."""

    def test_storage_adapter_direct(self):
        """Test HelloWorldStorageAdapter directly."""
        adapter = HelloWorldStorageAdapter()
        model = adapter.get_saved_greeting("Test")
        assert isinstance(model, HelloWorld)
        assert model.name == "Test"
        assert "Hello, Test!" in model.formatted_greeting

    def test_adapter_persistence(self):
        """Test that adapter can save and retrieve data."""
        adapter = HelloWorldStorageAdapter()

        # Create a greeting
        original_model = adapter.get_saved_greeting("PersistenceTest")

        # Verify the model was created correctly
        assert isinstance(original_model, HelloWorld)
        assert original_model.name == "PersistenceTest"
        assert "Hello, PersistenceTest!" in original_model.formatted_greeting

        # Retrieve the same greeting again
        retrieved_model = adapter.get_saved_greeting("PersistenceTest")

        # Verify consistency
        assert retrieved_model.name == original_model.name
        assert retrieved_model.formatted_greeting == original_model.formatted_greeting

    def test_adapter_different_names(self):
        """Test adapter with different names."""
        adapter = HelloWorldStorageAdapter()

        # Test multiple different names
        names = ["Alice", "Bob", "Charlie"]

        for name in names:
            model = adapter.get_saved_greeting(name)
            assert isinstance(model, HelloWorld)
            assert model.name == name
            assert f"Hello, {name}!" in model.formatted_greeting

    def test_adapter_initialization(self):
        """Test adapter initialization."""
        adapter = HelloWorldStorageAdapter()
        assert adapter is not None

        # Test that adapter can be used immediately
        model = adapter.get_saved_greeting("InitTest")
        assert isinstance(model, HelloWorld)
