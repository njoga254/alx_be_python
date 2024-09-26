task = input("Enter your task: ")
priority = input("Choose the priority level (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

print("reminder: This is your task.")
#match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Wrong input for priority level. Please choose high, medium or low."

#modify reminder
if time_bound == "yes":
    reminder += "Don't forget it is time sensitive."
else:
    reminder += "Not urgent."


print(reminder)