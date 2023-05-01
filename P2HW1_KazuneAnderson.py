#Calculates and Displays travel expenses
#Feb27,2023
#CTI-110P2HW2 - Travel
#Anderson_Kazune

print("This program calculates and displays travel expenses ")
print()
#Ask user to enter their budget
badget = int(input("Please Enter your badget: "))
print()
#Ask user to enter travel destination
destination = (input("Please Enter your travel destination: "))
print()
#Ask user for amount they will spend on gas
gas = int(input("How much do you think you will spend on gas? "))
print()
#Ask user for amount they will spend on accommodation
hotel = int(input("Approximately,how much will you need for accommodation/hotel? "))
print()
#Ask user for amount they will spend on food
food = int(input("Lastly, how much do you need for food?"))
print()

#Add expenses AND Subtract expenses from budget
totalAdd = int( gas + hotel + food )
remaining = int( badget - totalAdd )

#Display results
print("----------Travel Expenses----------")
print("Location:" + "            " + destination)
print(f'Initial Budget:      ${badget:.1f}')
print(f'Fuel:                ${gas:.1f}')
print(f'Accomodation:        ${hotel:.1f}')
print(f'Food:                ${food:.1f}')
print("-----------------------------------")
print()
print(f'Remaining Balance:   ${remaining:.1f}')
