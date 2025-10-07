# Windsurf Free VIP - Installation Guide

## Quick Installation

### Windows (PowerShell)

**Method 1: Copy and paste this code in PowerShell:**

```powershell
# Download and run Windsurf Free VIP
$url = "https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/windsurf_bypass.py"
$output = "$env:TEMP\windsurf_bypass.py"
Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing
python $output
```

**Method 2: Manual download**

1. Go to: https://github.com/keizenx/windsurf-bypass
2. Click on `windsurf_bypass.py`
3. Click "Raw" button
4. Save the file as `windsurf_bypass.py`
5. Run: `python windsurf_bypass.py`

### Linux/macOS (Bash)

```bash
# Download and run
curl -L https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/windsurf_bypass.py -o windsurf_bypass.py
python3 windsurf_bypass.py
```

## Requirements

- Python 3.6 or higher
- Internet connection (for download only)
- Administrator/sudo privileges (recommended)

## What it does

1. Generates random UUID for machine ID
2. Creates random MAC address
3. Generates device ID
4. Modifies system identifiers (platform-specific)
5. Saves identity to `windsurf_identity.json`

## Troubleshooting

### If download fails:
- Check your internet connection
- Try downloading manually from GitHub
- Ensure Python is installed and in PATH

### If registry modification fails:
- Run as administrator (Windows)
- Use sudo (Linux/macOS)
- Some changes may require system restart

## Repository

**GitHub**: https://github.com/keizenx/windsurf-bypass

## License

CC BY-NC-ND 4.0 - Educational purposes only
