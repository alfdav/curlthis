# Pokemon-themed Terminal Styling Installation Template
# This template follows the terminal styling standards with Pokemon-themed function naming
# Requires -Version 5.1

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

# System verification function
function Hitmonlee-VerifyPython {
    Write-Status "Hitmonlee uses High Jump Kick to verify Python installation..."
    
    try {
        $PythonCommand = Get-Command python -ErrorAction Stop
        $PythonVersion = & python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
        
        $Major, $Minor = $PythonVersion.Split('.')
        
        if ([int]$Major -lt 3 -or ([int]$Major -eq 3 -and [int]$Minor -lt 8)) {
            Write-Error "Python version $PythonVersion detected. Version 3.8 or higher is required."
            return $false
        }
        
        Write-Success "Python $PythonVersion detected."
        return $true
    }
    catch {
        Write-Error "Python is not installed or not in PATH. Please install Python 3.8 or higher."
        return $false
    }
}

# Environment setup function
function Machoke-SetupVenv {
    Write-Status "Machoke uses Strength to set up virtual environment..."
    
    $VenvDir = Join-Path $env:USERPROFILE ".app_venv"
    
    # Create virtual environment if it doesn't exist
    if (-not (Test-Path $VenvDir)) {
        Write-Info "Creating virtual environment at $VenvDir..."
        
        try {
            & python -m venv $VenvDir
            if (-not $?) {
                Write-Error "Failed to create virtual environment."
                return $false
            }
        }
        catch {
            Write-Error "Failed to create virtual environment: $_"
            return $false
        }
    }
    else {
        Write-Info "Using existing virtual environment at $VenvDir..."
    }
    
    # Activate virtual environment
    $ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
    try {
        . $ActivateScript
        if (-not $?) {
            Write-Error "Failed to activate virtual environment."
            return $false
        }
    }
    catch {
        Write-Error "Failed to activate virtual environment: $_"
        return $false
    }
    
    # Install the package in development mode
    Write-Info "Installing package..."
    try {
        & pip install --upgrade pip
        & pip install -e .
        if (-not $?) {
            Write-Error "Failed to install package."
            return $false
        }
    }
    catch {
        Write-Error "Failed to install package: $_"
        return $false
    }
    
    Write-Success "Virtual environment setup complete."
    return $true
}

# Shell configuration function
function Machamp-ConfigureShell {
    Write-Status "Machamp uses Dynamic Punch to configure shell..."
    
    $ScriptsDir = Join-Path $env:USERPROFILE "Documents\WindowsPowerShell\Scripts"
    
    # Create scripts directory if it doesn't exist
    if (-not (Test-Path $ScriptsDir)) {
        New-Item -ItemType Directory -Path $ScriptsDir -Force | Out-Null
    }
    
    # Create wrapper script
    $WrapperPath = Join-Path $ScriptsDir "mycommand.ps1"
    Write-Info "Creating wrapper script at $WrapperPath..."
    
    $VenvDir = Join-Path $env:USERPROFILE ".app_venv"
    $ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
    
    $WrapperContent = @"
# Wrapper script for mycommand
. "$ActivateScript"
python -m mypackage `$args
"@
    
    Set-Content -Path $WrapperPath -Value $WrapperContent
    
    # Add to PATH if not already there
    $CurrentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if (-not $CurrentPath.Contains($ScriptsDir)) {
        Write-Info "Adding scripts directory to PATH..."
        [Environment]::SetEnvironmentVariable("PATH", "$CurrentPath;$ScriptsDir", "User")
        $env:PATH = "$env:PATH;$ScriptsDir"
    }
    else {
        Write-Info "Scripts directory already in PATH."
    }
    
    # Create PowerShell profile if it doesn't exist
    $ProfilePath = $PROFILE.CurrentUserAllHosts
    if (-not (Test-Path $ProfilePath)) {
        Write-Info "Creating PowerShell profile..."
        New-Item -ItemType File -Path $ProfilePath -Force | Out-Null
    }
    
    # Add alias to profile if not already there
    $AliasLine = "Set-Alias -Name mycommand -Value '$WrapperPath'"
    $ProfileContent = Get-Content -Path $ProfilePath -Raw -ErrorAction SilentlyContinue
    
    if (-not $ProfileContent -or -not $ProfileContent.Contains($AliasLine)) {
        Write-Info "Adding alias to PowerShell profile..."
        Add-Content -Path $ProfilePath -Value "`n# Added by mypackage installer"
        Add-Content -Path $ProfilePath -Value $AliasLine
    }
    else {
        Write-Info "Alias already in PowerShell profile."
    }
    
    Write-Success "Shell configuration complete."
    return $true
}

# User feedback function
function Hitmonchan-ShowSuccess {
    Write-Status "Hitmonchan uses Sky Uppercut to show installation results..."
    
    Write-Banner "Installation Complete" "Your application is ready to use"
    
    Write-Success "Application has been successfully installed!"
    Write-Host ""
    Write-Host "Application is now available in your terminal!" -ForegroundColor $Colors.Cyan
    Write-Host "Try it now with: mycommand -h"
    Write-Host ""
    Write-Host "Example usage:" -ForegroundColor White
    Write-Host "  mycommand command1    # Description 1" -ForegroundColor $Colors.Gray
    Write-Host "  mycommand command2    # Description 2" -ForegroundColor $Colors.Gray
    Write-Host ""
    
    return $true
}

# Dependencies installation function
function Alakazam-InstallDependencies {
    Write-Status "Alakazam uses Psychic to install dependencies..."
    
    # Install core UI dependencies explicitly first
    Write-Info "Installing core UI dependencies..."
    try {
        & pip install --upgrade typer>=0.15.1 rich>=13.9.4
        if (-not $?) {
            Write-Error "Failed to install core UI dependencies."
            return $false
        }
    }
    catch {
        Write-Error "Failed to install core UI dependencies: $_"
        return $false
    }
    
    # Verify Typer installation
    try {
        & python -c "import typer" 2>$null
        if (-not $?) {
            Write-Warning "Typer installation verification failed, trying again..."
            & pip install --force-reinstall typer>=0.15.1
            
            # Check again
            & python -c "import typer" 2>$null
            if (-not $?) {
                Write-Error "Failed to install Typer. Please install it manually with: pip install typer>=0.15.1"
                return $false
            }
        }
    }
    catch {
        Write-Error "Failed to verify Typer installation: $_"
        return $false
    }
    
    # Verify Rich installation
    try {
        & python -c "import rich" 2>$null
        if (-not $?) {
            Write-Warning "Rich installation verification failed, trying again..."
            & pip install --force-reinstall rich>=13.9.4
            
            # Check again
            & python -c "import rich" 2>$null
            if (-not $?) {
                Write-Error "Failed to install Rich. Please install it manually with: pip install rich>=13.9.4"
                return $false
            }
        }
    }
    catch {
        Write-Error "Failed to verify Rich installation: $_"
        return $false
    }
    
    # Install project-specific dependencies
    Write-Info "Installing project-specific dependencies..."
    try {
        & pip install -e . --use-pep517
        if (-not $?) {
            Write-Error "Failed to install project-specific dependencies."
            return $false
        }
    }
    catch {
        Write-Error "Failed to install project-specific dependencies: $_"
        return $false
    }
    
    Write-Success "All dependencies installed successfully"
    return $true
}

# Main installation process
function Install-Project {
    Write-Banner "Application Installer" "Installing your application"
    
    # Verify Python installation
    if (-not (Hitmonlee-VerifyPython)) {
        return
    }
    
    # Install dependencies
    if (-not (Alakazam-InstallDependencies)) {
        return
    }
    
    # Setup virtual environment
    if (-not (Machoke-SetupVenv)) {
        return
    }
    
    # Configure shell
    if (-not (Machamp-ConfigureShell)) {
        return
    }
    
    # Show success message
    Hitmonchan-ShowSuccess
    
    Write-Success "Installation complete!"
}

# Run the main function
Install-Project