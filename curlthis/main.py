#!/usr/bin/env python3
"""
Main module for curlthis CLI application.

Author: David Diaz (https://github.com/alfdav)
Version: 0.1.0
"""
from typing import Optional, List, Dict, Any
import sys
import typer
import pyperclip
from pathlib import Path

from rich.markdown import Markdown
from rich.progress import BarColumn, TaskProgressColumn
from rich.traceback import install as install_rich_traceback

from curlthis.parser import alakazam_parse_request
from curlthis.formatter import kadabra_format_curl
from curlthis.utils import (
    console, error_console, STATUS,
    hitmonchan_show_banner, primeape_show_error, primeape_show_warning,
    hitmonchan_show_success, hitmonchan_show_progress, create_table,
    create_section, kadabra_display_code
)

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create Typer app with rich formatting
app = typer.Typer(
    help="Transform raw HTTP requests with headers into curl one-liners",
    add_completion=True,
    rich_markup_mode="rich"
)

def machamp_create_command_group(name: str, help_text: str) -> typer.Typer:
    """Create a new command group with standardized styling.
    
    Machamp's multiple arms represent handling multiple operations,
    making it perfect for creating command groups.
    
    Args:
        name: The name of the command group
        help_text: The help text for the command group
        
    Returns:
        A Typer instance configured for the command group
    """
    return typer.Typer(
        name=name,
        help=help_text,
        rich_markup_mode="rich"
    )

@app.command()
def machamp_process_request(
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="Input file containing raw request"),
    clipboard: bool = typer.Option(False, "--clipboard", "-c", help="Copy result to clipboard"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Transform raw HTTP requests with headers into curl one-liners.
    
    This command processes raw HTTP requests from various inputs (file, stdin, clipboard)
    and converts them into curl commands that can be executed in a terminal.
    
    Examples:
        $ curlthis -f request.txt
        $ cat request.txt | curlthis
        $ curlthis -f request.txt -c
        $ curlthis -f request.txt -v
    """
    hitmonchan_show_banner(author="David Diaz (https://github.com/alfdav)")
    
    # Get input from file, clipboard, or stdin
    raw_request = ""
    
    try:
        if file:
            raw_request = file.read_text()
            if verbose:
                hitmonchan_show_progress(f"Reading from file: {file}")
        elif not sys.stdin.isatty():
            raw_request = sys.stdin.read()
            if verbose:
                hitmonchan_show_progress("Reading from stdin")
        else:
            # Try to get from clipboard
            try:
                raw_request = pyperclip.paste()
                if verbose:
                    hitmonchan_show_progress("Reading from clipboard")
            except Exception as e:
                primeape_show_error("Failed to read from clipboard", e)
                raise typer.Exit(code=1)
    
        if not raw_request.strip():
            primeape_show_error("No input provided")
            raise typer.Exit(code=1)
            
        # Parse the raw request
        if verbose:
            hitmonchan_show_progress("Parsing raw request...", spinner=True)
        
        request_data = alakazam_parse_request(raw_request)
        
        # Format as curl command
        if verbose:
            hitmonchan_show_progress("Formatting as curl command...", spinner=True)
            
        curl_command = kadabra_format_curl(request_data)
        
        # Display the result using panel for consistency with andns2
        kadabra_display_code(curl_command, language="bash", title="Generated curl command")
        
        # Copy to clipboard if requested
        if clipboard:
            try:
                pyperclip.copy(curl_command)
                hitmonchan_show_success("Copied to clipboard")
            except Exception as e:
                primeape_show_error("Failed to copy to clipboard", e)
                
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

def main() -> None:
    """Entry point for the application."""
    try:
        app()
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()
