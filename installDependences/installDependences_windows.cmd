@echo off
echo [*] Checking if Python is installed...
where python >nul 2>&1
if errorlevel 1 (
    echo [!] Python is not installed. Please install it from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [*] Checking if pip is installed...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [*] Pip is not installed. Trying to install it...
    python -m ensurepip --upgrade
    if errorlevel 1 (
        echo [!] Could not install pip. Please install it manually.
        pause
        exit /b 1
    )
)

echo [*] Installing required packages...
python -m pip install --upgrade pip
python -m pip install dnspython python-whois colorama

echo [✓] Installation completed successfully.
pause
