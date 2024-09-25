task = input("Add a task description: ")
priority = input("Choose the priority level (high, medium,low): ")
time_bound = input("Is the task time sensitive(yes/no): ")

#Process the Task Based on Priority and Time Sensitivity
reminder = f"Attention! {task} is a {priority} level."

#match case
match priority:
    case "high":
        print("Attention!This should be done first.")
    case "medium":
        print("Attention!Could be done on lunch recess")
    case "low":
        print("Attention!After work activity.")
    case _:
        print("Wrong input.")

#modify reminder
if time_bound == "yes":
    print("Don't forget it is time sensitive.")

print(reminder)
    
        