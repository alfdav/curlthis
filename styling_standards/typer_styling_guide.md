# Typer CLI Styling Guide

This guide extends the existing terminal styling standards to specifically address Typer implementation with Pokemon naming convention.

## Overview

Typer is the preferred CLI framework for all new projects. It provides a clean, modern interface with built-in rich formatting support. This guide demonstrates how to combine Typer with the Pokemon naming convention required by our terminal styling standards.

## Basic Setup

```python
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import box
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
    rich_markup_mode="rich"  # Enable rich markup in help text
)
```

## Key Differences from Click Implementation

The Typer implementation differs from the Click implementation in several key ways:

1. **Built-in Rich Formatting**: Typer has built-in support for Rich formatting in help text via the `rich_markup_mode="rich"` parameter.
2. **Type Annotations**: Typer uses Python type annotations for parameters, making the code more readable and self-documenting.
3. **Command Groups**: Typer has built-in support for command groups, making it easier to organize complex CLIs.
4. **Help Text Formatting**: Typer's help text is automatically formatted with Rich, eliminating the need for custom help command classes.

## Command Structure

When creating commands with Typer, use the Pokemon naming convention for the function name:

```python
@app.command()
def machamp_process_file(
    file_path: str = typer.Argument(..., help="Path to the file to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Process a file with detailed analysis.
    
    This command demonstrates how to structure a Typer command with
    the Pokemon naming convention while maintaining clean help output.
    """
    # Implementation...
```

## Command Groups

For applications with multiple command groups, use the `machamp_create_command_group` function:

```python
# Create a command group
data_commands = machamp_create_command_group("data", "Data processing commands")

@data_commands.command()
def alakazam_analyze_content(
    file_path: str = typer.Argument(..., help="File to analyze")
) -> None:
    """Analyze content of a file."""
    # Implementation...

# Add the command group to the main app
app.add_typer(data_commands)
```

## Helper Functions

Use these standardized helper functions with Pokemon naming:

### Banner Display

```python
def hitmonchan_show_banner(title: str, description: str = None) -> None:
    """Display application banner with standardized styling."""
    panel = Panel.fit(
        f"[bold cyan]{title}[/bold cyan]" + 
        (f"\n\n{description}" if description else ""),
        border_style="blue"
    )
    console.print(panel)
```

Usage:
```python
hitmonchan_show_banner("Application Name", "Application description")
```

### Error Handling

```python
def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details."""
    console.print(f"{STATUS['error']} {message}")
    if exception and str(exception):
        console.print(f"[dim]{str(exception)}[/dim]")
```

Usage:
```python
try:
    # Some operation
except Exception as e:
    primeape_show_error("Operation failed", e)
```

### Warning Messages

```python
def primeape_show_warning(message: str) -> None:
    """Display warning message."""
    console.print(f"{STATUS['warning']} {message}")
```

Usage:
```python
if some_condition:
    primeape_show_warning("This operation may take a long time")
```

### Success Messages

```python
def hitmonchan_show_success(message: str) -> None:
    """Display success message."""
    console.print(f"{STATUS['success']} {message}")
```

Usage:
```python
hitmonchan_show_success("Operation completed successfully")
```

### Progress Indication

```python
def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message with optional spinner."""
    if spinner:
        with Progress(
            SpinnerColumn(),
            TextColumn("[blue]{task.description}[/blue]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
    else:
        console.print(f"{STATUS['info']} {message}")
```

Usage:
```python
hitmonchan_show_progress("Processing data...", spinner=True)
```

### Code Display

```python
def kadabra_display_code(code: str, language: str = "bash", title: str = "Generated code") -> None:
    """Display code with syntax highlighting in a panel."""
    panel = Panel(
        Syntax(code, language, theme="monokai", word_wrap=True, line_numbers=True),
        title=f"[bold]{title}[/bold]",
        border_style="green",
        expand=False
    )
    console.print(panel)
```

Usage:
```python
kadabra_display_code("print('Hello, World!')", "python", "Example Code")
```

### Input Validation

```python
def mewtwo_validate_input(value: str, pattern: str = None) -> bool:
    """Validate input against a pattern."""
    if not value:
        return False
        
    if pattern:
        import re
        return bool(re.match(pattern, value))
        
    return True
```

Usage:
```python
if not mewtwo_validate_input(file_path, r'^[\w\-. /]+$'):
    primeape_show_error(f"Invalid file path format: {file_path}")
    raise typer.Exit(code=1)
```

## Rich Formatting in Help Text

Typer supports rich formatting in help text when `rich_markup_mode="rich"` is set:

```python
@app.command()
def hitmonlee_verify_file(
    file_path: str = typer.Argument(
        ..., 
        help="File to [bold cyan]verify[/bold cyan]"
    )
) -> None:
    """
    [bold]Verify[/bold] a file's integrity and contents.
    
    This command will:
    - Check [green]file existence[/green]
    - Verify [yellow]file permissions[/yellow]
    - Analyze [red]file content[/red]
    """
    # Implementation...
```

This will render the help text with Rich formatting, making it more readable and visually appealing.

## Main Function

Always use a standardized main function:

```python
def main():
    """Main entry point for the application."""
    try:
        app()
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()
```

## Complete Example

Here's a complete example of a Typer application with Pokemon naming convention:

```python
import typer
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback

# Install Rich traceback handler
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Create console for rich output
console = Console()

# Status indicators
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

# Create Typer app
app = typer.Typer(
    help="File processing tool",
    add_completion=True,
    rich_markup_mode="rich"
)

# Helper functions
def hitmonchan_show_banner(title: str, description: str = None) -> None:
    """Display application banner."""
    panel = Panel.fit(
        f"[bold cyan]{title}[/bold cyan]" + 
        (f"\n\n{description}" if description else ""),
        border_style="blue"
    )
    console.print(panel)

def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message."""
    console.print(f"{STATUS['error']} {message}")
    if exception and str(exception):
        console.print(f"[dim]{str(exception)}[/dim]")

def hitmonchan_show_success(message: str) -> None:
    """Display success message."""
    console.print(f"{STATUS['success']} {message}")

# Command implementation
@app.command()
def machamp_process_file(
    file_path: str = typer.Argument(..., help="File to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Process a file with detailed analysis.
    
    This command will analyze the file and provide information about its
    content, size, and other properties.
    """
    hitmonchan_show_banner("File Processor", "Analyze file content")
    
    try:
        # Process file
        hitmonchan_show_success(f"File {file_path} processed successfully")
        
        if verbose:
            # Show detailed results
            table = Table(title="File Analysis Results")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="white")
            
            table.add_row("File", file_path)
            table.add_row("Status", "[green]Processed[/green]")
            
            console.print(table)
    except Exception as e:
        primeape_show_error("Failed to process file", e)
        raise typer.Exit(code=1)

def main():
    """Main entry point."""
    try:
        app()
    except Exception as e:
        primeape_show_error("An unexpected error occurred", e)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    main()
```

## Reference Implementation

See the complete reference implementation in `styling_standards/python_terminal_styling/typer_template.py`.

## Author

David Diaz (https://github.com/alfdav)