"""
Integration tests for HelloWorldService.

Tests the service's business logic and coordination with adapters.
"""

import os

import pytest
from adapters.hello_world_storage_adapter import HelloWorldStorageAdapter

# Clean imports without src/shared prefixes
from domain.services.hello_world_service import HelloWorldService

# Import test utilities
from tests.utils.resource_discovery import get_dynamodb_table_name


@pytest.fixture(autouse=True)
def dynamodb_table():
    """Get DynamoDB table name and set environment variable."""
    table_name = get_dynamodb_table_name("GreetingsTable")
    os.environ["HELLO_WORLD_TABLE_NAME"] = table_name
    return table_name


class TestHelloWorldService:
    """Test suite for HelloWorldService."""

    def test_service_with_default_adapter(self):
        """Test HelloWorldService with default adapter."""
        service = HelloWorldService()
        greeting = service.get_greeting("Test")
        assert "Hello, Test!" in greeting

    def test_service_with_explicit_adapter(self):
        """Test HelloWorldService with explicit adapter."""
        adapter = HelloWorldStorageAdapter()
        service = HelloWorldService(hello_world_port=adapter)
        greeting = service.get_greeting("Test")
        assert "Hello, Test!" in greeting

    def test_service_integration(self):
        """Test HelloWorldService integration."""
        service = HelloWorldService()
        greeting = service.get_greeting("TestUser")
        assert "Hello, TestUser!" in greeting

    def test_service_default_adapter(self):
        """Test HelloWorldService with default adapter."""
        service = HelloWorldService()
        greeting = service.get_greeting("TestUser")
        assert "Hello, TestUser!" in greeting

    def test_service_business_logic(self):
        """Test service business logic coordination."""
        service = HelloWorldService()

        # Test multiple names to verify business logic
        names = ["Alice", "Bob", "Charlie", "Diana"]

        for name in names:
            greeting = service.get_greeting(name)
            assert f"Hello, {name}!" in greeting
            assert isinstance(greeting, str)
            assert len(greeting) > 0

    def test_service_adapter_integration(self):
        """Test service integration with different adapters."""
        # Test with default adapter
        service1 = HelloWorldService()
        greeting1 = service1.get_greeting("ServiceTest1")

        # Test with explicit adapter
        adapter = HelloWorldStorageAdapter()
        service2 = HelloWorldService(hello_world_port=adapter)
        greeting2 = service2.get_greeting("ServiceTest2")

        # Both should work correctly
        assert "Hello, ServiceTest1!" in greeting1
        assert "Hello, ServiceTest2!" in greeting2

    def test_service_consistency(self):
        """Test service consistency across multiple calls."""
        service = HelloWorldService()

        # Make multiple calls with the same name
        name = "ConsistencyTest"
        greeting1 = service.get_greeting(name)
        greeting2 = service.get_greeting(name)
        greeting3 = service.get_greeting(name)

        # All should return the same greeting
        assert greeting1 == greeting2 == greeting3
        assert f"Hello, {name}!" in greeting1
