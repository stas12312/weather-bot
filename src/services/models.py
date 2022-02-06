import datetime
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime.datetime
