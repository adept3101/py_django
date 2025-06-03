<#
.SYNOPSIS
Activates a Python virtual environment and provides Uvicorn server management

.DESCRIPTION
This script activates a Python virtual environment and provides control over 
the Uvicorn server with start/stop/restart functionality while maintaining 
proper virtual environment activation/deactivation practices.
#>

param(
    [ValidateSet("start", "stop", "restart", "status")]
    [string]$Action = "start"
)

# Virtual Environment Configuration
$VENV_PATH = "D:\django\prdip\.venv"
$UVICORN_CMD = "prdip.asgi:application"
$hostip = "127.0.0.1"
$PORT = 8888

# Store original environment variables
$global:_OLD_VIRTUAL_PATH = $env:PATH
$global:_OLD_VIRTUAL_PROMPT = $function:prompt
if (Test-Path env:PYTHONHOME) {
    $global:_OLD_VIRTUAL_PYTHONHOME = $env:PYTHONHOME
}

# Activate the virtual environment
function Activate-Venv {
    # Set virtual environment variables
    $env:VIRTUAL_ENV = $VENV_PATH
    $env:VIRTUAL_ENV_PROMPT = "(.venv)"
    
    # Modify PATH
    $env:PATH = "$VENV_PATH\Scripts;$env:PATH"
    
    # Clear PYTHONHOME if set
    if (Test-Path env:PYTHONHOME) {
        Remove-Item env:PYTHONHOME
    }
    
    # Change the prompt to show we're in a venv
    function global:prompt {
        Write-Host -NoNewline -ForegroundColor Green "(.venv) "
        & $global:_OLD_VIRTUAL_PROMPT
    }
}

# Deactivate the virtual environment
function Deactivate-Venv {
    # Stop Uvicorn if running
    Stop-Uvicorn
    
    # Restore original environment variables
    $env:PATH = $global:_OLD_VIRTUAL_PATH
    if ($global:_OLD_VIRTUAL_PROMPT) {
        $function:prompt = $global:_OLD_VIRTUAL_PROMPT
    }
    if ($global:_OLD_VIRTUAL_PYTHONHOME) {
        $env:PYTHONHOME = $global:_OLD_VIRTUAL_PYTHONHOME
    }
    
    # Remove virtual environment variables
    Remove-Item env:VIRTUAL_ENV -ErrorAction SilentlyContinue
    Remove-Item env:VIRTUAL_ENV_PROMPT -ErrorAction SilentlyContinue
    
    Write-Host "Virtual environment deactivated" -ForegroundColor Cyan
    
    # Clean up global variables
    Remove-Variable _OLD_VIRTUAL_PATH -Scope Global -ErrorAction SilentlyContinue
    Remove-Variable _OLD_VIRTUAL_PROMPT -Scope Global -ErrorAction SilentlyContinue
    Remove-Variable _OLD_VIRTUAL_PYTHONHOME -Scope Global -ErrorAction SilentlyContinue
}

# Uvicorn process management
$global:UvicornProcess = $null
$global:UvicornRunning = $false

function Show-Status {
    if ($global:UvicornRunning) {
        Write-Host "Uvicorn is running (PID: $($global:UvicornProcess.Id))" -ForegroundColor Green
    } else {
        Write-Host "Uvicorn is not running" -ForegroundColor Yellow
    }
}

function Start-Uvicorn {
    if ($global:UvicornRunning) {
        Write-Host "Uvicorn is already running" -ForegroundColor Yellow
        return
    }

    Write-Host "Starting Uvicorn server..." -ForegroundColor Cyan
    
    $global:UvicornProcess = Start-Process -FilePath "$VENV_PATH\Scripts\python.exe" `
        -ArgumentList "-m uvicorn $UVICORN_CMD --host $hostip --port $PORT --reload" `
        -PassThru -NoNewWindow
    
    $global:UvicornRunning = $true
    Write-Host "Uvicorn started (PID: $($global:UvicornProcess.Id))" -ForegroundColor Green
}

function Stop-Uvicorn {
    if (-not $global:UvicornRunning) {
        Write-Host "Uvicorn is not running" -ForegroundColor Yellow
        return
    }

    Write-Host "Stopping Uvicorn (PID: $($global:UvicornProcess.Id))..." -ForegroundColor Cyan
    try {
        Stop-Process -Id $global:UvicornProcess.Id -Force -ErrorAction Stop
        $global:UvicornRunning = $false
        $global:UvicornProcess = $null
        Write-Host "Uvicorn stopped" -ForegroundColor Green
    } catch {
        Write-Host "Failed to stop Uvicorn: $_" -ForegroundColor Red
    }
}

function Restart-Uvicorn {
    Stop-Uvicorn
    Start-Uvicorn
}

# Main script execution
try {
    # Activate the virtual environment
    Activate-Venv
    
    # Perform the requested action
    switch ($Action.ToLower()) {
        "start" { Start-Uvicorn }
        "stop" { Stop-Uvicorn }
        "restart" { Restart-Uvicorn }
        "status" { Show-Status }
    }
    
    Write-Host "`nUsage:" -ForegroundColor Magenta
    Write-Host "  .\activate.ps1 start    - Start the server"
    Write-Host "  .\activate.ps1 stop     - Stop the server"
    Write-Host "  .\activate.ps1 restart  - Restart the server"
    Write-Host "  .\activate.ps1 status   - Show server status"
    Write-Host "  Deactivate-Venv         - Deactivate the environment`n"
}
catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    Deactivate-Venv
    exit 1
}