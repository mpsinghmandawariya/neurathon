@echo off
REM Quick start script - same as run.bat
call run.bat
echo ========================================
echo Bharat Biz-Agent - Starting Server
echo ========================================
echo.

cd backend

echo Checking database...
python -c "from db import init_db; init_db(); print('Database ready')"

echo.
echo Starting FastAPI server on http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn main:app --reload --port 8000
