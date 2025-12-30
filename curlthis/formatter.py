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
        request_data: Dictionary containing parsed request components.
                     Required keys: method, url, headers
                     Optional keys: body, cookies, proxy, cookie_jar
        
    Returns:
        A cross-platform compatible curl command string
        
    Raises:
        ValueError: If required fields are missing or invalid
    """
    # Validate required fields
    if not request_data.get('url'):
        raise ValueError(
            "Missing URL in request data. Cannot generate curl command without a URL."
        )
    
    method = request_data.get('method', 'GET')
    url = request_data.get('url', '')
    headers = request_data.get('headers', {})
    body = request_data.get('body')
    cookies = request_data.get('cookies')
    proxy = request_data.get('proxy')
    cookie_jar = request_data.get('cookie_jar')
    
    # Start building the curl command
    curl_parts = [f"curl -X {method}"]
    
    # Properly escape the URL for all platforms
    escaped_url = shlex.quote(url)
    curl_parts.append(escaped_url)
    
    # Add proxy if specified
    if proxy:
        escaped_proxy = shlex.quote(proxy)
        curl_parts.append(f"--proxy {escaped_proxy}")
    
    # Add headers with proper escaping
    for header, value in headers.items():
        # Skip headers that are handled separately
        if header.lower() in ('host', 'cookie'):
            continue
        # Escape the header value to handle special characters
        header_arg = f"{header}: {value}"
        escaped_header = shlex.quote(header_arg)
        curl_parts.append(f"-H {escaped_header}")
    
    # Add cookies if present
    if cookies:
        escaped_cookies = shlex.quote(cookies)
        curl_parts.append(f"--cookie {escaped_cookies}")
    
    # Add cookie jar if specified
    if cookie_jar:
        escaped_jar = shlex.quote(cookie_jar)
        curl_parts.append(f"--cookie-jar {escaped_jar}")
    
    # Add body if present with proper escaping
    if body and body.strip():
        # Check if the body looks like a raw HTTP request (starts with HTTP method or version)
        # Updated to include PATCH and OPTIONS
        http_prefixes = ['GET ', 'POST ', 'PUT ', 'DELETE ', 'PATCH ', 'HEAD ', 'OPTIONS ', 'TRACE ', 'CONNECT ', 'HTTP/']
        if not any(body.strip().startswith(prefix) for prefix in http_prefixes):
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
