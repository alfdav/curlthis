[//]: # (File: techContext.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 12:16 PM (America/Chicago, UTC-6:00))
[//]: # (Description: Documents the technologies and technical context of the curlthis project)

# Tech Context

## Technologies used

*   **Python 3.8+**: Core programming language
*   **typer 0.15.1+**: Modern command-line interface framework
*   **rich 13.9.4+**: Terminal formatting and styling library
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

## CLI Framework Implementation

The `curlthis` application now uses Typer as its CLI framework, following the established standards:

1. **Typer Implementation**: The application has been migrated from Click to Typer (version 0.15.1+), which provides several advantages:
   - Built-in Rich formatting support via `rich_markup_mode="rich"`
   - Type annotations for parameters
   - Command groups for organizing complex CLIs
   - Less boilerplate code

2. **Implementation Details**:
   - Removed the custom `RichHelpCommand` class as Typer has built-in rich formatting
   - Added type annotations to function parameters
   - Updated the file input handling to use `Path` from `pathlib`
   - Added proper error handling with `typer.Exit`
   - Maintained the Pokemon naming convention
   - Added support for `-h` short flag via context settings (2025-03-06 13:03)
   - Fixed usage message to match README documentation (2025-03-06 13:03)

3. **Reference Resources**:
   - Reference implementation: `styling_standards/python_terminal_styling/typer_template.py`
   - Styling guide: `styling_standards/typer_styling_guide.md`
   - Architectural Decision Record: `styling_standards/adr_001_typer_styling_standard.md`

This migration was completed on March 6, 2025, and the application now fully complies with the CLI framework standards. The installation scripts were also updated to provide clearer instructions for using the application immediately after installation. (2025-03-06 12:36)