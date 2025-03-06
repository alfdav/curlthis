#!/bin/bash

# curlthis installation script for Unix-like systems
# Following the Pokemon-themed function naming convention

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
    echo -e "${BLUE}┌────────────────────────────────────────────┐${NC}"
    echo -e "${BLUE}│${NC}           ${BOLD}curlthis Installer${NC}               ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}                                            ${BLUE}│${NC}"
    echo -e "${BLUE}│${NC}  Transform raw HTTP requests to curl       ${BLUE}│${NC}"
    echo -e "${BLUE}└────────────────────────────────────────────┘${NC}"
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
    
    VENV_DIR="$HOME/.curlthis_venv"
    
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
    print_info "Installing curlthis..."
    pip install --upgrade pip
    pip install -e .
    if [ $? -ne 0 ]; then
        print_error "Failed to install curlthis package."
        exit 1
    fi
    
    print_success "Virtual environment setup complete."
    return 0
}

# Shell configuration function
machamp_configure_shell() {
    print_status "Machamp uses Dynamic Punch to configure shell..."
    
    VENV_DIR="$HOME/.curlthis_venv"
    BIN_DIR="$VENV_DIR/bin"
    
    # Create a symlink in a common bin directory
    LOCAL_BIN="$HOME/.local/bin"
    if [ ! -d "$LOCAL_BIN" ]; then
        mkdir -p "$LOCAL_BIN"
        print_info "Created $LOCAL_BIN directory."
    fi
    
    # Find a directory in PATH that we can write to
    FOUND_PATH_DIR=""
    IFS=':' read -ra PATH_DIRS <<< "$PATH"
    for dir in "${PATH_DIRS[@]}"; do
        if [ -d "$dir" ] && [ -w "$dir" ] && [ "$dir" != "$LOCAL_BIN" ]; then
            FOUND_PATH_DIR="$dir"
            break
        fi
    done
    
    # Try to create a direct executable in /usr/local/bin if possible (requires sudo)
    SYSTEM_BIN="/usr/local/bin"
    if [ -d "$SYSTEM_BIN" ] && [ -w "$SYSTEM_BIN" ]; then
        print_info "Found writable $SYSTEM_BIN directory, creating executable there..."
        # Create a wrapper script that activates the venv and runs the command
        cat > "$SYSTEM_BIN/curlthis" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m curlthis "\$@"
EOF
        chmod +x "$SYSTEM_BIN/curlthis"
        print_success "Created executable in $SYSTEM_BIN"
        FOUND_PATH_DIR="$SYSTEM_BIN"
    fi
    
    # Create symlink to curlthis in ~/.local/bin
    if [ -f "$BIN_DIR/curlthis" ]; then
        ln -sf "$BIN_DIR/curlthis" "$LOCAL_BIN/curlthis"
        print_info "Created symlink for curlthis in $LOCAL_BIN"
        chmod +x "$LOCAL_BIN/curlthis"
    else
        # Create a wrapper script that activates the venv and runs the module
        cat > "$LOCAL_BIN/curlthis" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m curlthis "\$@"
EOF
        chmod +x "$LOCAL_BIN/curlthis"
        print_info "Created wrapper script in $LOCAL_BIN"
    fi
    
    # If we found a directory in PATH, create a symlink there too
    if [ -n "$FOUND_PATH_DIR" ] && [ "$FOUND_PATH_DIR" != "$SYSTEM_BIN" ]; then
        ln -sf "$LOCAL_BIN/curlthis" "$FOUND_PATH_DIR/curlthis"
        print_success "Created symlink in $FOUND_PATH_DIR which is already in your PATH"
        print_success "curlthis is now immediately available!"
    fi
    
    # Detect shell type
    SHELL_TYPE=$(basename "$SHELL")
    RC_FILE=""
    
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
    
    # Add both BIN_DIR and LOCAL_BIN to PATH in appropriate RC files
    PATH_UPDATED=false
    
    for RC_FILE in "${RC_FILES[@]}"; do
        # Create the file if it doesn't exist
        if [ ! -f "$RC_FILE" ]; then
            mkdir -p "$(dirname "$RC_FILE")"
            touch "$RC_FILE"
            print_info "Created $RC_FILE"
        fi
        
        # Check if paths are already in RC file
        if ! grep -q "# curlthis path configuration" "$RC_FILE"; then
            echo "" >> "$RC_FILE"
            echo "# curlthis path configuration" >> "$RC_FILE"
            
            # For fish shell, use the fish syntax
            if [[ "$RC_FILE" == *"fish"* ]]; then
                echo "set -gx PATH \$PATH $BIN_DIR $LOCAL_BIN" >> "$RC_FILE"
            else
                # Make sure .local/bin comes first in the PATH to ensure it's found
                echo "export PATH=\"$LOCAL_BIN:$BIN_DIR:\$PATH\"" >> "$RC_FILE"
            fi
            
            print_info "Added paths to $RC_FILE"
            PATH_UPDATED=true
        fi
    done
    
    # Also update current session PATH - put our paths at the beginning to ensure they're found
    export PATH="$LOCAL_BIN:$BIN_DIR:$PATH"
    
    # Create a function in the current shell that can be used immediately
    if [ -z "$FOUND_PATH_DIR" ]; then
        # Define a function for the current shell session
        cat << EOF

# You can use curlthis immediately in this terminal session
curlthis() {
  "$LOCAL_BIN/curlthis" "\$@"
}

# Try it with: curlthis -h
EOF
    fi
    
    if [ "$PATH_UPDATED" = true ]; then
        print_success "PATH configuration updated in shell configuration files."
        print_warning "For new terminal sessions, curlthis will be available automatically."
    else
        print_info "PATH already configured in shell files."
    fi
    
    print_success "Shell configuration complete."
    return 0
}

# User feedback function
hitmonchan_show_success() {
    print_status "Hitmonchan uses Sky Uppercut to show installation results..."
    
    echo
    print_banner
    echo
    print_success "curlthis has been successfully installed!"
    echo
    echo -e "${CYAN}curlthis is now available in your terminal!${NC}"
    echo "Try it now with: curlthis -h"
    echo
    echo -e "${BOLD}Example usage:${NC}"
    echo "  curlthis -f request.txt    # Read from file"
    echo "  cat request.txt | curlthis  # Read from stdin"
    echo "  curlthis -c                # Copy result to clipboard"
    echo
    
    # Create a global alias that will work in the current shell session
    GLOBAL_ALIAS_CREATED=false
    
    # Try to create a global alias for the current shell
    if [ -f "$LOCAL_BIN/curlthis" ]; then
        # Make the command available in the current shell without restarting
        CURLTHIS_PATH="$LOCAL_BIN/curlthis"
        
        # Export the function to make it available immediately
        cat << EOF

${CYAN}You can now use curlthis immediately in this terminal session!${NC}
${GRAY}Example: curlthis -h${NC}
EOF
        
        # Export the function to the current shell
        export -f curlthis 2>/dev/null || GLOBAL_ALIAS_CREATED=false
        
        # If export failed, create a symbolic link in a directory that's likely in PATH
        if [ "$GLOBAL_ALIAS_CREATED" = false ]; then
            # Try to find a directory in PATH that we can write to
            IFS=':' read -ra PATH_DIRS <<< "$PATH"
            for dir in "${PATH_DIRS[@]}"; do
                if [ -d "$dir" ] && [ -w "$dir" ]; then
                    if [ "$dir" != "$LOCAL_BIN" ]; then
                        ln -sf "$LOCAL_BIN/curlthis" "$dir/curlthis" 2>/dev/null && {
                            print_success "Created symlink in $dir which is in your current PATH"
                            GLOBAL_ALIAS_CREATED=true
                            break
                        }
                    fi
                fi
            done
        fi
    fi
    
    return 0
}

# Main installation process
main() {
    print_banner
    
    # Verify Python installation
    hitmonlee_verify_python || exit 1
    
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
