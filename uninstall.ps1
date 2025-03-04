# curlthis uninstallation script for Windows
# Following the Pokemon-themed function naming convention

# Cleanup operations function
function Invoke-PrimeapeRemoveInstallation {
    Write-Host "Primeape uses Thrash to remove installation..." -ForegroundColor Blue
    
    $venvDir = "$env:USERPROFILE\.curlthis_venv"
    $binDir = "$venvDir\Scripts"
    
    # Remove virtual environment
    if (Test-Path $venvDir) {
        Write-Host "Removing virtual environment at $venvDir..."
        Remove-Item -Path $venvDir -Recurse -Force
        Write-Host "Virtual environment removed."
    }
    else {
        Write-Host "Virtual environment not found at $venvDir."
    }
    
    # Remove from PATH
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ($currentPath -like "*$binDir*") {
        $newPath = ($currentPath -split ';' | Where-Object { $_ -ne $binDir }) -join ';'
        [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
        Write-Host "Removed $binDir from PATH"
    }
    
    Write-Host "Uninstallation complete." -ForegroundColor Green
    return $true
}

# User feedback function
function Invoke-HitmonchanShowSuccess {
    Write-Host "Hitmonchan uses Mach Punch to show uninstallation results..." -ForegroundColor Blue
    
    Write-Host "curlthis has been successfully uninstalled!" -ForegroundColor Green
    Write-Host ""
    Write-Host "To complete the uninstallation, you may need to:"
    Write-Host "  1. Restart your terminal to refresh PATH"
    Write-Host ""
    
    return $true
}

# Main uninstallation process
function Uninstall-CurlThis {
    Write-Host "=== curlthis Uninstallation ===" -ForegroundColor Blue
    
    # Remove installation
    if (-not (Invoke-PrimeapeRemoveInstallation)) {
        exit 1
    }
    
    # Show success message
    Invoke-HitmonchanShowSuccess
    
    Write-Host "Uninstallation complete!" -ForegroundColor Green
}

# Run the uninstallation
Uninstall-CurlThis
