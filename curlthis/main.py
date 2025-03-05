#!/usr/bin/env python3
"""
Main module for curlthis CLI application.
"""
from typing import Optional, TextIO, List
import sys
import click
import pyperclip

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.table import Table
from rich import box
from rich.markdown import Markdown
from rich.rule import Rule
from rich.progress import Progress, SpinnerColumn, TextColumn

from curlthis.parser import alakazam_parse_request
from curlthis.formatter import kadabra_format_curl

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Console instances
console = Console()
error_console = Console(stderr=True)

# ANSI color codes (for compatibility with other tools)
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color


def hitmonchan_show_banner() -> None:
    """Display application banner.
    
    Hitmonchan's precision and presentation style is perfect for displaying
    the application banner with clean, impactful visual feedback.
    """
    # Use the same style as andns2
    banner = Panel(
        "[bold cyan]Transform raw HTTP requests into curl one-liners[/bold cyan]",
        title="[bold]curlthis v0.1.0[/bold]",
        border_style="blue"
    )
    console.print(banner)


def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Primeape's intense and reactive nature makes it perfect for error handling,
    quickly responding to problems with clear, attention-grabbing messages.
    """
    # Match andns2 error style
    error_console.print(f"[red][[/red][bold white]✗[/bold white][red]][/red] {message}")
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")


def primeape_show_warning(message: str) -> None:
    """Display warning message.
    
    Primeape's alertness helps identify potential issues that need attention
    but aren't critical failures.
    """
    console.print(f"[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow] {message}")


def hitmonchan_show_success(message: str) -> None:
    """Display success message.
    
    Hitmonchan's precision delivers clear success indicators with style.
    """
    console.print(f"[green][[/green][bold white]✓[/bold white][green]][/green] {message}")


def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message.
    
    Hitmonchan's speed and precision are perfect for showing progress updates.
    """
    if spinner:
        with Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
    else:
        console.print(f"[blue][[/blue][bold white]*[/bold white][blue]][/blue] {message}")


class RichHelpCommand(click.Command):
    """Custom click.Command that displays help using Rich styling."""
    
    def format_help(self, ctx, formatter):
        # Use Rich for help display instead of the default formatter
        hitmonchan_show_banner()
        
        # Command description with rule
        console.print(Rule(title="[bold cyan]Description[/bold cyan]", style="cyan"))
        console.print(f"{self.help}\n")
        
        # Usage section with rule
        usage_text = self.collect_usage(ctx)
        console.print(Rule(title="[bold cyan]Usage[/bold cyan]", style="cyan"))
        console.print(f"{usage_text}\n")
        
        # Options table with rule
        options = self.collect_options(ctx)
        if options:
            console.print(Rule(title="[bold cyan]Options[/bold cyan]", style="cyan"))
            options_table = Table(box=box.ROUNDED, show_header=False, expand=True)
            options_table.add_column("Option", style="bold")
            options_table.add_column("Description")
            
            for opt in options:
                options_table.add_row(opt["name"], opt["help"])
            
            console.print(options_table)
            console.print()
        
        # Examples section with rule
        console.print(Rule(title="[bold cyan]Examples[/bold cyan]", style="cyan"))
        examples = [
            ("From a file:", "curlthis -f request.txt"),
            ("From stdin:", "cat request.txt | curlthis"),
            ("Copy to clipboard:", "curlthis -f request.txt -c"),
            ("Verbose output:", "curlthis -f request.txt -v")
        ]
        
        examples_table = Table(box=box.ROUNDED, show_header=False, expand=True)
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
        result_panel = Panel(
            Syntax(curl_command, "bash", theme="monokai", word_wrap=True),
            title="[bold]Generated curl command[/bold]",
            border_style="green",
            expand=False
        )
        console.print(result_panel)
        
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
