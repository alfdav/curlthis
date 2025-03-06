#!/bin/bash
# Example script demonstrating the shell styling standards

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

# Example function using Pokemon-themed naming
hitmonlee_verify_file() {
    local file_path="$1"
    
    print_status "Hitmonlee uses High Jump Kick to verify file..."
    
    if [ ! -f "$file_path" ]; then
        print_error "File not found: $file_path"
        return 1
    fi
    
    print_success "File exists: $file_path"
    return 0
}

# Example function using Pokemon-themed naming
machamp_process_data() {
    local input="$1"
    
    print_status "Machamp uses Dynamic Punch to process data..."
    
    # Simulate processing with a simple transformation
    local output=$(echo "$input" | tr '[:lower:]' '[:upper:]')
    
    print_success "Data processed successfully"
    echo "$output"
}

# Example function using Pokemon-themed naming
hitmonchan_show_results() {
    local result="$1"
    
    print_status "Hitmonchan uses Sky Uppercut to show results..."
    
    echo
    echo -e "${BLUE}========== RESULTS ==========${NC}"
    echo -e "$result"
    echo -e "${BLUE}============================${NC}"
    echo
}

# Main function
main() {
    # Display banner
    print_banner "Shell Styling Example" "Demonstrating shell styling standards"
    
    # Display different status messages
    print_info "This is an information message"
    print_success "This is a success message"
    print_warning "This is a warning message"
    print_error "This is an error message"
    
    echo
    
    # Get the full path to this script
    SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/$(basename "${BASH_SOURCE[0]}")"
    
    # Verify a file
    if hitmonlee_verify_file "$SCRIPT_PATH"; then
        # Process some data
        result=$(machamp_process_data "hello world")
        
        # Show results
        hitmonchan_show_results "$result"
    fi
    
    echo
    print_success "Example completed successfully!"
}

# Run the main function
main