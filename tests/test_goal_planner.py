import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.tools.goal_planner_tools import calculate_goal_plan

result = calculate_goal_plan.invoke(
    {
        "goal_amount": 10000000,
        "years": 15
    }
)

print(result)