"""
Scenario definitions for OpsDecisionAgent.

This module centralizes operational scenarios used for
testing, demos, and future automated evaluations.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderDelayScenario:
    incident_type: str = "order_delay"
    delay_minutes: int = 0
    sla_threshold: int = 30
    courier_available: bool = True
    priority_order: bool = False


@dataclass
class CourierShortageScenario:
    incident_type: str = "courier_shortage"
    available_couriers: int = 0
    active_orders: int = 0
    region: Optional[str] = None


def sample_order_delay_high_risk() -> dict:
    """
    High-risk order delay scenario.
    """
    return OrderDelayScenario(
        delay_minutes=25,
        sla_threshold=30,
        courier_available=False,
        priority_order=True
    ).__dict__


def sample_order_delay_low_risk() -> dict:
    """
    Low-risk order delay scenario.
    """
    return OrderDelayScenario(
        delay_minutes=10,
        sla_threshold=30,
        courier_available=True,
        priority_order=False
    ).__dict__


def sample_courier_shortage() -> dict:
    """
    Courier shortage scenario.
    """
    return CourierShortageScenario(
        available_couriers=2,
        active_orders=15,
        region="Downtown"
    ).__dict__
