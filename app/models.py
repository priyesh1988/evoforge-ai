from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Event(BaseModel):
    user_id: str
    segment: str
    screen: str
    event_type: str
    feature: str
    duration_seconds: float = 0.0
    success: bool = True
    frustration_score: float = Field(ge=0, le=1, default=0.0)
    support_ticket: bool = False


class EventBatch(BaseModel):
    events: List[Event]


class Opportunity(BaseModel):
    opportunity_id: str
    feature: str
    screen: str
    pain_score: float
    abandonment_rate: float
    ticket_rate: float
    recommendation_hint: str


class Proposal(BaseModel):
    proposal_id: str
    title: str
    feature: str
    screen: str
    summary: str
    changes: List[str]
    confidence: float
    impacted_segments: List[str]
    before: Dict[str, float]
    after: Dict[str, float]
    risks: List[str]


class SimulationRequest(BaseModel):
    proposal_id: str
    version_name: str
    changes: List[str]


class SimulationResponse(BaseModel):
    proposal_id: str
    version_name: str
    before: Dict[str, float]
    after: Dict[str, float]
    delta: Dict[str, float]
    confidence: float
    notes: List[str]


class CompareResponse(BaseModel):
    proposal_id: str
    title: str
    before: Dict[str, float]
    after: Dict[str, float]
    narrative: str
    risks: List[str]
