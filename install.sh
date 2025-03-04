#!/bin/bash

# curlthis installation script for Unix-like systems
# Following the Pokemon-themed function naming convention

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# System verification function
hitmonlee_verify_python() {
    echo -e "${BLUE}Hitmonlee uses High Jump Kick to verify Python installation...${NC}"
    
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Python 3 is not installed. Please install Python 3.8 or higher.${NC}"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    
    # Compare major version first
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ $PYTHON_MAJOR -lt 3 ] || ([ $PYTHON_MAJOR -eq 3 ] && [ $PYTHON_MINOR -lt 8 ]); then
        echo -e "${RED}Python version $PYTHON_VERSION detected. Version 3.8 or higher is required.${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Python $PYTHON_VERSION detected.${NC}"
    return 0
}

# Environment setup function
machoke_setup_venv() {
    echo -e "${BLUE}Machoke uses Strength to set up virtual environment...${NC}"
    
    VENV_DIR="$HOME/.curlthis_venv"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment at $VENV_DIR..."
        python3 -m venv "$VENV_DIR"
    else
        echo "Using existing virtual environment at $VENV_DIR..."
    fi
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Install the package in development mode
    echo "Installing curlthis..."
    pip install --upgrade pip
    pip install -e .
    
    echo -e "${GREEN}Virtual environment setup complete.${NC}"
    return 0
}

# Shell configuration function
machamp_configure_shell() {
    echo -e "${BLUE}Machamp uses Dynamic Punch to configure shell...${NC}"
    
    VENV_DIR="$HOME/.curlthis_venv"
    BIN_DIR="$VENV_DIR/bin"
    
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
            echo -e "${YELLOW}Unsupported shell: $SHELL_TYPE. You may need to manually add $BIN_DIR to your PATH.${NC}"
            return 1
            ;;
    esac
    
    # Check if BIN_DIR is already in PATH
    if echo "$PATH" | grep -q "$BIN_DIR"; then
        echo "Path already configured."
    else
        # Add to PATH in RC file
        echo "# curlthis path configuration" >> "$RC_FILE"
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$RC_FILE"
        echo "Added $BIN_DIR to PATH in $RC_FILE"
    fi
    
    echo -e "${GREEN}Shell configuration complete.${NC}"
    return 0
}

# User feedback function
hitmonchan_show_success() {
    echo -e "${BLUE}Hitmonchan uses Sky Uppercut to show installation results...${NC}"
    
    echo -e "${GREEN}curlthis has been successfully installed!${NC}"
    echo ""
    echo "To use curlthis, you may need to:"
    echo "  1. Restart your terminal or run: source $RC_FILE"
    echo "  2. Run 'curlthis' to transform raw HTTP requests from clipboard"
    echo "  3. Run 'curlthis -h' for help and additional options"
    echo ""
    echo "Example usage:"
    echo "  curlthis -f request.txt    # Read from file"
    echo "  cat request.txt | curlthis  # Read from stdin"
    echo "  curlthis -c                # Copy result to clipboard"
    echo ""
    
    return 0
}

# Main installation process
main() {
    echo -e "${BLUE}=== curlthis Installation ===${NC}"
    
    # Verify Python installation
    hitmonlee_verify_python || exit 1
    
    # Setup virtual environment
    machoke_setup_venv || exit 1
    
    # Configure shell
    machamp_configure_shell || exit 1
    
    # Show success message
    hitmonchan_show_success
    
    echo -e "${GREEN}Installation complete!${NC}"
}

# Run the main function
main
