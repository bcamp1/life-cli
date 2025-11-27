#!/bin/bash
# Setup script for life - terminal life board visualization

echo "Setting up life..."
echo ""

# Create a symlink in ~/.local/bin or /usr/local/bin
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/life.py"

# Try to create in ~/.local/bin first
if [ -d "$HOME/.local/bin" ]; then
    ln -sf "$SCRIPT_PATH" "$HOME/.local/bin/life"
    echo "✓ Created symlink: $HOME/.local/bin/life"
    echo ""
    if [[ ":$PATH:" == *":$HOME/.local/bin:"* ]]; then
        echo "✓ $HOME/.local/bin is in your PATH"
    else
        echo "⚠ Add $HOME/.local/bin to your PATH to use 'life' command"
        echo "  Add this to your ~/.bashrc or ~/.zshrc:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    fi
elif command -v sudo &> /dev/null; then
    sudo ln -sf "$SCRIPT_PATH" /usr/local/bin/life
    echo "✓ Created symlink: /usr/local/bin/life (requires sudo)"
else
    echo "✗ Could not create symlink automatically"
    echo ""
    echo "Please manually create a symlink:"
    echo "  ln -s $SCRIPT_PATH ~/.local/bin/life"
    echo ""
    exit 1
fi

echo ""
echo "✓ Life board has been installed!"
echo ""
echo "Get started with:"
echo "  life          # Display your life board"
echo ""
