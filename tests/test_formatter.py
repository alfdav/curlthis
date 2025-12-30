import pytest
import shlex
from curlthis.formatter import kadabra_format_curl

def test_format_basic_get():
    data = {
        'method': 'GET',
        'url': 'https://example.com/api',
        'headers': {'Accept': 'application/json'}
    }
    cmd = kadabra_format_curl(data)
    assert cmd.startswith('curl -X GET')
    assert "https://example.com/api" in cmd
    assert "Accept: application/json" in cmd

def test_format_post_json():
    data = {
        'method': 'POST',
        'url': 'https://example.com/api',
        'headers': {'Content-Type': 'application/json'},
        'body': '{"key": "value"}'
    }
    cmd = kadabra_format_curl(data)
    assert "-d '{\"key\": \"value\"}'" in cmd

def test_format_with_proxy():
    data = {
        'method': 'GET',
        'url': 'https://example.com',
        'headers': {},
        'proxy': 'http://proxy.local:8080'
    }
    cmd = kadabra_format_curl(data)
    assert "http://proxy.local:8080" in cmd

def test_format_with_cookies():
    data = {
        'method': 'GET',
        'url': 'https://example.com',
        'headers': {},
        'cookies': 'foo=bar; baz=qux'
    }
    cmd = kadabra_format_curl(data)
    assert "--cookie 'foo=bar; baz=qux'" in cmd

def test_format_with_cookie_jar():
    data = {
        'method': 'GET',
        'url': 'https://example.com',
        'headers': {},
        'cookie_jar': '/path/to/cookies.txt'
    }
    cmd = kadabra_format_curl(data)
    assert "/path/to/cookies.txt" in cmd

def test_format_missing_url():
    with pytest.raises(ValueError, match="Missing URL"):
        kadabra_format_curl({'method': 'GET'})

def test_format_body_escaping():
    # Test complicated body with quotes
    body = '{"name": "O\'Reilly"}'
    data = {
        'method': 'POST',
        'url': 'https://example.com',
        'body': body
    }
    cmd = kadabra_format_curl(data)
    # shlex.quote should handle the single quote
    expected_body = shlex.quote(body)
    assert f"-d {expected_body}" in cmd
