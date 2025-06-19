@echo off
set "PYTHONPATH=%CD%"
start /B python -m uvicorn token_api:app --port 8000
start /B python main.py
cd frontend-react && start /B npm run dev 