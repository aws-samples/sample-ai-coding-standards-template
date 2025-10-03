"""
Integration tests for HelloWorld model.

Tests the domain model's validation, serialization, and business logic.
"""

from datetime import UTC, datetime

from models.hello_world_model import HelloWorld

# Constants
TIMESTAMP_TOLERANCE_SECONDS = 60


class TestHelloWorldModel:
    """Test suite for HelloWorld model."""

    def test_model_creation(self):
        """Test creating a HelloWorld model."""
        model = HelloWorld(name="Test", greeting="Custom greeting")
        assert model.name == "Test"
        assert model.greeting == "Custom greeting"
        assert model.created_at is not None
        assert model.updated_at is not None

    def test_default_greeting(self):
        """Test default greeting when none provided."""
        model = HelloWorld(name="Test", greeting=None)
        assert model.formatted_greeting == "Hello, Test!"

    def test_custom_greeting(self):
        """Test custom greeting."""
        model = HelloWorld(name="Test", greeting="Hi Test!")
        assert model.formatted_greeting == "Hi Test!"

    def test_to_and_from_dict(self):
        """Test dictionary serialization."""
        original = HelloWorld(name="Test", greeting="Hi Test!")
        data = original.to_dict()
        restored = HelloWorld.from_dict(data)
        assert restored.name == original.name
        assert restored.greeting == original.greeting
        assert restored.created_at == original.created_at
        assert restored.updated_at == original.updated_at

    def test_model_validation(self):
        """Test model validation rules."""
        # Test valid model
        model = HelloWorld(name="ValidName", greeting="Valid greeting")
        assert model.name == "ValidName"
        assert model.greeting == "Valid greeting"

    def test_model_timestamps(self):
        """Test model timestamp handling."""
        model = HelloWorld(name="TimestampTest", greeting="Test greeting")

        # Verify timestamps are set
        assert isinstance(model.created_at, datetime)
        assert isinstance(model.updated_at, datetime)

        # Verify timestamps are recent (within last minute)
        now = datetime.now(UTC)
        time_diff = now - model.created_at
        assert time_diff.total_seconds() < TIMESTAMP_TOLERANCE_SECONDS

    def test_model_equality(self):
        """Test model equality comparison."""
        model1 = HelloWorld(name="Test", greeting="Hello")
        model2 = HelloWorld(name="Test", greeting="Hello")

        # Models with same data should be equal (based on name)
        assert model1.name == model2.name

    def test_formatted_greeting_logic(self):
        """Test formatted greeting business logic."""
        # Test with custom greeting
        model1 = HelloWorld(name="Alice", greeting="Hi Alice!")
        assert model1.formatted_greeting == "Hi Alice!"

        # Test with None greeting (should use default)
        model2 = HelloWorld(name="Bob", greeting=None)
        assert model2.formatted_greeting == "Hello, Bob!"

        # Test with empty greeting (should use default)
        model3 = HelloWorld(name="Charlie", greeting="")
        assert model3.formatted_greeting == "Hello, Charlie!"

    def test_model_serialization_roundtrip(self):
        """Test complete serialization roundtrip."""
        # Create model with all fields
        original = HelloWorld(
            name="SerializationTest", greeting="Custom serialization greeting"
        )

        # Convert to dict and back
        data = original.to_dict()
        restored = HelloWorld.from_dict(data)

        # Verify all fields are preserved
        assert restored.name == original.name
        assert restored.greeting == original.greeting
        assert restored.formatted_greeting == original.formatted_greeting
        assert restored.created_at == original.created_at
        assert restored.updated_at == original.updated_at

    def test_model_with_special_characters(self):
        """Test model with special characters in name and greeting."""
        special_names = ["José", "François", "李明", "محمد"]

        for name in special_names:
            model = HelloWorld(
                name=name, greeting=None
            )  # Use None to trigger default greeting
            assert model.name == name
            assert f"Hello, {name}!" in model.formatted_greeting

            # Test serialization with special characters
            data = model.to_dict()
            restored = HelloWorld.from_dict(data)
            assert restored.name == name

    def test_model_with_none_greeting(self):
        """Test model behavior with None greeting."""
        model = HelloWorld(name="TestUser", greeting=None)
        assert model.name == "TestUser"
        assert model.greeting is None
        assert model.formatted_greeting == "Hello, TestUser!"

    def test_model_with_empty_string_greeting(self):
        """Test model behavior with empty string greeting."""
        model = HelloWorld(name="TestUser", greeting="")
        assert model.name == "TestUser"
        assert model.greeting == ""
        assert model.formatted_greeting == "Hello, TestUser!"
