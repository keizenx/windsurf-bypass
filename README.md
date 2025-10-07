# Windsurf Free VIP

**Release License: CC BY-NC-ND 4.0** | **Stars** | **Downloads** | **Buy Me a Coffee** | **Ask DeepWiki.com**

![Windsurf Free VIP](https://img.shields.io/badge/Windsurf-Free%20VIP-blue?style=for-the-badge&logo=github)

> **Support Latest Windsurf Version**

This tool is for educational purposes, currently the repo does not violate any laws. Please support the original project. This tool will not generate any fake email accounts and OAuth access.

Supports Windows, macOS and Linux.

For optimal performance, run with privileges and always stay up to date.

## Features

- **Multi-platform Support** - Windows, macOS and Linux systems
- **Reset Windsurf's configuration** - Generate new system identities
- **Multi-language support** - English, Vietnamese
- **Random UUID Generation** - Unique machine ID generation
- **MAC Address Spoofing** - Random valid MAC address generation
- **Registry Bypass** - Windows registry modification
- **Device ID Creation** - Unique device identifier generation
- **System Info Spoofing** - Complete system information generation

## System Support

| Operating System | Architecture | Supported |
|------------------|---------------|-----------|
| Windows | x64, x86 | Yes |
| macOS | Intel, Apple Silicon | Yes |
| Linux | x64, x86, ARM64 | Yes |

## How to use

### Auto Run Script

**Windows:**
```powershell
# Method 1: Direct download and run
irm https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/install_github.ps1 | iex

# Method 2: Manual download
# Download windsurf_bypass.py from GitHub and run:
python windsurf_bypass.py
```

**Linux/macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/keizenx/windsurf-bypass/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

**Direct Python execution:**
```bash
python windsurf_bypass.py
```

> **Note**
> 
> If you want to stop the script, please press Ctrl+C

## How it works

The tool automatically generates:

1. **Machine ID** - Unique UUID for machine identification
2. **MAC Address** - Random valid MAC address
3. **Device ID** - Unique device identifier
4. **Registry Data** - Modified Windows registry data
5. **System Info** - Complete system information

## Project Files

- `windsurf_bypass.py` - Main bypass script
- `run_bypass.bat` - Windows Batch execution script
- `run_bypass.ps1` - Windows PowerShell execution script
- `config.json` - Tool configuration
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

### Generated Files
- `windsurf_identity.json` - Contains all generated identity data

## Important Notes

- **Administrator privileges** - Required for Windows registry modification
- **System restart** - May be required for changes to take effect
- **Backup** - Identity is saved for future reference

## Security

- All generated data is random and unique
- No personal data is collected
- Tool operates locally only

## Repeated Usage

To generate a new identity:
1. Re-run the script
2. A new identity will be generated automatically
3. Previous identity will be replaced

## Support

If you encounter issues:
1. Verify Python is installed
2. Run as administrator
3. Check Windows registry permissions

## Contributing

We welcome contributions! Feel free to:
- Fork the repository
- Create feature branches
- Submit pull requests
- Report issues

## License

This project is licensed under the CC BY-NC-ND 4.0 License - see the [LICENSE](LICENSE) file for details.

---
**Disclaimer**: This tool is intended for educational and testing purposes only. Please use responsibly and in accordance with applicable laws and terms of service.