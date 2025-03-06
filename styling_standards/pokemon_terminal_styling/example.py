#!/usr/bin/env python3
"""
Example usage of the Pokemon Terminal Styling package.

This example demonstrates how to use the various functions provided by the
Pokemon Terminal Styling package to create a consistent terminal UI.
"""

import time
import sys
from typing import Dict, Any, List

# Import functions from the pokemon_terminal_styling package
from pokemon_terminal_styling import (
    # UI/Display functions
    hitmonchan_show_banner,
    hitmonchan_show_success,
    hitmonchan_show_info,
    hitmonchan_show_progress,
    hitmonchan_display_results_table,
    hitmonchan_display_info_panel,
    
    # Error handling functions
    primeape_show_error,
    primeape_show_warning,
    
    # Progress tracking functions
    rapidash_create_progress,
    
    # Code display functions
    kadabra_display_code,
    snorlax_display_file_content,
    
    # Helper functions
    create_table,
    create_section,
    get_styled_status,
    
    # Processing functions
    machamp_process_request,
    
    # Verification functions
    hitmonlee_verify_python,
    
    # Setup functions
    machoke_setup_venv,
    
    # Pokemon selection helper
    get_function_name_suggestion
)

def main():
    """Main function demonstrating the Pokemon Terminal Styling package."""
    # Display banner
    hitmonchan_show_banner(
        "Pokemon Terminal Styling Demo",
        "Demonstration of Pokemon-themed terminal styling",
        "David Diaz"
    )
    
    # Display progress
    hitmonchan_show_progress("Initializing...", spinner=True)
    time.sleep(1)
    
    # Display success message
    hitmonchan_show_success("Initialization complete")
    
    # Display info panel
    hitmonchan_display_info_panel(
        "Information",
        "This is a demonstration of the Pokemon Terminal Styling package.\n"
        "It shows how to use the various functions to create a consistent UI."
    )
    
    # Display code
    sample_code = """
def hello_world():
    print("Hello, World!")
    
hello_world()
"""
    kadabra_display_code(sample_code, language="python", title="Sample Python Code")
    
    # Display progress bar
    with rapidash_create_progress() as progress:
        task = progress.add_task("[green]Processing...", total=100, status="Starting")
        
        for i in range(100):
            # Simulate work
            time.sleep(0.01)
            progress.update(task, advance=1, status=f"Processing item {i+1}")
    
    # Display results table
    results = [
        {"name": "Item 1", "status": "success", "value": 42},
        {"name": "Item 2", "status": "warning", "value": 18},
        {"name": "Item 3", "status": "error", "value": 0}
    ]
    
    columns = [
        {"name": "Name", "key": "name"},
        {"name": "Status", "key": "status"},
        {"name": "Value", "key": "value"}
    ]
    
    hitmonchan_display_results_table(results, columns)
    
    # Display section
    create_section("Verification")
    
    # Verify Python
    hitmonlee_verify_python()
    
    # Display warning
    primeape_show_warning("This is a warning message")
    
    # Display error
    try:
        # Simulate an error
        raise ValueError("This is a simulated error")
    except Exception as e:
        primeape_show_error("An error occurred", e)
    
    # Demonstrate Pokemon selection helper
    create_section("Pokemon Selection Helper")
    
    # Example 1: Get a function name for displaying a banner
    suggestion = get_function_name_suggestion(
        "Display a banner with application information", 
        "show", 
        "banner"
    )
    hitmonchan_show_info(f"Suggested function name: {suggestion['function_name']}")
    hitmonchan_show_info(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
    
    # Example 2: Get a function name for error handling
    suggestion = get_function_name_suggestion(
        "Display an error message with exception details", 
        "show", 
        "error"
    )
    hitmonchan_show_info(f"Suggested function name: {suggestion['function_name']}")
    hitmonchan_show_info(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
    
    # Example 3: Get a function name for file operations
    suggestion = get_function_name_suggestion(
        "Read a file from disk and return its contents", 
        "read", 
        "file"
    )
    hitmonchan_show_info(f"Suggested function name: {suggestion['function_name']}")
    hitmonchan_show_info(f"Pokemon: {suggestion['pokemon']} (Reason: {suggestion['reason']})")
    
    # Display completion message
    hitmonchan_show_success("Demo completed successfully")

if __name__ == "__main__":
    main()