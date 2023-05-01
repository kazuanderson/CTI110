#CTI-110
#P3HW1 - Debugging
#Kazune Anderson
#3/8/2023

print("This program takes a number grade, determines average and displays letter grade for average. ")
print()

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
print()
mod_2 = float(input('Enter grade for Module 2: '))
print()
mod_3 = float(input('Enter grade for Module 3: '))
print()
mod_4 = float(input('Enter grade for Module 4: '))
print()
mod_5 = float(input('Enter grade for Module 5: '))
print()
mod_6 = float(input('Enter grade for Module 6: '))
print()

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = float( mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6 )
avg = float( (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6)/6 )

#Display results
print("----------Results----------")
print(f'Lowest Grade:       {low:.1f}')
print(f'Highest Grade:      {high:.1f}')
print(f'Sum of Grades:      {sum:.1f}')
print(f'Average:            {avg:.2f}')
print("--------------------------------------------------")

# determine letter grade for average

if avg >= 90:
   print('Your grade is: A')
elif avg > 80:
   print('Your grade is: B')
else:
   print('Your grade is: F') # TO DO: finish this





