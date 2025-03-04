# curlthis installation script for Windows
# Following the Pokemon-themed function naming convention

# System verification function
function Invoke-HitmonleeVerifyPython {
    Write-Host "Hitmonlee uses High Jump Kick to verify Python installation..." -ForegroundColor Blue
    
    try {
        $pythonInfo = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
        $pythonVersion = [version]$pythonInfo
        
        if ($pythonVersion -lt [version]"3.8") {
            Write-Host "Python version $pythonVersion detected. Version 3.8 or higher is required." -ForegroundColor Red
            return $false
        }
        
        Write-Host "Python $pythonVersion detected." -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "Python 3 is not installed or not in PATH. Please install Python 3.8 or higher." -ForegroundColor Red
        return $false
    }
}

# Environment setup function
function Invoke-MachokeSetupVenv {
    Write-Host "Machoke uses Strength to set up virtual environment..." -ForegroundColor Blue
    
    $venvDir = "$env:USERPROFILE\.curlthis_venv"
    
    # Create virtual environment if it doesn't exist
    if (-not (Test-Path $venvDir)) {
        Write-Host "Creating virtual environment at $venvDir..."
        python -m venv $venvDir
    }
    else {
        Write-Host "Using existing virtual environment at $venvDir..."
    }
    
    # Activate virtual environment
    & "$venvDir\Scripts\Activate.ps1"
    
    # Install the package in development mode
    Write-Host "Installing curlthis..."
    pip install --upgrade pip
    pip install -e .
    
    Write-Host "Virtual environment setup complete." -ForegroundColor Green
    return $true
}

# System configuration function
function Invoke-MachampConfigureShell {
    Write-Host "Machamp uses Dynamic Punch to configure system..." -ForegroundColor Blue
    
    $venvDir = "$env:USERPROFILE\.curlthis_venv"
    $binDir = "$venvDir\Scripts"
    
    # Add to PATH if not already present
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ($currentPath -notlike "*$binDir*") {
        [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$binDir", "User")
        Write-Host "Added $binDir to PATH"
    }
    else {
        Write-Host "Path already configured."
    }
    
    Write-Host "System configuration complete." -ForegroundColor Green
    return $true
}

# User feedback function
function Invoke-HitmonchanShowSuccess {
    Write-Host "Hitmonchan uses Sky Uppercut to show installation results..." -ForegroundColor Blue
    
    Write-Host "curlthis has been successfully installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "To use curlthis, you may need to:"
    Write-Host "  1. Restart your terminal to refresh PATH"
    Write-Host "  2. Run 'curlthis' to transform raw HTTP requests from clipboard"
    Write-Host "  3. Run 'curlthis -h' for help and additional options"
    Write-Host ""
    Write-Host "Example usage:"
    Write-Host "  curlthis -f request.txt    # Read from file"
    Write-Host "  Get-Content request.txt | curlthis  # Read from stdin"
    Write-Host "  curlthis -c                # Copy result to clipboard"
    Write-Host ""
    
    return $true
}

# Main installation process
function Install-CurlThis {
    Write-Host "=== curlthis Installation ===" -ForegroundColor Blue
    
    # Verify Python installation
    if (-not (Invoke-HitmonleeVerifyPython)) {
        exit 1
    }
    
    # Setup virtual environment
    if (-not (Invoke-MachokeSetupVenv)) {
        exit 1
    }
    
    # Configure system
    if (-not (Invoke-MachampConfigureShell)) {
        exit 1
    }
    
    # Show success message
    Invoke-HitmonchanShowSuccess
    
    Write-Host "Installation complete!" -ForegroundColor Green
}

# Run the installation
Install-CurlThis
