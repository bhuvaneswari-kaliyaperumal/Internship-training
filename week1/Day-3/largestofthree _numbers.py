num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find largest
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)

else:
    print("Largest number is:", num3)

    #output 
"""Enter first number: 22
Enter second number: 44
Enter third number: 55
Largest number is: 55.0"""