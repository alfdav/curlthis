# Pokemon Terminal Styling

A Python package providing standardized terminal styling utilities with Pokemon-themed naming conventions.

## Features

- Consistent terminal styling using the Rich library
- Pokemon-themed function naming convention
- Helper utilities for selecting appropriate Pokemon names
- Progress indicators, error handling, and more
- Cross-platform support
- **NEW**: Typer-based CLI template for modern command-line interfaces

## Installation

### From PyPI (Not Yet Available)

```bash
pip install pokemon-terminal-styling
```

### From Source

```bash
# Clone the repository
git clone https://github.com/alfdav/pokemon-terminal-styling.git
cd pokemon-terminal-styling

# Install in development mode
pip install -e .

# Or build and install
pip install build
python -m build
pip install dist/python_terminal_styling-0.1.0-py3-none-any.whl
```

### In Your Project

You can also install directly from the directory:

```bash
pip install -e /path/to/python_terminal_styling
```

## Usage

### Basic Usage

```python
from python_terminal_styling import (
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

# Show a success message
hitmonchan_show_success("Operation completed successfully")

# Show an error message
try:
    # Some operation that might fail
    result = some_function()
except Exception as e:
    primeape_show_error("Failed to perform operation", e)
```

### Typer-based CLI Template (Recommended)

The package now includes a Typer-based template for creating modern CLI applications:

```python
from python_terminal_styling.typer_template import (
    app,
    hitmonchan_show_banner,
    primeape_show_error,
    hitmonchan_show_success
)

@app.command()
def machamp_process_data(
    input_file: str = typer.Argument(..., help="Input file path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show verbose output")
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

This template provides:
- Clean, modern CLI interfaces with Typer
- Built-in rich formatting for help text
- Type annotations for parameters
- Command groups for organizing complex CLIs
- All while maintaining the Pokemon naming convention

See the `typer_template.py` file for a complete reference implementation and the `typer_styling_guide.md` for detailed documentation.

### Pokemon Selection Helper

The package includes a Pokemon selection helper that can suggest appropriate Pokemon names for your functions:

```python
from python_terminal_styling import get_function_name_suggestion

# Get a function name suggestion
suggestion = get_function_name_suggestion(
    "Display a banner with application information",
    "show",
    "banner"
)

print(f"Suggested function name: {suggestion['function_name']}")
print(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
```

### Creating Custom Functions

When creating custom functions, follow the Pokemon-themed naming convention:

```python
def porygon_fetch_data(url):
    """Fetch data from a URL.
    
    Porygon's digital nature makes it perfect for network operations.
    
    Args:
        url: The URL to fetch data from
        
    Returns:
        The fetched data
    """
    # Implementation...
```

## Available Functions

### UI/Display Functions

- `hitmonchan_show_banner`: Display application banner
- `hitmonchan_show_success`: Display success message
- `hitmonchan_show_info`: Display info message
- `hitmonchan_show_progress`: Display progress message
- `hitmonchan_display_results_table`: Display results in a table
- `hitmonchan_display_info_panel`: Display information in a panel

### Error Handling Functions

- `primeape_show_error`: Display error message with optional exception details
- `primeape_show_warning`: Display warning message

### Progress Tracking Functions

- `rapidash_create_progress`: Create and return a Rich progress bar

### Code Display Functions

- `kadabra_display_code`: Display code with syntax highlighting
- `snorlax_display_file_content`: Display file content with syntax highlighting

### Helper Functions

- `create_table`: Create a table with the given title
- `create_section`: Create a section header with a rule
- `get_styled_status`: Get a styled status string

### Processing Functions

- `machamp_process_request`: Process a request with the given input data
- `machamp_create_command_group`: Create a Typer command group (Typer template only)

### Verification Functions

- `hitmonlee_verify_python`: Verify Python installation
- `mewtwo_validate_input`: Validate input against a pattern (Typer template only)

### Setup Functions

- `machoke_setup_venv`: Set up a virtual environment

## CLI Framework Options

The package provides two options for creating CLI applications:

### 1. Click-based (Original)

The original implementation uses Click with a custom `RichHelpCommand` class to override the default help display.

### 2. Typer-based (Recommended)

The new recommended implementation uses Typer with its built-in rich formatting support. This provides a cleaner, more modern interface with less code.

Key advantages of the Typer implementation:
- Built-in rich formatting for help text
- Type annotations for parameters
- Command groups for organizing complex CLIs
- Less boilerplate code
- Cleaner help output

See the `typer_styling_guide.md` document for detailed information on using the Typer template.

## Pokemon Selection Guide

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

## Examples

- See the `example.py` file for a complete example of using the original Click-based implementation.
- See the `typer_template.py` file for a complete example of using the new Typer-based implementation.

## License

This package is provided under the MIT License. See the LICENSE file for details.

## Author

David Diaz (https://github.com/alfdav)
email = "alfdav@users.noreply.github.com"