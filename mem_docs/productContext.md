# Product Context

## Why this project exists

This project, `curlthis`, exists to simplify the process of converting raw HTTP requests into curl commands. This is useful for developers who need to quickly generate curl commands for testing, debugging, or documentation purposes.

## What problems it solves

`curlthis` solves the problem of manually constructing curl commands from raw HTTP requests. This can be a tedious and error-prone process, especially for complex requests with many headers and a body. `curlthis` automates this process, making it faster and easier to generate accurate curl commands.

## How it should work

The application should take a raw HTTP request as input, parse it into its constituent parts (method, URL, headers, body), and then format these parts into a valid curl command. The application should support reading input from a file, stdin, or the clipboard. It should also support copying the generated curl command to the clipboard.

## Pokemon Function Naming Convention

As a project created after February 17, 2025, `curlthis` follows the Pokemon Function Naming Convention with:

### Psychic Types (Data Processing)
- `alakazam_parse_request()` - Parses raw HTTP requests into structured data
- `kadabra_format_curl()` - Transforms parsed data into curl command strings

### Fighting Types (System Operations)
- `machamp_process_request()` - Main processing function handling multiple inputs/outputs
- `hitmonchan_show_banner()` - Displays application banner with precision
- `primeape_show_error()` - Handles and displays errors with appropriate intensity