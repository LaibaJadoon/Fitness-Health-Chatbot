from pydantic_ai import Agent
from tools import calculate_bmi, step_goal_suggestion, nutrition_suggestion

# Create the agent
agent = Agent(
    model="openai:gpt-4.1-mini",
    system_prompt=(
        "You are a helpful and smart health assistant. "
        "You help users with fitness, BMI, steps, and nutrition advice. "
        "Use tools whenever needed to give accurate answers. "
        "If the user provides weight and height, calculate BMI. "
        "If the user asks about steps, use the step goal tool. "
        "If the user asks about diet or food, use the nutrition tool."
    ),
     tools=[
        calculate_bmi,
        step_goal_suggestion,
        nutrition_suggestion,
    ],
)

