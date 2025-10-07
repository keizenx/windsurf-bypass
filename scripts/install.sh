#!/bin/bash
# Windsurf Free VIP - Linux/macOS Installation Script
# Bash installation script for Linux and macOS

echo "========================================"
echo "    Windsurf Free VIP - Installation"
echo "========================================"
echo ""

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    echo "⚠️  Warning: Running as root is not recommended"
    echo "   Consider running as a regular user"
    echo ""
fi

# Check Python installation
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python is not installed"
        echo "   Please install Python from https://python.org"
        echo "   Or use your package manager:"
        echo "   - Ubuntu/Debian: sudo apt install python3"
        echo "   - CentOS/RHEL: sudo yum install python3"
        echo "   - macOS: brew install python3"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✓ Python detected: $($PYTHON_CMD --version)"

# Create project directory
PROJECT_DIR="$HOME/windsurf-bypass"
mkdir -p "$PROJECT_DIR"
echo "✓ Project directory created: $PROJECT_DIR"

# Download main script
MAIN_SCRIPT_URL="https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/windsurf_bypass.py"
MAIN_SCRIPT_PATH="$PROJECT_DIR/windsurf_bypass.py"

if curl -fsSL "$MAIN_SCRIPT_URL" -o "$MAIN_SCRIPT_PATH"; then
    echo "✓ Main script downloaded"
else
    echo "❌ Failed to download main script"
    echo "   Please check your internet connection"
    exit 1
fi

# Download bash runner
RUNNER_URL="https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/scripts/run_bypass.sh"
RUNNER_PATH="$PROJECT_DIR/run_bypass.sh"

if curl -fsSL "$RUNNER_URL" -o "$RUNNER_PATH"; then
    chmod +x "$RUNNER_PATH"
    echo "✓ Bash runner downloaded and made executable"
else
    echo "⚠️  Failed to download bash runner, but main script is ready"
fi

# Download config
CONFIG_URL="https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/config.json"
CONFIG_PATH="$PROJECT_DIR/config.json"

if curl -fsSL "$CONFIG_URL" -o "$CONFIG_PATH"; then
    echo "✓ Configuration downloaded"
else
    echo "⚠️  Configuration download failed, using defaults"
fi

# Test the installation
echo ""
echo "🧪 Testing installation..."
cd "$PROJECT_DIR"

if $PYTHON_CMD windsurf_bypass.py --test 2>/dev/null; then
    echo "✓ Installation test successful"
else
    echo "⚠️  Installation test failed, but script is ready"
fi

echo ""
echo "========================================"
echo "    Installation completed successfully!"
echo "========================================"
echo ""
echo "To use Windsurf Free VIP:"
echo "1. Navigate to: $PROJECT_DIR"
echo "2. Run: ./run_bypass.sh"
echo "3. Or run: $PYTHON_CMD windsurf_bypass.py"
echo ""
echo "For updates, run this script again."
echo ""
read -p "Press Enter to exit"
