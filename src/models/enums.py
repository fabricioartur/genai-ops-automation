from enum import Enum


class IncidentType(str, Enum):
    ORDER_DELAY = "order_delay"
    COURIER_SHORTAGE = "courier_shortage"


class RiskLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class RecommendedAction(str, Enum):
    MONITOR = "Monitor"
    ESCALATE = "Escalate to regional ops team"
    PROACTIVE_MONITOR = "Proactively monitor"
