# tools.py

from pydantic_ai import Tool


@Tool
def calculate_bmi(weight: float, height: float) -> str:
    """
    Calculate BMI using weight (kg) and height (cm)
    """
    height_in_m = height / 100
    bmi = weight / (height_in_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"Your BMI is {bmi:.2f}, which is considered {category}."


@Tool
def step_goal_suggestion(goal: str, current_steps: int = 0) -> str:
    """
    Suggest daily step goals based on user's fitness goal
    """
    goal = goal.lower()

    if goal == "weight loss":
        target = 10000
    elif goal == "maintain":
        target = 8000
    elif goal == "active":
        target = 12000
    else:
        target = 7000

    remaining = target - current_steps

    if current_steps > 0:
        return f"Your goal is {target} steps per day. You have walked {current_steps} steps, so you need {remaining} more steps."
    else:
        return f"Your recommended daily step goal is {target} steps."


@Tool
def nutrition_suggestion(goal: str) -> str:
    """
    Provide basic diet suggestions based on user's goal
    """
    goal = goal.lower()

    if goal == "weight loss":
        return "Focus on vegetables, fruits, lean protein. Avoid sugar and fried food."
    elif goal == "weight gain":
        return "Eat calorie-dense foods like nuts, dairy, rice, and protein-rich meals."
    elif goal == "healthy":
        return "Maintain a balanced diet with carbs, protein, and healthy fats."
    else:
        return "Try to maintain a balanced diet with whole foods."