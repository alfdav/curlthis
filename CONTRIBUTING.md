# Contributing to curlthis

Thank you for considering contributing to curlthis! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Any relevant logs or screenshots
6. Your environment (OS, Python version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:

1. A clear, descriptive title
2. A detailed description of the proposed feature
3. Any relevant examples or use cases
4. If possible, a rough implementation idea

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Run tests and ensure code quality
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature-name`)
7. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/alfdav/curlthis.git
cd curlthis

# Install in development mode
pip install -e .

# Install development dependencies
pip install black mypy flake8 pytest isort
```

## Coding Standards

This project follows these standards:

1. **Python PEPs**: All code must adhere to:
   - [PEP 8](https://www.python.org/dev/peps/pep-0008/): Style Guide for Python Code
   - [PEP 20](https://www.python.org/dev/peps/pep-0020/): The Zen of Python
   - [PEP 257](https://www.python.org/dev/peps/pep-0257/): Docstring Conventions
   - [PEP 517/518](https://www.python.org/dev/peps/pep-0517/): Build System Specification

2. **Code Formatting**: Use Black with a line length of 88 characters
   ```bash
   black curlthis/
   ```

3. **Import Sorting**: Use isort configured to be compatible with Black
   ```bash
   isort curlthis/
   ```

4. **Type Checking**: Use MyPy for static type checking
   ```bash
   mypy curlthis/
   ```

5. **Linting**: Use flake8 for additional linting
   ```bash
   flake8 curlthis/
   ```

6. **Documentation**: All functions, classes, and modules should have Google-style docstrings

## Testing

When adding new features or fixing bugs, please include appropriate tests.

```bash
# Run tests
pytest
```

## Release Process

The maintainers will handle the release process, including:

1. Version bumping in pyproject.toml
2. Creating release notes
3. Publishing to PyPI

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT license.

## Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER, AUTHORS, OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES.