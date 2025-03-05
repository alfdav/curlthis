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
    
    # Create a common bin directory in user profile
    $localBin = "$env:USERPROFILE\.local\bin"
    if (-not (Test-Path $localBin)) {
        New-Item -Path $localBin -ItemType Directory -Force | Out-Null
        Write-Host "Created $localBin directory."
    }
    
    # Find a directory in PATH that we can write to
    $foundPathDir = $null
    $pathDirs = $env:PATH -split ';' | Where-Object { $_ -ne "" }
    foreach ($dir in $pathDirs) {
        if ((Test-Path $dir) -and (Test-Path "$dir\.." -PathType Container)) {
            try {
                $testFile = "$dir\curlthis_test.tmp"
                "test" | Out-File -FilePath $testFile -Force -ErrorAction Stop
                Remove-Item -Path $testFile -Force -ErrorAction Stop
                $foundPathDir = $dir
                Write-Host "Found writable directory in PATH: $foundPathDir" -ForegroundColor Green
                break
            }
            catch {
                # Continue to next directory
            }
        }
    }
    
    # Try to create a wrapper in a system-wide location if possible
    $systemBin = "C:\Windows\System32"
    $systemWrapperCreated = $false
    if ((Test-Path $systemBin) -and (Test-Path "$systemBin\cmd.exe")) {
        try {
            # Create a .cmd wrapper that calls the exe or script
            $systemWrapper = "$systemBin\curlthis.cmd"
            "@echo off" | Out-File -FilePath $systemWrapper -Encoding ascii -Force -ErrorAction Stop
            """$venvDir\Scripts\activate.bat"" && python -m curlthis %*" | Out-File -FilePath $systemWrapper -Encoding ascii -Append -ErrorAction Stop
            Write-Host "Created system-wide command wrapper at $systemWrapper" -ForegroundColor Green
            $systemWrapperCreated = $true
            $foundPathDir = $systemBin
        }
        catch {
            Write-Host "Unable to create system-wide wrapper (requires admin privileges): $_" -ForegroundColor Yellow
        }
    }
    
    # Create a .cmd wrapper in the common bin directory
    $cmdWrapper = "$localBin\curlthis.cmd"
    $exePath = "$binDir\curlthis.exe"
    
    if (Test-Path $exePath) {
        # Create a .cmd wrapper that calls the exe
        "@echo off" | Out-File -FilePath $cmdWrapper -Encoding ascii -Force
        """$exePath"" %*" | Out-File -FilePath $cmdWrapper -Encoding ascii -Append
        Write-Host "Created command wrapper at $cmdWrapper"
    }
    else {
        # If exe not found, create a wrapper for the Python module
        "@echo off" | Out-File -FilePath $cmdWrapper -Encoding ascii -Force
        """$venvDir\Scripts\activate.bat"" && python -m curlthis %*" | Out-File -FilePath $cmdWrapper -Encoding ascii -Append
        Write-Host "Created module wrapper at $cmdWrapper"
    }
    
    # Create a PowerShell script wrapper too
    $psWrapper = "$localBin\curlthis.ps1"
    "# curlthis PowerShell wrapper" | Out-File -FilePath $psWrapper -Force
    "& '$venvDir\Scripts\Activate.ps1'" | Out-File -FilePath $psWrapper -Append
    "python -m curlthis @args" | Out-File -FilePath $psWrapper -Append
    Write-Host "Created PowerShell wrapper at $psWrapper"
    
    # If we found a directory in PATH, create a copy there too (if not already system bin)
    if ($foundPathDir -and -not $systemWrapperCreated -and $foundPathDir -ne $localBin) {
        try {
            Copy-Item -Path $cmdWrapper -Destination "$foundPathDir\curlthis.cmd" -Force -ErrorAction Stop
            Write-Host "Created command wrapper in $foundPathDir which is already in your PATH" -ForegroundColor Green
            Write-Host "curlthis is now immediately available!" -ForegroundColor Green
        }
        catch {
            Write-Host "Unable to create wrapper in $foundPathDir: $_" -ForegroundColor Yellow
        }
    }
    
    # Add directories to PATH - put local bin at the beginning to ensure it's found
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    $pathsToAdd = @($localBin, $binDir)
    $pathUpdated = $false
    
    # Create a new PATH with our directories at the beginning
    $newPath = ""
    foreach ($path in $pathsToAdd) {
        # Remove path if it already exists (we'll add it to the beginning)
        if ($currentPath -like "*$path*") {
            $currentPath = $currentPath -replace [regex]::Escape($path), ""
            $currentPath = $currentPath -replace ";;+", ";"
            $currentPath = $currentPath.Trim(';')
        }
        $newPath += "$path;"
    }
    $newPath += $currentPath
    
    # Update the PATH environment variable
    [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
    Write-Host "Updated PATH environment variable with $localBin at the beginning" -ForegroundColor Green
    
    # Also update current session PATH
    $env:PATH = $newPath
    
    # Create a PowerShell profile if it doesn't exist
    $profilePath = $PROFILE.CurrentUserAllHosts
    if (-not (Test-Path $profilePath)) {
        New-Item -Path $profilePath -ItemType File -Force | Out-Null
        Write-Host "Created PowerShell profile at $profilePath"
    }
    
    # Add PATH to PowerShell profile if not already there
    $profileContent = Get-Content -Path $profilePath -Raw -ErrorAction SilentlyContinue
    if (-not ($profileContent -like "*curlthis path configuration*")) {
        "# curlthis path configuration" | Out-File -FilePath $profilePath -Append
        "$env:PATH = `"$localBin;$binDir;$env:PATH`"" | Out-File -FilePath $profilePath -Append
        Write-Host "Added PATH configuration to PowerShell profile"
    }
    
    # Add a function definition to the profile for immediate use
    if (-not ($profileContent -like "*curlthis function definition*")) {
        "" | Out-File -FilePath $profilePath -Append
        "# curlthis function definition" | Out-File -FilePath $profilePath -Append
        "function global:curlthis { & '$cmdWrapper' `$args }" | Out-File -FilePath $profilePath -Append
        Write-Host "Added function definition to PowerShell profile"
    }
    
    Write-Host "System configuration complete." -ForegroundColor Green
    return $true
}

# User feedback function
function Invoke-HitmonchanShowSuccess {
    Write-Host "Hitmonchan uses Sky Uppercut to show installation results..." -ForegroundColor Blue
    
    Write-Host "curlthis has been successfully installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "curlthis is now available in your terminal!" -ForegroundColor Yellow
    Write-Host "Try it now with: curlthis -h"
    Write-Host ""
    Write-Host "Example usage:"
    Write-Host "  curlthis -f request.txt    # Read from file"
    Write-Host "  Get-Content request.txt | curlthis  # Read from stdin"
    Write-Host "  curlthis -c                # Copy result to clipboard"
    Write-Host ""
    
    # Create a function for the current session
    $venvDir = "$env:USERPROFILE\.curlthis_venv"
    $localBin = "$env:USERPROFILE\.local\bin"
    $cmdWrapper = "$localBin\curlthis.cmd"
    
    if (Test-Path $cmdWrapper) {
        # Create a PowerShell function for immediate use
        Write-Host "# Function created for immediate use in this session:" -ForegroundColor Cyan
        Write-Host "function global:curlthis { & '$cmdWrapper' `$args }" -ForegroundColor Cyan
        Write-Host ""
        
        # Actually create the function
        $scriptBlock = {
            param($wrapper, $args)
            & $wrapper $args
        }
        
        Set-Item -Path function:global:curlthis -Value { 
            & "$cmdWrapper" $args 
        }
    }
    
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
