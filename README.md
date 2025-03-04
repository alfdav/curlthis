# curlthis

Transform raw HTTP requests with headers into curl one-liners.

> This project follows the Pokemon Function Naming Convention for projects.

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
# From clipboard
curlthis

# From file
curlthis -f request.txt

# From stdin
cat request.txt | curlthis

# Output to clipboard
curlthis -c

# Show verbose output
curlthis -v
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

## License

MIT
