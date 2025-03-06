"""
Utility module for curlthis CLI styling and output functions.
"""
from typing import Optional, Any
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.theme import Theme
from rich.rule import Rule

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Define custom theme
custom_theme = Theme({
    "info": "blue",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "header": "cyan bold"
})

# Console instances
console = Console(theme=custom_theme)
error_console = Console(stderr=True, theme=custom_theme)

# Status indicators dictionary
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}


def hitmonchan_show_banner(title: str = "curlthis v0.1.0", 
                         description: str = "Transform raw HTTP requests into curl one-liners",
                         author: str = "Alfredo Davis") -> None:
    """Display application banner.
    
    Hitmonchan's precision and presentation style is perfect for displaying
    the application banner with clean, impactful visual feedback.
    
    Args:
        title: The title to display in the banner
        description: The description to display in the banner
        author: The author name to display in the banner subtitle
    """
    content = f"[bold cyan]{description}[/bold cyan]"
    
    banner = Panel(
        content,
        title=f"[bold]{title}[/bold]",
        subtitle=f"By {author}" if author else None,
        border_style="blue"
    )
    console.print(banner)


def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Primeape's intense and reactive nature makes it perfect for error handling,
    quickly responding to problems with clear, attention-grabbing messages.
    
    Args:
        message: The error message to display
        exception: Optional exception to display details for
    """
    error_panel = Panel(
        f"{STATUS['error']} {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")


def primeape_show_warning(message: str) -> None:
    """Display warning message.
    
    Primeape's alertness helps identify potential issues that need attention
    but aren't critical failures.
    
    Args:
        message: The warning message to display
    """
    warning_panel = Panel(
        f"{STATUS['warning']} {message}",
        border_style="yellow", 
        title="Warning"
    )
    console.print(warning_panel)


def hitmonchan_show_success(message: str) -> None:
    """Display success message.
    
    Hitmonchan's precision delivers clear success indicators with style.
    
    Args:
        message: The success message to display
    """
    console.print(f"{STATUS['success']} {message}")


def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message.
    
    Hitmonchan's speed and precision are perfect for showing progress updates.
    
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


def create_table(title: str, style: str = "header") -> Table:
    """Create a table with the given title.
    
    Args:
        title: The title of the table
        style: The style to apply to the title
        
    Returns:
        A Rich Table object with rounded box styling
    """
    table = Table(title=title, title_style=style, box=box.ROUNDED)
    return table


def create_section(title: str) -> None:
    """Create a section header with a rule.
    
    Args:
        title: The title of the section
    """
    console.print(Rule(title=f"[bold cyan]{title}[/bold cyan]", style="cyan"))


def display_code(code: str, language: str = "bash", theme: str = "monokai", 
                title: str = "Generated code", border_style: str = "green") -> None:
    """Display code with syntax highlighting in a panel.
    
    Args:
        code: The code to display
        language: The language for syntax highlighting
        theme: The color theme for syntax highlighting
        title: The title of the panel
        border_style: The color of the panel border
    """
    panel = Panel(
        Syntax(code, language, theme=theme, word_wrap=True),
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)