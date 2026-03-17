from __future__ import annotations

from collections import defaultdict
from typing import List
from app.models import Event, Opportunity


def discover_opportunities(events: List[Event]) -> List[Opportunity]:
    grouped = defaultdict(list)
    for event in events:
        grouped[(event.feature, event.screen)].append(event)

    opportunities: List[Opportunity] = []
    idx = 1
    for (feature, screen), rows in grouped.items():
        total = len(rows)
        if total == 0:
            continue
        failures = sum(1 for r in rows if not r.success)
        avg_frustration = sum(r.frustration_score for r in rows) / total
        tickets = sum(1 for r in rows if r.support_ticket)
        abandonment_rate = failures / total
        ticket_rate = tickets / total
        pain_score = round((abandonment_rate * 0.5) + (avg_frustration * 0.35) + (ticket_rate * 0.15), 3)

        if pain_score < 0.18:
            continue

        if abandonment_rate > 0.25:
            hint = "reduce steps and simplify the decision path"
        elif ticket_rate > 0.15:
            hint = "add contextual guidance and self-serve clarity"
        else:
            hint = "improve discoverability and workflow efficiency"

        opportunities.append(
            Opportunity(
                opportunity_id=f"opp-{idx:03d}",
                feature=feature,
                screen=screen,
                pain_score=pain_score,
                abandonment_rate=round(abandonment_rate, 3),
                ticket_rate=round(ticket_rate, 3),
                recommendation_hint=hint,
            )
        )
        idx += 1

    return sorted(opportunities, key=lambda o: o.pain_score, reverse=True)
