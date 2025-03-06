#!/usr/bin/env python3
"""
Main module for curlthis CLI application.
"""
from typing import Optional, TextIO, List
import sys
import click
import pyperclip

from rich.markdown import Markdown
from rich.progress import BarColumn, TaskProgressColumn

from curlthis.parser import alakazam_parse_request
from curlthis.formatter import kadabra_format_curl
from curlthis.utils import (
    console, error_console, STATUS,
    hitmonchan_show_banner, primeape_show_error, primeape_show_warning,
    hitmonchan_show_success, hitmonchan_show_progress, create_table,
    create_section, display_code
)


class RichHelpCommand(click.Command):
    """Custom click.Command that displays help using Rich styling."""
    
    def format_help(self, ctx, formatter):
        # Use Rich for help display instead of the default formatter
        hitmonchan_show_banner(author="David Diaz (https://github.com/alfdav)")
        
        # Command description with rule
        create_section("Description")
        console.print(f"{self.help}\n")
        
        # Usage section with rule
        usage_text = self.collect_usage(ctx)
        create_section("Usage")
        console.print(f"{usage_text}\n")
        
        # Options table with rule
        options = self.collect_options(ctx)
        if options:
            create_section("Options")
            options_table = create_table("", "")
            options_table.add_column("Option", style="bold")
            options_table.add_column("Description")
            
            for opt in options:
                options_table.add_row(opt["name"], opt["help"])
            
            console.print(options_table)
            console.print()
        
        # Examples section with rule
        create_section("Examples")
        examples = [
            ("From a file:", "curlthis -f request.txt"),
            ("From stdin:", "cat request.txt | curlthis"),
            ("Copy to clipboard:", "curlthis -f request.txt -c"),
            ("Verbose output:", "curlthis -f request.txt -v")
        ]
        
        examples_table = create_table("", "")
        examples_table.add_column("Description", style="bold")
        examples_table.add_column("Command", style="cyan")
        
        for desc, cmd in examples:
            examples_table.add_row(desc, cmd)
        
        console.print(examples_table)
        console.print()
    
    def collect_usage(self, ctx) -> str:
        """Collect and format usage string."""
        formatter = ctx.make_formatter()
        self.format_usage(ctx, formatter)
        return formatter.getvalue().rstrip("\n")
    
    def collect_options(self, ctx) -> List[dict]:
        """Collect and format options."""
        options = []
        for param in self.get_params(ctx):
            if isinstance(param, click.Option):
                # Format option names
                names = []
                for opt in param.opts:
                    if opt.startswith('--'):
                        names.append(opt)
                    else:
                        names.append(opt)
                
                opt_name = ", ".join(names)
                if param.metavar:
                    opt_name += f" {param.metavar}"
                
                options.append({
                    "name": opt_name,
                    "help": param.help or ""
                })
        
        return options


@click.command(cls=RichHelpCommand, context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-f", "--file", type=click.File("r"), help="Input file containing raw request")
@click.option("-c", "--clipboard", is_flag=True, help="Copy result to clipboard")
@click.option("-v", "--verbose", is_flag=True, help="Show verbose output")
def machamp_process_request(file: Optional[TextIO], clipboard: bool, verbose: bool) -> None:
    """Transform raw HTTP requests with headers into curl one-liners.
    
    This function processes raw HTTP requests from various inputs (file, stdin, clipboard)
    and converts them into curl commands that can be executed in a terminal.
    """
    hitmonchan_show_banner(author="David Diaz (https://github.com/alfdav)")
    
    # Get input from file, clipboard, or stdin
    raw_request = ""
    
    try:
        if file:
            raw_request = file.read()
            if verbose:
                hitmonchan_show_progress(f"Reading from file: {file.name}")
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
                return
    
        if not raw_request.strip():
            primeape_show_error("No input provided")
            return
            
        # Parse the raw request
        if verbose:
            hitmonchan_show_progress("Parsing raw request...", spinner=True)
        
        request_data = alakazam_parse_request(raw_request)
        
        # Format as curl command
        if verbose:
            hitmonchan_show_progress("Formatting as curl command...", spinner=True)
            
        curl_command = kadabra_format_curl(request_data)
        
        # Display the result using panel for consistency with andns2
        display_code(curl_command, language="bash", theme="monokai", title="Generated curl command")
        
        # Copy to clipboard if requested
        if clipboard:
            try:
                pyperclip.copy(curl_command)
                hitmonchan_show_success("Copied to clipboard")
            except Exception as e:
                primeape_show_error("Failed to copy to clipboard", e)
                
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)


def main() -> None:
    """Entry point for the application."""
    machamp_process_request()


if __name__ == "__main__":
    main()
