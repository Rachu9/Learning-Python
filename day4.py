# Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:

# Both numbers are greater than 10 (using and).
# At least one of the numbers is less than 5 (using or).
# The first number is not greater than the second (using not).

# a=int(input("Enter the value 0f a:"))
# b=int(input("Enter the value 0f b:"))
# if a>10 and b>10:
#     print("True")
# else:
#     print("False")


# a=int(input("Enter the value 0f a:"))
# b=int(input("Enter the value 0f b:"))
# if a<5 or b<5:
#     print("True")
# else:
#     print("False")

# a=int(input("Enter the value 0f a:"))
# b=int(input("Enter the value 0f b:"))
# if not a>b:
#     print("True")
# else:
#     print("False")




# Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

# "You are an adult" if the age is greater than or equal to 18.
# "You are a minor" if the age is less than 18.
# Use >= and < comparison operators.


# age=int(input("Enter the age:"))
# if age>=18:
#     print("You are an adult")
# else:
#      print("You are a  minor")


# Membership Operator Exercise: Write a Python program that:

# Takes a string as input from the user.
# Checks if the letter 'a' is in the string (using in).
# Checks if the string doesn't contain the word "Python" (using not in).


# value=input("Enter the string:")
# if 'a' in value:
#     print("Present")
# else:
#     print("Not present")

a=int(input("Enter the value 0f a:"))
b=int(input("Enter the value 0f b:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(a>>1)
