#!/usr/bin/env python3
"""
Main module for curlthis CLI application.

Author: David Diaz (https://github.com/alfdav)
Version: 0.1.0
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
    disable_clipboard: bool = typer.Option(False, "--disable-clipboard", "--ssh", help="Disable clipboard completely (useful for SSH sessions)"),
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
        $ curlthis --disable-clipboard     # Completely disables clipboard (for SSH sessions)
        $ curlthis --ssh                   # Alias for --disable-clipboard
        $ curlthis -f request.txt -v       # Reads from file with verbose output
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
        
        # Format as curl command
        if verbose:
            hitmonchan_show_progress("Formatting as curl command...", spinner=True)
            
        curl_command = kadabra_format_curl(request_data)
        
        # Check for SSH session
        is_ssh_session = False
        try:
            # Check common SSH environment variables
            is_ssh_session = bool(os.environ.get('SSH_CLIENT') or os.environ.get('SSH_TTY') or 
                                os.environ.get('SSH_CONNECTION'))
        except Exception:
            pass
            
        # Display the command differently based on session type
        if is_ssh_session:
            # For SSH sessions, display a plain one-liner that can be easily selected and copied
            # First show a header with clear instructions
            console.print("\n[bold yellow]Copy-Paste Command:[/bold yellow]")
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
        else:
            # For regular sessions, display with syntax highlighting and line numbers
            kadabra_display_code(curl_command, language="bash", title="Generated curl command", line_numbers=True)
            
            # Add a blank line for better visual separation
            console.print("")
        
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
