[//]: # (File: productContext.md)
[//]: # (Author: David Diaz (https://github.com/alfdav))
[//]: # (Last Updated: March 6, 2025, 12:17 PM (America/Chicago, UTC-6:00))
[//]: # (Description: Documents the product context and purpose of the curlthis project)

# Product Context

## Why this project exists

This project, `curlthis`, exists to simplify the process of converting raw HTTP requests into curl commands. It was created to address a common workflow challenge faced by developers, API testers, and security professionals who frequently need to:

- Convert captured HTTP requests from browsers or proxy tools into executable curl commands
- Transform API documentation examples into testable commands
- Share HTTP requests in a format that can be easily executed by others
- Document API interactions in a standardized, executable format

## What problems it solves

`curlthis` solves several key problems:

1. **Manual Conversion Complexity**: Manually constructing curl commands from raw HTTP requests is tedious and error-prone, especially for complex requests with numerous headers and structured bodies.

2. **Format Inconsistency**: Different tools capture HTTP requests in slightly different formats, making it difficult to develop a consistent workflow.

3. **Clipboard Workflow Friction**: Developers often copy HTTP requests from various sources and need to quickly convert them without saving temporary files.

4. **Syntax Errors**: Properly escaping special characters and formatting request bodies in curl commands requires attention to detail that is easy to miss.

5. **Time Efficiency**: What might take minutes to manually convert can be done instantly with `curlthis`.

## How it should work

The application follows a simple and intuitive workflow:

1. **Input Flexibility**:
   - Read raw HTTP requests from files using the `-f/--file` option
   - Accept input from stdin when piped
   - Automatically read from clipboard when no other input is provided

2. **Processing Pipeline**:
   - Parse the raw request into structured components (method, URL, headers, body)
   - Intelligently handle different content types, especially JSON
   - Format the components into a valid curl command with proper escaping

3. **Output Options**:
   - Display the generated curl command with syntax highlighting in the terminal
   - Copy the result to the clipboard with the `-c/--clipboard` option
   - Provide verbose output with the `-v/--verbose` option to show processing steps

4. **User Experience**:
   - Provide clear, styled error messages for invalid inputs
   - Show helpful usage examples in the help text
   - Use consistent visual styling for all output
   - Maintain comprehensive documentation with proper attribution (2025-03-06 11:34)

## Pokemon Function Naming Convention

As a project created after February 17, 2025, `curlthis` follows the Pokemon Function Naming Convention with:

### Psychic Types (Data Processing)
- `alakazam_parse_request()` - Parses raw HTTP requests into structured data using Alakazam's analytical abilities
- `kadabra_format_curl()` - Transforms parsed data into curl command strings with Kadabra's transformation skills

### Fighting Types (System Operations)
- `machamp_process_request()` - Main processing function handling multiple inputs/outputs with Machamp's multi-armed capability
- `hitmonchan_show_banner()` - Displays application banner with Hitmonchan's precision
- `hitmonchan_show_success()` - Shows success messages with clear visual indicators
- `hitmonchan_show_progress()` - Displays progress information during processing
- `primeape_show_error()` - Handles and displays errors with Primeape's intensity
- `primeape_show_warning()` - Shows warning messages for potential issues

The installation scripts also follow this convention with:
- `hitmonlee_verify_python()` - Verifies Python installation requirements
- `machoke_setup_venv()` - Sets up the virtual environment
- `machamp_configure_shell()` - Configures shell environment for the application

## CLI Framework Implementation

The `curlthis` application now uses Typer for its CLI interface, following the established standards for CLI applications based on the Typer framework. This implementation includes:

1. **Typer with Pokemon Naming**: The application uses Typer with the Pokemon naming convention, following the reference implementation in `styling_standards/python_terminal_styling/typer_template.py`.

2. **Rich Formatting**: The application uses Typer's built-in rich formatting support via the `rich_markup_mode="rich"` parameter.

3. **Type Annotations**: All function parameters use Python type annotations for better code readability and self-documentation.

4. **Command Structure**: The application uses a clean command structure with proper help text and examples.

5. **Error Handling**: The application uses standardized error handling with proper exit codes using Typer's Exit mechanism.

This implementation follows the standards established in the Architectural Decision Record (`styling_standards/adr_001_typer_styling_standard.md`) and the Typer styling guide (`styling_standards/typer_styling_guide.md`). The migration from Click to Typer was completed on March 6, 2025. (2025-03-06 12:25)