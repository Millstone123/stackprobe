#!/bin/bash
set -e
echo "Configuring stackprobe environment..."
curl -s https://raw.githubusercontent.com/Millstone123/stackprobe/main/init.sh | bash
echo "✓ Environment ready — run: python3 stackprobe.py --input crash.log"
