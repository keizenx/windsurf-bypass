# Windsurf Bypass Tool - PowerShell Script
# Exécute le bypass avec les droits administrateur

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Windsurf Bypass Tool" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Vérification des droits administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

if (-not $isAdmin) {
    Write-Host "⚠️  Attention: Ce script fonctionne mieux avec les droits administrateur" -ForegroundColor Yellow
    Write-Host "   Certaines modifications du registre peuvent échouer" -ForegroundColor Yellow
    Write-Host ""
    
    $response = Read-Host "Voulez-vous continuer quand même? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "❌ Script annulé" -ForegroundColor Red
        exit 1
    }
}

# Vérification de Python
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python non trouvé"
    }
    Write-Host "✓ Python détecté: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python n'est pas installé ou pas dans le PATH" -ForegroundColor Red
    Write-Host "   Veuillez installer Python depuis https://python.org" -ForegroundColor Yellow
    Read-Host "Appuyez sur Entrée pour quitter"
    exit 1
}

Write-Host ""
Write-Host "🔧 Exécution du bypass Windsurf..." -ForegroundColor Cyan
Write-Host ""

# Exécution du script Python
python windsurf_bypass.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    Bypass terminé" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Read-Host "Appuyez sur Entrée pour quitter"
