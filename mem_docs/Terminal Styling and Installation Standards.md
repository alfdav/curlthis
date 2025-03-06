# Terminal Styling and Installation Standards

This document defines standardized patterns for terminal styling and installation scripts that can be replicated across projects. These standards ensure consistency, improve user experience, and simplify maintenance.

## Table of Contents

- [Terminal Styling and Installation Standards](#terminal-styling-and-installation-standards)
  - [Table of Contents](#table-of-contents)
  - [Terminal Styling](#terminal-styling)
    - [Setup and Initialization](#setup-and-initialization)
      - [Basic Setup](#basic-setup)
      - [Key Points](#key-points)
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
  - [Implementation Examples](#implementation-examples)
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
  - [Advanced Installation Techniques](#advanced-installation-techniques)
    - [Themed Function Naming](#themed-function-naming)
    - [Smart PATH Management](#smart-path-management)
    - [Multi-Shell Support](#multi-shell-support)
    - [Immediate Command Availability](#immediate-command-availability)
    - [Wrapper Script Creation](#wrapper-script-creation)
    - [User-Friendly Success Messages](#user-friendly-success-messages)
    - [Global Installation vs. User Installation](#global-installation-vs-user-installation)
  - [Author](#author)

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
```

#### Key Points

- Import all necessary Rich components at the module level
- Install the Rich traceback handler early in your application
- Create separate console instances for stdout and stderr
- Initialize these objects at the module level, not inside functions
- Use a custom theme for consistent styling

### Console Output

#### Basic Output

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

#### Warning Display Function

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

#### Usage Example

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

### UI Components

#### Banner

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

#### Tables

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

#### Panels

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

### Progress Indicators

#### Basic Progress Bar

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

#### Multiple Tasks

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

#### File Content Display

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
# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
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
}
```

### Output Functions

#### Bash Implementation

```bash
# Function to print status messages
print_status() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[-]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[ℹ]${NC} $1"
}
```

#### PowerShell Implementation

```powershell
# Logging functions
function Write-Status {
    param([string]$Message)
    Write-Host "[+] $Message" -ForegroundColor $Colors.Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[!] $Message" -ForegroundColor $Colors.Yellow
}

function Write-Info {
    param([string]$Message)
    Write-Host "[ℹ] $Message" -ForegroundColor $Colors.Blue
}

function Write-Error {
    param([string]$Message)
    Write-Host "[-] $Message" -ForegroundColor $Colors.Red
}
```

## Installation Scripts

### Cross-Platform Support

Projects should include installation scripts for both Unix-like systems (Bash) and Windows (PowerShell):

1. `install.sh` - Main installation script for Unix-like systems
2. `install.ps1` - PowerShell installation script for Windows
3. `install_dependencies.sh` - Optional separate script for dependencies

### Bash Installation Script

Standard structure for Bash installation scripts:

1. **Color and Output Definitions**: Define colors and output functions
2. **Error Handling**: Set up error trapping and cleanup functions
3. **System Checks**: Verify system requirements (Python version, disk space)
4. **Virtual Environment**: Create and activate a virtual environment
5. **Dependencies Installation**: Install required packages
6. **Command Wrapper**: Create a global command for easy access
7. **Project Structure**: Set up necessary directories and files

Key components to include:

```bash
#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Error handling
set -e
trap 'handle_error $? $LINENO' ERR

# Function to handle errors
handle_error() {
    local exit_code=$1
    local line_number=$2
    print_error "Installation failed on line $line_number with exit code $exit_code"
    print_error "Please check the error message above and try again"
    cleanup
    exit $exit_code
}

# Cleanup function
cleanup() {
    if [ -d "venv" ] && [ -z "$VIRTUAL_ENV" ]; then
        print_warning "Cleaning up temporary files..."
        rm -rf venv
    fi
}

# Output functions
print_status() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[-]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[ℹ]${NC} $1"
}

# Version comparison function
version_compare() {
    echo "$1" "$2" | awk '{
        split($1, a, ".")
        split($2, b, ".")
        for (i = 1; i <= 2; i++) {
            if (a[i] < b[i]) exit 1
            if (a[i] > b[i]) exit 0
        }
        exit 0
    }'
}

# Check system requirements
check_system() {
    print_status "Checking system requirements..."
    
    # Check Python version
    print_info "Checking Python version..."
    if ! command -v python3 &>/dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.9 or newer."
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if ! version_compare "$PYTHON_VERSION" "3.9"; then
        print_error "Python 3.9+ is required (found $PYTHON_VERSION)"
        exit 1
    fi
    print_status "Python version $PYTHON_VERSION found"

    # Check disk space
    print_info "Checking available disk space..."
    REQUIRED_SPACE=500 # MB
    if command -v df &>/dev/null; then
        AVAILABLE_SPACE=$(df -m . | awk 'NR==2 {print $4}')
        if [ "$AVAILABLE_SPACE" -lt "$REQUIRED_SPACE" ]; then
            print_error "Insufficient disk space. Required: ${REQUIRED_SPACE}MB, Available: ${AVAILABLE_SPACE}MB"
            exit 1
        fi
        print_status "Sufficient disk space available"
    else
        print_warning "Could not check disk space, proceeding anyway"
    fi
}

# Setup virtual environment
setup_venv() {
    print_status "Creating a new virtual environment..."
    python3 -m venv venv
    print_status "Activating virtual environment..."
    source venv/bin/activate
    
    print_info "Upgrading pip and build tools..."
    python3 -m pip install --upgrade pip setuptools wheel
}

# Main installation process
main() {
    echo -e "${CYAN}=== Project Installation ===${NC}"
    print_info "This script will install the project and its dependencies"
    
    check_system
    setup_venv
    # Install dependencies
    # Setup command wrapper
    # Create project structure
    
    echo -e "\n${CYAN}=== Installation Complete! ===${NC}"
    print_status "Project has been installed successfully!"
}

# Run main installation
main
```

### PowerShell Installation Script

Standard structure for PowerShell installation scripts:

1. **Color and Output Definitions**: Define colors and output functions
2. **Error Handling**: Set up error trapping and cleanup functions
3. **System Checks**: Verify system requirements (Python version, disk space)
4. **Virtual Environment**: Create and activate a virtual environment
5. **Dependencies Installation**: Install required packages
6. **Command Wrapper**: Create a global command for easy access
7. **Project Structure**: Set up necessary directories and files

Key components to include:

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
}

# Error handling
$ErrorActionPreference = "Stop"
trap {
    Write-Error "Installation failed: $_"
    Write-Error "Please check the error message above and try again"
    Cleanup
    exit 1
}

# Logging functions
function Write-Status {
    param([string]$Message)
    Write-Host "[+] $Message" -ForegroundColor $Colors.Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[!] $Message" -ForegroundColor $Colors.Yellow
}

function Write-Info {
    param([string]$Message)
    Write-Host "[ℹ] $Message" -ForegroundColor $Colors.Blue
}

function Write-Error {
    param([string]$Message)
    Write-Host "[-] $Message" -ForegroundColor $Colors.Red
}

# Cleanup function
function Cleanup {
    if (Test-Path "venv" -and -not $env:VIRTUAL_ENV) {
        Write-Warning "Cleaning up temporary files..."
        Remove-Item -Path "venv" -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# Version comparison function
function Compare-Versions {
    param(
        [string]$Version1,
        [string]$Version2
    )
    
    $v1 = [version]$Version1
    $v2 = [version]$Version2
    return $v1 -ge $v2
}

# Check system requirements
function Test-SystemRequirements {
    Write-Status "Checking system requirements..."
    
    # Check Python version
    Write-Info "Checking Python version..."
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Write-Error "Python 3 is not installed. Please install Python 3.9 or newer."
        exit 1
    }
    
    $pythonVersion = (python -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
    if (-not (Compare-Versions $pythonVersion "3.9")) {
        Write-Error "Python 3.9+ is required (found $pythonVersion)"
        exit 1
    }
    Write-Status "Python version $pythonVersion found"
    
    # Check disk space
    Write-Info "Checking available disk space..."
    $requiredSpace = 500MB
    $drive = (Get-Item $PWD.Path).PSDrive
    $freeSpace = $drive.Free
    if ($freeSpace -lt $requiredSpace) {
        Write-Error "Insufficient disk space. Required: $($requiredSpace/1MB)MB, Available: $($freeSpace/1MB)MB"
        exit 1
    }
    Write-Status "Sufficient disk space available"
}

# Setup virtual environment
function Initialize-VirtualEnv {
    Write-Status "Creating a new virtual environment..."
    python -m venv venv
    
    Write-Status "Activating virtual environment..."
    . .\venv\Scripts\Activate.ps1
    
    Write-Info "Upgrading pip and build tools..."
    python -m pip install --upgrade pip setuptools wheel
}

# Install dependencies
function Install-Dependencies {
    Write-Status "Installing dependencies..."
    
    # Install core UI dependencies explicitly first
    Write-Info "Installing core UI dependencies..."
    python -m pip install --upgrade typer>=0.15.1 rich>=13.9.4
    
    # Verify Typer installation
    try {
        $null = python -c "import typer"
    } catch {
        Write-Warning "Typer installation verification failed, trying again..."
        python -m pip install --force-reinstall typer>=0.15.1
        
        # Check again
        try {
            $null = python -c "import typer"
        } catch {
            Write-Error "Failed to install Typer. Please install it manually with: python -m pip install typer>=0.15.1"
            exit 1
        }
    }
    
    # Verify Rich installation
    try {
        $null = python -c "import rich"
    } catch {
        Write-Warning "Rich installation verification failed, trying again..."
        python -m pip install --force-reinstall rich>=13.9.4
        
        # Check again
        try {
            $null = python -c "import rich"
        } catch {
            Write-Error "Failed to install Rich. Please install it manually with: python -m pip install rich>=13.9.4"
            exit 1
        }
    }
    
    # Install project-specific dependencies
    Write-Info "Installing project-specific dependencies..."
    python -m pip install -e . --use-pep517
    
    # Optionally install extra UI dependencies
    if ($env:INSTALL_EXTRAS -eq "true") {
        Write-Info "Installing extra UI dependencies..."
        python -m pip install tqdm>=4.66.0 colorama>=0.4.6 prompt_toolkit>=3.0.36
    }
    
    Write-Status "All dependencies installed successfully"
}

# Main installation process
function Install-Project {
    Write-Host "=== Project Installation ===" -ForegroundColor $Colors.Cyan
    Write-Info "This script will install the project and its dependencies"
    
    Test-SystemRequirements
    Initialize-VirtualEnv
    Install-Dependencies
    # Setup command wrapper
    # Create project structure
    
    Write-Host "`n=== Installation Complete! ===" -ForegroundColor $Colors.Cyan
    Write-Status "Project has been installed successfully!"
}

# Run main installation
Install-Project
```

### Dependencies Installation

Standard pattern for dependencies installation:

1. **Core Dependencies**: Install critical dependencies first
2. **Verification**: Verify successful installation of each critical dependency
3. **Fallback Installation**: Attempt alternative installation methods if needed
4. **Additional Dependencies**: Install remaining dependencies

Example implementation:

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

## Implementation Examples

### Python Utility Module

Create a `utils/terminal.py` module for standardized terminal output using Rich:

```python
"""
Terminal styling utilities using Rich
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.syntax import Syntax
from rich.traceback import install as install_rich_traceback
from rich.theme import Theme
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

# Create console with theme
console = Console(theme=custom_theme)
error_console = Console(stderr=True, theme=custom_theme)

# Basic output functions
def print_success(message: str) -> None:
    """Print success message with rich formatting"""
    console.print(f"[success]✓[/success] {message}")

def print_error(message: str, exception=None) -> None:
    """Print error message with rich formatting"""
    error_panel = Panel(
        f"[bold red]ERROR:[/bold red] {message}",
        border_style="red", 
        title="Error"
    )
    error_console.print(error_panel)
    if exception and str(exception):
        error_console.print(f"[dim]{str(exception)}[/dim]")

def print_warning(message: str) -> None:
    """Print warning message with rich formatting"""
    warning_panel = Panel(
        f"[bold yellow]WARNING:[/bold yellow] {message}",
        border_style="yellow", 
        title="Warning"
    )
    console.print(warning_panel)

def print_info(message: str) -> None:
    """Print info message with rich formatting"""
    console.print(f"[info]ℹ[/info] {message}")

def print_header(message: str) -> None:
    """Print header with rich formatting"""
    console.print(f"[header]{message}[/header]")

# Progress indicators
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

def print_progress(message: str, spinner: bool = False) -> None:
    """
    Print progress message with rich formatting
    If spinner is True, add a spinner animation to indicate ongoing process
    """
    if spinner:
        with Progress(
            SpinnerColumn(),
            TextColumn("[info]{task.description}[/info]"),
            transient=True
        ) as progress:
            progress.add_task(message, total=None)
    else:
        console.print(f"[info]*[/info] {message}")

# UI Components
def create_panel(title: str, content: str, style: str = "info") -> Panel:
    """Create a panel with the given title and content"""
    return Panel(content, title=title, border_style=style)

def create_table(title: str, style: str = "header") -> Table:
    """Create a table with the given title"""
    table = Table(title=title, title_style=style, box=box.ROUNDED)
    return table

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

# Code display
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

# Status styling
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

# Fallback implementation for environments without Rich
try:
    # Test that Rich is working
    console.print("")
except ImportError:
    # Basic ANSI color codes as fallback
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color
    
    def print_success(message: str) -> None:
        print(f"{GREEN}✓{NC} {message}")
    
    def print_error(message: str, exception=None) -> None:
        print(f"{RED}ERROR: {message}{NC}")
        if exception and str(exception):
            print(f"  {str(exception)}")
    
    def print_warning(message: str) -> None:
        print(f"{YELLOW}WARNING: {message}{NC}")
    
    def print_info(message: str) -> None:
        print(f"{BLUE}ℹ{NC} {message}")
    
    def print_header(message: str) -> None:
        print(f"{CYAN}{message}{NC}")
    
    def print_progress(message: str, spinner: bool = False) -> None:
        print(f"{BLUE}*{NC} {message}")
    
    # Dummy implementations for Rich-specific functions
    def create_panel(title: str, content: str, style: str = "info") -> str:
        return f"{CYAN}{title}{NC}\n{content}"
    
    def create_table(title: str, style: str = "header") -> None:
        print(f"{CYAN}{title}{NC}")
        return None
        
    def print_banner(app_name, description, version="1.0.0", author=None):
        print(f"{CYAN}{app_name}{NC} - {description}")
        print(f"Version: {version}")
        if author:
            print(f"By {author}")
            
    def display_code(code, language="python", line_numbers=True):
        print(code)
        
    def display_file_content(file_path, language=None):
        try:
            with open(file_path, "r") as f:
                content = f.read()
            print(content)
        except Exception as e:
            print_error(f"Failed to display file: {file_path}", e)
            
    def get_styled_status(status):
        status_lower = status.lower()
        if status_lower == "success":
            return f"{GREEN}{status}{NC}"
        elif status_lower == "warning":
            return f"{YELLOW}{status}{NC}"
        elif status_lower == "error":
            return f"{RED}{status}{NC}"
        elif status_lower == "info":
            return f"{BLUE}{status}{NC}"
        elif status_lower == "pending":
            return f"{CYAN}{status}{NC}"
        else:
            return status
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

### Installation Scripts
- [ ] Create cross-platform installation scripts
- [ ] Include proper error handling
- [ ] Verify system requirements
- [ ] Set up virtual environment
- [ ] Install and verify dependencies
- [ ] Create command wrappers for easy access

## Advanced Installation Techniques

The following section includes additional advanced installation techniques inspired by the curlthis project's installation script.

### Themed Function Naming

Using a consistent theme for function naming can make installation scripts more memorable and enjoyable to use:

```bash
# Example from curlthis using Pokemon-themed function names
hitmonlee_verify_python() {
    echo -e "${BLUE}Hitmonlee uses High Jump Kick to verify Python installation...${NC}"
    # Function implementation...
}

machoke_setup_venv() {
    echo -e "${BLUE}Machoke uses Strength to set up virtual environment...${NC}"
    # Function implementation...
}

machamp_configure_shell() {
    echo -e "${BLUE}Machamp uses Dynamic Punch to configure shell...${NC}"
    # Function implementation...
}
```

This approach adds personality to your scripts and makes them more engaging for users.

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
        echo -e "${YELLOW}Unsupported shell: $SHELL_TYPE. Adding to common shell files.${NC}"
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
echo "Example usage:"
echo "  mycommand --option1    # Example 1"
echo "  mycommand --option2    # Example 2"
```

### Global Installation vs. User Installation

Provide options for both global (system-wide) and user-specific installations:

```bash
# Try to create a direct executable in /usr/local/bin if possible (requires sudo)
SYSTEM_BIN="/usr/local/bin"
if [ -d "$SYSTEM_BIN" ] && [ -w "$SYSTEM_BIN" ]; then
    echo "Found writable $SYSTEM_BIN directory, creating executable there..."
    # Create system-wide installation
else
    echo "Creating user-specific installation in $LOCAL_BIN..."
    # Create user-specific installation
fi
```

## Author

David Diaz (https://github.com/alfdav)