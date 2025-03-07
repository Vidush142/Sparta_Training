print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
for i in range(5):
    print(x[i])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in x:
    if i%2 == 0:
        print(i)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for i in range(5):
    if x[i]%2 == 0:
        print(x[i])

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
letter_list = []
for i in names:
    letter_list.append(i[0])

print(letter_list)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index = []
for i in names:
    space_index.append(i.index(" "))

print(space_index)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials_list = []
for i in names:
    input_index = i.index(" ") + 1
    initials_list.append(i[0] + i[input_index])

print(initials_list)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

list_of_lists_refined = []
for i in list_of_lists:
    if len(set(i)) == len(i):
        list_of_lists_refined.append(i)

print(list_of_lists_refined)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
valid_input = False
prime_check = False
while not valid_input:
    int_input = int(input("Enter a number greater than 100: "))
    if int_input > 100:
        valid_input = True
        print("Your number is: " + str(int_input) )
        # Answer for 4b starts here
        for i in range (2, int_input):
            if int_input % i == 0:
                prime_check = True
        if int_input <= 1:
            print("Your number is not prime")
        elif int_input > 1 and prime_check:
            print("Your number is not prime")
        elif int_input > 1 and not prime_check:
            print("Your number is prime")
print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:





