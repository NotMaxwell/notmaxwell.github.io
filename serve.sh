#!/bin/bash
# Quick script to start a local web server for testing

cd "$(dirname "$0")" || exit 1

if [ "$1" == "--port" ]; then
    python3 serve.py --port "$2"
else
    python3 serve.py
fi
