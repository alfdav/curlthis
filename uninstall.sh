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
    BIN_DIR="$VENV_DIR/bin"
    LOCAL_BIN="$HOME/.local/bin"
    SYSTEM_BIN="/usr/local/bin"
    
    # Remove symlink or wrapper script from ~/.local/bin
    if [ -e "$LOCAL_BIN/curlthis" ]; then
        echo "Removing curlthis from $LOCAL_BIN..."
        rm -f "$LOCAL_BIN/curlthis"
        echo "curlthis removed from $LOCAL_BIN."
    fi
    
    # Remove from system bin if it exists and we have permission
    if [ -e "$SYSTEM_BIN/curlthis" ] && [ -w "$SYSTEM_BIN/curlthis" ]; then
        echo "Removing curlthis from $SYSTEM_BIN..."
        rm -f "$SYSTEM_BIN/curlthis"
        echo "curlthis removed from $SYSTEM_BIN."
    fi
    
    # Remove virtual environment
    if [ -d "$VENV_DIR" ]; then
        echo "Removing virtual environment at $VENV_DIR..."
        rm -rf "$VENV_DIR"
        echo "Virtual environment removed."
    else
        echo "Virtual environment not found at $VENV_DIR."
    fi
    
    # Detect shell type and identify RC files to clean
    SHELL_TYPE=$(basename "$SHELL")
    RC_FILES=()
    
    case "$SHELL_TYPE" in
        bash)
            RC_FILES=("$HOME/.bashrc" "$HOME/.bash_profile")
            ;;
        zsh)
            RC_FILES=("$HOME/.zshrc" "$HOME/.zprofile")
            ;;
        fish)
            RC_FILES=("$HOME/.config/fish/config.fish")
            ;;
        *)
            RC_FILES=("$HOME/.profile")
            ;;
    esac
    
    # Add common profile file
    RC_FILES+=("$HOME/.profile")
    
    # Remove path configuration from all RC files
    for RC_FILE in "${RC_FILES[@]}"; do
        if [ -f "$RC_FILE" ]; then
            echo "Checking $RC_FILE for curlthis configuration..."
            
            # Create a temporary file
            TEMP_FILE="$(mktemp)"
            
            # Filter out curlthis path configurations - handle all possible formats
            grep -v "# curlthis path configuration" "$RC_FILE" | \
            grep -v "export PATH=\"\$PATH:$BIN_DIR:$LOCAL_BIN\"" | \
            grep -v "export PATH=\"\$PATH:$BIN_DIR\"" | \
            grep -v "export PATH=\"$LOCAL_BIN:$BIN_DIR:\$PATH\"" | \
            grep -v "set -gx PATH \$PATH $BIN_DIR $LOCAL_BIN" > "$TEMP_FILE"
            
            # Replace original file with filtered content
            mv "$TEMP_FILE" "$RC_FILE"
            echo "Cleaned up $RC_FILE"
        fi
    done
    
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
