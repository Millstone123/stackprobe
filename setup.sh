#!/bin/bash
set -e

echo "Configuring stackprobe environment..."

python3 --version >/dev/null 2>&1 || { echo "Error: Python 3 required"; exit 1; }



echo "✓ Environment ready — run: python3 stackprobe.py --input crash.log"
