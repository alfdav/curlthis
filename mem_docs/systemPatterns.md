# System Patterns

## How the system is built

The `curlthis` application is built using Python and consists of three main modules:

*   `main.py`: Contains the main application logic, including command-line argument parsing and output formatting.
*   `parser.py`: Parses the raw HTTP request into its constituent parts (method, URL, headers, body).
*   `formatter.py`: Formats the parsed request into a valid curl command.

## Key technical decisions

*   Using the `click` library for command-line argument parsing.
*   Using the `rich` library for styled console output.
*   Using `pyperclip` to copy the result to the clipboard.

## Architecture patterns

The application follows a simple procedural pattern, with the main function calling the parser and formatter functions in sequence. The application uses a dictionary to represent the parsed HTTP request, which is then passed to the formatter function.