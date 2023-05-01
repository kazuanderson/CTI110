#Feb16,2023
#CTI-110P1HW1_Lab_ Basic Output With Variable
#Anderson_Kazune

# Output the user's input
userNum1 = int(input("Please Enter integer:\n "))
print(f'You entered: {userNum1}')

# Output the input squared
squared = int(userNum1 * userNum1)
print( f'{userNum1} squared is {squared}')

#Output the input cubed
cubed = int(userNum1 * userNum1 * userNum1)
print( f'And {userNum1} cubed is {cubed} !!')

#Get a second user input into user_num2
userNum2 = int(input("Please Enter another integer:\n "))
print(f'You entered: {userNum2}')

#output the sum and product
totalAdd = int( userNum1 + userNum2)
print( f'{userNum1} + {userNum2} is {totalAdd}')
totalSquared = int( userNum1 * userNum2)
print( f'{userNum1} * {userNum2} is {totalSquared}')
