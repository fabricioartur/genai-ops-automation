class OpsDecisionAgent:
    """
    Decision-oriented agent for operational workflows in food delivery platforms.

    This agent analyzes structured operational scenarios and returns
    risk classifications and recommended actions.

    Current implementation uses deterministic logic and mock reasoning,
    without dependency on external AI APIs.
    """

    def analyze(self, scenario: dict) -> dict:
        """
        Analyze an operational scenario and return a decision recommendation.

        :param scenario: Dictionary containing operational inputs
        :return: Dictionary with incident classification and recommendations
        """

        self._validate_input(scenario)

        incident_type = scenario.get("incident_type", "unknown")

        if incident_type == "order_delay":
            return self._handle_order_delay(scenario)

        return self._default_response(incident_type)

    def _handle_order_delay(self, scenario: dict) -> dict:
        delay = scenario.get("delay_minutes", 0)
        priority = scenario.get("priority_order", False)

        if delay >= 20:
            return {
                "incident_type": "Order Delay",
                "risk_level": "High",
                "recommended_action": "Escalate to regional ops team",
                "escalation_guidance": "Notify senior operator",
                "notes": "High risk of SLA breach detected"
            }

        if priority and delay >= 10:
            return {
                "incident_type": "Order Delay",
                "risk_level": "Medium",
                "recommended_action": "Proactively monitor",
                "escalation_guidance": "Prepare escalation if delay increases",
                "notes": "Priority order with growing delay"
            }

        return {
            "incident_type": "Order Delay",
            "risk_level": "Low",
            "recommended_action": "Monitor",
            "escalation_guidance": "None",
            "notes": "Delay within acceptable limits"
        }

    def _default_response(self, incident_type: str) -> dict:
        return {
            "incident_type": incident_type,
            "risk_level": "Low",
            "recommended_action": "Monitor",
            "escalation_guidance": "None",
            "notes": "No predefined risk rules for this incident"
        }

    def _validate_input(self, scenario: dict):
        if not isinstance(scenario, dict):
            raise ValueError("Scenario must be a dictionary")
