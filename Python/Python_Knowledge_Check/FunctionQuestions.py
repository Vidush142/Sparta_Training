from curses.ascii import isalnum, isdigit

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(n):
    divisor_list = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor_list.append(i)

    return divisor_list


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def check_factor(int_1, int_2):
    factor_list_1 = divisors(int_1)
    factor_list_2 = divisors(int_2)
    if int_1 in factor_list_2:
        return True
    elif int_2 in factor_list_1:
        return True
    else:
        return False

print(check_factor(6, 7))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def get_position(char):
    return ord(char.lower())-97

print(get_position("z"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def code_name(name):
    result = ""
    for i in name:
        result += str(get_position(i))

    return result

print(code_name('bob'))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def generate_password(name):
    id = code_name(name)
    sum_of_id = 0
    for i in id:
        sum_of_id += int(i)

    password = int(id) - sum_of_id
    return password

print(generate_password('bob'))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_check(n):
    # 3b answer
    if not str(n).isdigit():
        return "Function only accepts numbers"
    #3a answer
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False

    return True

print(prime_check(4))
print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #






