from datetime import datetime

def format_message(e: dict) -> str:
    """
    Formats an event dictionary into a human-readable message.
    Assumes timestamp is an ISO-8601 string in UTC (Z).
    """

    ts = datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00"))
    formatted_time = ts.strftime("%d %B %Y - %I:%M %p")

    action = e.get("action")

    if action == "PUSH":
        return (
            f'{e["author"]} pushed to {e["to_branch"]} '
            f'on {formatted_time}'
        )

    if action == "PULL_REQUEST":
        return (
            f'{e["author"]} submitted a pull request '
            f'from {e["from_branch"]} to {e["to_branch"]} '
            f'on {formatted_time}'
        )

    if action == "MERGE":
        return (
            f'{e["author"]} merged branch '
            f'{e["from_branch"]} to {e["to_branch"]} '
            f'on {formatted_time}'
        )

    return "Unknown event"
