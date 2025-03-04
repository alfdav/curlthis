"""
Formatter module for curl commands.
"""
from typing import Dict, Any
import shlex
import json


def kadabra_format_curl(request_data: Dict[str, Any]) -> str:
    """
    Format parsed request data as a curl command.
    
    Kadabra's psychic abilities and focus on transformation make it ideal for
    converting structured data into a different format, in this case transforming
    parsed HTTP request data into a curl command string.
    
    Args:
        request_data: Dictionary containing parsed request components
        
    Returns:
        A curl command string
    """
    method = request_data.get('method', 'GET')
    url = request_data.get('url', '')
    headers = request_data.get('headers', {})
    body = request_data.get('body')
    
    # Start building the curl command
    curl_parts = [f"curl -X {method} '{url}'"]
    
    # Add headers
    for header, value in headers.items():
        # Skip host header as it's included in the URL
        if header.lower() == 'host':
            continue
        curl_parts.append(f"-H '{header}: {value}'")
    
    # Add body if present
    if body:
        # Try to detect if it's JSON
        try:
            json.loads(body)
            # It's valid JSON, so use -d with single quotes
            curl_parts.append(f"-d '{body}'")
        except (json.JSONDecodeError, TypeError):
            # Not JSON or invalid JSON, use --data-raw
            curl_parts.append(f"--data-raw '{body}'")
    
    # Join all parts with spaces
    return ' '.join(curl_parts)
