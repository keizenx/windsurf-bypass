# Windsurf Free VIP - GitHub Deployment Script (PowerShell)
# Script to prepare and deploy the project to GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Windsurf Free VIP - Deployment" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Git not found"
    }
    Write-Host "✓ Git detected: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed" -ForegroundColor Red
    Write-Host "   Please install Git from https://git-scm.com" -ForegroundColor Yellow
    exit 1
}

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "🔧 Initializing Git repository..." -ForegroundColor Cyan
    git init
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
}

# Add all files
Write-Host "📁 Adding files to Git..." -ForegroundColor Cyan
git add .

# Check if there are changes to commit
$gitStatus = git status --porcelain
if ([string]::IsNullOrEmpty($gitStatus)) {
    Write-Host "ℹ️  No changes to commit" -ForegroundColor Yellow
} else {
    Write-Host "💾 Committing changes..." -ForegroundColor Cyan
    git commit -m "feat: Initial release of Windsurf Free VIP

- Add core bypass functionality
- Add multi-platform support (Windows, macOS, Linux)
- Add installation scripts for all platforms
- Add comprehensive documentation
- Add identity generation and management
- Add Windows registry bypass
- Add MAC address spoofing
- Add device ID creation
- Add system information spoofing
- Add educational purpose disclaimer
- Add license and contribution guidelines"
    Write-Host "✓ Changes committed" -ForegroundColor Green
}

# Check if remote origin exists
try {
    $remoteUrl = git remote get-url origin 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "No remote origin"
    }
} catch {
    Write-Host "🔗 Adding remote origin..." -ForegroundColor Cyan
    git remote add origin https://github.com/keizenx/windsurf-bypass.git
    Write-Host "✓ Remote origin added" -ForegroundColor Green
}

# Push to GitHub
Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Cyan
try {
    git push -u origin main
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Repository URL: https://github.com/keizenx/windsurf-bypass" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Next steps:" -ForegroundColor Yellow
        Write-Host "1. Visit the repository on GitHub" -ForegroundColor White
        Write-Host "2. Add a description and topics" -ForegroundColor White
        Write-Host "3. Enable GitHub Pages if needed" -ForegroundColor White
        Write-Host "4. Create releases for versioning" -ForegroundColor White
    } else {
        throw "Push failed"
    }
} catch {
    Write-Host "❌ Failed to push to GitHub" -ForegroundColor Red
    Write-Host "   Please check your GitHub credentials and repository permissions" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Deployment completed successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
