.PHONY: help install install-dev clean test coverage lint format type-check

help:
	@echo "Available commands:"
	@echo "  make install       - Install the package"
	@echo "  make install-dev   - Install the package with dev dependencies"
	@echo "  make clean         - Remove build artifacts"
	@echo "  make test          - Run tests"
	@echo "  make coverage      - Run tests with coverage report"
	@echo "  make lint          - Run linters (flake8)"
	@echo "  make format        - Format code with black and isort"
	@echo "  make type-check    - Run type checking with mypy"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

clean:
	rm -rf build/ dist/ *.egg-info htmlcov/ .pytest_cache/ .mypy_cache/ .coverage

test:
	pytest

coverage:
	pytest --cov=src --cov-report=html --cov-report=term-missing

lint:
	flake8 src/ tests/

format:
	black src/ tests/
	isort src/ tests/

type-check:
	mypy src/
