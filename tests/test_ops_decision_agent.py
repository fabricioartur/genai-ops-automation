from src.agent.ops_decision_agent import OpsDecisionAgent
from src.models.scenarios import (
    sample_order_delay_high_risk,
    sample_order_delay_low_risk
)


def test_high_risk_order_delay():
    agent = OpsDecisionAgent()
    scenario = sample_order_delay_high_risk()

    result = agent.analyze(scenario)

    assert result["incident_type"] == "Order Delay"
    assert result["risk_level"] == "High"
    assert "Escalate" in result["recommended_action"]


def test_low_risk_order_delay():
    agent = OpsDecisionAgent()
    scenario = sample_order_delay_low_risk()

    result = agent.analyze(scenario)

    assert result["risk_level"] == "Low"
    assert result["recommended_action"] == "Monitor"
