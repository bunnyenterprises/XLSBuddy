@echo off
title XLSBuddy Launcher
echo ========================================
echo   Starting XLSBuddy
echo ========================================

:: Step 1 - Start MongoDB if not running
echo [1/3] Checking MongoDB...
sc query MongoDB | find "RUNNING" >nul
if errorlevel 1 (
    echo     Starting MongoDB service...
    net start MongoDB
    timeout /t 3 /nobreak >nul
) else (
    echo     MongoDB already running.
)

:: Step 2 - Start Backend
echo [2/3] Starting Backend on port 8001...
start "XLSBuddy Backend" cmd /k "cd /d D:\xlsbuddy\backend && python -m uvicorn server:app --reload --host 0.0.0.0 --port 8001"
timeout /t 4 /nobreak >nul

:: Step 3 - Start Frontend
echo [3/3] Starting Frontend on port 3000...
start "XLSBuddy Frontend" cmd /k "cd /d D:\xlsbuddy\frontend && yarn start"

echo ========================================
echo   Done! Open http://localhost:3000
echo ========================================
pause
