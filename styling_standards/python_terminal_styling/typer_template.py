"""
Typer-based terminal styling template with Pokemon naming convention.

This template demonstrates how to implement the Pokemon naming convention
with Typer for cleaner, more modern CLI applications.

Author: David Diaz (https://github.com/alfdav)
"""
from typing import Optional, List, Dict, Any
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create console for rich output
console = Console()

# Status indicators - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

# Create Typer app with rich formatting
app = typer.Typer(
    help="Application description",
    add_completion=True,
    rich_markup_mode="rich"
)

# Pokemon-themed helper functions
def hitmonchan_show_banner(title: str, description: str = None) -> None:
    """Display application banner with standardized styling.
    
    Hitmonchan's precision and presentation style is perfect for displaying
    the application banner with clean, impactful visual feedback.
    
    Args:
        title: The title to display in the banner
        description: Optional description to display below the title
    """
    panel = Panel.fit(
        f"[bold cyan]{title}[/bold cyan]" + 
        (f"\n\n{description}" if description else ""),
        border_style="blue"
    )
    console.print(panel)

def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Primeape's intense and reactive nature makes it perfect for error handling,
    quickly responding to problems with clear, attention-grabbing messages.
    
    Args:
        message: The error message to display
        exception: Optional exception to display details for
    """
    console.print(f"{STATUS['error']} {message}")
    if exception and str(exception):
        console.print(f"[dim]{str(exception)}[/dim]")

def primeape_show_warning(message: str) -> None:
    """Display warning message.
    
    Primeape's alertness helps identify potential issues that need attention
    but aren't critical failures.
    
    Args:
        message: The warning message to display
    """
    console.print(f"{STATUS['warning']} {message}")

def hitmonchan_show_success(message: str) -> None:
    """Display success message.
    
    Hitmonchan's precision ensures success messages are clear and impactful.
    
    Args:
        message: The success message to display
    """
    console.print(f"{STATUS['success']} {message}")

def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message with optional spinner.
    
    Hitmonchan's speed and precision make it ideal for showing progress updates.
    
    Args:
        message: The progress message to display
        spinner: Whether to show a spinner animation
    """
    if spinner:
        with Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
    else:
        console.print(f"{STATUS['info']} {message}")

def kadabra_display_code(code: str, language: str = "bash", title: str = "Generated code") -> None:
    """Display code with syntax highlighting in a panel.
    
    Kadabra's transformation abilities make it perfect for formatting and
    displaying code with proper syntax highlighting.
    
    Args:
        code: The code to display
        language: The language for syntax highlighting
        title: The title of the panel
    """
    panel = Panel(
        Syntax(code, language, theme="monokai", word_wrap=True, line_numbers=True),
        title=f"[bold]{title}[/bold]",
        border_style="green",
        expand=False
    )
    console.print(panel)

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

def rapidash_create_progress(transient: bool = True):
    """Create and return a Rich progress bar.
    
    Rapidash's speed represents progress tracking, making it
    perfect for creating progress indicators.
    
    Args:
        transient: Whether the progress bar should disappear after completion
        
    Returns:
        A Progress instance configured with standard columns
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        transient=transient
    )

def mewtwo_validate_input(value: str, pattern: str = None) -> bool:
    """Validate input against a pattern.
    
    Mewtwo's analytical abilities make it perfect for validating input.
    
    Args:
        value: The value to validate
        pattern: Optional regex pattern to validate against
        
    Returns:
        True if valid, False otherwise
    """
    if not value:
        return False
        
    if pattern:
        import re
        return bool(re.match(pattern, value))
        
    return True

# Example command implementation
@app.command()
def machamp_process_file(
    file_path: str = typer.Argument(..., help="Path to the file to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path")
) -> None:
    """
    Process a file with detailed analysis.
    
    This command demonstrates how to structure a Typer command with
    the Pokemon naming convention while maintaining clean help output.
    
    Examples:
        $ app data.txt
        $ app data.txt --verbose
        $ app data.txt --output results.txt
    """
    # Show banner
    hitmonchan_show_banner(
        "File Processor",
        "Analyze and process file content"
    )
    
    # Validate input
    if not file_path:
        primeape_show_error("No file path provided")
        raise typer.Exit(code=1)
    
    # Show progress
    hitmonchan_show_progress(f"Processing file: {file_path}", spinner=True)
    
    # Show success
    hitmonchan_show_success(f"File {file_path} processed successfully")
    
    # Example table output
    if verbose:
        table = Table(title="File Analysis Results")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("File", file_path)
        table.add_row("Status", "[green]Processed[/green]")
        table.add_row("Size", "1.2 KB")
        
        console.print(table)
    
    # Example code display
    sample_code = f"cat {file_path} | grep 'pattern'"
    kadabra_display_code(sample_code, "bash", "Example Command")
    
    # Example output to file
    if output:
        try:
            with open(output, 'w') as f:
                f.write(f"File: {file_path}\nStatus: Processed\nSize: 1.2 KB\n")
            hitmonchan_show_success(f"Results saved to {output}")
        except Exception as e:
            primeape_show_error(f"Failed to write to {output}", e)

# Example command group
data_commands = machamp_create_command_group("data", "Data processing commands")

@data_commands.command()
def alakazam_analyze_content(
    file_path: str = typer.Argument(..., help="File to analyze")
) -> None:
    """
    Analyze content of a file.
    
    This command demonstrates how to use command groups with
    the Pokemon naming convention.
    """
    hitmonchan_show_banner("Content Analyzer", "Analyze file content")
    hitmonchan_show_progress(f"Analyzing content of {file_path}", spinner=True)
    hitmonchan_show_success(f"Content analysis complete for {file_path}")

# Add the command group to the main app
app.add_typer(data_commands)

def main():
    """Main entry point for the application."""
    try:
        app()
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()