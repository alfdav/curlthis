# Rich Terminal Styling Guide

## Overview

This guide provides comprehensive instructions for implementing consistent and professional terminal styling using the Rich library. The patterns and practices outlined here can be adapted to any Python CLI application.

## Table of Contents

1. [Setup and Initialization](#setup-and-initialization)
2. [Console Output](#console-output)
3. [Error Handling](#error-handling)
4. [UI Components](#ui-components)
5. [Progress Indicators](#progress-indicators)
6. [Status Styling](#status-styling)
7. [Code Display](#code-display)
8. [Implementation Checklist](#implementation-checklist)

## Setup and Initialization

### Basic Setup

```python
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich import box
import sys

# Install Rich traceback handler for global exception beautification
install_rich_traceback(show_locals=True, width=120, word_wrap=True)

# Main console instance
console = Console()

# Error console (stderr)
error_console = Console(stderr=True)
```

### Key Points

- Import all necessary Rich components at the module level
- Install the Rich traceback handler early in your application
- Create separate console instances for stdout and stderr
- Initialize these objects at the module level, not inside functions

## Console Output

### Basic Output

```python
# Simple output
console.print("Processing data...")

# Styled output
console.print("[bold green]Success![/bold green] Operation completed.")
console.print(f"Found [bold]{count}[/bold] matching items.")

# Multi-line output
console.print(
    "[bold blue]Summary:[/bold blue]\n"
    f"- Processed: [green]{processed}[/green]\n"
    f"- Skipped: [yellow]{skipped}[/yellow]\n"
    f"- Failed: [red]{failed}[/red]"
)
```

### Styling Tags

| Tag | Description | Example |
|-----|-------------|---------|
| `[bold]` | Bold text | `[bold]Important[/bold]` |
| `[italic]` | Italic text | `[italic]Note[/italic]` |
| `[underline]` | Underlined text | `[underline]Warning[/underline]` |
| `[red]` | Red text | `[red]Error[/red]` |
| `[green]` | Green text | `[green]Success[/green]` |
| `[blue]` | Blue text | `[blue]Information[/blue]` |
| `[yellow]` | Yellow text | `[yellow]Warning[/yellow]` |
| `[dim]` | Dimmed text | `[dim]Less important[/dim]` |

Combine tags: `[bold red]Critical Error[/bold red]`

## Error Handling

### Error Display Function

```python
def print_error(message, exception=None):
    """Display error message with optional exception details."""
    error_panel = Panel(
        f"[bold red]ERROR:[/bold red] {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")
```

### Warning Display Function

```python
def print_warning(message):
    """Display warning message."""
    warning_panel = Panel(
        f"[bold yellow]WARNING:[/bold yellow] {message}",
        border_style="yellow", 
        title="Warning"
    )
    console.print(warning_panel)
```

### Usage Example

```python
try:
    # Some operation that might fail
    result = process_data(input_data)
except Exception as e:
    print_error("Failed to process data", e)
    return False

if result.has_warnings:
    print_warning("Processing completed with warnings")
```

## UI Components

### Banner

```python
def print_banner(app_name, description, version="1.0.0", author=None):
    """Display application banner."""
    content = f"[bold]{app_name}[/bold] - [italic]{description}[/italic]\n\n"
    content += f"[dim]Version: {version}[/dim]"
    
    banner = Panel(
        content,
        subtitle=f"By {author}" if author else None,
        border_style="blue",
        box=box.ROUNDED
    )
    console.print(banner)
```

### Tables

```python
def create_results_table(title="Results"):
    """Create and return a styled table."""
    table = Table(
        title=title,
        show_header=True,
        header_style="bold magenta",
        box=box.ROUNDED
    )
    return table

def display_results_table(results, columns):
    """Display results in a formatted table."""
    table = create_results_table()
    
    # Add columns
    for col in columns:
        table.add_column(col["name"], style=col.get("style", "white"))
    
    # Add rows
    for result in results:
        row_values = [str(result.get(col["key"], "N/A")) for col in columns]
        table.add_row(*row_values)
    
    console.print(table)
```

### Panels

```python
def display_info_panel(title, content, style="blue"):
    """Display information in a panel."""
    panel = Panel(
        content,
        title=title,
        border_style=style,
        box=box.ROUNDED
    )
    console.print(panel)
```

## Progress Indicators

### Basic Progress Bar

```python
def create_progress():
    """Create and return a Rich progress bar."""
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(),
        TaskProgressColumn(),
        TextColumn("• {task.fields[status]}"),
        expand=True
    )

# Usage example
with create_progress() as progress:
    task = progress.add_task("[green]Processing...", total=100, status="Starting")
    
    for i in range(100):
        # Do some work
        progress.update(task, advance=1, status=f"Processing item {i+1}")
        time.sleep(0.1)
```

### Multiple Tasks

```python
with create_progress() as progress:
    task1 = progress.add_task("[green]Downloading...", total=100)
    task2 = progress.add_task("[yellow]Processing...", total=100)
    
    # Update tasks independently
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        time.sleep(0.1)
```

## Status Styling

### Status Dictionary

```python
# Define status styles in a central location
STATUS_STYLES = {
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "info": "bold blue",
    "pending": "bold cyan",
    "skipped": "dim",
    "unknown": "white"
}

def get_styled_status(status):
    """Get a styled status string."""
    status_lower = status.lower()
    style = STATUS_STYLES.get(status_lower, "white")
    return f"[{style}]{status}[/{style}]"

# Usage example
console.print(f"Operation status: {get_styled_status('success')}")
```

## Code Display

### Syntax Highlighting

```python
def display_code(code, language="python", line_numbers=True):
    """Display code with syntax highlighting."""
    syntax = Syntax(
        code,
        language,
        theme="monokai",
        line_numbers=line_numbers,
        word_wrap=True
    )
    console.print(syntax)

# Usage example
sample_code = """
def hello_world():
    print("Hello, World!")
"""
display_code(sample_code)
```

### File Content Display

```python
def display_file_content(file_path, language=None):
    """Display file content with syntax highlighting."""
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
        
        display_code(content, language)
    except Exception as e:
        print_error(f"Failed to display file: {file_path}", e)
```

## Implementation Checklist

### Basic Setup
- [ ] Import all necessary Rich components
- [ ] Install Rich traceback handler
- [ ] Create console instances at the module level
- [ ] Replace all print() calls with console.print()

### Error Handling
- [ ] Create helper functions for errors and warnings
- [ ] Use error_console for error output
- [ ] Add proper exception handling with Rich formatting

### UI Components
- [ ] Create consistent banner with app information
- [ ] Use tables with consistent styling (box.ROUNDED)
- [ ] Use panels for important information
- [ ] Apply consistent color schemes

### Progress Indicators
- [ ] Use progress bars for long-running operations
- [ ] Include status updates in progress bars
- [ ] Use spinners for indeterminate operations

### Status Styling
- [ ] Define status styles in a central location
- [ ] Create helper functions for status display
- [ ] Apply consistent styling across the application

### Code Display
- [ ] Use Syntax for code display
- [ ] Add proper syntax highlighting
- [ ] Include line numbers when appropriate

## Adaptation Guide

To adapt this styling guide to a specific project:

1. Copy the necessary helper functions to your project
2. Customize the color scheme to match your project's branding
3. Create project-specific UI components (banners, tables)
4. Define status styles relevant to your application
5. Replace all print() calls with the appropriate Rich alternatives
6. Add error handling with Rich formatting
7. Use progress indicators for long-running operations

By following this guide, you can create a consistent, professional terminal UI for any Python CLI application.
