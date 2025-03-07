print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions


def square(n):
    return n*n


def percentage(n):
    return n/100


def multiplier(n, m):
    return n*m


def addition(a, b, c):
    return a + b + c

# A1a:

square_l = lambda x:x*x

percentage_l = lambda x: x/100

multiplier_l = lambda x,y: x*y

addition_l = lambda x,y,z: x+y+z

# print(addition_l(1,2,3))
print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1

# A1b:
# It is a recursive function that runs the expression a*factorial(a-1) if the if condition is met else returns 1


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:
square_list = list(map(lambda x: x**2, list_of_numbers))
print(square_list)

# -------------------------------------------------------------------------------------- #
