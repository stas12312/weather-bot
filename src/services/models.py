import datetime
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str | None
    username: str | None
    created_at: datetime.datetime


@dataclass
class WeatherWidget:
    widget_id: int
    user_id: int
    name: str
    timezone_offset: int
    latitude: float
    longitude: float
    city_name: str | None
    settings: dict
    is_default: bool
