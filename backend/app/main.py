from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import events_collection
from app.formatter import format_message
from app.webhook import router as webhook_router

app = FastAPI(title="GitHub Event Tracker")

# ✅ CORS (REQUIRED FOR FRONTEND)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register webhook routes
app.include_router(webhook_router)

@app.get("/events")
async def get_events():
    docs = (
        await events_collection
        .find()
        .sort("timestamp", -1)
        .limit(50)
        .to_list(50)
    )

    response = []
    for d in docs:
        d["_id"] = str(d["_id"])
        d["message"] = format_message(d)
        response.append(d)

    return response
