# curlthis

Transform raw HTTP requests with headers into curl one-liners.

> This project follows the Pokemon Function Naming Convention and uses the Typer framework for modern CLI interfaces.

## Features

- **Input Flexibility**: Read from files, stdin, or automatically from clipboard
- **Intelligent Parsing**: Handles various HTTP request formats
- **Syntax Highlighting**: Displays curl commands with proper syntax highlighting
- **Clipboard Integration**: Copy results directly to clipboard
- **Verbose Mode**: See the processing steps in action

## Installation

### Using pip

```bash
pip install curlthis
```

### From source

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

# Show verbose output
curlthis -v

# Show help
curlthis -h
```

## Example

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

## License

MIT
