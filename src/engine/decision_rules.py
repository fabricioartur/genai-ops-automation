"""
Decision rules for OpsDecisionAgent.

This module contains deterministic, explainable rules
used to classify incidents and recommend actions.
"""

def order_delay_rule(scenario: dict) -> dict:
    delay = scenario.get("delay_minutes", 0)
    sla = scenario.get("sla_threshold", 30)

    if delay >= sla - 10:
        return {
            "incident_type": "Order Delay",
            "risk_level": "High",
            "recommended_action": "Escalate to regional ops team",
            "notes": "Risk of SLA breach detected"
        }

    return {
        "incident_type": "Order Delay",
        "risk_level": "Low",
        "recommended_action": "Monitor",
        "notes": "No immediate action required"
    }
