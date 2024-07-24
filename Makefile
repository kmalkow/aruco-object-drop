# Makefile

# Directory containing the main package
PACKAGE_DIR = aruco-object-drop

# Find all Python files in the main package and tests directories
PY_FILES = $(shell find $(PACKAGE_DIR) tests -name '*.py')

# Check variable types
.PHONY: check-type
check-type:
	@echo "Running mypy for type checking..."
	@-poetry run mypy .

# Check docstring formatting
.PHONY: check-docstring
check-docstring:
	@echo "Running pydocstyle to check docstrings..."
	@-poetry run pydocstyle .

# Check if Python files are formatted according to black
.PHONY: check-format
check-format:
	@echo "Running black to check formatting..."
	@-poetry run black --check $(PY_FILES)

# Run all checks
.PHONY: checks
checks: check-type check-docstring check-format
	@echo "All checks complete."

# Format all Python files in the specified directories
.PHONY: format
format: $(PY_FILES)
	@echo "Running black to format files..."
	@poetry run black $(PY_FILES)

# Run tests using pytest
.PHONY: test
test:
	@echo "Running tests with pytest..."
	@poetry run pytest