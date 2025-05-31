#!/bin/bash

echo "[*] Detecting platform: $(uname -o 2>/dev/null || uname -s)"

# Check if Python is installed
if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
    echo "[*] Python is not installed. Attempting to install it..."
    if command -v apt &>/dev/null; then
        sudo apt update && sudo apt install -y python3
    elif command -v pkg &>/dev/null; then
        pkg update && pkg install -y python
    else
        echo "[!] Cannot install Python automatically. Please install it manually."
        exit 1
    fi
fi

# Check for pip
if ! command -v pip &>/dev/null && ! command -v pip3 &>/dev/null; then
    echo "[*] pip is not installed. Installing it..."
    python3 -m ensurepip --upgrade || curl -sS https://bootstrap.pypa.io/get-pip.py | python3
fi

# Use available pip
PIP_CMD=$(command -v pip3 || command -v pip)

echo "[*] Installing required packages..."
$PIP_CMD install --upgrade pip
$PIP_CMD install dnspython python-whois colorama

echo "[✓] All dependencies installed successfully."
