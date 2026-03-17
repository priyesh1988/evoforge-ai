from __future__ import annotations

from fastapi import APIRouter, HTTPException
from app.models import EventBatch, SimulationRequest, CompareResponse
from app.services.ingest import ingest_events, get_events
from app.services.learner import discover_opportunities
from app.services.proposals import generate_proposals, get_proposal
from app.services.simulator import simulate_future_version

router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {"ok": True, "service": "evoforge-ai"}


@router.post("/v1/ingest/events")
def ingest(batch: EventBatch) -> dict:
    total = ingest_events(batch.events)
    return {"ingested": len(batch.events), "store_size": total}


@router.get("/v1/opportunities")
def opportunities() -> list:
    return discover_opportunities(get_events())


@router.post("/v1/proposals/generate")
def proposals() -> list:
    opps = discover_opportunities(get_events())
    return generate_proposals(opps, get_events())


@router.post("/v1/simulate")
def simulate(req: SimulationRequest):
    proposal = get_proposal(req.proposal_id)
    if not proposal:
        raise HTTPException(status_code=404, detail="proposal not found")
    return simulate_future_version(proposal, req.version_name, req.changes)


@router.get("/v1/compare/{proposal_id}", response_model=CompareResponse)
def compare(proposal_id: str):
    proposal = get_proposal(proposal_id)
    if not proposal:
        raise HTTPException(status_code=404, detail="proposal not found")
    return CompareResponse(
        proposal_id=proposal.proposal_id,
        title=proposal.title,
        before=proposal.before,
        after=proposal.after,
        narrative=(
            f"Before the enhancement, {proposal.feature} on {proposal.screen} shows higher friction. "
            f"After the proposed version, the model projects a lower pain score and better user flow."
        ),
        risks=proposal.risks,
    )
