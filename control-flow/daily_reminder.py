task_variable = input("Enter your task: ")
priority_variable = input("Choose the priority level (high/medium/low): ")
time_bound_variable = input("Is it time bound? (yes/no): ")

#Process the Task Based on Priority and Time Sensitivity
reminder = f"Attention! {task_variable} is a {priority_variable} level task."

#match case
match priority_variable:
    case "high":
        reminder += ("This should be done first.")
    case "medium":
        reminder +=("Could be done on lunch recess")
    case "low":
        reminder +=("An after work activity.")
    case _:
        reminder += ("Wrong input for priority level.")

#modify reminder
if time_bound_variable == "yes":
    reminder += ("Don't forget it is time sensitive.")

print(reminder)
    
        