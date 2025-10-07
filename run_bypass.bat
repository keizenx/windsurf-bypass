@echo off
echo ========================================
echo    Windsurf Bypass Tool
echo ========================================
echo.

REM Vérification de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé ou pas dans le PATH
    echo    Veuillez installer Python depuis https://python.org
    pause
    exit /b 1
)

echo ✓ Python détecté
echo.

REM Exécution du script avec les droits administrateur
echo 🔧 Exécution du bypass Windsurf...
echo.

python windsurf_bypass.py

echo.
echo ========================================
echo    Bypass terminé
echo ========================================
pause
