# Importing the math module
import math

# Creating an empty list to store the numbers inputed by the user
# using a for loop to prompt user to input the numbers and append them to the list
list_numbers = []
for i in range(10):
    float_numbers = float(input("\nPlease enter 10 different float numbers: "))
    list_numbers.append(float_numbers)
    

# Calculating the total of all the numbers using the sum() function
sum = sum(list_numbers)
print("\nThe toal of all numbers is: ", sum)

# Finding and printing the maximum using the max() function
max_number = max(list_numbers)
print("The maximum number is: ", max_number)

# Finding and printing the minimum using the min() function
min_number = min(list_numbers)
print("The minimum nuber is: ", min_number)

# Calculating the average and rounding the result to 2 decials
average_num = (sum/len(list_numbers))
round_average = print("The average number is: ", round(average_num, 2))


# Finding the median number, calculate the lenght of the list and sort the list in ascending order using the sort() function
# Check if the if the number is even or odd. If even , find 2 middle elements in the list and get their average and if odd
# find the middle element in the list
# Source of information: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
list_len = len(list_numbers)
list_numbers.sort()

if list_len % 2 == 0:
    median1 = list_numbers[list_len//2]
    median2 = list_numbers[list_len//2-1]
    median = (median1 + median2)/2
else:
    median = list_numbers[list_len//2]

print("The median number is:", median)
