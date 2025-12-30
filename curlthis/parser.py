"""
Parser module for raw HTTP requests.

Author: David Diaz (https://github.com/alfdav)
Version: 1.0.0
"""
from typing import Dict, Optional, Tuple, Any


def alakazam_parse_request(raw_request: str) -> Dict[str, Any]:
    """
    Parse a raw HTTP request into its components.
    
    Alakazam's psychic abilities represent its capacity for complex analysis and
    data transformation, making it perfect for parsing and structuring raw text data.
    
    Args:
        raw_request: The raw HTTP request string
        
    Returns:
        A dictionary containing the parsed request components
        
    Raises:
        ValueError: If the request is empty, malformed, or contains invalid HTTP method
    """
    # Supported HTTP methods
    VALID_METHODS = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT'}
    
    lines = raw_request.strip().split('\n')
    
    # Validate request is not empty
    if not lines or not lines[0].strip():
        raise ValueError(
            "No HTTP request found. Please provide a valid HTTP request.\n"
            "Example:\n"
            "  GET /api/users HTTP/1.1\n"
            "  Host: example.com"
        )
    
    # Parse request line
    request_line = lines[0].strip()
    parts = request_line.split()
    
    if len(parts) < 2:
        raise ValueError(
            f"Invalid request line format: '{request_line}'\n"
            "Expected format: METHOD /path HTTP/1.1\n"
            "Example: GET /api/users HTTP/1.1"
        )
    
    method = parts[0].upper()
    path = parts[1]
    protocol = parts[2] if len(parts) > 2 else None
    
    # Validate HTTP method
    if method not in VALID_METHODS:
        raise ValueError(
            f"Invalid HTTP method: '{method}'\n"
            f"Supported methods: {', '.join(sorted(VALID_METHODS))}\n"
            "Did you mean one of: GET, POST, PUT, PATCH, DELETE?"
        )
    
    # Parse headers
    headers = {}
    host = None
    cookies = None
    proxy = None
    body_start_index = len(lines)
    
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():
            body_start_index = i + 1
            break
            
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            headers[key] = value
            
            # Extract special headers
            if key.lower() == 'host':
                host = value
            elif key.lower() == 'cookie':
                cookies = value
            elif key.lower() in ('proxy-connection', 'x-forwarded-for'):
                # Note: These headers don't directly translate to curl proxy
                # but we capture them for potential future use
                proxy = value
    
    # Validate Host header is present
    if not host:
        raise ValueError(
            "Missing Host header. Please include 'Host: example.com' in your request.\n"
            "Example:\n"
            "  GET /api/users HTTP/1.1\n"
            "  Host: api.example.com"
        )
    
    # Extract body if present
    body = None
    if body_start_index < len(lines):
        body_content = '\n'.join(lines[body_start_index:])
        # Only set body if there's actual content
        if body_content.strip():
            body = body_content
    
    # Construct URL
    url = f"{host}{path}" if host else path
    
    # Add scheme if missing
    if host and not url.startswith(('http://', 'https://')):
        # Default to https if not specified
        url = f"https://{url}"
    
    result = {
        'method': method,
        'url': url,
        'headers': headers,
        'body': body
    }
    
    # Add optional fields if present
    if cookies:
        result['cookies'] = cookies
    if proxy:
        result['proxy'] = proxy
    
    return result
