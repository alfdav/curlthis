# Terminal Styling and Installation Standards

This document defines standardized patterns for terminal styling and installation scripts that can be replicated across projects. These standards ensure consistency, improve user experience, and simplify maintenance.

## Table of Contents

- [Terminal Styling and Installation Standards](#terminal-styling-and-installation-standards)
  - [Table of Contents](#table-of-contents)
  - [Pokemon-Themed Function Naming](#pokemon-themed-function-naming)
    - [Naming Convention](#naming-convention)
    - [Pokemon Selection Guide](#pokemon-selection-guide)
      - [Automated Pokemon Selection](#automated-pokemon-selection)
    - [Reserved Pokemon](#reserved-pokemon)
  - [Terminal Styling](#terminal-styling)
    - [Setup and Initialization](#setup-and-initialization)
      - [Basic Setup](#basic-setup)
      - [Key Points](#key-points)
    - [Status Indicators](#status-indicators)
    - [Console Output](#console-output)
      - [Basic Output](#basic-output)
      - [Styling Tags](#styling-tags)
    - [Error Handling](#error-handling)
      - [Error Display Function](#error-display-function)
      - [Warning Display Function](#warning-display-function)
      - [Usage Example](#usage-example)
    - [UI Components](#ui-components)
      - [Banner](#banner)
      - [Tables](#tables)
      - [Panels](#panels)
      - [Sections](#sections)
    - [Progress Indicators](#progress-indicators)
      - [Basic Progress Bar](#basic-progress-bar)
      - [Multiple Tasks](#multiple-tasks)
    - [Status Styling](#status-styling)
      - [Status Dictionary](#status-dictionary)
    - [Code Display](#code-display)
      - [Syntax Highlighting](#syntax-highlighting)
      - [File Content Display](#file-content-display)
  - [Standard Dependencies](#standard-dependencies)
    - [Core UI Dependencies](#core-ui-dependencies)
    - [Version Requirements](#version-requirements)
    - [Optional Dependencies](#optional-dependencies)
  - [Shell Script Styling](#shell-script-styling)
    - [Bash Color Definitions](#bash-color-definitions)
    - [PowerShell Color Definitions](#powershell-color-definitions)
    - [Output Functions](#output-functions)
      - [Bash Implementation](#bash-implementation)
      - [PowerShell Implementation](#powershell-implementation)
  - [Installation Scripts](#installation-scripts)
    - [Cross-Platform Support](#cross-platform-support)
    - [Bash Installation Script](#bash-installation-script)
    - [PowerShell Installation Script](#powershell-installation-script)
    - [Dependencies Installation](#dependencies-installation)
    - [Smart PATH Management](#smart-path-management)
    - [Multi-Shell Support](#multi-shell-support)
    - [Immediate Command Availability](#immediate-command-availability)
    - [Wrapper Script Creation](#wrapper-script-creation)
    - [User-Friendly Success Messages](#user-friendly-success-messages)
  - [Implementation Examples](#implementation-examples)
    - [Ready-to-Use Template](#ready-to-use-template)
      - [Template Features](#template-features)
      - [Using the Template](#using-the-template)
    - [Python Utility Module](#python-utility-module)
    - [Installation Script Templates](#installation-script-templates)
  - [Implementation Checklist](#implementation-checklist)
    - [Basic Setup](#basic-setup-1)
    - [Error Handling](#error-handling-1)
    - [UI Components](#ui-components-1)
    - [Progress Indicators](#progress-indicators-1)
    - [Status Styling](#status-styling-1)
    - [Code Display](#code-display-1)
    - [Installation Scripts](#installation-scripts-1)
  - [Standards Compliance Verification](#standards-compliance-verification)
    - [Standards Version Tracking](#standards-version-tracking)
    - [Compliance Verification Function](#compliance-verification-function)
    - [Individual Check Functions](#individual-check-functions)
    - [Command-line Interface](#command-line-interface)
    - [How to Use](#how-to-use)
  - [Author](#author)

## Pokemon-Themed Function Naming

All functions should follow a Pokemon-themed naming convention to add personality and make the code more engaging.

### Naming Convention

Format: `pokemon_action_description()`

Example: `hitmonchan_show_banner()`, `primeape_show_error()`, `machamp_process_request()`

### Pokemon Selection Guide

Choose Pokemon based on their characteristics that match the function's purpose:

| Function Type | Recommended Pokemon | Reasoning |
|---------------|---------------------|-----------|
| **Display/UI** | Hitmonchan | Known for precision and presentation style |
| **Error Handling** | Primeape | Reactive nature, good for alerting to problems |
| **Processing** | Machamp | Multiple arms represent handling multiple operations |
| **Verification** | Hitmonlee | High Jump Kick represents verification leaps |
| **Setup** | Machoke | Strength represents setting up environments |
| **Configuration** | Machamp | Dynamic Punch represents configuring systems |
| **Parsing** | Alakazam | Psychic abilities represent parsing and understanding |
| **Formatting** | Kadabra | Transformation abilities represent formatting data |
| **Progress** | Rapidash | Speed represents progress tracking |
| **File Operations** | Snorlax | Storage capacity represents file handling |
| **Network** | Porygon | Digital nature represents network operations |
| **Data Validation** | Mewtwo | Analytical abilities represent validation |
| **Logging** | Slowbro | Methodical nature represents logging |

#### Automated Pokemon Selection

For automated Pokemon selection, you can use the PokeAPI (https://pokeapi.co/) to fetch Pokemon data and match it with function purposes. The `terminal_styling_template` includes a helper module (`pokemon_selector.py`) that uses the PokeAPI to suggest appropriate Pokemon names based on function descriptions:

```python
from terminal_styling_template import get_function_name_suggestion

# Get a function name suggestion
suggestion = get_function_name_suggestion(
    "Display a banner with application information",
    "show",
    "banner"
)

print(f"Suggested function name: {suggestion['function_name']}")
print(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
```

This is particularly useful for coders who may not be familiar with Pokemon characteristics.

### Reserved Pokemon

To avoid repetition, each Pokemon should be used for only one type of function across the project. The following are standard reservations:

```python
# Standard reservations
# UI/Display functions
hitmonchan_show_banner()
hitmonchan_show_success()
hitmonchan_show_progress()

# Error handling
primeape_show_error()
primeape_show_warning()

# Processing
machamp_process_request()

# Verification
hitmonlee_verify_python()

# Setup
machoke_setup_venv()

# Configuration
machamp_configure_shell()

# Parsing
alakazam_parse_request()

# Formatting
kadabra_format_output()
```

## Terminal Styling

### Setup and Initialization

#### Basic Setup

```python
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
```

#### Key Points

- Import all necessary Rich components at the module level
- Install the Rich traceback handler early in your application
- Create separate console instances for stdout and stderr
- Initialize these objects at the module level, not inside functions
- Use a custom theme for consistent styling
- Define a standardized STATUS dictionary for consistent indicators

### Status Indicators

Always use the standardized STATUS dictionary for consistent indicators across all output functions:

```python
# Status indicators dictionary - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}
```

For shell scripts, use these standardized indicators:

```bash
# Status indicators
STATUS_INFO="[*]"
STATUS_SUCCESS="[✓]"
STATUS_WARNING="[!]"
STATUS_ERROR="[✗]"
```

### Console Output

#### Basic Output

```python
# Simple output
console.print(f"{STATUS['info']} Processing data...")

# Styled output
console.print(f"{STATUS['success']} Operation completed.")
console.print(f"Found [bold]{count}[/bold] matching items.")

# Multi-line output
console.print(
    "[bold blue]Summary:[/bold blue]\n"
    f"- Processed: [green]{processed}[/green]\n"
    f"- Skipped: [yellow]{skipped}[/yellow]\n"
    f"- Failed: [red]{failed}[/red]"
)
```

#### Styling Tags

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

### Error Handling

#### Error Display Function

```python
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
```

#### Warning Display Function

```python
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
```

#### Usage Example

```python
try:
    # Some operation that might fail
    result = machamp_process_request(input_data)
except Exception as e:
    primeape_show_error("Failed to process data", e)
    return False

if result.has_warnings:
    primeape_show_warning("Processing completed with warnings")
```

### UI Components

#### Banner

```python
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
```

#### Tables

```python
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

def hitmonchan_display_results_table(results, columns):
    """Display results in a formatted table."""
    table = create_table("Results")
    
    # Add columns
    for col in columns:
        table.add_column(col["name"], style=col.get("style", "white"))
    
    # Add rows
    for result in results:
        row_values = [str(result.get(col["key"], "N/A")) for col in columns]
        table.add_row(*row_values)
    
    console.print(table)
```

#### Panels

```python
def hitmonchan_display_info_panel(title, content, style="blue"):
    """Display information in a panel."""
    panel = Panel(
        content,
        title=title,
        border_style=style,
        box=box.ROUNDED
    )
    console.print(panel)
```

#### Sections

```python
def create_section(title: str) -> None:
    """Create a section header with a rule.
    
    Args:
        title: The title of the section
    """
    console.print(Rule(title=f"[bold cyan]{title}[/bold cyan]", style="cyan"))
```

### Progress Indicators

#### Basic Progress Bar

```python
def rapidash_create_progress():
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
with rapidash_create_progress() as progress:
    task = progress.add_task("[green]Processing...", total=100, status="Starting")
    
    for i in range(100):
        # Do some work
        progress.update(task, advance=1, status=f"Processing item {i+1}")
        time.sleep(0.1)
```

#### Multiple Tasks

```python
with rapidash_create_progress() as progress:
    task1 = progress.add_task("[green]Downloading...", total=100)
    task2 = progress.add_task("[yellow]Processing...", total=100)
    
    # Update tasks independently
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        time.sleep(0.1)
```

### Status Styling

#### Status Dictionary

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

### Code Display

#### Syntax Highlighting

```python
def kadabra_display_code(code: str, language: str = "bash", theme: str = "monokai", 
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
        Syntax(code, language, theme=theme, word_wrap=True, line_numbers=True),
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)

# Usage example
sample_code = """
def hello_world():
    print("Hello, World!")
"""
kadabra_display_code(sample_code, language="python", title="Sample Python Code")
```

#### File Content Display

```python
def snorlax_display_file_content(file_path, language=None):
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
        
        kadabra_display_code(content, language, title=f"File: {file_path}")
    except Exception as e:
        primeape_show_error(f"Failed to display file: {file_path}", e)
```

## Standard Dependencies

To ensure consistent terminal styling and user experience across all projects, standardize on the following dependencies.

### Core UI Dependencies

All projects should include these core UI dependencies:

1. **Rich** - For advanced terminal formatting, tables, progress bars, and more
   - Features: Syntax highlighting, tables, panels, progress bars, markdown rendering
   - Usage: Primary tool for all advanced terminal output

2. **Typer** - For building beautiful command-line interfaces
   - Features: Type annotations, command groups, automatic help pages
   - Usage: Main framework for CLI applications

### Version Requirements

Specify minimum versions in your `pyproject.toml` or `requirements.txt`:

```toml
# In pyproject.toml
dependencies = [
    "rich>=13.9.4",
    "typer>=0.15.1",
]
```

```
# In requirements.txt
rich>=13.9.4
typer>=0.15.1
```

### Optional Dependencies

Consider these additional dependencies for specific use cases:

1. **tqdm** - For simple progress bars when Rich is too heavyweight
   - Minimum version: `tqdm>=4.66.0`

2. **colorama** - For basic cross-platform colored terminal text
   - Minimum version: `colorama>=0.4.6`
   - Note: Only use when Rich is not suitable

3. **prompt_toolkit** - For interactive command prompts
   - Minimum version: `prompt_toolkit>=3.0.36`

Example in `pyproject.toml`:

```toml
[project.optional-dependencies]
ui-extras = [
    "tqdm>=4.66.0",
    "colorama>=0.4.6",
    "prompt_toolkit>=3.0.36",
]
```

## Shell Script Styling

### Bash Color Definitions

For Bash scripts, use ANSI color codes:

```bash
# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Status indicators
STATUS_INFO="[*]"
STATUS_SUCCESS="[✓]"
STATUS_WARNING="[!]"
STATUS_ERROR="[✗]"
```

### PowerShell Color Definitions

For PowerShell scripts, use ConsoleColor:

```powershell
# Output colors
$Colors = @{
    Red    = [System.ConsoleColor]::Red
    Green  = [System.ConsoleColor]::Green
    Yellow = [System.ConsoleColor]::Yellow
    Blue   = [System.ConsoleColor]::Blue
    Cyan   = [System.ConsoleColor]::Cyan
    Gray   = [System.ConsoleColor]::DarkGray
}

# Status indicators
$StatusInfo = "[*]"
$StatusSuccess = "[✓]"
$StatusWarning = "[!]"
$StatusError = "[✗]"
```

### Output Functions

#### Bash Implementation

```bash
# Function to print status messages
print_info() {
    echo -e "${BLUE}${STATUS_INFO}${NC} $1"
}

print_success() {
    echo -e "${GREEN}${STATUS_SUCCESS}${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}${STATUS_WARNING}${NC} $1"
}

print_error() {
    echo -e "${RED}${STATUS_ERROR}${NC} $1"
}

print_status() {
    echo -e "${CYAN}==>${NC} ${BOLD}$1${NC}"
}

print_banner() {
    echo -e "${BLUE}┌────────────────────────────────────────────┐${NC}"
    echo -e "${BLUE}│${NC}           ${BOLD}$1${NC}               ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}                                            ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}  $2       ${BLUE}│${NC}"
    echo -e "${BLUE}└────────────────────────────────────────────┘${NC}"
    echo
}
```

#### PowerShell Implementation

```powershell
# Logging functions
function Write-Info {
    param([string]$Message)
    Write-Host "$StatusInfo $Message" -ForegroundColor $Colors.Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "$StatusSuccess $Message" -ForegroundColor $Colors.Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "$StatusWarning $Message" -ForegroundColor $Colors.Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "$StatusError $Message" -ForegroundColor $Colors.Red
}

function Write-Status {
    param([string]$Message)
    Write-Host "==> " -ForegroundColor $Colors.Cyan -NoNewline
    Write-Host $Message -ForegroundColor White
}
```

## Installation Scripts

### Cross-Platform Support

Projects should include installation scripts for both Unix-like systems (Bash) and Windows (PowerShell):

1. `install.sh` - Main installation script for Unix-like systems
2. `install.ps1` - PowerShell installation script for Windows
3. `install_dependencies.sh` - Optional separate script for dependencies

### Bash Installation Script

Standard structure for Bash installation scripts with Pokemon-themed function names:

```bash
#!/bin/bash

# Colors and status indicators
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Status indicators
STATUS_INFO="[*]"
STATUS_SUCCESS="[✓]"
STATUS_WARNING="[!]"
STATUS_ERROR="[✗]"

# Output functions
print_info() {
    echo -e "${BLUE}${STATUS_INFO}${NC} $1"
}

print_success() {
    echo -e "${GREEN}${STATUS_SUCCESS}${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}${STATUS_WARNING}${NC} $1"
}

print_error() {
    echo -e "${RED}${STATUS_ERROR}${NC} $1"
}

print_status() {
    echo -e "${CYAN}==>${NC} ${BOLD}$1${NC}"
}

print_banner() {
    echo -e "${BLUE}┌────────────────────────────────────────────┐${NC}"
    echo -e "${BLUE}│${NC}           ${BOLD}$1${NC}               ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}                                            ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}  $2       ${BLUE}│${NC}"
    echo -e "${BLUE}└────────────────────────────────────────────┘${NC}"
    echo
}

# System verification function
hitmonlee_verify_python() {
    print_status "Hitmonlee uses High Jump Kick to verify Python installation..."
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    
    # Compare major version first
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ $PYTHON_MAJOR -lt 3 ] || ([ $PYTHON_MAJOR -eq 3 ] && [ $PYTHON_MINOR -lt 8 ]); then
        print_error "Python version $PYTHON_VERSION detected. Version 3.8 or higher is required."
        exit 1
    fi
    
    print_success "Python $PYTHON_VERSION detected."
    return 0
}

# Environment setup function
machoke_setup_venv() {
    print_status "Machoke uses Strength to set up virtual environment..."
    
    VENV_DIR="$HOME/.app_venv"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "$VENV_DIR" ]; then
        print_info "Creating virtual environment at $VENV_DIR..."
        python3 -m venv "$VENV_DIR"
        if [ $? -ne 0 ]; then
            print_error "Failed to create virtual environment."
            exit 1
        fi
    else
        print_info "Using existing virtual environment at $VENV_DIR..."
    fi
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    if [ $? -ne 0 ]; then
        print_error "Failed to activate virtual environment."
        exit 1
    fi
    
    # Install the package in development mode
    print_info "Installing package..."
    pip install --upgrade pip
    pip install -e .
    if [ $? -ne 0 ]; then
        print_error "Failed to install package."
        exit 1
    fi
    
    print_success "Virtual environment setup complete."
    return 0
}

# Shell configuration function
machamp_configure_shell() {
    print_status "Machamp uses Dynamic Punch to configure shell..."
    
    # Implementation details...
    
    print_success "Shell configuration complete."
    return 0
}

# User feedback function
hitmonchan_show_success() {
    print_status "Hitmonchan uses Sky Uppercut to show installation results..."
    
    echo
    print_banner "Installation Complete" "Your application is ready to use"
    echo
    print_success "Application has been successfully installed!"
    echo
    echo -e "${CYAN}Application is now available in your terminal!${NC}"
    echo "Try it now with: app -h"
    echo
    echo -e "${BOLD}Example usage:${NC}"
    echo -e "  ${GRAY}app command1${NC}    # Description 1"
    echo -e "  ${GRAY}app command2${NC}    # Description 2"
    echo
    
    return 0
}

# Main installation process
main() {
    print_banner "Application Installer" "Installing your application"
    
    # Verify Python installation
    hitmonlee_verify_python || exit 1
    
    # Setup virtual environment
    machoke_setup_venv || exit 1
    
    # Configure shell
    machamp_configure_shell || exit 1
    
    # Show success message
    hitmonchan_show_success
    
    print_success "Installation complete!"
}

# Run the main function
main
```

### PowerShell Installation Script

Standard structure for PowerShell installation scripts with Pokemon-themed function names:

```powershell
# Project Installation Script
# Requires -Version 5.1

# Output colors
$Colors = @{
    Red    = [System.ConsoleColor]::Red
    Green  = [System.ConsoleColor]::Green
    Yellow = [System.ConsoleColor]::Yellow
    Blue   = [System.ConsoleColor]::Blue
    Cyan   = [System.ConsoleColor]::Cyan
    Gray   = [System.ConsoleColor]::DarkGray
}

# Status indicators
$StatusInfo = "[*]"
$StatusSuccess = "[✓]"
$StatusWarning = "[!]"
$StatusError = "[✗]"

# Logging functions
function Write-Info {
    param([string]$Message)
    Write-Host "$StatusInfo $Message" -ForegroundColor $Colors.Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "$StatusSuccess $Message" -ForegroundColor $Colors.Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "$StatusWarning $Message" -ForegroundColor $Colors.Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "$StatusError $Message" -ForegroundColor $Colors.Red
}

function Write-Status {
    param([string]$Message)
    Write-Host "==> " -ForegroundColor $Colors.Cyan -NoNewline
    Write-Host $Message -ForegroundColor White
}

# System verification function
function Hitmonlee-VerifyPython {
    Write-Status "Hitmonlee uses High Jump Kick to verify Python installation..."
    
    # Implementation details...
    
    Write-Success "Python verification complete."
}

# Environment setup function
function Machoke-SetupVenv {
    Write-Status "Machoke uses Strength to set up virtual environment..."
    
    # Implementation details...
    
    Write-Success "Virtual environment setup complete."
}

# Shell configuration function
function Machamp-ConfigureShell {
    Write-Status "Machamp uses Dynamic Punch to configure shell..."
    
    # Implementation details...
    
    Write-Success "Shell configuration complete."
}

# User feedback function
function Hitmonchan-ShowSuccess {
    Write-Status "Hitmonchan uses Sky Uppercut to show installation results..."
    
    # Implementation details...
    
    Write-Success "Installation complete!"
}

# Main installation process
function Install-Project {
    # Banner
    Write-Host "=== Application Installation ===" -ForegroundColor $Colors.Cyan
    
    # Verify Python installation
    Hitmonlee-VerifyPython
    
    # Setup virtual environment
    Machoke-SetupVenv
    
    # Configure shell
    Machamp-ConfigureShell
    
    # Show success message
    Hitmonchan-ShowSuccess
}

# Run the main function
Install-Project
```

### Dependencies Installation

Standard pattern for dependencies installation:

```bash
# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Install core UI dependencies explicitly first
    print_info "Installing core UI dependencies..."
    python3 -m pip install --upgrade typer>=0.15.1 rich>=13.9.4
    
    # Verify Typer installation
    if ! python3 -c "import typer" &>/dev/null; then
        print_warning "Typer installation verification failed, trying again..."
        python3 -m pip install --force-reinstall typer>=0.15.1
        
        # Check again
        if ! python3 -c "import typer" &>/dev/null; then
            print_error "Failed to install Typer. Please install it manually with: python3 -m pip install typer>=0.15.1"
            exit 1
        fi
    fi
    
    # Verify Rich installation
    if ! python3 -c "import rich" &>/dev/null; then
        print_warning "Rich installation verification failed, trying again..."
        python3 -m pip install --force-reinstall rich>=13.9.4
        
        # Check again
        if ! python3 -c "import rich" &>/dev/null; then
            print_error "Failed to install Rich. Please install it manually with: python3 -m pip install rich>=13.9.4"
            exit 1
        fi
    fi
    
    # Install project-specific dependencies
    print_info "Installing project-specific dependencies..."
    python3 -m pip install -e . --use-pep517
    
    # Optionally install extra UI dependencies
    if [ "$INSTALL_EXTRAS" = "true" ]; then
        print_info "Installing extra UI dependencies..."
        python3 -m pip install tqdm>=4.66.0 colorama>=0.4.6 prompt_toolkit>=3.0.36
    fi
    
    print_status "All dependencies installed successfully"
}
```

### Smart PATH Management

Intelligently managing PATH additions ensures your command is available across different shells and sessions:

```bash
# Find a directory in PATH that we can write to
FOUND_PATH_DIR=""
IFS=':' read -ra PATH_DIRS <<< "$PATH"
for dir in "${PATH_DIRS[@]}"; do
    if [ -d "$dir" ] && [ -w "$dir" ] && [ "$dir" != "$LOCAL_BIN" ]; then
        FOUND_PATH_DIR="$dir"
        break
    fi
done
```

### Multi-Shell Support

Detecting and configuring multiple shell types ensures compatibility across different user environments:

```bash
# Detect shell type
SHELL_TYPE=$(basename "$SHELL")
RC_FILE=""

case "$SHELL_TYPE" in
    bash)
        RC_FILES=("$HOME/.bashrc" "$HOME/.bash_profile")
        ;;
    zsh)
        RC_FILES=("$HOME/.zshrc" "$HOME/.zprofile")
        ;;
    fish)
        RC_FILES=("$HOME/.config/fish/config.fish")
        ;;
    *)
        print_warning "Unsupported shell: $SHELL_TYPE. Adding to common shell files."
        RC_FILES=("$HOME/.profile")
        ;;
esac

# Always include .profile for login shells
if ! [[ "${RC_FILES[@]}" =~ "$HOME/.profile" ]]; then
    RC_FILES+=("$HOME/.profile")
fi
```

### Immediate Command Availability

Make commands available immediately without requiring a shell restart:

```bash
# Create a function in the current shell that can be used immediately
cat << EOF

# You can use mycommand immediately in this terminal session
mycommand() {
  "$LOCAL_BIN/mycommand" "\$@"
}

# Try it with: mycommand -h
EOF

# Also update current session PATH
export PATH="$LOCAL_BIN:$BIN_DIR:$PATH"
```

### Wrapper Script Creation

Create wrapper scripts that handle environment activation:

```bash
# Create a wrapper script that activates the venv and runs the module
cat > "$LOCAL_BIN/mycommand" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m mypackage "\$@"
EOF
chmod +x "$LOCAL_BIN/mycommand"
```

### User-Friendly Success Messages

Provide clear examples and next steps after successful installation:

```bash
echo -e "${GREEN}mycommand has been successfully installed!${NC}"
echo ""
echo "mycommand is now available in your terminal!"
echo "Try it now with: mycommand -h"
echo ""
echo -e "${BOLD}Example usage:${NC}"
echo -e "  ${GRAY}mycommand --option1${NC}    # Example 1"
echo -e "  ${GRAY}mycommand --option2${NC}    # Example 2"
```

## Implementation Examples

### Ready-to-Use Template

A complete implementation template is available in the `terminal_styling_template` directory. This template provides a ready-to-use implementation of these standards that you can copy into your projects.

#### Template Features

- Complete implementation of all terminal styling standards
- Pokemon selection helper using the PokeAPI
- Example usage and documentation
- Ready-to-use utility functions

#### Using the Template

1. Copy the `terminal_styling_template` directory to your project
2. Install the required dependencies:

```bash
pip install -r terminal_styling_template/requirements.txt
```

3. Import and use the functions in your code:

```python
from terminal_styling_template import (
    hitmonchan_show_banner,
    hitmonchan_show_success,
    primeape_show_error
)

# Display a banner
hitmonchan_show_banner(
    "My Application",
    "A description of my application",
    "Your Name"
)
```

4. For help with Pokemon selection, use the included helper:

```python
from terminal_styling_template import get_function_name_suggestion

# Get a function name suggestion
suggestion = get_function_name_suggestion(
    "Display a banner with application information",
    "show",
    "banner"
)

print(f"Suggested function name: {suggestion['function_name']}")
print(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
```

See the `terminal_styling_template/README.md` file for more details on using the template.

### Python Utility Module

Create a `utils.py` module for standardized terminal output using Rich:

```python
"""
Utility module for CLI styling and output functions.
"""
from typing import Optional, Any
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.theme import Theme
from rich.rule import Rule
from rich import box

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

# Status indicators dictionary - STANDARDIZED FORMAT
STATUS = {
    "info": "[blue][[/blue][bold white]*[/bold white][blue]][/blue]",
    "success": "[green][[/green][bold white]✓[/bold white][green]][/green]",
    "warning": "[yellow][[/yellow][bold white]![/bold white][yellow]][/yellow]",
    "error": "[red][[/red][bold white]✗[/bold white][red]][/red]"
}

def hitmonchan_show_banner(title: str = "Application v1.0.0", 
                         description: str = "Application description",
                         author: str = "David Diaz") -> None:
    """Display application banner."""
    content = f"[bold cyan]{description}[/bold cyan]"
    
    banner = Panel(
        content,
        title=f"[bold]{title}[/bold]",
        subtitle=f"By {author}" if author else None,
        border_style="blue",
        box=box.ROUNDED
    )
    console.print(banner)

def primeape_show_error(message: str, exception: Optional[Exception] = None) -> None:
    """Display error message with optional exception details."""
    error_panel = Panel(
        f"{STATUS['error']} {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")

def primeape_show_warning(message: str) -> None:
    """Display warning message."""
    warning_panel = Panel(
        f"{STATUS['warning']} {message}",
        border_style="yellow", 
        title="Warning"
    )
    console.print(warning_panel)

def hitmonchan_show_success(message: str) -> None:
    """Display success message."""
    console.print(f"{STATUS['success']} {message}")

def hitmonchan_show_progress(message: str, spinner: bool = False) -> None:
    """Display progress message."""
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
    """Create a table with the given title."""
    table = Table(title=title, title_style=style, box=box.ROUNDED)
    return table

def create_section(title: str) -> None:
    """Create a section header with a rule."""
    console.print(Rule(title=f"[bold cyan]{title}[/bold cyan]", style="cyan"))

def kadabra_display_code(code: str, language: str = "bash", theme: str = "monokai", 
                       title: str = "Generated code", border_style: str = "green") -> None:
    """Display code with syntax highlighting in a panel."""
    panel = Panel(
        Syntax(code, language, theme=theme, word_wrap=True, line_numbers=True),
        title=f"[bold]{title}[/bold]",
        border_style=border_style,
        expand=False
    )
    console.print(panel)
```

### Installation Script Templates

Create template files for installation scripts:

1. `install_template.sh` - Template for Bash installation
2. `install_template.ps1` - Template for PowerShell installation

These templates can be copied and customized for each new project, ensuring consistent installation experiences across all projects.

## Implementation Checklist

### Basic Setup
- [ ] Import all necessary Rich components
- [ ] Install Rich traceback handler
- [ ] Create console instances at the module level
- [ ] Define standardized STATUS dictionary
- [ ] Replace all print() calls with console.print()

### Error Handling
- [ ] Create Pokemon-themed helper functions for errors and warnings
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

### Installation Scripts
- [ ] Create cross-platform installation scripts
- [ ] Include proper error handling
- [ ] Verify system requirements
- [ ] Set up virtual environment
- [ ] Install and verify dependencies
- [ ] Create command wrappers for easy access

## Standards Compliance Verification

To ensure your project meets the terminal styling standards, you can use the built-in verification tool. This tool checks for compliance with the standards and provides detailed feedback on which standards are met and which need attention.

### Standards Version Tracking

```python
# utils/standards.py
"""
Terminal styling standards compliance verification.
"""
from importlib.metadata import version
from pathlib import Path
import inspect
import sys
import os

# Standards version
STANDARDS_VERSION = "1.0.0"
```

### Compliance Verification Function

```python
def mewtwo_verify_standards_compliance():
    """
    Verify that the project meets terminal styling standards.
    
    Mewtwo's analytical abilities make it perfect for validating standards compliance.
    
    Returns:
        dict: Dictionary of check results with details
    """
    results = {
        'version': STANDARDS_VERSION,
        'passed': True,
        'checks': {}
    }
    
    # Run all checks
    checks = {
        'rich_installed': _check_rich_version(),
        'typer_configured': _check_typer_setup(),
        'has_install_scripts': _check_install_scripts_exist(),
        'has_status_dictionary': _check_status_dictionary(),
        'has_pokemon_naming': _check_pokemon_naming(),
        'has_standard_output_functions': _check_standard_output_functions(),
        'has_banner_function': _check_banner_function()
    }
    
    results['checks'] = checks
    results['passed'] = all(check['passed'] for check in checks.values())
    
    return results
```

### Individual Check Functions

```python
def _check_rich_version():
    """Check if Rich is installed with correct version."""
    try:
        rich_version = version('rich')
        return {
            'passed': version('rich') >= '13.9.4',
            'message': f"Rich version {rich_version} installed",
            'required': '13.9.4'
        }
    except Exception:
        return {
            'passed': False,
            'message': "Rich not installed",
            'required': '13.9.4'
        }

def _check_typer_setup():
    """Check if Typer is installed with correct version."""
    try:
        typer_version = version('typer')
        return {
            'passed': version('typer') >= '0.15.1',
            'message': f"Typer version {typer_version} installed",
            'required': '0.15.1'
        }
    except Exception:
        return {
            'passed': False,
            'message': "Typer not installed",
            'required': '0.15.1'
        }

def _check_install_scripts_exist():
    """Check if installation scripts exist."""
    project_root = _find_project_root()
    has_bash = (project_root / 'install.sh').exists()
    has_powershell = (project_root / 'install.ps1').exists()
    
    return {
        'passed': has_bash and has_powershell,
        'message': f"Installation scripts: Bash: {has_bash}, PowerShell: {has_powershell}",
        'required': 'Both install.sh and install.ps1'
    }

def _check_status_dictionary():
    """Check if STATUS dictionary is defined correctly."""
    # Look for STATUS dictionary in all modules
    status_dict = None
    for module_name, module in sys.modules.items():
        if hasattr(module, 'STATUS'):
            status_dict = getattr(module, 'STATUS')
            break
    
    if not status_dict:
        return {
            'passed': False,
            'message': "STATUS dictionary not found",
            'required': "STATUS dictionary with info, success, warning, error keys"
        }
    
    required_keys = ['info', 'success', 'warning', 'error']
    has_all_keys = all(key in status_dict for key in required_keys)
    
    return {
        'passed': has_all_keys,
        'message': f"STATUS dictionary has keys: {', '.join(status_dict.keys())}",
        'required': "info, success, warning, error keys"
    }

def _check_pokemon_naming():
    """Check if Pokemon-themed function naming is used."""
    pokemon_prefixes = [
        'hitmonchan', 'primeape', 'machamp', 'hitmonlee',
        'machoke', 'alakazam', 'kadabra', 'rapidash', 'snorlax',
        'mewtwo', 'porygon', 'slowbro'
    ]
    
    # Look for functions with Pokemon prefixes
    pokemon_functions = []
    for module_name, module in sys.modules.items():
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and any(name.startswith(prefix) for prefix in pokemon_prefixes):
                pokemon_functions.append(name)
    
    return {
        'passed': len(pokemon_functions) > 0,
        'message': f"Found {len(pokemon_functions)} Pokemon-themed functions",
        'required': "At least one Pokemon-themed function"
    }

def _check_standard_output_functions():
    """Check if standard output functions are defined."""
    required_functions = [
        'show_error', 'show_warning', 'show_success', 'show_progress',
        'show_banner', 'display_code'
    ]
    
    found_functions = []
    for module_name, module in sys.modules.items():
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and any(name.endswith(func) for func in required_functions):
                found_functions.append(name)
    
    return {
        'passed': len(found_functions) >= 3,  # At least 3 standard functions
        'message': f"Found standard output functions: {', '.join(found_functions)}",
        'required': "At least 3 standard output functions"
    }

def _check_banner_function():
    """Check if banner function is defined."""
    banner_functions = []
    for module_name, module in sys.modules.items():
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and 'banner' in name.lower():
                banner_functions.append(name)
    
    return {
        'passed': len(banner_functions) > 0,
        'message': f"Found banner functions: {', '.join(banner_functions)}",
        'required': "At least one banner function"
    }

def _find_project_root():
    """Find the project root directory."""
    current_dir = Path.cwd()
    while current_dir != current_dir.parent:
        if (current_dir / 'pyproject.toml').exists() or (current_dir / 'setup.py').exists():
            return current_dir
        current_dir = current_dir.parent
    return Path.cwd()
```

### Command-line Interface

```python
# Command-line interface for standards verification
if __name__ == "__main__":
    from rich.console import Console
    from rich.table import Table
    
    console = Console()
    
    results = mewtwo_verify_standards_compliance()
    
    console.print(f"\n[bold]Terminal Styling Standards Compliance Check v{STANDARDS_VERSION}[/bold]\n")
    
    table = Table(title="Compliance Results")
    table.add_column("Check", style="cyan")
    table.add_column("Result", style="white")
    table.add_column("Details", style="white")
    table.add_column("Required", style="dim")
    
    for check_name, check_result in results['checks'].items():
        status = "[green]✓ PASS[/green]" if check_result['passed'] else "[red]✗ FAIL[/red]"
        table.add_row(
            check_name,
            status,
            check_result['message'],
            check_result.get('required', '')
        )
    
    console.print(table)
    
    overall = "[green]PASSED[/green]" if results['passed'] else "[red]FAILED[/red]"
    console.print(f"\nOverall compliance: {overall}\n")
```

### How to Use

To use the standards verification tool in your project:

1. Copy the `standards.py` file to your project's utils directory
2. Run the verification:

```python
from utils.standards import mewtwo_verify_standards_compliance

# Check compliance
results = mewtwo_verify_standards_compliance()
if results['passed']:
    print("Project meets all terminal styling standards!")
else:
    print("Project does not meet all standards. See details:")
    for check_name, check_result in results['checks'].items():
        if not check_result['passed']:
            print(f"- {check_name}: {check_result['message']}")
```

You can also run the verification directly from the command line:

```bash
python -m utils.standards
```

This will display a formatted table showing which standards are met and which need attention.

## Author

David Diaz (https://github.com/alfdav)
email = "alfdav@users.noreply.github.com"