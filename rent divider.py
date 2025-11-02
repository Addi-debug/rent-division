rent = float(input("Enter your hostel rent: "))
food = float(input("Enter the amount spent on food: "))
electricity_spend = float(input("Enter electricity units used: "))
unit = float(input("Charge per unit: "))
persons = int(input("Enter the number of people: "))

total_electricity = electricity_spend * unit
total_bill = rent + food + total_electricity
per_person = total_bill / persons

print("Total bill per person is:", per_person)
