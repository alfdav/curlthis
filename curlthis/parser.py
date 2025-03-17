"""
Parser module for raw HTTP requests.

Author: David Diaz (https://github.com/alfdav)
Version: 0.1.0
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
    """
    lines = raw_request.strip().split('\n')
    
    # Parse request line
    if not lines:
        raise ValueError("Empty request")
        
    request_line = lines[0]
    method, path, *protocol = request_line.split()
    
    # Parse headers
    headers = {}
    host = None
    body_start_index = 0
    
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():
            body_start_index = i + 1
            break
            
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            headers[key] = value
            
            if key.lower() == 'host':
                host = value
    
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
    
    return {
        'method': method,
        'url': url,
        'headers': headers,
        'body': body
    }
