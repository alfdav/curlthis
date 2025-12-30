#!/usr/bin/env python3
"""
Main module for curlthis CLI application.

Author: David Diaz (https://github.com/alfdav)
Version: 1.0.0
"""
from typing import Optional, List, Dict, Any
import sys
import os
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
    create_section, kadabra_display_code, meowth_copy_to_clipboard
)

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create Typer app with rich formatting
app = typer.Typer(
    help="Transform raw HTTP requests with headers into curl one-liners",
    add_completion=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["--help", "-h"]}
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
    clipboard: bool = typer.Option(True, "--clipboard", "-c", help="Copy result to clipboard (default: True)", show_default=False),
    no_clipboard: bool = typer.Option(False, "--no-clipboard", "--no-c", help="Disable clipboard copying"),
    disable_clipboard: bool = typer.Option(False, "--disable-clipboard", "--ssh", help="Force SSH mode: disable clipboard and use plain text display (useful for SSH sessions)"),
    proxy: Optional[str] = typer.Option(None, "--proxy", "-p", help="Proxy server (e.g., http://proxy.example.com:8080)"),
    cookie_jar: Optional[Path] = typer.Option(None, "--cookie-jar", "-j", help="Cookie jar file path for saving/loading cookies"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Transform raw HTTP requests with headers into curl one-liners.
    
    This command processes raw HTTP requests from various inputs (file, stdin, clipboard)
    and converts them into curl commands that can be executed in a terminal.
    By default, the generated curl command is copied to the clipboard for immediate use.
    
    Examples:
        $ curlthis -f request.txt          # Reads from file and copies to clipboard
        $ cat request.txt | curlthis       # Reads from stdin and copies to clipboard
        $ curlthis -f request.txt --no-c   # Reads from file without copying to clipboard
        $ curlthis --ssh                   # Force SSH mode: plain text display and no clipboard
        $ curlthis --disable-clipboard     # Same as --ssh (alias)
        $ curlthis -f request.txt -v       # Reads from file with verbose output
        $ curlthis -f request.txt --ssh -v # Combines SSH mode with verbose output
        $ curlthis -f request.txt --proxy http://proxy.example.com:8080  # Use proxy
        $ curlthis -f request.txt --cookie-jar cookies.txt  # Save cookies to file
    """
    hitmonchan_show_banner(author="David Diaz (https://github.com/alfdav)")
    # Add a blank line for better visual separation
    console.print("")
    
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
        
        # Add CLI-provided options to request data
        if proxy:
            request_data['proxy'] = proxy
            if verbose:
                hitmonchan_show_progress(f"Using proxy: {proxy}")
        
        if cookie_jar:
            request_data['cookie_jar'] = str(cookie_jar)
            if verbose:
                hitmonchan_show_progress(f"Using cookie jar: {cookie_jar}")
        
        # Format as curl command
        if verbose:
            hitmonchan_show_progress("Formatting as curl command...", spinner=True)
            
        curl_command = kadabra_format_curl(request_data)
        
        # Check for SSH session or if --ssh flag was used
        is_ssh_session = False
        try:
            # Check common SSH environment variables
            is_ssh_session = bool(os.environ.get('SSH_CLIENT') or os.environ.get('SSH_TTY') or 
                                os.environ.get('SSH_CONNECTION'))
            
            # Also treat as SSH session if --ssh or --disable-clipboard flag was used
            is_ssh_session = is_ssh_session or disable_clipboard
        except Exception:
            pass
            
        # Always display the syntax-highlighted version first
        kadabra_display_code(curl_command, language="bash", title="Generated curl command", line_numbers=True)
        
        # Add a blank line for better visual separation
        console.print("")
        
        # For SSH sessions or when --ssh flag is used, also display a plain text version for easy copying
        if is_ssh_session:
            # First show a header with clear instructions
            console.print("[bold yellow]Copy-Paste Command:[/bold yellow]")
            console.print("[dim]The command below is formatted for easy selection in SSH environments:[/dim]")
            
            # Add a blank line before the command for easier selection
            console.print("")
            
            # Print the command as plain text with no styling or formatting
            # This makes it extremely easy to select with triple-click or drag selection
            console.print(curl_command, highlight=False, markup=False, emoji=False, overflow="fold")
            
            # Add a blank line after the command
            console.print("")
            
            # Add a separator for visual clarity
            console.print("[dim]---[/dim]")
        
        # Copy to clipboard by default unless explicitly disabled
        # Important: Copy the raw command without line numbers to make it directly usable
        should_copy = clipboard and not no_clipboard and not disable_clipboard
        if should_copy:
            # Use the cross-platform clipboard function for better error handling
            success, message = meowth_copy_to_clipboard(curl_command)
            if success:
                hitmonchan_show_success(message)
            else:
                # Show a warning with helpful instructions instead of an error
                # Use multiline=True to preserve formatting in the installation instructions
                primeape_show_warning(message, title="Clipboard Issue", multiline=True)
                
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

def main() -> None:
    """Entry point for the application."""
    try:
        app(prog_name="curlthis")
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()
