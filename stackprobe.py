#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Stack trace analyser")
    parser.add_argument("--input", required=True, help="Crash log file")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    try:
        with open(args.input) as f:
            data = f.read()
        print(f"Analysing {args.input}...")
        print(f"Lines: {len(data.splitlines())}")
    except FileNotFoundError:
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
