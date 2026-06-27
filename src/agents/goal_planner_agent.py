from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

from src.tools.goal_planner_tools import calculate_goal_plan

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

goal_planner_prompt = ChatPromptTemplate.from_messages([

    ("system", """
You are an AI Financial Goal Planning Assistant.

Your job is to help users achieve their financial goals.

When a user asks about:
- monthly SIP
- investment goals
- financial planning
- retirement planning
- wealth creation
- target corpus
- buying a house
- child's education
- goal-based investing

use the calculate_goal_plan tool.

If the user does not specify an expected annual return,
assume the default value provided by the tool.

After receiving the tool result:

- Explain the result in simple English.
- Mention the required monthly SIP.
- Mention the investment duration.
- Mention the expected annual return.
- Mention the target corpus.
- Keep the explanation concise and easy to understand.
"""),

    MessagesPlaceholder(variable_name="messages")

])

goal_planner_agent = goal_planner_prompt | llm.bind_tools(
    [
        calculate_goal_plan
    ]
)