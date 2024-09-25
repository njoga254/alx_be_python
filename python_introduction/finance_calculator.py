monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
#Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
#Project annual savings
annual_savings = monthly_savings * 12
Projected_Savings = annual_savings + (annual_savings* 0.05)
print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year, with interest, is:", Projected_Savings)
