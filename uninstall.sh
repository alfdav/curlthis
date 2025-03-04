#!/bin/bash

# curlthis uninstallation script for Unix-like systems
# Following the Pokemon-themed function naming convention

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Cleanup operations function
primeape_remove_installation() {
    echo -e "${BLUE}Primeape uses Thrash to remove installation...${NC}"
    
    VENV_DIR="$HOME/.curlthis_venv"
    
    # Remove virtual environment
    if [ -d "$VENV_DIR" ]; then
        echo "Removing virtual environment at $VENV_DIR..."
        rm -rf "$VENV_DIR"
        echo "Virtual environment removed."
    else
        echo "Virtual environment not found at $VENV_DIR."
    fi
    
    # Detect shell type
    SHELL_TYPE=$(basename "$SHELL")
    RC_FILE=""
    
    case "$SHELL_TYPE" in
        bash)
            RC_FILE="$HOME/.bashrc"
            ;;
        zsh)
            RC_FILE="$HOME/.zshrc"
            ;;
        *)
            echo -e "${YELLOW}Unsupported shell: $SHELL_TYPE. You may need to manually remove curlthis path from your configuration.${NC}"
            ;;
    esac
    
    # Remove path configuration from RC file
    if [ -n "$RC_FILE" ] && [ -f "$RC_FILE" ]; then
        echo "Removing path configuration from $RC_FILE..."
        sed -i '/# curlthis path configuration/d' "$RC_FILE"
        sed -i "\|export PATH=\"\$PATH:$VENV_DIR/bin\"|d" "$RC_FILE"
        echo "Path configuration removed."
    fi
    
    echo -e "${GREEN}Uninstallation complete.${NC}"
    return 0
}

# User feedback function
hitmonchan_show_success() {
    echo -e "${BLUE}Hitmonchan uses Mach Punch to show uninstallation results...${NC}"
    
    echo -e "${GREEN}curlthis has been successfully uninstalled!${NC}"
    echo ""
    echo "To complete the uninstallation, you may need to:"
    echo "  1. Restart your terminal or run: source $RC_FILE"
    echo ""
    
    return 0
}

# Main uninstallation process
main() {
    echo -e "${BLUE}=== curlthis Uninstallation ===${NC}"
    
    # Remove installation
    primeape_remove_installation || exit 1
    
    # Show success message
    hitmonchan_show_success
    
    echo -e "${GREEN}Uninstallation complete!${NC}"
}

# Run the main function
main
