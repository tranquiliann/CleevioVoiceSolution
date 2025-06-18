import os
from fastapi import FastAPI, HTTPException
from livekit import api as lk_api

app = FastAPI()

API_KEY = os.getenv("LIVEKIT_API_KEY")
API_SECRET = os.getenv("LIVEKIT_API_SECRET")

@app.get("/token")
async def get_token(room: str, identity: str):
    if not API_KEY or not API_SECRET:
        raise HTTPException(status_code=500, detail="Missing LiveKit credentials")
    token = lk_api.AccessToken(API_KEY, API_SECRET, identity=identity)
    token.add_grant(lk_api.VideoGrant(room=room))
    token.ttl = 3600
    return {"token": token.to_jwt()}

