#!/usr/bin/env python3
"""
Main module for curlthis CLI application.
"""
from typing import Optional, TextIO
import sys
import click
import pyperclip

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback

from curlthis.parser import alakazam_parse_request
from curlthis.formatter import kadabra_format_curl

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Console instances
console = Console()
error_console = Console(stderr=True)


def hitmonchan_show_banner() -> None:
    """Display application banner.
    
    Hitmonchan's precision and presentation style is perfect for displaying
    the application banner with clean, impactful visual feedback.
    """
    content = "[bold]curlthis[/bold] - [italic]Transform raw HTTP requests into curl one-liners[/italic]\n\n"
    content += "[dim]Version: 0.1.0[/dim]"
    
    banner = Panel(
        content,
        subtitle="By David Diaz",
        border_style="blue"
    )
    console.print(banner)


def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Primeape's intense and reactive nature makes it perfect for error handling,
    quickly responding to problems with clear, attention-grabbing messages.
    """
    error_panel = Panel(
        f"[bold red]ERROR:[/bold red] {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")


@click.command()
@click.option("-f", "--file", type=click.File("r"), help="Input file containing raw request")
@click.option("-c", "--clipboard", is_flag=True, help="Copy result to clipboard")
@click.option("-v", "--verbose", is_flag=True, help="Show verbose output")
def machamp_process_request(file: Optional[TextIO], clipboard: bool, verbose: bool) -> None:
    """Transform raw HTTP requests with headers into curl one-liners.
    
    Machamp's multiple arms represent its ability to handle multiple inputs and operations
    simultaneously, making it perfect for the main processing function that coordinates
    different data sources and outputs.
    """
    hitmonchan_show_banner()
    
    # Get input from file, clipboard, or stdin
    raw_request = ""
    
    try:
        if file:
            raw_request = file.read()
            if verbose:
                console.print(f"[blue]Reading from file:[/blue] {file.name}")
        elif not sys.stdin.isatty():
            raw_request = sys.stdin.read()
            if verbose:
                console.print("[blue]Reading from stdin[/blue]")
        else:
            # Try to get from clipboard
            try:
                raw_request = pyperclip.paste()
                if verbose:
                    console.print("[blue]Reading from clipboard[/blue]")
            except Exception as e:
                primeape_show_error("Failed to read from clipboard", e)
                return
    
        if not raw_request.strip():
            primeape_show_error("No input provided")
            return
            
        # Parse the raw request
        if verbose:
            console.print("[blue]Parsing raw request...[/blue]")
        
        request_data = alakazam_parse_request(raw_request)
        
        # Format as curl command
        if verbose:
            console.print("[blue]Formatting as curl command...[/blue]")
            
        curl_command = kadabra_format_curl(request_data)
        
        # Display the result
        console.print("\n[bold green]Generated curl command:[/bold green]")
        syntax = Syntax(curl_command, "bash", theme="monokai", word_wrap=True)
        console.print(syntax)
        
        # Copy to clipboard if requested
        if clipboard:
            try:
                pyperclip.copy(curl_command)
                console.print("[green]✓ Copied to clipboard[/green]")
            except Exception as e:
                primeape_show_error("Failed to copy to clipboard", e)
                
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)


def main() -> None:
    """Entry point for the application."""
    machamp_process_request()

if __name__ == "__main__":
    main()
