print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
# Now that we have the bill amount, we need the user to select the desired tip amount  
percent = input("What precentage tip would you like to give? 10,12, or 15? ")
percent_float = float(percent)/100
# turn the percent into a decimal  
bill_percent = float(bill) * (percent_float)
# Find the percentage of the bill
people = input("how many people are spliting the bill?")
people_int = int(people)
# Convert the string into an integer 
bill_total = float(bill)+(bill_percent)
# add the bill plus tip to find the total 
total_per_person = float( bill_total)/(people_int)
# Divide the total among the number of people eating eqaully 
final_total = round(total_per_person,2)
# Round the number to the nearest hundredth
print(f"Each person should pay ${final_total}")