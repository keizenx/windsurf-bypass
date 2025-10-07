# Windsurf Free VIP - Quick Installation Script
# Alternative installation method

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Windsurf Free VIP - Quick Install" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

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

Write-Host ""
Write-Host "🔧 Running Windsurf Free VIP..." -ForegroundColor Cyan
Write-Host ""

# Run the main script
python windsurf_bypass.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Installation completed!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Read-Host "Press Enter to exit"
