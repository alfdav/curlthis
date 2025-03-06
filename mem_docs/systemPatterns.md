[//]: # (File: systemPatterns.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 11:37 AM (America/Chicago, UTC-6:00))
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
*   **Click for CLI**: Using the `click` library for command-line argument parsing and interface design.
*   **Rich for UI**: Using the `rich` library for styled console output, including panels, tables, progress bars, and syntax highlighting.
*   **Clipboard Integration**: Using `pyperclip` to read from and write to the clipboard.
*   **Custom Help Command**: Implementing a custom `RichHelpCommand` class to override Click's default help display with rich-formatted output.
*   **Consistent Error Handling**: Using standardized error display functions with appropriate styling.
*   **Installation Scripts**: Providing platform-specific installation scripts (install.sh for Unix/Linux, install.ps1 for Windows) that handle virtual environment setup and PATH configuration.
*   **Author Headers**: Added standardized author headers to all source files for proper attribution (2025-03-06 11:33)

## Architecture patterns

The application follows a modular procedural pattern with clear separation of concerns:

1. **Input Handling**: The `machamp_process_request()` function handles input from various sources (file, stdin, clipboard).
2. **Parsing**: The `alakazam_parse_request()` function parses the raw HTTP request into a structured dictionary.
3. **Formatting**: The `kadabra_format_curl()` function transforms the structured data into a curl command string.
4. **Output Presentation**: The `display_code()` function presents the result with syntax highlighting.

The application uses a dictionary data structure to represent the parsed HTTP request, which is passed between the parser and formatter functions. This approach provides a simple and flexible way to handle the data without introducing unnecessary complexity.