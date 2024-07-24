# Makefile

# Directory containing the main package
PACKAGE_DIR = aruco-object-drop

# Find all Python files in the main package and tests directories
PY_FILES = $(shell find $(PACKAGE_DIR) tests -name '*.py')

.PHONY: format

# Format all Python files in the specified directories
format: $(PY_FILES)
	@echo "Formatting Python files with black..."
	poetry run black $(PY_FILES)

.PHONY: check-format

# Check if Python files are formatted according to black
check-format:
	@echo "Checking Python files formatting with black..."
	poetry run black --check $(PY_FILES)

.PHONY: test

# Run tests using pytest
test:
	@echo "Running tests with pytest..."
	poetry run pytest