# FILE-C

A Python/Cython project designed to run on **Termux** (Android Terminal Emulator).

## Project Description

This project contains a compiled Cython module (`tom`) that provides enhanced functionality for Termux environments. The main executable script (`TOM-X`) automatically detects the device architecture and loads the Cython module.

## Files

| File | Description |
|------|-------------|
| `TOM-X` | Main executable Python script |
| `tom.cpython-313-aarch64-linux-android.so` | Compiled Cython module for ARM64 architecture |
| `README.md` | Project documentation |

## System Requirements

- **Device**: 64-bit ARM64 Android device
- **App**: [Termux](https://termux.dev/) (Free Android terminal emulator)
- **Python**: 3.10+
- **Git**: For cloning and version control

## Installation

### Step 1: Open Termux and Update
```bash
apt update && apt upgrade -y
```

### Step 2: Install Required Packages
```bash
pkg install git python python-dev clang -y
```

### Step 3: Clone the Repository
```bash
cd ~
git clone https://github.com/MR-TOM-143/FILE-C.git
cd FILE-C
```

### Step 4: Make TOM-X Executable
```bash
chmod +x TOM-X
```

## Usage

### Run the Main Script
```bash
python TOM-X
```

Or with absolute path:
```bash
python ~/FILE-C/TOM-X
```

Or run directly:
```bash
./TOM-X
```

### What TOM-X Does

1. ✓ Detects system architecture (64-bit or 32-bit)
2. ✓ Auto-updates git repository
3. ✓ Makes all files executable
4. ✓ Imports the `tom` Cython module
5. ✓ Executes `tom.main()` function
6. ✓ Auto-installs dependencies if needed

## Features

- **Auto-Update**: Automatically pulls latest changes from Git
- **Architecture Detection**: Only runs on 64-bit ARM64 devices
- **Compiled Cython Module**: High-performance compiled Python code
- **Self-Configuring**: Automatically installs missing dependencies

## Architecture Support

| Architecture | Status |
|-------------|--------|
| ARM64 (64-bit) | ✅ Supported |
| ARM32 (32-bit) | ❌ Not Supported |
| x86/x64 | ❌ Not Supported |

## Error Handling

If you encounter import errors:

```bash
# Option 1: Reinstall Python
pkg install python -y
python TOM-X

# Option 2: Update packages
pkg update -y && pkg upgrade -y
python TOM-X

# Option 3: Check permissions
chmod +x TOM-X
chmod 777 *
python TOM-X
```

## Troubleshooting

### Error: "TOOL NOT AVAILABLE FOR 32 BIT DEVICE"
- Your device uses 32-bit architecture
- This tool only works on 64-bit ARM64 Android devices

### Error: "ModuleNotFoundError: No module named 'tom'"
```bash
# Reinstall dependencies
pkg install python -y
cd ~/FILE-C
python TOM-X
```

### Permission Denied
```bash
chmod +x TOM-X
python TOM-X
```

## Quick Start Command

```bash
git clone https://github.com/MR-TOM-143/FILE-C.git && cd FILE-C && chmod +x TOM-X && python TOM-X
```

## Development

To modify or recompile the Cython module:
- Source files needed: `tom.pyx` and `setup.py`
- Requires: Cython compiler and build tools
- Command: `python setup.py build_ext --inplace`

## Author

**MR-TOM-143** - [GitHub Profile](https://github.com/MR-TOM-143)

## License

Not specified - Use at your own risk

## Support

For issues or questions:
1. Check Termux documentation: https://termux.dev/
2. Verify device is 64-bit ARM64
3. Ensure all packages are updated
4. Check GitHub issues in this repository

---

**Last Updated**: 2026-05-04
