import pytest
import os
import sys

# Add the project root to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def basic_get_request():
    return """GET /api/v1/users HTTP/1.1
Host: example.com
Accept: application/json
"""

@pytest.fixture
def post_json_request():
    return """POST /api/v1/users HTTP/1.1
Host: example.com
Content-Type: application/json

{"name": "John", "email": "john@example.com"}
"""

@pytest.fixture
def patch_request():
    return """PATCH /api/v1/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{"name": "John Updated"}
"""

@pytest.fixture
def options_request():
    return """OPTIONS /api/v1/users HTTP/1.1
Host: example.com
"""

@pytest.fixture
def request_with_cookies():
    return """GET /dashboard HTTP/1.1
Host: example.com
Cookie: session_id=12345; theme=dark
"""

@pytest.fixture
def request_with_proxy_headers():
    return """GET / HTTP/1.1
Host: example.com
X-Forwarded-For: 10.0.0.1
Proxy-Connection: keep-alive
"""
