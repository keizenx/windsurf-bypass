# Windsurf Free VIP - Admin Mode
Write-Host "Windsurf Free VIP - Admin Mode" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host "This script requires administrator privileges" -ForegroundColor Yellow
Write-Host ""

# Check if running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "ERROR: This script requires administrator privileges!" -ForegroundColor Red
    Write-Host "Please run PowerShell as administrator and try again." -ForegroundColor Red
    Write-Host ""
    Write-Host "Alternative: Use --safe mode instead:" -ForegroundColor Yellow
    Write-Host "python windsurf_bypass.py --safe" -ForegroundColor Cyan
    pause
    exit 1
}

Write-Host "Admin privileges confirmed. Starting aggressive bypass..." -ForegroundColor Green
Write-Host ""

# Run the admin bypass
python windsurf_bypass.py --admin

Write-Host ""
Write-Host "Admin bypass completed!" -ForegroundColor Green
Write-Host "Please restart your computer for changes to take effect." -ForegroundColor Yellow
pause
