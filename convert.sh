#!/bin/bash
# Quick script to convert markdown posts to HTML

cd "$(dirname "$0")" || exit 1

if ! command -v pandoc &> /dev/null; then
    echo "ERROR: pandoc not found. Install with:"
    echo "  brew install pandoc"
    exit 1
fi

if [ "$1" == "--watch" ]; then
    echo "Watching for markdown changes..."
    python3 convert.py --watch
else
    python3 convert.py
fi
