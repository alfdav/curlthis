# curlthis uninstallation script for Windows
# Following the Pokemon-themed function naming convention

# Cleanup operations function
function Invoke-PrimeapeRemoveInstallation {
    Write-Host "Primeape uses Thrash to remove installation..." -ForegroundColor Blue
    
    $venvDir = "$env:USERPROFILE\.curlthis_venv"
    $binDir = "$venvDir\Scripts"
    $localBin = "$env:USERPROFILE\.local\bin"
    $systemBin = "C:\Windows\System32"
    
    # Remove all command wrappers
    $wrappers = @(
        "$localBin\curlthis.cmd",
        "$localBin\curlthis.ps1",
        "$systemBin\curlthis.cmd"
    )
    
    foreach ($wrapper in $wrappers) {
        if (Test-Path $wrapper) {
            Write-Host "Removing wrapper at $wrapper..."
            try {
                Remove-Item -Path $wrapper -Force -ErrorAction Stop
                Write-Host "Wrapper removed." -ForegroundColor Green
            }
            catch {
                Write-Host "Unable to remove $wrapper: $_" -ForegroundColor Yellow
            }
        }
    }
    
    # Remove virtual environment
    if (Test-Path $venvDir) {
        Write-Host "Removing virtual environment at $venvDir..."
        Remove-Item -Path $venvDir -Recurse -Force
        Write-Host "Virtual environment removed." -ForegroundColor Green
    }
    else {
        Write-Host "Virtual environment not found at $venvDir."
    }
    
    # Remove from PATH - handle paths that might be at the beginning, middle, or end
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    $pathsToRemove = @($binDir, $localBin)
    $pathUpdated = $false
    
    foreach ($path in $pathsToRemove) {
        # Handle paths with or without trailing backslash
        $pathToFind = $path
        $pathToFindWithSlash = $path + "\"
        
        # Check for the path with or without trailing slash
        if ($currentPath -like "*$pathToFind*" -or $currentPath -like "*$pathToFindWithSlash*") {
            # Split the path and remove any matching entries
            $pathParts = $currentPath -split ';'
            $newPathParts = $pathParts | Where-Object { 
                $_ -ne $pathToFind -and $_ -ne $pathToFindWithSlash -and 
                $_ -ne $pathToFind.TrimEnd('\') -and $_ -ne $pathToFindWithSlash.TrimEnd('\')
            }
            $currentPath = $newPathParts -join ';'
            $pathUpdated = $true
        }
    }
    
    # Clean up any empty or duplicate semicolons
    if ($pathUpdated) {
        $currentPath = $currentPath -replace ';;+', ';'
        $currentPath = $currentPath.Trim(';')
        
        [Environment]::SetEnvironmentVariable("PATH", $currentPath, "User")
        Write-Host "Updated PATH environment variable" -ForegroundColor Green
        
        # Also update current session PATH
        $env:PATH = $currentPath
    }
    
    # Clean up PowerShell profile
    $profilePath = $PROFILE.CurrentUserAllHosts
    if (Test-Path $profilePath) {
        Write-Host "Cleaning up PowerShell profile..."
        $profileContent = Get-Content -Path $profilePath -Raw
        
        if ($profileContent -like "*curlthis path configuration*") {
            $newContent = ($profileContent -split "`r`n" | Where-Object { 
                -not ($_ -like "*curlthis path configuration*" -or 
                      $_ -like "*$binDir*" -or 
                      $_ -like "*$localBin*" -or
                      $_ -like "*$env:PATH = `"$localBin;$binDir;$env:PATH`"*" -or
                      $_ -like "*$env:PATH = `"$env:PATH;$binDir;$localBin`"*")
            }) -join "`r`n"
            
            Set-Content -Path $profilePath -Value $newContent
            Write-Host "Removed curlthis configuration from PowerShell profile" -ForegroundColor Green
        }
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
