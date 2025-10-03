"""
Hello World domain model.
"""

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class HelloWorld:
    """
    Hello World domain model.

    This model represents a greeting with its associated metadata.
    """

    name: str
    greeting: str
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        """Initialize timestamps if not provided."""
        if not self.created_at:
            self.created_at = datetime.now(UTC)
        if not self.updated_at:
            self.updated_at = self.created_at

    @property
    def formatted_greeting(self) -> str:
        """Get the formatted greeting message."""
        return self.greeting or f"Hello, {self.name}!"

    def to_dict(self) -> dict:
        """Convert model to dictionary for storage."""
        return {
            "name": self.name,
            "greeting": self.greeting,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "HelloWorld":
        """Create model from dictionary data."""
        return cls(
            name=data["name"],
            greeting=data.get("greeting"),
            created_at=(
                datetime.fromisoformat(data["created_at"])
                if "created_at" in data
                else None
            ),
            updated_at=(
                datetime.fromisoformat(data["updated_at"])
                if "updated_at" in data
                else None
            ),
        )
