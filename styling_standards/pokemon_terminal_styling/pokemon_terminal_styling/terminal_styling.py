"""
Terminal styling utility module implementing the terminal styling standards.

This module provides standardized functions for terminal output styling using the Rich library.
It follows the Pokemon-themed naming convention for functions.
"""

from typing import Optional, Any, List, Dict
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.theme import Theme
from rich.rule import Rule
from rich import box
import sys
import time

# Install Rich traceback handler for global exception beautification
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Define custom theme
custom_theme = Theme({
    "info": "blue",
    "warning": "yellow",
    "error": "red",
    "success": "green",
    "header": "cyan bold"
})

# Main console instance
console = Console(theme=custom_theme)

# Error console (stderr)
error_console = Console(stderr=True, theme=custom_theme)

# Status indicators dictionary - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

# Status styles dictionary
STATUS_STYLES = {
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "info": "bold blue",
    "pending": "bold cyan",
    "skipped": "dim",
    "unknown": "white"
}

# UI/Display functions

def hitmonchan_show_banner(title: str = "Application v1.0.0", 
                         description: str = "Application description",
                         author: str = "David Diaz") -> None:
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
        border_style="blue",
        box=box.ROUNDED
    )
    console.print(banner)

def hitmonchan_show_success(message: str) -> None:
    """Display success message.
    
    Args:
        message: The success message to display
    """
    console.print(f"{STATUS['success']} {message}")

def hitmonchan_show_info(message: str) -> None:
    """Display info message.
    
    Args:
        message: The info message to display
    """
    console.print(f"{STATUS['info']} {message}")

def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message.
    
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

def hitmonchan_display_results_table(results: List[Dict[str, Any]], columns: List[Dict[str, str]]) -> None:
    """Display results in a formatted table.
    
    Args:
        results: List of dictionaries containing the results
        columns: List of dictionaries with 'name' and 'key' keys
    """
    table = create_table("Results")
    
    # Add columns
    for col in columns:
        table.add_column(col["name"], style=col.get("style", "white"))
    
    # Add rows
    for result in results:
        row_values = [str(result.get(col["key"], "N/A")) for col in columns]
        table.add_row(*row_values)
    
    console.print(table)

def hitmonchan_display_info_panel(title: str, content: str, style: str = "blue") -> None:
    """Display information in a panel.
    
    Args:
        title: The title of the panel
        content: The content to display in the panel
        style: The style to apply to the panel border
    """
    panel = Panel(
        content,
        title=title,
        border_style=style,
        box=box.ROUNDED
    )
    console.print(panel)

# Error handling functions

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

# Progress tracking functions

def rapidash_create_progress():
    """Create and return a Rich progress bar.
    
    Rapidash's speed makes it perfect for tracking progress.
    
    Returns:
        A Rich Progress object
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(),
        TaskProgressColumn(),
        TextColumn("• {task.fields[status]}"),
        expand=True
    )

# Code display functions

def kadabra_display_code(code: str, language: str = "bash", theme: str = "monokai", 
                       title: str = "Generated code", border_style: str = "green") -> None:
    """Display code with syntax highlighting in a panel.
    
    Kadabra's transformation abilities make it perfect for formatting and displaying code.
    
    Args:
        code: The code to display
        language: The language for syntax highlighting
        theme: The color theme for syntax highlighting
        title: The title of the panel
        border_style: The color of the panel border
    """
    panel = Panel(
        Syntax(code, language, theme=theme, word_wrap=True, line_numbers=True),
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)

def snorlax_display_file_content(file_path: str, language: Optional[str] = None) -> None:
    """Display file content with syntax highlighting.
    
    Snorlax's storage capacity makes it perfect for handling file operations.
    
    Args:
        file_path: The path to the file to display
        language: The language for syntax highlighting (auto-detected if None)
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()
        
        # Auto-detect language from file extension if not provided
        if language is None:
            import os
            ext = os.path.splitext(file_path)[1].lstrip(".")
            language = {
                "py": "python",
                "js": "javascript",
                "html": "html",
                "css": "css",
                "json": "json",
                "md": "markdown"
            }.get(ext, "text")
        
        kadabra_display_code(content, language, title=f"File: {file_path}")
    except Exception as e:
        primeape_show_error(f"Failed to display file: {file_path}", e)

# Helper functions

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

def get_styled_status(status: str) -> str:
    """Get a styled status string.
    
    Args:
        status: The status string
        
    Returns:
        A styled status string
    """
    status_lower = status.lower()
    style = STATUS_STYLES.get(status_lower, "white")
    return f"[{style}]{status}[/{style}]"

# Processing functions

def machamp_process_request(input_data: Any) -> Dict[str, Any]:
    """Process a request with the given input data.
    
    Machamp's multiple arms represent handling multiple operations simultaneously.
    
    Args:
        input_data: The input data to process
        
    Returns:
        A dictionary with the processed results
    """
    # This is a placeholder implementation
    # Replace with actual processing logic
    result = {
        "status": "success",
        "message": "Request processed successfully",
        "data": input_data
    }
    return result

# Verification functions

def hitmonlee_verify_python() -> bool:
    """Verify Python installation.
    
    Hitmonlee's High Jump Kick represents verification leaps.
    
    Returns:
        True if Python is installed correctly, False otherwise
    """
    import sys
    python_version = sys.version_info
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        primeape_show_error(f"Python version {python_version.major}.{python_version.minor} detected. Version 3.8 or higher is required.")
        return False
    
    hitmonchan_show_success(f"Python {python_version.major}.{python_version.minor}.{python_version.micro} detected.")
    return True

# Setup functions

def machoke_setup_venv(venv_dir: str) -> bool:
    """Set up a virtual environment.
    
    Machoke's strength represents setting up environments.
    
    Args:
        venv_dir: The directory for the virtual environment
        
    Returns:
        True if setup was successful, False otherwise
    """
    import subprocess
    import os
    
    hitmonchan_show_info(f"Setting up virtual environment at {venv_dir}...")
    
    try:
        # Create virtual environment
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        
        # Determine activation script path
        if os.name == "nt":  # Windows
            activate_script = os.path.join(venv_dir, "Scripts", "activate")
        else:  # Unix/Linux/Mac
            activate_script = os.path.join(venv_dir, "bin", "activate")
        
        hitmonchan_show_success(f"Virtual environment created at {venv_dir}")
        hitmonchan_show_info(f"Activate with: source {activate_script}")
        return True
    except Exception as e:
        primeape_show_error("Failed to set up virtual environment", e)
        return False

# Example usage
if __name__ == "__main__":
    # Display banner
    hitmonchan_show_banner(
        "Terminal Styling Demo",
        "Demonstration of terminal styling standards",
        "David Diaz"
    )
    
    # Display progress
    hitmonchan_show_progress("Initializing...", spinner=True)
    time.sleep(1)
    
    # Display success message
    hitmonchan_show_success("Initialization complete")
    
    # Display info panel
    hitmonchan_display_info_panel(
        "Information",
        "This is a demonstration of the terminal styling standards.\n"
        "It shows how to use the various functions to create a consistent UI."
    )
    
    # Display code
    sample_code = """
def hello_world():
    print("Hello, World!")
    
hello_world()
"""
    kadabra_display_code(sample_code, language="python", title="Sample Python Code")
    
    # Display progress bar
    with rapidash_create_progress() as progress:
        task = progress.add_task("[green]Processing...", total=100, status="Starting")
        
        for i in range(100):
            # Simulate work
            time.sleep(0.01)
            progress.update(task, advance=1, status=f"Processing item {i+1}")
    
    # Display results table
    results = [
        {"name": "Item 1", "status": "success", "value": 42},
        {"name": "Item 2", "status": "warning", "value": 18},
        {"name": "Item 3", "status": "error", "value": 0}
    ]
    
    columns = [
        {"name": "Name", "key": "name"},
        {"name": "Status", "key": "status"},
        {"name": "Value", "key": "value"}
    ]
    
    hitmonchan_display_results_table(results, columns)
    
    # Display section
    create_section("Verification")
    
    # Verify Python
    hitmonlee_verify_python()
    
    # Display warning
    primeape_show_warning("This is a warning message")
    
    # Display error
    try:
        # Simulate an error
        raise ValueError("This is a simulated error")
    except Exception as e:
        primeape_show_error("An error occurred", e)