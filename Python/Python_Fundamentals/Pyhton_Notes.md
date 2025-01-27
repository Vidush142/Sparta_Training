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

| Priority (1:highest, 4:lowest) | Operator |
| ------------------------------- | ---------- |
| 1                              | +, - (unary) |
| 2                              | **
| 3                              |*, /, %
| 4                              |+, - (binary)

 - The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression
 - Most of python’s operators have left-sided binding
 - For example, in 9 % 6 % 2, 9 % 6 is done first and then the result % 2
 - The exponentiation operator uses right-sided binding
 
#### String
 - Strings are used when you need to process text 
 - String needs quotes the way float needs points 
 - Backslash can be used as escape character when string has quotes in it.