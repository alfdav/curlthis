import pytest
from typer.testing import CliRunner
from curlthis.main import app

runner = CliRunner()

def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Transform raw HTTP requests" in result.stdout

def test_cli_file_input(tmp_path):
    # Create a temporary request file
    req_file = tmp_path / "request.txt"
    req_file.write_text("GET /api HTTP/1.1\nHost: example.com")
    
    # Run with --no-clipboard to avoid clipboard interaction in tests
    # and --ssh to force plain text output suitable for assertion
    result = runner.invoke(app, ["-f", str(req_file), "--no-c", "--ssh"])
    
    assert result.exit_code == 0
    assert "curl -X GET" in result.stdout
    assert "'https://example.com/api'" in result.stdout

def test_cli_stdin_input():
    req_content = "POST /api HTTP/1.1\nHost: example.com\n\n{}"
    result = runner.invoke(app, ["--no-c", "--ssh"], input=req_content)
    
    assert result.exit_code == 0
    assert "curl -X POST" in result.stdout

def test_cli_proxy_option(tmp_path):
    req_file = tmp_path / "request.txt"
    req_file.write_text("GET /api HTTP/1.1\nHost: example.com")
    
    result = runner.invoke(app, ["-f", str(req_file), "--proxy", "http://proxy:8080", "--no-c", "--ssh"])
    
    assert result.exit_code == 0
    assert "--proxy 'http://proxy:8080'" in result.stdout

def test_cli_cookie_jar_option(tmp_path):
    req_file = tmp_path / "request.txt"
    req_file.write_text("GET /api HTTP/1.1\nHost: example.com")
    
    result = runner.invoke(app, ["-f", str(req_file), "--cookie-jar", "cookies.txt", "--no-c", "--ssh"])
    
    assert result.exit_code == 0
    assert "--cookie-jar 'cookies.txt'" in result.stdout

def test_cli_error_empty_input(tmp_path):
    req_file = tmp_path / "empty.txt"
    req_file.write_text("")
    
    result = runner.invoke(app, ["-f", str(req_file), "--no-c"])
    
    assert result.exit_code == 1
    assert "No input provided" in result.stdout or "No HTTP request found" in result.stdout
