"""
Utility module for curlthis CLI styling and output functions.

This module provides standardized styling functions for the curlthis CLI
using the Rich library. It follows the Pokemon-themed function naming convention
with Fighting-type Pokemon for system operations.
"""
from typing import Optional, Any, List, Dict, Union
import sys
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.theme import Theme
from rich.rule import Rule
from rich.markdown import Markdown

# Install Rich traceback handler for global exception beautification
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Define custom theme matching standards
custom_theme = Theme({
    # Base colors
    "info": "blue",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "header": "cyan bold",
    
    # Additional styles
    "code": "cyan",
    "command": "cyan bold",
    "filename": "cyan",
    "path": "cyan",
    "url": "blue underline",
    "dim": "dim",
    "bold": "bold",
    "italic": "italic",
    "underline": "underline",
    "strike": "strike",
    "highlight": "black on yellow",
    "title": "cyan bold"
})

# Main console instance
console = Console(theme=custom_theme)

# Error console (stderr)
error_console = Console(stderr=True, theme=custom_theme)

# Status indicators dictionary with standardized styling
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}


def hitmonchan_show_banner(title: str = "curlthis v0.1.0", 
                         description: str = "Transform raw HTTP requests into curl one-liners",
                         author: str = "David Diaz (https://github.com/alfdav)",
                         version: str = "0.1.0") -> None:
    """Display application banner with standardized styling.
    
    Creates a styled banner with the application title, description, version,
    and author information using Rich panels.
    
    Args:
        title: The title to display in the banner
        description: The description to display in the banner
        author: The author name to display in the banner subtitle
        version: The version to display in the banner
    """
    # Format content with description and version
    content = f"[bold]{title}[/bold] - [italic]{description}[/italic]\n\n"
    content += f"[dim]Version: {version}[/dim]"
    
    # Create banner panel with standardized styling
    banner = Panel(
        content,
        border_style="blue",
        subtitle=f"By {author}" if author else None,
        expand=False
    )
    console.print(banner)


def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details.
    
    Shows a styled error panel with the provided message and optionally
    displays exception details if provided.
    
    Args:
        message: The error message to display
        exception: Optional exception to display details for
    """
    # Create error panel with standardized styling
    error_panel = Panel(
        f"[bold red]ERROR:[/bold red] {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    
    # Show exception details if available
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")


def primeape_show_warning(message: str) -> None:
    """Display warning message in a styled panel.
    
    Shows a yellow-bordered panel with the warning message to
    draw attention to potential issues.
    
    Args:
        message: The warning message to display
    """
    # Create warning panel with standardized styling
    warning_panel = Panel(
        f"[bold yellow]WARNING:[/bold yellow] {message}",
        border_style="yellow", 
        title="Warning"
    )
    console.print(warning_panel)


def hitmonchan_show_success(message: str) -> None:
    """Display success message with a checkmark indicator.
    
    Shows a green checkmark followed by the success message.
    
    Args:
        message: The success message to display
    """
    console.print(f"{STATUS['success']} {message}")


def hitmonchan_show_progress(message: str, spinner: bool = False, 
                           total: Optional[float] = None) -> Optional[Progress]:
    """Display progress message or create a progress bar.
    
    Shows a simple progress message, a spinner animation, or a full progress bar
    depending on the parameters provided.
    
    Args:
        message: The progress message to display
        spinner: Whether to show a spinner animation
        total: Optional total for progress tracking (None for indeterminate)
        
    Returns:
        Progress object if total is provided, None otherwise
    """
    if spinner:
        # Create spinner with standardized styling
        with Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
        return None
    elif total is not None:
        # Create progress bar with standardized columns
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        )
        task_id = progress.add_task(message, total=total)
        return progress
    else:
        # Simple progress message
        console.print(f"{STATUS['info']} {message}")
        return None


def create_table(title: str, style: str = "header", 
                show_header: bool = True, box_style: box = box.ROUNDED) -> Table:
    """Create a table with the given title and standardized styling.
    
    Args:
        title: The title of the table
        style: The style to apply to the title
        show_header: Whether to show the header
        box_style: The box style to use
        
    Returns:
        A Rich Table object with standardized styling
    """
    table = Table(
        title=title, 
        title_style=style, 
        box=box_style,
        show_header=show_header,
        header_style="bold cyan"
    )
    return table


def create_section(title: str, style: str = "cyan") -> None:
    """Create a section header with a rule.
    
    Args:
        title: The title of the section
        style: The style to apply to the rule
    """
    console.print(Rule(title=f"[bold {style}]{title}[/bold {style}]", style=style))


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
    # Create syntax-highlighted code with standardized styling
    syntax = Syntax(
        code, 
        language, 
        theme=theme, 
        word_wrap=True, 
        line_numbers=False,
        code_width=100
    )
    
    # Create panel with standardized styling
    panel = Panel(
        syntax,
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)