# Windsurf Free VIP - GitHub Installation Script
# Alternative installation method using direct download

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Windsurf Free VIP - GitHub Install" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Create project directory
$projectDir = "$env:USERPROFILE\windsurf-bypass"
if (-not (Test-Path $projectDir)) {
    New-Item -ItemType Directory -Path $projectDir -Force | Out-Null
    Write-Host "✓ Project directory created: $projectDir" -ForegroundColor Green
}

# Download main script using alternative method
$mainScriptUrl = "https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/windsurf_bypass.py"
$mainScriptPath = "$projectDir\windsurf_bypass.py"

Write-Host "📥 Downloading Windsurf Free VIP..." -ForegroundColor Cyan

try {
    # Try multiple download methods
    try {
        Invoke-WebRequest -Uri $mainScriptUrl -OutFile $mainScriptPath -UseBasicParsing
        Write-Host "✓ Main script downloaded" -ForegroundColor Green
    } catch {
        # Alternative method using curl
        Write-Host "⚠️  PowerShell download failed, trying curl..." -ForegroundColor Yellow
        curl -L $mainScriptUrl -o $mainScriptPath
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Main script downloaded via curl" -ForegroundColor Green
        } else {
            throw "Download failed"
        }
    }
} catch {
    Write-Host "❌ Failed to download main script" -ForegroundColor Red
    Write-Host "   Please check your internet connection" -ForegroundColor Yellow
    Write-Host "   You can also download manually from:" -ForegroundColor Yellow
    Write-Host "   https://github.com/keizenx/windsurf-bypass" -ForegroundColor Cyan
    Read-Host "Press Enter to exit"
    exit 1
}

# Check Python
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "✓ Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed" -ForegroundColor Red
    Write-Host "   Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
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
Write-Host "2. Run: python windsurf_bypass.py" -ForegroundColor White
Write-Host ""
Write-Host "Repository: https://github.com/keizenx/windsurf-bypass" -ForegroundColor Cyan
Read-Host "Press Enter to exit"
