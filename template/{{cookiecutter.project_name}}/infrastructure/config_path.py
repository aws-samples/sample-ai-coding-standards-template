"""
Centralized path configuration for the infrastructure directory.
"""

from from_root import from_root

# Project root and main directories
PROJECT_ROOT = from_root()
INFRASTRUCTURE_ROOT = PROJECT_ROOT / "infrastructure"
SRC_ROOT = PROJECT_ROOT / "src"
DIST_ROOT = PROJECT_ROOT / "dist"

# Infrastructure paths
CDK_STACKS = INFRASTRUCTURE_ROOT / "stacks"
CDK_CONSTRUCTS = INFRASTRUCTURE_ROOT / "constructs"
SCRIPTS_ROOT = INFRASTRUCTURE_ROOT / "scripts"

# Distribution paths
LAMBDA_DIST = DIST_ROOT / "functions"
LAMBDA_DIST_LAYERS = DIST_ROOT / "layers"
LAMBDA_DIST_SHARED = DIST_ROOT / "shared"

# Source paths (needed for build scripts)
LAMBDA_ROOT = SRC_ROOT / "functions"
LAMBDA_SHARED = SRC_ROOT / "shared"
LAMBDA_LAYERS = SRC_ROOT / "layers"
LAMBDA_FUNCTIONS = SRC_ROOT / "functions"  # Fixed path


# Ensure critical directories exist
def ensure_directories_exist():
    """
    Ensure all critical directories exist.
    """
    directories = [
        INFRASTRUCTURE_ROOT,
        CDK_STACKS,
        CDK_CONSTRUCTS,
        SCRIPTS_ROOT,
        DIST_ROOT,
        LAMBDA_DIST,
        LAMBDA_DIST_LAYERS,
        LAMBDA_DIST_SHARED,
    ]

    for directory in directories:
        directory.mkdir(exist_ok=True, parents=True)


# Call this function if this script is run directly
if __name__ == "__main__":
    ensure_directories_exist()
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Infrastructure root: {INFRASTRUCTURE_ROOT}")
    print(f"Distribution root: {DIST_ROOT}")
