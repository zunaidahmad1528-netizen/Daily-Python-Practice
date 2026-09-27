
# Day 1 - Python Basics
# Topic: Variables and Data Types

# ----------------------------------------
# Part 1: Variables (values ko naam dena)
# ----------------------------------------

name = "Zunaid"          # str  - text
age = 20                 # int  - whole number
height = 5.11            # float - decimal number
is_learning = True       # bool - True ya False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is learning:", is_learning)

# ----------------------------------------
# Part 2: Type check karna
# ----------------------------------------

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_learning)) # <class 'bool'>

# ----------------------------------------
# Part 3: Variable ka value badalna
# ----------------------------------------

age = age + 1            # birthday aa gayi
print("Next year age:", age)

# ----------------------------------------
# Part 4: String formatting (f-string)
# ----------------------------------------

print(f"{name} is {age} years old and {height} feet tall.")

# ----------------------------------------
# Part 5: User se input lena
# ----------------------------------------

# input() hamesha string deta hai, isliye int() me convert karte hain
user_age = int(input("Apni age daalo: "))
print("5 saal baad tumhari age hogi:", user_age + 5)

# ----------------------------------------
# Practice Challenges (khud solve karo)
# ----------------------------------------
# 1. Ek variable banao jisme apna favorite number ho, aur usko print karo
# 2. Do variables me apna first name aur last name rakho,
#    phir dono ko jod kar poora naam print karo
# 3. int ka ek variable banao aur usko float me convert karke print karo
