# Python Notes
## Fundamentals
### What is Python?
 - Python is an interpreted language. This means Python executes instructions directly, 
without first compiling them into machine code
 - Python is widely used
 - It is an object-oriented language
#### What makes python special?
 - It is easy to learn
 - It is easy to teach
 - It is easy to use
 - It is easy to understand
 - It is easy to obtain, install and deploy
### Installation
 - Following link can be used to download python: https://www.python.org/downloads/
### Comments in Python
 - Comment is a piece of text that begins with a hash # sign and extends to end of the line.
 - To add comments in multiple lines, you have to put a hash in front of all the lines. 
 - Alternatively triple quotes can be used for multiline comments
 - Good, responsible developers describe each important piece of code. 
 - Comments can also be used to mark a piece of code that currently isn’t needed.
```py
#This is a comment
#This is a second comment

'''
This is a 
multiline
comment
'''

```
### Python Data Types
#### Numbers and Operators
 - Number can be of type int or float in Python. 
 - Integer numbers are of type int, e.g. 4 and decimal numbers are of type float, e.g. 4.0
 - Following operators can be used in Python:
   - \+ : Add 
   - \- : Subtract 
   - \* : Multiple 
   - \\ : Divide
   - **: Exponent
   - % : Modulo - returns remainder
 - Example
```
2 + 3
4 - 2
3 * 4
6 / 2
3 ** 3
5 % 2
```
 - Priority of operators <br>

| Priority (1:highest, 4:lowest)   | Operator |
|----------------------------------| ---------- |
| 1                                | +, - (unary) |
| 2                                | **|
| 3                                |*, /, %|
| 4                                |+, - (binary)|

 - The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression
 - Most of python’s operators have left-sided binding
 - For example, in 9 % 6 % 2, 9 % 6 is done first and then the result % 2
 - The exponentiation operator uses right-sided binding
#### Equality operators
 - Python has two boolean values; True and False
 - Following are equality operators in Python:
   - == : Equal to
   - != : Not equal to
   - \> : Greater than
   - \< : Lesser than
   - \>= : Greater than or equal to
   - \<= : Lesser than or equal to
 - Example
```
4 == 4 (True)
5 != 4 (True)
3 > 9 (False)
3 < 9 (False)
3 > = 3 (True)
1 <= 2 (True)
```

#### String
 - Strings are used when you need to process text 
 - String needs quotes the way float needs points 
 - Backslash can be used as escape character when string has quotes in it.

### Variables
 - A variable is a named location reserved to store values in memory
 - Python variable have:
   - Name(Identifier)
   - A value
 - The name of the variable must be composed of upper-case or lower-case letters, digits and the _ character
 - Name of variable must begin with a letter
 - Example
```py
#This would print 6
value_1 = 2
value_2 = 4
print(value_1 + value_2)
```
### String Methods
 - Below is a list of string methods:
 - 
| Function     | What it does                                                        |
|--------------|---------------------------------------------------------------------|
| list()       | creates list of all characters in string                            |
| max()        | finds the character with maximal codepoint                          |
| min()        | finds the character with minimal codepoint                          |
| index()      | finds index of given substring inside the string                    |
| captalize()  | changes all string to upper case                                    |
| center()     | centers the string inside the field of a known string               |
| count()      | counts the occurrence of given character                            |
| join()       | joins all items of tuple/list into a string                         |
| lower()      | converts all letters to lower case                                  |
| lstrip()     | removes white characters(or specified characters) from beginning of string |
| replace()    | replaces a given substring with another                             |     
| rfind()      | finds a substring starting from end of string                       |
| split()      | splits string ino substring using given separator/delimiter         |
| strip()      | removes leading and trailing whitespace or specified character      |
| swapcase()   | swaps the letters’ cases                                            |
| title()      | makes first letter in each word upper case                          |
| upper()      | converts all string’s letters to upper case                         |

### Control Flow
 - Python uses if, elif (short for else if), and else keywords to create control flow structures in the program.
```py
def control_flow(x):
    if x<0:
        print("Its Negative")
    elif x==0:
        print("Equal to Zero")
    else:
        print("Its Positive")

control_flow(-1) # Output = Its Negative
control_flow(0) # Output = Equal to Zero
control_flow(2) # Output = Its Positive

```
### Python Collections
 - There are 4 types of built-in collections in Python:
   - List
   - Sets
   - Tuple
   - Dictionary
 - Below are the syntax for each of these types
```py
new_list = [1,2,3,4]
new_tuple = (1,2,3,4)
new_set = {1,2,3,4}
new_dict = {1:3, 2:4}
```
 - While lists, tuples and sets store values in a list format, dictionaries store them as key:value pairs
### Loops
 - Loops in Python are used to repeat actions efficiently. 
 - The main types are For loops and While loops.
 - Examples
```python
x = 0
while x<5:
    print(x)
    x += 1

#Output:0 1 2 3 4

for i in range(5):
   print(i)
#Output: 0 1 2 3 4
```
### Functions
 - A function is a block of code which only runs when it is called.
 - In Python a function is defined by the *def* keyword
 - Example
```python
def add(a, b):
    print(a + b)

add(1,2)

#Output: 3
```