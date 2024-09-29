from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    print("Current Date and Time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        number_of_days = int(input("Enter number of days to add to current date: "))
        current_date = datetime.now()
        #Future date
        future_date = current_date + timedelta(days=number_of_days)

        print("Future Date: ", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input! Enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

