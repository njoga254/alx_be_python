Task = input("Enter your task: ")
Priority = input("Choose priority (high/medium/low): ")
Time_Bound = input("Is it time bound? (yes/no): ")

print("Reminder: This is your task.")
#matchcase
match Priority:
    case "high":
        reminder = f"Reminder: '{Task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{Task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{Task}' is a low priority task."
    case _:
        reminder = "Wrong input for priority level. Please choose high, medium or low."

#modify reminder
if Time_Bound == "yes":
    reminder += "Don't forget it is time sensitive."
else:
    Time_Bound == "no"
    reminder += "Not urgent."


print(reminder)