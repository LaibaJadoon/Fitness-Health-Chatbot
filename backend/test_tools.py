# from tools import calculate_bmi, step_goal_suggestion, nutrition_suggestion

# print(calculate_bmi(70, 160))
# print(step_goal_suggestion("weight loss", 4000))
# print(nutrition_suggestion("weight loss"))


from agent import agent

response = agent.run_sync("I weigh 70kg and my height is 160 cm. Am I overweight?")
print(response.output)