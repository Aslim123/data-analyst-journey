Day 1 – Python Setup & Basics

📘 1. Introduction to Python
Python is a high-level, interpreted, and general-purpose programming language.
It’s known for its simplicity, readability, and wide use in fields like:
Data Analysis
Machine Learning
Web Development
Automation

💡 Why Python for Data Analysis?

Easy to learn and use
Libraries like Pandas, NumPy, Matplotlib, Seaborn make data handling powerful
Strong community and free resources

⚙️ 2. Setting Up Your Environment

Steps completed today:
Installed Python from python.org
Installed a code editor (VS Code)
Verified installation of python:
python --version

💾 3. Variables

Variables are names that store values.
Python is dynamically typed → no need to declare data type manually.

Example:
name = "Aslim"
age = 23

can check type:
print(type(name))
print(type(age))

🔢 4. Data Types
* Primitive Data Types (Built-in / Basic types)
Type	            Description	                                Example
int	               Integer numbers	                            x = 10
float	           Decimal numbers	                            pi = 3.14
bool	           Boolean values (True/False)	                flag = True
str	               Sequence of characters (string)	            name = "Aslim"
complex	           Complex numbers	                             z = 2 + 3j

* Non-Primitive Data Types (Composite / Collection types)
These can store multiple values or structured data.
Type	               Description	                             Example
list	          Ordered, mutable collection	                 numbers = [1, 2, 3]
tuple	          Ordered, immutable                             collection	coords = (10, 20)
set	              Unordered, unique elements	                 colors = {"red", "green", "blue"}
dict	          Key-value pairs	                            student = {"name": "Aslim", "age": 23}

* Some additional types in Python

Type	                Description	                                Example
range	               Sequence of numbers	                        range(1, 10)
bytes	             Immutable sequence of bytes	                b = b"hello"
bytearray	          Mutable sequence of bytes	                    ba = bytearray(5)
NoneType	          Represents absence of value	                x = None

💬 5. Input and Output
input() → takes input from user
print() → displays output

Example:
user_name = input("Enter your name: ")
print("Hello,", user_name)

🧮 6. Operators
Arithmetic Operators
+, -, *, /, //, %, **
example:
x = 5
y = 2
print(x + y)  # 7
print(x ** y) # 25

Comparison Operators
==, !=, <, >, <=, >=

Logical Operators
and, or, not

💭 7. Expressions

An expression is a combination of values, variables, and operators that produces a result.
Example:

x = 5
y = 3
result = (x + y) * 2  # Expression → evaluates to 16

💡 8. Comments

Use # to describe your code — helps readability.
comment part never get executed
example: 
# This program prints a greeting      -- single line comment
print("Hello, Aslim!")  

for multiline comment use triple quote(""" or ''')
eg:
""" 
This is multiline comment
using a multiline string
"""