task = input("Add a task description: ")
priority = input("Choose the priority level (high, medium, low): ")
time_bound = input("Is the task time sensitive (yes/no): ")

#Process the Task Based on Priority and Time Sensitivity
reminder = f"Attention! {task} is a {priority} level task."

#match case
match priority:
    case "high":
        reminder += ("This should be done first.")
    case "medium":
        reminder +=("Could be done on lunch recess")
    case "low":
        reminder +=("After work activity.")
    case _:
        reminder += ("Wrong input for priority level.")

#modify reminder
if time_bound == "yes":
    reminder += ("Don't forget it is time sensitive.")

print(reminder)
    
        