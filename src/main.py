
from agent.ops_decision_agent import OpsDecisionAgent

def run_demo():
    agent = OpsDecisionAgent()

    scenario = {
        "incident_type": "order_delay",
        "delay_minutes": 25,
        "sla_threshold": 30,
        "courier_available": False,
        "priority_order": True
    }

    result = agent.analyze(scenario)

    print("\n=== OpsDecisionAgent Result ===")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run_demo()
