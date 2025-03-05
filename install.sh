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
    
    # Create a symlink in a common bin directory
    LOCAL_BIN="$HOME/.local/bin"
    if [ ! -d "$LOCAL_BIN" ]; then
        mkdir -p "$LOCAL_BIN"
        echo "Created $LOCAL_BIN directory."
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
        echo "Found writable $SYSTEM_BIN directory, creating executable there..."
        # Create a wrapper script that activates the venv and runs the command
        cat > "$SYSTEM_BIN/curlthis" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m curlthis "\$@"
EOF
        chmod +x "$SYSTEM_BIN/curlthis"
        echo "Created executable in $SYSTEM_BIN"
        FOUND_PATH_DIR="$SYSTEM_BIN"
    fi
    
    # Create symlink to curlthis in ~/.local/bin
    if [ -f "$BIN_DIR/curlthis" ]; then
        ln -sf "$BIN_DIR/curlthis" "$LOCAL_BIN/curlthis"
        echo "Created symlink for curlthis in $LOCAL_BIN"
        chmod +x "$LOCAL_BIN/curlthis"
    else
        # Create a wrapper script that activates the venv and runs the module
        cat > "$LOCAL_BIN/curlthis" << EOF
#!/bin/bash
source "$VENV_DIR/bin/activate"
python -m curlthis "\$@"
EOF
        chmod +x "$LOCAL_BIN/curlthis"
        echo "Created wrapper script in $LOCAL_BIN"
    fi
    
    # If we found a directory in PATH, create a symlink there too
    if [ -n "$FOUND_PATH_DIR" ] && [ "$FOUND_PATH_DIR" != "$SYSTEM_BIN" ]; then
        ln -sf "$LOCAL_BIN/curlthis" "$FOUND_PATH_DIR/curlthis"
        echo -e "${GREEN}Created symlink in $FOUND_PATH_DIR which is already in your PATH${NC}"
        echo -e "${GREEN}curlthis is now immediately available!${NC}"
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
            echo -e "${YELLOW}Unsupported shell: $SHELL_TYPE. Adding to common shell files.${NC}"
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
            echo "Created $RC_FILE"
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
            
            echo "Added paths to $RC_FILE"
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
        echo -e "${GREEN}PATH configuration updated in shell configuration files.${NC}"
        echo -e "${YELLOW}For new terminal sessions, curlthis will be available automatically.${NC}"
    else
        echo "PATH already configured in shell files."
    fi
    
    echo -e "${GREEN}Shell configuration complete.${NC}"
    return 0
}

# User feedback function
hitmonchan_show_success() {
    echo -e "${BLUE}Hitmonchan uses Sky Uppercut to show installation results...${NC}"
    
    echo -e "${GREEN}curlthis has been successfully installed!${NC}"
    echo ""
    echo "curlthis is now available in your terminal!"
    echo "Try it now with: curlthis -h"
    echo ""
    echo "Example usage:"
    echo "  curlthis -f request.txt    # Read from file"
    echo "  cat request.txt | curlthis  # Read from stdin"
    echo "  curlthis -c                # Copy result to clipboard"
    echo ""
    
    # Create a global alias that will work in the current shell session
    GLOBAL_ALIAS_CREATED=false
    
    # Try to create a global alias for the current shell
    if [ -f "$LOCAL_BIN/curlthis" ]; then
        # Make the command available in the current shell without restarting
        CURLTHIS_PATH="$LOCAL_BIN/curlthis"
        
        # Export the function to make it available immediately
        cat << EOF

# You can now use curlthis immediately in this terminal session!
# Example: curlthis -h
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
                            echo -e "${GREEN}Created symlink in $dir which is in your current PATH${NC}"
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
