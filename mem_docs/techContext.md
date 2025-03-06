[//]: # (File: techContext.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 11:37 AM (America/Chicago, UTC-6:00))
[//]: # (Description: Documents the technologies and technical context of the curlthis project)

# Tech Context

## Technologies used

*   **Python 3.8+**: Core programming language
*   **click 8.0.0+**: Command-line interface creation toolkit
*   **rich 10.0.0+**: Terminal formatting and styling library
*   **pyperclip 1.8.2+**: Cross-platform clipboard interface
*   **setuptools**: Python package build and distribution tool

## Development setup

The development setup involves:

1. **Python Environment**: Python 3.8 or higher is required.

2. **Dependencies**: Install the required packages:
   ```bash
   pip install click rich pyperclip
   ```

3. **Development Installation**: For development, install in editable mode:
   ```bash
   pip install -e .
   ```

4. **Code Formatting**: The project uses Black for code formatting with a line length of 88 characters:
   ```bash
   pip install black
   black curlthis/
   ```

5. **Type Checking**: MyPy is configured for type checking:
   ```bash
   pip install mypy
   mypy curlthis/
   ```

6. **Installation Scripts**: For end users, platform-specific installation scripts are provided:
   - `install.sh` for Unix/Linux/macOS
   - `install.ps1` for Windows

## Technical constraints

*   **Python Version**: Requires Python 3.8 or higher due to type annotation features used.
*   **Platform Compatibility**: The application is designed to be cross-platform, but clipboard functionality may vary across operating systems.
*   **Terminal Support**: Rich formatting requires a terminal that supports ANSI color codes for optimal display.
*   **Installation Requirements**: The installation scripts require appropriate permissions to create symlinks and modify PATH variables.
*   **Documentation Standards**: All files require proper author attribution and documentation updates with timestamps (2025-03-06 11:34)