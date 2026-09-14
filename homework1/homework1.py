# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a "complex," a representation of complex numbers

d = "hello"
print(d)
print(type(d)) # d is a string, a word or series of letters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a data type used to store a collection of other data, whether words, numbers, or other data types

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, which contains "keys" that can be numbers or words that store values and extract values

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a list that cannot be changed once created and is "immutable"

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a data type used to store a collection of other data, whether words, numbers, or other data types

i = True
print(i)
print(type(i)) # i is a boolean, a data type that represents one of two values, either true or false

j = None
print(j)
print(type(j)) # j is a NoneType, a special data type that only states that there is no value/null state

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a data type used to store a collection of other data, whether words, numbers, or other data types

l = str(14)
print(l)
print(type(l)) # l is a string, a word or series of letters/numbers

m = 1e4
print(m)
print(type(m)) # m is a float, a number with decimals

# Q1: 9 different data types.

# Q2: String, list, integer, float, NoneType, Complex, Dictionary, Boolean, and Tuple

# Q3: k, h, and e were all lists. m and b were both floats.

# Q4: Without googling, I assume l is a string instead of an integer because the command str() would change the data type to a string

# Q5:

n = range(0, 10)
print(n)
print(type(n)) # n is a range, an immutable sequence of numbers mainly used for looping


# --------- Booleans ----------

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # Fales, 10 does not equal 9

print(10 <= 9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, because the string contains something

print(bool(123)) # True, as 123 is a nonzero number

print(bool(["apple", "cherry", "banana"])) # True, as the list contains items and is not empty

print(bool(True)) # True, as the boolean output of true is true 

print(bool(False)) # False, as the boolean output of false is false 

print(bool(0)) # False, as python considers 0 a "False" value, anything nonzero is true

print(bool("")) # False, as the string is empty

print(bool(" ")) # True, as a space is considered something within the string

print(bool(())) # False, as an empty tuple is considered false, along with most empty items

print(bool([])) # False, as there is nothing in the list

print(bool({})) # False, as it is an empty set

print(bool(True and False)) # False, as the word "and" requires both to be true, which it is not

print(bool(True and True)) # True, as the word "and" requires both to be true, which they are

print(bool(False and False)) # False, because both being false creates an outcome of false

print(bool(True or False)) # True, as the outcome is either true or false always, as seen with the word "or"

print(bool(True or True)) # True, as both outcomes are true, meaning it must be true

print(bool(False or False)) # False, as both outcomes are false, meaning the result is false

print(bool(not(False))) # True, because not being false means it is true, as there are only 2 outputs

print(bool(not(True))) # False, because not being true means it is false, as there are only 2 outputs

