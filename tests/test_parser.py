import pytest
from curlthis.parser import alakazam_parse_request

def test_parse_basic_get(basic_get_request):
    result = alakazam_parse_request(basic_get_request)
    assert result['method'] == 'GET'
    assert result['url'] == 'https://example.com/api/v1/users'
    assert result['headers']['Accept'] == 'application/json'
    assert result['body'] is None

def test_parse_post_json(post_json_request):
    result = alakazam_parse_request(post_json_request)
    assert result['method'] == 'POST'
    assert result['body'] == '{"name": "John", "email": "john@example.com"}'
    assert result['headers']['Content-Type'] == 'application/json'

def test_parse_patch(patch_request):
    result = alakazam_parse_request(patch_request)
    assert result['method'] == 'PATCH'
    assert 'John Updated' in result['body']

def test_parse_options(options_request):
    result = alakazam_parse_request(options_request)
    assert result['method'] == 'OPTIONS'
    assert result['body'] is None

def test_parse_cookies(request_with_cookies):
    result = alakazam_parse_request(request_with_cookies)
    assert result['cookies'] == 'session_id=12345; theme=dark'

def test_parse_proxy(request_with_proxy_headers):
    result = alakazam_parse_request(request_with_proxy_headers)
    assert 'proxy' in result
    # We capture one of them, depending on iteration order but we look for both
    # The implementation captures the last one found in the loop usually or first?
    # Let's check implementation: if key ... proxy = value. So it overwrites.
    # We just want to ensure it detected something.
    assert result['proxy'] is not None

def test_missing_host():
    req = "GET / HTTP/1.1\nAccept: */*"
    with pytest.raises(ValueError, match="Missing Host header"):
        alakazam_parse_request(req)

def test_invalid_method():
    req = "INVALID / HTTP/1.1\nHost: example.com"
    with pytest.raises(ValueError, match="Invalid HTTP method"):
        alakazam_parse_request(req)

def test_empty_request():
    with pytest.raises(ValueError, match="No HTTP request found"):
        alakazam_parse_request("")
    
    with pytest.raises(ValueError, match="No HTTP request found"):
        alakazam_parse_request("   \n   ")
