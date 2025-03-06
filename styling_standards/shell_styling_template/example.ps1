# Example script demonstrating the shell styling standards for PowerShell

# Output colors
$Colors = @{
    Red    = [System.ConsoleColor]::Red
    Green  = [System.ConsoleColor]::Green
    Yellow = [System.ConsoleColor]::Yellow
    Blue   = [System.ConsoleColor]::Blue
    Cyan   = [System.ConsoleColor]::Cyan
    Gray   = [System.ConsoleColor]::DarkGray
}

# Status indicators
$StatusInfo = "[*]"
$StatusSuccess = "[✓]"
$StatusWarning = "[!]"
$StatusError = "[✗]"

# Logging functions
function Write-Info {
    param([string]$Message)
    Write-Host "$StatusInfo $Message" -ForegroundColor $Colors.Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "$StatusSuccess $Message" -ForegroundColor $Colors.Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "$StatusWarning $Message" -ForegroundColor $Colors.Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "$StatusError $Message" -ForegroundColor $Colors.Red
}

function Write-Status {
    param([string]$Message)
    Write-Host "==> " -ForegroundColor $Colors.Cyan -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-Banner {
    param(
        [string]$Title,
        [string]$Description
    )
    
    Write-Host ""
    Write-Host "=========================================" -ForegroundColor $Colors.Blue
    Write-Host $Title -ForegroundColor White
    Write-Host $Description
    Write-Host "=========================================" -ForegroundColor $Colors.Blue
    Write-Host ""
}

# Example function using Pokemon-themed naming
function Hitmonlee-VerifyFile {
    param([string]$FilePath)
    
    Write-Status "Hitmonlee uses High Jump Kick to verify file..."
    
    if (-not (Test-Path $FilePath)) {
        Write-Error "File not found: $FilePath"
        return $false
    }
    
    Write-Success "File exists: $FilePath"
    return $true
}

# Example function using Pokemon-themed naming
function Machamp-ProcessData {
    param([string]$Input)
    
    Write-Status "Machamp uses Dynamic Punch to process data..."
    
    # Simulate processing with a simple transformation
    $Output = $Input.ToUpper()
    
    Write-Success "Data processed successfully"
    return $Output
}

# Example function using Pokemon-themed naming
function Hitmonchan-ShowResults {
    param([string]$Result)
    
    Write-Status "Hitmonchan uses Sky Uppercut to show results..."
    
    Write-Host ""
    Write-Host "========== RESULTS ==========" -ForegroundColor $Colors.Blue
    Write-Host $Result
    Write-Host "============================" -ForegroundColor $Colors.Blue
    Write-Host ""
}

# Main function
function Main {
    # Display banner
    Write-Banner "PowerShell Styling Example" "Demonstrating shell styling standards"
    
    # Display different status messages
    Write-Info "This is an information message"
    Write-Success "This is a success message"
    Write-Warning "This is a warning message"
    Write-Error "This is an error message"
    
    Write-Host ""
    
    # Get the full path to this script
    $ScriptPath = $MyInvocation.MyCommand.Path
    
    # Verify a file
    if (Hitmonlee-VerifyFile $ScriptPath) {
        # Process some data
        $Result = Machamp-ProcessData "hello world"
        
        # Show results
        Hitmonchan-ShowResults $Result
    }
    
    Write-Host ""
    Write-Success "Example completed successfully!"
}

# Run the main function
Main