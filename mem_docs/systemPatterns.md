[//]: # (File: systemPatterns.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 12:15 PM (America/Chicago, UTC-6:00))
[//]: # (Description: Documents the architecture and system patterns of the curlthis project)

# System Patterns

## How the system is built

The `curlthis` application is built using Python and consists of several key modules:

*   `main.py`: Contains the main application logic, including command-line argument parsing, input handling (file, stdin, clipboard), and output formatting. It defines a custom `RichHelpCommand` class that extends Click's Command class to provide rich-formatted help output.
*   `parser.py`: Contains the `alakazam_parse_request()` function that parses the raw HTTP request into its constituent parts (method, URL, headers, body).
*   `formatter.py`: Contains the `kadabra_format_curl()` function that formats the parsed request into a valid curl command.
*   `utils.py`: Contains utility functions for console output styling, progress indicators, and other UI elements.
*   `__main__.py`: Entry point for running the package as a module.

## Key technical decisions

*   **Pokemon Function Naming Convention**: All functions follow a Pokemon-themed naming convention, with Psychic types for data processing and Fighting types for system operations.
*   **Typer for CLI**: Using the `typer` library for command-line argument parsing and interface design, with built-in rich formatting support.
*   **Rich for UI**: Using the `rich` library for styled console output, including panels, tables, progress bars, and syntax highlighting.
*   **Clipboard Integration**: Using `pyperclip` to read from and write to the clipboard.
*   **Consistent Error Handling**: Using standardized error display functions with appropriate styling.
*   **Installation Scripts**: Providing platform-specific installation scripts (install.sh for Unix/Linux, install.ps1 for Windows) that handle virtual environment setup and PATH configuration.
*   **Author Headers**: Added standardized author headers to all source files for proper attribution (2025-03-06 11:33)
*   **Migration to Typer**: Migrated from Click to Typer following the new CLI framework standards (2025-03-06 12:22)
*   **Improved Installation**: Enhanced installation scripts with clearer user instructions (2025-03-06 12:36)

## Architecture patterns

The application follows a modular procedural pattern with clear separation of concerns:

1. **Input Handling**: The `machamp_process_request()` function handles input from various sources (file, stdin, clipboard).
2. **Parsing**: The `alakazam_parse_request()` function parses the raw HTTP request into a structured dictionary.
3. **Formatting**: The `kadabra_format_curl()` function transforms the structured data into a curl command string.
4. **Output Presentation**: The `kadabra_display_code()` function presents the result with syntax highlighting.

The application uses a dictionary data structure to represent the parsed HTTP request, which is passed between the parser and formatter functions. This approach provides a simple and flexible way to handle the data without introducing unnecessary complexity.

## CLI Framework Implementation

The application now uses Typer as the CLI framework, following the established standards:

1. **Typer Implementation**: The application has been migrated from Click to Typer, leveraging its built-in Rich formatting support, type annotations, and command groups.

2. **Pokemon Naming Convention**: All functions follow the Pokemon naming convention, with appropriate Pokemon types for different function purposes.

3. **Rich Formatting**: The application uses Rich for terminal styling, with standardized status indicators and output formatting.

4. **Command Structure**: The main command is implemented as a Typer command with proper type annotations and help text.

5. **Error Handling**: The application uses standardized error handling with proper exit codes using Typer's Exit mechanism.

This implementation follows the standards established in the Architectural Decision Record (`styling_standards/adr_001_typer_styling_standard.md`) and the Typer styling guide (`styling_standards/typer_styling_guide.md`). The migration was completed on March 6, 2025. (2025-03-06 12:22)