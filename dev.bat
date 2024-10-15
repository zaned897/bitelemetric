@echo off
cd /d %~dp0
if not exist static mkdir static
start "FastAPI" cmd /k "uvicorn main:app --reload --reload-include='*.html' --reload-include='*.css' --reload-include='*.js' --port 8080"
timeout /t 5 >nul
start "Browser-Sync" cmd /k "browser-sync start --proxy 'http://localhost:8080' --files '**/*.html' '**/*.css' '**/*.js' --no-notify"
