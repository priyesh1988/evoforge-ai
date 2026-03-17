from fastapi.testclient import TestClient

from app.main import app
from app.services.ingest import reset_events
from app.services.proposals import reset_proposals

client = TestClient(app)


def setup_function():
    reset_events()
    reset_proposals()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["ok"] is True


def test_full_flow():
    payload = {
        "events": [
            {
                "user_id": "u1",
                "segment": "new_user",
                "screen": "settings",
                "event_type": "submit",
                "feature": "configuration",
                "duration_seconds": 440,
                "success": False,
                "frustration_score": 0.85,
                "support_ticket": True,
            },
            {
                "user_id": "u2",
                "segment": "new_user",
                "screen": "settings",
                "event_type": "abandon",
                "feature": "configuration",
                "duration_seconds": 230,
                "success": False,
                "frustration_score": 0.91,
                "support_ticket": True,
            },
            {
                "user_id": "u3",
                "segment": "admin",
                "screen": "settings",
                "event_type": "submit",
                "feature": "configuration",
                "duration_seconds": 360,
                "success": True,
                "frustration_score": 0.42,
                "support_ticket": False,
            }
        ]
    }

    ingest = client.post("/v1/ingest/events", json=payload)
    assert ingest.status_code == 200
    assert ingest.json()["ingested"] == 3

    opps = client.get("/v1/opportunities")
    assert opps.status_code == 200
    assert len(opps.json()) >= 1

    proposals = client.post("/v1/proposals/generate")
    assert proposals.status_code == 200
    proposal_id = proposals.json()[0]["proposal_id"]

    sim = client.post(
        "/v1/simulate",
        json={
            "proposal_id": proposal_id,
            "version_name": "settings-v2",
            "changes": ["guided_setup", "progressive_disclosure", "contextual_help"],
        },
    )
    assert sim.status_code == 200
    assert sim.json()["proposal_id"] == proposal_id

    compare = client.get(f"/v1/compare/{proposal_id}")
    assert compare.status_code == 200
    assert compare.json()["proposal_id"] == proposal_id
