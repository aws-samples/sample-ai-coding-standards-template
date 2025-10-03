"""
Lambda build script.

This script builds Lambda functions and shared layers for deployment.
"""

import logging
import shutil
import subprocess
import sys
from pathlib import Path
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add infrastructure directory to path
infrastructure_dir = Path(__file__).parent.parent.absolute()
if str(infrastructure_dir) not in sys.path:
    sys.path.insert(0, str(infrastructure_dir))

from config_path import (  # noqa: E402
    LAMBDA_DIST,
    LAMBDA_DIST_SHARED,
    LAMBDA_FUNCTIONS,
    LAMBDA_SHARED,
    PROJECT_ROOT,
)


class LambdaBuild:
    """
    Lambda build process implementation.
    """

    def __init__(self):
        """Initialize build paths."""
        self.dist_dir = LAMBDA_DIST
        # self.layers_dir = LAMBDA_DIST_LAYERS
        self.shared_dir = LAMBDA_DIST_SHARED

        # Remove dist directories to be cleaned
        if self.dist_dir.exists():
            logger.info("Clean dir folders before building functions")
            shutil.rmtree(self.dist_dir)
        if self.shared_dir.exists():
            shutil.rmtree(self.shared_dir)

        # Create dist directories
        logger.info("Create dist folders")
        self.dist_dir.mkdir(parents=True, exist_ok=True)
        self.shared_dir.mkdir(parents=True, exist_ok=True)

    def build_all(self) -> bool:
        """
        Build all Lambda functions and shared layer.

        Returns:
            True if build was successful, False otherwise
        """

        # Build shared layer first
        if not self.build_shared():
            return False

        # Build each function
        for function_dir in LAMBDA_FUNCTIONS.iterdir():
            if (
                function_dir.is_dir()
                and not function_dir.name.startswith(".")
                and not self.build_function(function_dir)
            ):
                return False

        return True

    def build_function(self, function_src: Path) -> bool:
        """
        Build a Lambda function.

        Args:
            function_src: Source directory of the function

        Returns:
            True if build was successful, False otherwise
        """
        function_name = function_src.name
        function_dist = self.dist_dir / function_name

        logger.info(f"Building function: {function_name}")

        # Clean and create function dist directory
        if function_dist.exists():
            shutil.rmtree(function_dist)
        function_dist.mkdir(parents=True, exist_ok=True)

        # Copy function code
        for item in function_src.iterdir():
            if item.is_file() and item.suffix in [
                ".py",
                ".json",
                ".opml",
                ".yaml",
                ".yml",
            ]:
                shutil.copy2(item, function_dist / item.name)

        # Copy .project-root file if it exists in project root
        project_root_file = PROJECT_ROOT / ".project-root"
        if project_root_file.exists():
            shutil.copy2(project_root_file, function_dist / ".project-root")

        # Copy shared code for inline deployment
        # This allows imports like 'from domain.services.greeting_service import GreetingService'
        if LAMBDA_SHARED.exists():
            logger.debug(f"Copying shared code for function: {function_name}")
            self._copy_shared_for_inline(LAMBDA_SHARED, function_dist)

        # Install dependencies if requirements.txt exists
        requirements_file = function_src / "requirements.txt"
        if requirements_file.exists():
            logger.debug(f"Installing requirements for function: {function_name}")
            if not self._install_requirements(requirements_file, function_dist):
                return False

        logger.info(f"Successfully built function: {function_name}")
        return True

    def _copy_shared_for_inline(self, shared_src: Path, function_dist: Path) -> None:
        """
        Copy shared code for inline deployment without the 'shared' directory structure.

        This copies the contents of src/shared/ directly into the function directory,
        allowing clean imports without the 'shared' prefix.

        Args:
            shared_src: Source shared directory (src/shared)
            function_dist: Function distribution directory
        """
        # Copy each subdirectory of shared directly to function root
        for item in shared_src.iterdir():
            if (
                item.is_dir()
                and not item.name.startswith(".")
                and item.name != "__pycache__"
            ):
                target_dir = function_dist / item.name
                if target_dir.exists():
                    shutil.rmtree(target_dir)
                shutil.copytree(item, target_dir)
            elif (
                item.is_file()
                and item.suffix == ".py"
                and not item.name.startswith(".")
            ):
                # Copy Python files from shared root
                shutil.copy2(item, function_dist / item.name)

        # Copy shared dependencies to function directory
        if self.shared_dir.exists():
            logger.debug("Copying shared dependencies to function")
            for item in self.shared_dir.iterdir():
                if item.name == "shared":
                    # Skip the shared code directory as it's already copied above
                    continue
                if item.is_dir() and not item.name.startswith("."):
                    target_dir = function_dist / item.name
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.copytree(item, target_dir)
                elif item.is_file() and not item.name.startswith("."):
                    shutil.copy2(item, function_dist / item.name)

    def build_shared(self) -> bool:
        """
        Build shared layer.

        Returns:
            True if build was successful, False otherwise
        """
        logger.info("Building shared dependencies")

        # Clean and create shared dist directory
        if self.shared_dir.exists():
            shutil.rmtree(self.shared_dir)
        self.shared_dir.mkdir(parents=True, exist_ok=True)

        # Copy shared code
        if LAMBDA_SHARED.exists():
            logger.debug("Copying shared code to distribution directory")
            shutil.copytree(LAMBDA_SHARED, self.shared_dir / "shared")

        # Install shared dependencies
        requirements_file = LAMBDA_SHARED / "requirements.txt"
        if requirements_file.exists():
            logger.debug("Installing shared dependencies")
            if not self._install_requirements(requirements_file, self.shared_dir):
                return False

        logger.info("Successfully built shared dependencies")
        return True

    def _install_requirements(self, requirements_file: Path, target_dir: Path) -> bool:
        """
        Install Python dependencies from requirements.txt.

        Args:
            requirements_file: Path to requirements.txt
            target_dir: Directory to install dependencies in

        Returns:
            True if installation was successful, False otherwise
        """
        try:
            # Use uv with python-platform specification for Lambda (Linux x86_64)
            # Allow building from source for packages without Linux wheels
            subprocess.run(
                [
                    "uv",
                    "pip",
                    "install",
                    "-r",
                    str(requirements_file),
                    "--target",
                    str(target_dir),
                    "--no-cache-dir",
                    "--quiet",
                    "--python-platform",
                    "x86_64-unknown-linux-gnu",
                ],
                check=True,
            )
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Error installing requirements: {e!s}")
            return False


if __name__ == "__main__":
    builder = LambdaBuild()
    if not builder.build_all():
        sys.exit(1)
