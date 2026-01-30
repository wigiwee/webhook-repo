from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    action_type: str
    author: str
    from_branch: Optional[str] = None
    to_branch: str
    timestamp: datetime
    message: str
