from __future__ import annotations

from typing import List
from app.models import Event

EVENT_STORE: List[Event] = []


def ingest_events(events: List[Event]) -> int:
    EVENT_STORE.extend(events)
    return len(EVENT_STORE)


def get_events() -> List[Event]:
    return EVENT_STORE


def reset_events() -> None:
    EVENT_STORE.clear()
