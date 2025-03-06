"""
Terminal styling template package.

This package provides standardized terminal styling utilities with Pokemon-themed naming.
"""

from .terminal_styling import (
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
    machoke_setup_venv
)

from .pokemon_selector import get_function_name_suggestion

__version__ = "0.1.0"