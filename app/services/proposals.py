from __future__ import annotations

from typing import List
from app.models import Opportunity, Proposal, Event

PROPOSAL_STORE: dict[str, Proposal] = {}


def _segments_for(feature: str, screen: str, events: List[Event]) -> List[str]:
    segments = sorted({e.segment for e in events if e.feature == feature and e.screen == screen})
    return segments or ["general"]


def generate_proposals(opportunities: List[Opportunity], events: List[Event]) -> List[Proposal]:
    results: List[Proposal] = []
    for idx, opp in enumerate(opportunities, start=1):
        before = {
            "abandonment_rate": opp.abandonment_rate,
            "ticket_rate": opp.ticket_rate,
            "pain_score": opp.pain_score,
        }
        uplift_factor = max(0.08, min(0.45, opp.pain_score * 0.8))
        after = {
            "abandonment_rate": round(max(0.0, opp.abandonment_rate * (1 - uplift_factor)), 3),
            "ticket_rate": round(max(0.0, opp.ticket_rate * (1 - uplift_factor * 0.7)), 3),
            "pain_score": round(max(0.0, opp.pain_score * (1 - uplift_factor)), 3),
        }
        proposal = Proposal(
            proposal_id=f"prop-{idx:03d}",
            title=f"Enhance {opp.feature} on {opp.screen}",
            feature=opp.feature,
            screen=opp.screen,
            summary=f"AI recommends improving {opp.feature} on {opp.screen} to address observed friction and support burden.",
            changes=[
                "guided_setup",
                "progressive_disclosure",
                "contextual_help",
            ],
            confidence=round(min(0.93, 0.55 + opp.pain_score), 2),
            impacted_segments=_segments_for(opp.feature, opp.screen, events),
            before=before,
            after=after,
            risks=[
                "segment-specific regression is possible",
                "simulated effect depends on representative telemetry",
            ],
        )
        PROPOSAL_STORE[proposal.proposal_id] = proposal
        results.append(proposal)
    return results


def get_proposal(proposal_id: str) -> Proposal | None:
    return PROPOSAL_STORE.get(proposal_id)


def reset_proposals() -> None:
    PROPOSAL_STORE.clear()
