from src.engine.decision_rules import order_delay_rule
from src.models.enums import IncidentType


class OpsDecisionAgent:
    """
    Decision-oriented agent for operational workflows in food delivery platforms.

    This agent orchestrates decision-making by:
    - Validating input scenarios
    - Routing scenarios to the appropriate decision rules
    - Returning structured, explainable recommendations

    The decision logic itself lives in the engine layer.
    """

    def analyze(self, scenario: dict) -> dict:
        """
        Analyze an operational scenario and return a decision recommendation.

        :param scenario: Dictionary containing operational inputs
        :return: Dictionary with incident classification and recommendations
        """

        self._validate_input(scenario)

        incident_type = scenario.get("incident_type")

        if incident_type == IncidentType.ORDER_DELAY:
            return order_delay_rule(scenario)

        return self._default_response(incident_type)

    def _default_response(self, incident_type: str) -> dict:
        """
        Fallback response for unsupported or unknown incident types.
        """
        return {
            "incident_type": incident_type or "unknown",
            "risk_level": "Low",
            "recommended_action": "Monitor",
            "notes": "No predefined decision rules for this incident type"
        }

    @staticmethod
    def _validate_input(scenario: dict):
        if not isinstance(scenario, dict):
            raise ValueError("Scenario must be a dictionary")
