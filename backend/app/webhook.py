from fastapi import APIRouter, Request, Header
from app.database import events_collection

router = APIRouter()

@router.post("/webhook/github")
async def github_webhook(
    request: Request,
    x_github_event: str = Header(None)
):
    payload = await request.json()

    if not x_github_event:
        return {"status": "ignored"}

    # ---------- PUSH ----------
    if x_github_event == "push":
        head_commit = payload.get("head_commit")
        if not head_commit:
            return {"status": "ignored"}

        event = {
            "request_id": head_commit["id"],
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": head_commit["timestamp"]
        }

    # ------ PULL REQUEST ------
    elif x_github_event == "pull_request":
        pr = payload.get("pull_request")
        if not pr:
            return {"status": "ignored"}

        if payload["action"] == "opened":
            event = {
                "request_id": str(pr["id"]),
                "author": pr["user"]["login"],
                "action": "PULL_REQUEST",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["created_at"]
            }

        elif payload["action"] == "closed" and pr.get("merged"):
            event = {
                "request_id": str(pr["id"]),
                "author": pr["merged_by"]["login"],
                "action": "MERGE",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": pr["merged_at"]
            }
        else:
            return {"status": "ignored"}

    else:
        return {"status": "ignored"}

    await events_collection.insert_one(event)
    return {"status": "stored"}
