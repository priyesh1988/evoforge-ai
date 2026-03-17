from __future__ import annotations

from app.models import Proposal, SimulationResponse


def simulate_future_version(proposal: Proposal, version_name: str, changes: list[str]) -> SimulationResponse:
    change_bonus = min(0.2, 0.03 * len(changes))
    before = proposal.before
    after = dict(proposal.after)
    after["abandonment_rate"] = round(max(0.0, after["abandonment_rate"] - change_bonus / 2), 3)
    after["ticket_rate"] = round(max(0.0, after["ticket_rate"] - change_bonus / 3), 3)
    after["pain_score"] = round(max(0.0, after["pain_score"] - change_bonus / 2), 3)

    delta = {
        key: round(after[key] - before[key], 3)
        for key in before
    }
    notes = [
        f"Simulation applied {len(changes)} modeled change(s).",
        "Projected impact is directional and should be validated with experiment or rollout telemetry.",
    ]
    return SimulationResponse(
        proposal_id=proposal.proposal_id,
        version_name=version_name,
        before=before,
        after=after,
        delta=delta,
        confidence=max(0.5, round(proposal.confidence - 0.03, 2)),
        notes=notes,
    )
