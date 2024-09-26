task = input("Enter your task: ")
priority = input("Choose priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

print("Reminder: This is your task.")
reminder = f"Reminder: Your task '{task}'."
#matchcase
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
    time_bound == "no"
    reminder += "Not urgent."


print(reminder)