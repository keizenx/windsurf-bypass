#!/bin/bash
# Windsurf Free VIP - Linux/macOS Runner Script
# Bash runner script for Linux and macOS

echo "========================================"
echo "    Windsurf Free VIP"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python is not installed or not in PATH"
        echo "   Please install Python from https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✓ Python detected: $($PYTHON_CMD --version)"
echo ""

# Check if main script exists
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_SCRIPT="$SCRIPT_DIR/windsurf_bypass.py"

if [[ ! -f "$MAIN_SCRIPT" ]]; then
    echo "❌ Main script not found: $MAIN_SCRIPT"
    echo "   Please run the installation script first"
    exit 1
fi

echo "🔧 Running Windsurf Free VIP..."
echo ""

# Run the main script
$PYTHON_CMD "$MAIN_SCRIPT"

echo ""
echo "========================================"
echo "    Bypass completed"
echo "========================================"
echo ""
read -p "Press Enter to exit"
