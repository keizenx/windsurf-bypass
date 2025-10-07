#!/bin/bash
# Windsurf Free VIP - GitHub Deployment Script
# Script to prepare and deploy the project to GitHub

echo "========================================"
echo "    Windsurf Free VIP - Deployment"
echo "========================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed"
    echo "   Please install Git from https://git-scm.com"
    exit 1
fi

# Check if we're in a git repository
if [[ ! -d ".git" ]]; then
    echo "🔧 Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
fi

# Add all files
echo "📁 Adding files to Git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "💾 Committing changes..."
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
    echo "✓ Changes committed"
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding remote origin..."
    git remote add origin https://github.com/keizenx/windsurf-bypass.git
    echo "✓ Remote origin added"
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
if git push -u origin main; then
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "Repository URL: https://github.com/keizenx/windsurf-bypass"
    echo ""
    echo "Next steps:"
    echo "1. Visit the repository on GitHub"
    echo "2. Add a description and topics"
    echo "3. Enable GitHub Pages if needed"
    echo "4. Create releases for versioning"
else
    echo "❌ Failed to push to GitHub"
    echo "   Please check your GitHub credentials and repository permissions"
    exit 1
fi

echo ""
echo "========================================"
echo "    Deployment completed successfully!"
echo "========================================"
