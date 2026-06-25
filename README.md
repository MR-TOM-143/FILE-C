A Python/Cython project designed to run on **Termux** (Android Terminal Emulator).


## System Requirements

- **Device**: 64-bit ARM64 Android device
- **App**: [Termux](https://termux.dev/) (Free Android terminal emulator)
- **Python**: 3.10+
- **Git**: For cloning and version control

## Installation

### Step 3: Clone the Repository
```bash
cd ~
git clone https://github.com/MR-TOM-143/FILE-C.git
cd FILE-C
chmod +x tom.py
python tom.py
```

### What TOM-X Does

1. ✓ Detects system architecture (64-bit or 32-bit)
2. ✓ Auto-updates git repository

## Features

- **Auto-Update**: Automatically pulls latest changes from Git
- **Architecture Detection**: Only runs on 64-bit ARM64 devices

## Architecture Support

| Architecture | Status |
|-------------|--------|
| ARM64 (64-bit) | ✅ Supported |
| ARM32 (32-bit) | ❌ Not Supported |
| x86/x64 | ❌ Not Supported |
2. Verify device is 64-bit ARM64
3. Ensure all packages are updated
4. Check GitHub issues in this repository

---

**Last Updated**: 25-JUNE-2026
