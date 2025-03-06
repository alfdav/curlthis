# Terminal Styling Templates

This project provides standardized terminal styling templates for both Python applications and shell scripts, following the Pokemon-themed naming convention as defined in the [Terminal Styling Standards](./terminal_styling_standards.md).

## Overview

The project includes two main components:

1. **Python Terminal Styling Template** - A Python package for consistent terminal styling in Python applications
2. **Shell Styling Template** - Bash and PowerShell templates for consistent terminal styling in shell scripts

Both templates follow the same styling standards and Pokemon-themed naming convention, ensuring a consistent user experience across different types of applications.

## Python Terminal Styling Template

The Python Terminal Styling Template provides:

- Consistent terminal styling using the Rich library
- Pokemon-themed function naming convention
- Helper utilities for selecting appropriate Pokemon names
- Progress indicators, error handling, and more
- Cross-platform support

### Installation

```bash
# Option 1: Copy the template folder to your project
cp -r terminal_styling_template your_project/

# Option 2: Install as a package
cd pokemon_terminal_styling
pip install -e .
```

### Usage

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

See the [terminal_styling_template/README.md](./terminal_styling_template/README.md) file for more details.

## Shell Styling Template

The Shell Styling Template provides:

- Consistent shell script styling for Bash and PowerShell
- Pokemon-themed function naming convention
- Standardized color schemes and status indicators
- Simple, AI-friendly formatting that works across all terminals
- Cross-platform support
- Ready-to-use installation script templates

### Installation

```bash
# Copy the template folder to your project
cp -r shell_styling_template your_project/
```

### Usage

```bash
# Bash
cp shell_styling_template/install_template.sh your_project/install.sh
chmod +x your_project/install.sh

# PowerShell
cp shell_styling_template/install_template.ps1 your_project/install.ps1
```

See the [shell_styling_template/README.md](./shell_styling_template/README.md) file for more details.

## Pokemon-Themed Function Naming

Both templates follow the Pokemon-themed function naming convention:

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

## Standards Compliance

These templates comply with the [Terminal Styling Standards](./terminal_styling_standards.md) document, which defines standardized patterns for terminal styling and installation scripts that can be replicated across projects.

## Author

David Diaz (https://github.com/alfdav)
email = "alfdav@users.noreply.github.com"