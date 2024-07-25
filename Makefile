# Makefile

# Directory containing the main package
PACKAGE_DIR = aruco-object-drop

# Find all Python files in the main package and tests directories
PY_FILES = $(shell find $(PACKAGE_DIR) tests -name '*.py')
TEST_FILES = $(shell find tests -name 'test_*.py')

# CHECKING STATIC TYPES AND DOCSTRINGS
# Check variable types
.PHONY: check-type
check-type:
	@echo "🔍 Checking static types (mypy)..."
	@if [ -n "$(PY_FILES)" ]; then \
		poetry run mypy $(PACKAGE_DIR) tests; \
	else \
		echo "No Python files found for type checking."; \
	fi

# Check docstring formatting
.PHONY: check-docstring
check-docstring:
	@echo "🔍 Checking docstrings (pydocstyle)..."
	@if [ -n "$(PY_FILES)" ]; then \
		poetry run pydocstyle --ignore D104 $(PACKAGE_DIR) tests; \
	else \
		echo "No Python files found for docstring checking."; \
	fi

# FORMATTING, LINTING, AND TESTING
# Format all Python files using black
.PHONY: format
format: $(PY_FILES)
	@echo "🔧 Formatting files (black)..."
	@if [ -n "$(PY_FILES)" ]; then \
		poetry run black $(PY_FILES); \
	else \
		echo "No Python files found for formatting."; \
	fi

# Lint the code using flake8
.PHONY: lint
lint:
	@echo "🔧 Linting files (flake8)..."
	@if [ -n "$(PY_FILES)" ]; then \
		poetry run flake8 $(PY_FILES); \
	else \
		echo "No Python files found for linting."; \
	fi

# Run tests using pytest
.PHONY: test
test:
	@echo "🔧 Testing files (pytest)..."
	@if [ -n "$(TEST_FILES)" ]; then \
		poetry run pytest; \
	else \
		echo "No test files found. Skipping tests."; \
	fi

# HOOKS
# Run pre-commit hook
.PHONY: pre-commit
pre-commit: check-type check-docstring format lint

# Run pre-push hook
.PHONY: pre-push
pre-push: test
