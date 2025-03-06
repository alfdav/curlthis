#!/usr/bin/env python3
"""
Test script for the Pokemon Terminal Styling package.

This script demonstrates how to use the Pokemon Terminal Styling package
in another project.
"""

from pokemon_terminal_styling import (
    hitmonchan_show_banner,
    hitmonchan_show_success,
    primeape_show_error,
    kadabra_display_code
)

def main():
    """Main function demonstrating the Pokemon Terminal Styling package."""
    # Display banner
    hitmonchan_show_banner(
        "Pokemon Styling Test",
        "Testing the Pokemon Terminal Styling package",
        "David Diaz"
    )
    
    # Display success message
    hitmonchan_show_success("Package imported successfully!")
    
    # Display some code
    sample_code = """
# Example of using the Pokemon Terminal Styling package
from pokemon_terminal_styling import hitmonchan_show_banner

hitmonchan_show_banner(
    "My Application",
    "A description of my application",
    "Your Name"
)
"""
    kadabra_display_code(sample_code, language="python", title="Example Usage")
    
    # Display error handling
    try:
        # Simulate an error
        raise ValueError("This is a test error")
    except Exception as e:
        primeape_show_error("Error demonstration", e)
    
    # Display completion message
    hitmonchan_show_success("Test completed successfully!")

if __name__ == "__main__":
    main()