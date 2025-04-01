"""
Formatter module for curl commands.

Author: David Diaz (https://github.com/alfdav)
Version: 1.0.0
"""
from typing import Dict, Any
import shlex
import json


def kadabra_format_curl(request_data: Dict[str, Any]) -> str:
    """
    Format parsed request data as a curl command.
    
    This function transforms parsed HTTP request data into a properly escaped
    curl command string that works across all platforms (Unix/Linux, macOS, Windows).
    
    Args:
        request_data: Dictionary containing parsed request components
        
    Returns:
        A cross-platform compatible curl command string
    """
    method = request_data.get('method', 'GET')
    url = request_data.get('url', '')
    headers = request_data.get('headers', {})
    body = request_data.get('body')
    
    # Start building the curl command
    curl_parts = [f"curl -X {method}"]
    
    # Properly escape the URL for all platforms
    escaped_url = shlex.quote(url)
    curl_parts.append(escaped_url)
    
    # Add headers with proper escaping
    for header, value in headers.items():
        # Skip host header as it's included in the URL
        if header.lower() == 'host':
            continue
        # Escape the header value to handle special characters
        header_arg = f"{header}: {value}"
        escaped_header = shlex.quote(header_arg)
        curl_parts.append(f"-H {escaped_header}")
    
    # Add body if present with proper escaping
    if body and body.strip():
        # Check if the body looks like a raw HTTP request (starts with HTTP method or version)
        if not any(body.strip().startswith(prefix) for prefix in ['GET ', 'POST ', 'PUT ', 'DELETE ', 'PATCH ', 'HEAD ', 'OPTIONS ', 'HTTP/']):
            # Try to detect if it's JSON
            try:
                json.loads(body)
                # It's valid JSON, use -d with proper escaping
                escaped_body = shlex.quote(body)
                curl_parts.append(f"-d {escaped_body}")
            except (json.JSONDecodeError, TypeError):
                # Not JSON or invalid JSON, use --data-raw with proper escaping
                escaped_body = shlex.quote(body)
                curl_parts.append(f"--data-raw {escaped_body}")
    
    # Join all parts with spaces to create a true one-liner
    return ' '.join(curl_parts)
