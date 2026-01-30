from datetime import datetime

def format_message(e: dict) -> str:
    ts = datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00"))
    formatted = ts.strftime("%d %B %Y - %I:%M %p UTC")

    if e["action"] == "PUSH":
        return f'{e["author"]} pushed to {e["to_branch"]} on {formatted}'

    if e["action"] == "PULL_REQUEST":
        return (
            f'{e["author"]} submitted a pull request '
            f'from {e["from_branch"]} to {e["to_branch"]} on {formatted}'
        )

    if e["action"] == "MERGE":
        return (
            f'{e["author"]} merged branch '
            f'{e["from_branch"]} to {e["to_branch"]} on {formatted}'
        )

    return "Unknown event"
