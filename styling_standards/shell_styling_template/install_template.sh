#!/bin/bash
# Pokemon-themed Terminal Styling Installation Template
# This template follows the terminal styling standards with Pokemon-themed function naming

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GRAY='\033[0;90m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Status indicators
STATUS_INFO="[*]"
STATUS_SUCCESS="[✓]"
STATUS_WARNING="[!]"
STATUS_ERROR="[✗]"

# Output functions
print_info() {
    echo -e "${BLUE}${STATUS_INFO}${NC} $1"
}

print_success() {
    echo -e "${GREEN}${STATUS_SUCCESS}${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}${STATUS_WARNING}${NC} $1"
}

print_error() {
    echo -e "${RED}${STATUS_ERROR}${NC} $1"
}

print_status() {
    echo -e "${CYAN}==>${NC} ${BOLD}$1${NC}"
}

print_banner() {
    echo
    echo -e "${BLUE}=========================================${NC}"
    echo -e "${BOLD}$1${NC}"
    echo -e "$2"
    echo -e "${BLUE}=========================================${NC}"
    echo
}

# System verification function
hitmonlee_verify_python() {
    print_status "Hitmonlee uses High Jump Kick to verify Python installation..."
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    
    # Compare major version first
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ $PYTHON_MAJOR -lt 3 ] || ([ $PYTHON_MAJOR -eq 3 ] && [ $PYTHON_MINOR -lt 8 ]); then
        print_error "Python version $PYTHON_VERSION detected. Version 3.8 or higher is required."
        exit 1
    fi
    
    print_success "Python $PYTHON_VERSION detected."
    return 0
}

# Environment setup function
machoke_setup_venv() {
    print_status "Machoke uses Strength to set up virtual environment..."
    
    VENV_DIR="$HOME/.app_venv"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "$VENV_DIR" ]; then
        print_info "Creating virtual environment at $VENV_DIR..."
        python3 -m venv "$VENV_DIR"
        if [ $? -ne 0 ]; then
            print_error "Failed to create virtual environment."
            exit 1
        fi
    else
        print_info "Using existing virtual environment at $VENV_DIR..."
    fi
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    if [ $? -ne 0 ]; then
        print_error "Failed to activate virtual environment."
        exit 1
    fi
    
    # Install the package in development mode
    print_info "Installing package..."
    pip install --upgrade pip
    pip install -e .
    if [ $? -ne 0 ]; then
        print_error "Failed to install package."
        exit 1
    fi
    
    print_success "Virtual environment setup complete."
    return 0
}

# Shell configuration function
machamp_configure_shell() {
    print_status "Machamp uses Dynamic Punch to configure shell..."
    
    # Detect shell type
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
            print_warning "Unsupported shell: $SHELL_TYPE. Adding to common shell files."
            RC_FILES=("$HOME/.profile")
            ;;
    esac
    
    # Always include .profile for login shells
    if ! [[ "${RC_FILES[@]}" =~ "$HOME/.profile" ]]; then
        RC_FILES+=("$HOME/.profile")
    fi
    
    # Find a directory in PATH that we can write to
    LOCAL_BIN="$HOME/.local/bin"
    mkdir -p "$LOCAL_BIN"
    
    # Create a wrapper script
    print_info "Creating wrapper script..."
    cat > "$LOCAL_BIN/mycommand" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m mypackage "\$@"
EOF
    chmod +x "$LOCAL_BIN/mycommand"
    
    # Add to PATH in shell config files
    for RC_FILE in "${RC_FILES[@]}"; do
        if [ -f "$RC_FILE" ]; then
            if ! grep -q "PATH=\"$LOCAL_BIN:\$PATH\"" "$RC_FILE"; then
                print_info "Adding to PATH in $RC_FILE..."
                echo "" >> "$RC_FILE"
                echo "# Added by mypackage installer" >> "$RC_FILE"
                echo "export PATH=\"$LOCAL_BIN:\$PATH\"" >> "$RC_FILE"
            else
                print_info "PATH already configured in $RC_FILE."
            fi
        fi
    done
    
    # Make command available immediately
    export PATH="$LOCAL_BIN:$PATH"
    
    print_success "Shell configuration complete."
    return 0
}

# User feedback function
hitmonchan_show_success() {
    print_status "Hitmonchan uses Sky Uppercut to show installation results..."
    
    echo
    print_banner "Installation Complete" "Your application is ready to use"
    echo
    print_success "Application has been successfully installed!"
    echo
    echo -e "${CYAN}Application is now available in your terminal!${NC}"
    echo "Try it now with: mycommand -h"
    echo
    echo -e "${BOLD}Example usage:${NC}"
    echo -e "  ${GRAY}mycommand command1${NC}    # Description 1"
    echo -e "  ${GRAY}mycommand command2${NC}    # Description 2"
    echo
    
    return 0
}

# Dependencies installation function
alakazam_install_dependencies() {
    print_status "Alakazam uses Psychic to install dependencies..."
    
    # Install core UI dependencies explicitly first
    print_info "Installing core UI dependencies..."
    python3 -m pip install --upgrade typer>=0.15.1 rich>=13.9.4
    
    # Verify Typer installation
    if ! python3 -c "import typer" &>/dev/null; then
        print_warning "Typer installation verification failed, trying again..."
        python3 -m pip install --force-reinstall typer>=0.15.1
        
        # Check again
        if ! python3 -c "import typer" &>/dev/null; then
            print_error "Failed to install Typer. Please install it manually with: python3 -m pip install typer>=0.15.1"
            exit 1
        fi
    fi
    
    # Verify Rich installation
    if ! python3 -c "import rich" &>/dev/null; then
        print_warning "Rich installation verification failed, trying again..."
        python3 -m pip install --force-reinstall rich>=13.9.4
        
        # Check again
        if ! python3 -c "import rich" &>/dev/null; then
            print_error "Failed to install Rich. Please install it manually with: python3 -m pip install rich>=13.9.4"
            exit 1
        fi
    fi
    
    # Install project-specific dependencies
    print_info "Installing project-specific dependencies..."
    python3 -m pip install -e . --use-pep517
    
    # Optionally install extra UI dependencies
    if [ "$INSTALL_EXTRAS" = "true" ]; then
        print_info "Installing extra UI dependencies..."
        python3 -m pip install tqdm>=4.66.0 colorama>=0.4.6 prompt_toolkit>=3.0.36
    fi
    
    print_success "All dependencies installed successfully"
    return 0
}

# Main installation process
main() {
    print_banner "Application Installer" "Installing your application"
    
    # Verify Python installation
    hitmonlee_verify_python || exit 1
    
    # Install dependencies
    alakazam_install_dependencies || exit 1
    
    # Setup virtual environment
    machoke_setup_venv || exit 1
    
    # Configure shell
    machamp_configure_shell || exit 1
    
    # Show success message
    hitmonchan_show_success
    
    print_success "Installation complete!"
}

# Run the main function
main