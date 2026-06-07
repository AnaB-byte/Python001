# Python001

A Python project template with best practices.

## Project Structure

```
Python001/
├── src/python001/          # Main package
│   ├── __init__.py
│   └── main.py
├── tests/                  # Test files
│   ├── conftest.py
│   └── test_main.py
├── pyproject.toml          # Project configuration
├── requirements.txt        # Development dependencies
├── Makefile               # Common commands
└── README.md              # This file
```

## Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   make install-dev
   ```

## Usage

### Run the main module

```bash
python -m python001.main
```

### Run tests

```bash
make test
```

### Run tests with coverage

```bash
make coverage
```

### Format code

```bash
make format
```

### Lint code

```bash
make lint
```

### Type checking

```bash
make type-check
```

## Development

See `make help` for all available commands.

## License

MIT
