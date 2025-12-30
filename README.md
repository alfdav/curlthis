# curlthis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Description

curlthis is a streamlined tool that transforms raw HTTP requests into executable curl commands. It elegantly handles headers, request bodies, and proper escaping to simplify API testing and documentation.

## Key Features

- **Input Flexibility**: Read from files, stdin, or automatically from clipboard
- **Intelligent Parsing**: Handles various HTTP request formats with ease
- **Syntax Highlighting**: Displays curl commands with proper syntax highlighting
- **Clipboard Integration**: Copy results directly to clipboard for immediate use
- **Verbose Mode**: See the processing steps in action

## Installation

```bash
# Clone the repository
git clone https://github.com/alfdav/curlthis.git
cd curlthis

# Install
./install.sh  # On Unix/macOS
./install.ps1  # On Windows
```

## Usage

```bash
# From clipboard (default)
curlthis

# From file
curlthis -f request.txt

# From stdin
cat request.txt | curlthis

# Output to clipboard
curlthis -c

# Use proxy
curlthis --proxy http://proxy.example.com:8080

# Handle cookies with cookie jar
curlthis --cookie-jar cookies.txt

# SSH mode (no clipboard, plain text output)
curlthis --ssh

# Show verbose output
curlthis -v

# Show help
curlthis -h
```

## Examples

### Example: Converting an HTTP Request

Input:
```
POST /api/v1/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer token123

{"name": "John Doe", "email": "john@example.com"}
```

Output:
```bash
curl -X POST 'https://example.com/api/v1/users' -H 'Content-Type: application/json' -H 'Authorization: Bearer token123' -d '{"name": "John Doe", "email": "john@example.com"}'
```

## Requirements

- Python 3.8 or higher
- Dependencies:
  - typer (0.15.1+)
  - rich (13.9.4+)
  - pyperclip (1.8.2+)

## Development

```bash
# Clone the repository
git clone https://github.com/alfdav/curlthis.git
cd curlthis

# Install in development mode
pip install -e .

# Run code formatting
black curlthis/

# Run type checking
mypy curlthis/
```

## Project Structure

```
curlthis/
├── curlthis/           # Core functionality
│   ├── __init__.py
│   ├── __main__.py     # Entry point
│   ├── main.py         # Main application logic
│   ├── parser.py       # HTTP request parsing
│   ├── formatter.py    # curl command formatting
│   └── utils.py        # Utility functions
├── install.sh          # Unix/macOS installer
├── install.ps1         # Windows installer
├── uninstall.sh        # Unix/macOS uninstaller
├── uninstall.ps1       # Windows uninstaller
├── LICENSE             # MIT License
└── README.md           # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER, AUTHORS, OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES.

---
Made with ❤️ by David
