# ADR 001: Standardizing Typer CLI Styling with Pokemon Naming Convention

## Status

Proposed

## Date

2025-03-06

## Context

We currently have two different approaches to CLI styling in our projects:

1. **andns2**: Uses `typer` with its built-in rich formatting support, resulting in a clean, modern interface
2. **curlthis**: Uses `click` with a custom `RichHelpCommand` class that completely overrides the default help display

Our existing terminal styling standards document (terminal_styling_standards.md) mandates the Pokemon naming convention but doesn't specifically address Typer implementation. The document mentions Typer as a core UI dependency but provides examples primarily using Click.

We prefer the styling approach used in andns2 and want to standardize this across all projects while maintaining the Pokemon naming convention.

## Decision

We will standardize on using Typer for CLI applications with the following guidelines:

1. **Keep the Pokemon naming convention** for all functions as specified in the existing standards
2. **Use Typer's built-in rich formatting** instead of custom Click command classes
3. **Adopt the cleaner styling approach** from andns2 for all CLI applications
4. **Create a reference implementation** that demonstrates how to combine Typer with Pokemon naming

## Implementation Steps

### 1. Create a Typer Template with Pokemon Naming

Create a new file `styling_standards/python_terminal_styling/typer_template.py` that demonstrates the standard:

```python
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
    """
    console.print(f"{STATUS['error']} {message}")
    if exception and str(exception):
        console.print(f"[dim]{str(exception)}[/dim]")

def primeape_show_warning(message: str) -> None:
    """Display warning message.
    
    Primeape's alertness helps identify potential issues that need attention
    but aren't critical failures.
    """
    console.print(f"{STATUS['warning']} {message}")

def hitmonchan_show_success(message: str) -> None:
    """Display success message.
    
    Hitmonchan's precision ensures success messages are clear and impactful.
    """
    console.print(f"{STATUS['success']} {message}")

def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message with optional spinner.
    
    Hitmonchan's speed and precision make it ideal for showing progress updates.
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
    """
    return typer.Typer(
        name=name,
        help=help_text,
        rich_markup_mode="rich"
    )

# Example command implementation
@app.command()
def machamp_process_request(
    domain: str = typer.Argument(..., help="Domain to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file path")
) -> None:
    """
    Process a domain request with detailed analysis.
    
    This command demonstrates how to structure a Typer command with
    the Pokemon naming convention while maintaining clean help output.
    """
    # Show banner
    hitmonchan_show_banner(
        "Domain Processor",
        "Analyze and process domain information"
    )
    
    # Show progress
    hitmonchan_show_progress(f"Processing domain: {domain}", spinner=True)
    
    # Show success
    hitmonchan_show_success(f"Domain {domain} processed successfully")
    
    # Example table output
    if verbose:
        table = Table(title="Domain Analysis Results")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("Domain", domain)
        table.add_row("Status", "[green]Active[/green]")
        table.add_row("Created", "2023-01-01")
        
        console.print(table)
    
    # Example code display
    sample_code = f"curl -X GET https://{domain}/api/status"
    kadabra_display_code(sample_code, "bash", "Example API Request")

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

### 2. Create a Typer-Specific Styling Guide

Create a new file `styling_standards/typer_styling_guide.md` that documents the Typer-specific styling standards:

```markdown
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

## Command Structure

When creating commands with Typer, use the Pokemon naming convention for the function name:

```python
@app.command()
def machamp_process_request(
    domain: str = typer.Argument(..., help="Domain to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
) -> None:
    """
    Process a domain request with detailed analysis.
    
    This command demonstrates how to structure a Typer command with
    the Pokemon naming convention while maintaining clean help output.
    """
    # Implementation...
```

## Command Groups

For applications with multiple command groups, use the `machamp_create_command_group` function:

```python
# Create a command group
dns_commands = machamp_create_command_group("dns", "DNS-related commands")

@dns_commands.command()
def alakazam_analyze_records(
    domain: str = typer.Argument(..., help="Domain to analyze")
) -> None:
    """Analyze DNS records for a domain."""
    # Implementation...

# Add the command group to the main app
app.add_typer(dns_commands)
```

## Helper Functions

Use these standardized helper functions with Pokemon naming:

1. **Banner Display**:
   ```python
   hitmonchan_show_banner("Application Name", "Application description")
   ```

2. **Error Handling**:
   ```python
   try:
       # Some operation
   except Exception as e:
       primeape_show_error("Operation failed", e)
   ```

3. **Progress Indication**:
   ```python
   hitmonchan_show_progress("Processing data...", spinner=True)
   ```

4. **Success Messages**:
   ```python
   hitmonchan_show_success("Operation completed successfully")
   ```

5. **Code Display**:
   ```python
   kadabra_display_code("print('Hello, World!')", "python", "Example Code")
   ```

## Rich Formatting in Help Text

Typer supports rich formatting in help text when `rich_markup_mode="rich"` is set:

```python
@app.command()
def hitmonlee_verify_domain(
    domain: str = typer.Argument(
        ..., 
        help="Domain to [bold cyan]verify[/bold cyan]"
    )
) -> None:
    """
    [bold]Verify[/bold] a domain's ownership and security.
    
    This command will:
    - Check [green]WHOIS[/green] information
    - Verify [yellow]DNS[/yellow] records
    - Analyze [red]SSL[/red] certificates
    """
    # Implementation...
```

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

## Reference Implementation

See the complete reference implementation in `styling_standards/python_terminal_styling/typer_template.py`.
```

### 3. Update the Python Terminal Styling README

Update the `styling_standards/python_terminal_styling/README.md` file to include information about the new Typer template:

```markdown
# Python Terminal Styling

This package provides standardized terminal styling templates for Python applications, following the Pokemon-themed naming convention.

## Templates

The package includes two main templates:

1. **Click-based Template** - The original template using Click for CLI applications
2. **Typer-based Template** - The new recommended template using Typer for cleaner CLI interfaces

## Typer Template

The Typer template is the recommended approach for all new CLI applications. It combines:

- The Pokemon naming convention required by our standards
- Typer's built-in rich formatting for cleaner help output
- The styling approach used in the andns2 project

### Usage

```python
from python_terminal_styling.typer_template import (
    app,
    hitmonchan_show_banner,
    primeape_show_error,
    hitmonchan_show_success
)

@app.command()
def machamp_process_data(
    input_file: str = typer.Argument(..., help="Input file path")
):
    """Process data from the input file."""
    hitmonchan_show_banner("Data Processor", "Process data files")
    
    try:
        # Process data
        hitmonchan_show_success("Data processed successfully")
    except Exception as e:
        primeape_show_error("Failed to process data", e)

if __name__ == "__main__":
    app()
```

See the `typer_template.py` file for a complete reference implementation.
```

## Consequences

### Positive

1. **Consistent User Experience**: All CLI applications will have a similar look and feel
2. **Improved Developer Experience**: Typer's type annotations and built-in help formatting make it easier to create well-documented CLIs
3. **Maintained Standards Compliance**: The Pokemon naming convention is preserved
4. **Reduced Code Duplication**: No need for custom help formatting classes
5. **Better Help Output**: Typer's built-in rich formatting provides cleaner, more readable help text

### Negative

1. **Migration Effort**: Existing Click-based applications will need to be migrated to Typer
2. **Learning Curve**: Developers familiar with Click will need to learn Typer
3. **Potential Inconsistency**: During the transition period, some applications will use Click while others use Typer

### Neutral

1. **Dual Standards**: We will maintain both Click and Typer examples in our standards documentation
2. **Gradual Adoption**: New projects will use Typer, while existing projects can migrate as needed

## References

1. [Typer Documentation](https://typer.tiangolo.com/)
2. [Rich Documentation](https://rich.readthedocs.io/)
3. [Terminal Styling Standards](./terminal_styling_standards.md)
4. [andns2 Project](https://github.com/alfdav/andns2)