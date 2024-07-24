# Makefile

# Directory containing the main package
PACKAGE_DIR = aruco-object-drop

# Find all Python files in the main package and tests directories
PY_FILES = $(shell find $(PACKAGE_DIR) tests -name '*.py')

# STATIC TYPES AND DOCSTRINGS
# Check variable types
.PHONY: check-type
check-type:
	@echo "Running mypy for to check static types..."
	@poetry run mypy .

# Check docstring formatting
.PHONY: check-docstring
check-docstring:
	@echo "Running pydocstyle to check docstrings..."
	@poetry run pydocstyle .

# FORMAT, LINT, SAFETY, AND TEST
# Format all Python files using black
.PHONY: format
format: $(PY_FILES)
	@echo "Running black to format files..."
	@poetry run black $(PY_FILES)

# Lint the code using flake8
.PHONY: lint
lint:
	@echo "Running flake8 to lint..."
	@poetry run flake8 .

# Check for security vulnerabilities
.PHONY: safety
safety:
	@echo "Running safety to check for security vulnerabilities..."
	@poetry run safety check

# Run tests using pytest
.PHONY: test
test:
	@echo "Running tests with pytest..."
	@poetry run pytest

# HOOKS
# Run pre-commit hook
.PHONY: pre-commit
pre-commit: check-type check-docstring format lint safety
	@echo "Pre-commit hook complete."

# Run pre-push hook
.PHONY: pre-push
pre-push: test
	@echo "Pre-push hook complete."