#!/usr/bin/env bash
uvicorn token_api:app --port 8000 &
python main.py &
python -m http.server --directory frontend 5500 &
wait

