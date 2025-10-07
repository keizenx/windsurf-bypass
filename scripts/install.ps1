# Windsurf Free VIP - Windows Installation Script
# PowerShell installation script for Windows

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Windsurf Free VIP - Installation" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "⚠️  Warning: This script works better with administrator privileges" -ForegroundColor Yellow
    Write-Host "   Some registry modifications may fail" -ForegroundColor Yellow
    Write-Host ""
    
    $response = Read-Host "Do you want to continue anyway? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "❌ Installation cancelled" -ForegroundColor Red
        exit 1
    }
}

# Check Python installation
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "✓ Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "   Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create project directory
$projectDir = "$env:USERPROFILE\windsurf-bypass"
if (-not (Test-Path $projectDir)) {
    New-Item -ItemType Directory -Path $projectDir -Force | Out-Null
    Write-Host "✓ Project directory created: $projectDir" -ForegroundColor Green
}

# Download main script
$mainScriptUrl = "https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/windsurf_bypass.py"
$mainScriptPath = "$projectDir\windsurf_bypass.py"

try {
    Invoke-WebRequest -Uri $mainScriptUrl -OutFile $mainScriptPath
    Write-Host "✓ Main script downloaded" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to download main script" -ForegroundColor Red
    Write-Host "   Please check your internet connection" -ForegroundColor Yellow
    exit 1
}

# Download PowerShell runner
$runnerUrl = "https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/run_bypass.ps1"
$runnerPath = "$projectDir\run_bypass.ps1"

try {
    Invoke-WebRequest -Uri $runnerUrl -OutFile $runnerPath
    Write-Host "✓ PowerShell runner downloaded" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to download PowerShell runner" -ForegroundColor Red
    exit 1
}

# Download config
$configUrl = "https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/config.json"
$configPath = "$projectDir\config.json"

try {
    Invoke-WebRequest -Uri $configUrl -OutFile $configPath
    Write-Host "✓ Configuration downloaded" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Configuration download failed, using defaults" -ForegroundColor Yellow
}

# Test the installation
Write-Host ""
Write-Host "🧪 Testing installation..." -ForegroundColor Cyan
Set-Location $projectDir

try {
    python windsurf_bypass.py --test
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Installation test successful" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Installation test failed, but script is ready" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️  Could not run test, but installation is complete" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Installation completed successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To use Windsurf Free VIP:" -ForegroundColor Yellow
Write-Host "1. Navigate to: $projectDir" -ForegroundColor White
Write-Host "2. Run: .\run_bypass.ps1" -ForegroundColor White
Write-Host "3. Or run: python windsurf_bypass.py" -ForegroundColor White
Write-Host ""
Write-Host "For updates, run this script again." -ForegroundColor Cyan
Read-Host "Press Enter to exit"
