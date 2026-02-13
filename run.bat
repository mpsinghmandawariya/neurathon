@echo off
echo.
echo ============================================================
echo BHARAT BIZ-AGENT - Voice-First Billing System
echo ============================================================
echo Bridging the Digital Divide with Autonomous AI Operations
echo.
echo Status: Starting your AI billing co-pilot...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Navigate to backend
cd /d "%~dp0backend"
if errorlevel 1 (
    echo ERROR: Could not change to backend directory
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Installing/updating dependencies...
echo ============================================================
python -m pip install --upgrade pip -q
python -m pip install --upgrade -q -r ..\requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.

REM Initialize database
echo ============================================================
echo Initializing database...
echo ============================================================
python -c "from db import init_db; init_db(); print('[OK] Database initialized')"

if errorlevel 1 (
    echo Warning: Database initialization had an issue, but continuing...
)

echo.
echo ============================================================
echo STARTING SERVER
echo ============================================================
echo.
echo [OK] Server starting on http://localhost:8000
echo [OK] Frontend: http://localhost:8000
echo [OK] API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.
echo Ready to accept voice commands in Hindi/Hinglish/English
echo [OK] GST Calculation Ready
echo [OK] UPI QR Code Generation Ready
echo [OK] Database Storage Active
echo.
echo ============================================================
echo.

REM Start the server
python -m uvicorn main:app --reload --port 8000 --host 0.0.0.0

if errorlevel 1 (
    echo.
    echo ERROR: Server failed to start
    echo.
    echo Common issues:
    echo - Port 8000 already in use: Change --port 8000 to --port 8001
    echo - Missing dependencies: python -m pip install -r requirements.txt
    echo - Database error: Delete backend/billing.db and try again
    echo.
    pause
    exit /b 1
)
