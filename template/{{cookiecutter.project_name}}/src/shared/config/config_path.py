"""
Centralized path configuration for the src directory.
"""

from from_root import from_root

# Project root and main directories
PROJECT_ROOT = from_root()
SRC_ROOT = PROJECT_ROOT / "src"

# Lambda-specific paths
LAMBDA_ROOT = SRC_ROOT / "functions"
LAMBDA_SHARED = SRC_ROOT / "shared"
LAMBDA_LAYERS = SRC_ROOT / "layers"

# Test paths
TESTS_ROOT = SRC_ROOT / "tests"
UNIT_TESTS = TESTS_ROOT / "unit"
INTEGRATION_TESTS = TESTS_ROOT / "integration"
TEST_DATA = TESTS_ROOT / "payloads"


# Ensure critical directories exist
def ensure_directories_exist():
    """
    Ensure all critical directories exist.
    """
    directories = [
        SRC_ROOT,
        LAMBDA_ROOT,
        LAMBDA_SHARED,
        TESTS_ROOT,
        UNIT_TESTS,
        INTEGRATION_TESTS,
        TEST_DATA,
    ]

    for directory in directories:
        directory.mkdir(exist_ok=True, parents=True)


# Call this function if this script is run directly
if __name__ == "__main__":
    ensure_directories_exist()
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Source root: {SRC_ROOT}")
    print(f"Lambda root: {LAMBDA_ROOT}")
    print(f"Tests root: {TESTS_ROOT}")
