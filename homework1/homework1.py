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

# Questions 

# Q1: I noticed that it cannot exist in both states at once, and that False often overrides True.

# Q2: I was surprised by the "False or False" because it appears to be a paradox. Since the outcome is False, then it would mean that the boolean was right and therefore is true, which is again a paradox.

# Q3: print(bool("hello world")) will return true because it has a string with something in it.

# Q4: print(bool(str())) will return false because it contains a string with nothing in it despite having a command.

# ----Operators----

print(10 + 5) # 15, + performs addition

print(10 - 5) # 5, + performs subtraction

print(2 * 4) # 8, + performs multiplication

print(6 / 3) # 2, + performs division

print(5 % 2) # 1, + performs division and outputs the remainder

print(3 ** 2) # 9, + performs exponentiation

print(15 // 2) # 7, + performs division and rounds down

print(5 == 2) # False, + checks if the numbers are equal

print(10 != 10) # False, + checks if the numbers are not equal

print(2 < 5) # True, + checks if the first number is less than the second number

print(12 > 5) # True, + checks if the first number is greater than the second number

print(5 <= 6) # True, + checks if the first number is less or equal to than the second number

print(1 >= 10) # False, + checks if the first number is greater than or equal to the second number

x = 5

x += 5
print(x)
x -= 4 # I tried to run all of these but they all showed an error of "invalid syntax." 
print(x)
x *= 3
print(x)

# Logical Operators

# Q1: "and" means that it must fulfill both conditions. print(bool(2 and 3)) is true, and print(bool(2 and "")) is false.

# Q2: "or" means that it must fulfill one of the conditions. print(bool(2 or "")) is true, and print(bool(0 or "")) is false.

# Q3: "not" gives the opposite outcome. print(bool(not"")) is true, print(bool(not"3234")) is false.

# More Questions

# Q1: / is division, // is division rounded down

# Q2: % gives the remainder, // is the result without the remainder

# Q3: I would use %, in an expression like print(11 % 3), which would output 2

# Q4: I am not sure what assignment operators do as I could not get them to work.

#-----Strings-----

my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h

print(my_string[1]) # Prints: e

print(my_string[2]) # Prints: l

print(my_string[3]) # Prints: l

print(my_string[4]) # Prints: o

print(my_string[-1]) # Prints: o

print(my_string[1:3]) # Prints: el

print(my_string[0:5:2]) # Prints: hlo

print(len(my_string)) # Prints: 5

print(my_string + "goodbye") # Prints: hellogoodbye

print(7 * my_string) # Prints: hellohellohellohellohellohellohello

# 3.4.1 Questions

# Q1: Slicing takes only a part of a piece of code, such as a single letter from a string.

# Q2: 
name = "Oski"
print("Hello, my name is", name)
# the result is "Hello, my name is Oski"

# Q3:
name = "Oski"
print(f"Hello, my name is {name}")
# the result is "Hello, my name is Oski"

# Q4: 3 is an f string that directly embeds the variable into the string instead of requiring you to add a comma and end the string

#---Terminal Commands---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# List. Use it to list directories you can move to
# Example: ls

# ls -a
# List. Use it to list directories, including hidden ones, that you can move to
# Example: ls -a

# mkdir
# Make Directory. Use it to create a new directory
# Example: mkdir NolanF

# cat
# Concatenate. Use it to read and edit a file.
# Example: cat homework1

# pwd
# Print Working Directory. Use it to learn what learn what directory you are currently in.
# Example: pwd

# cd ..
# Change Directory. Use it to change directories to the previous directory you were in.
# Example: cd ..

# cd .
# Change Directory. Use it to change directories to the one you already are in, effectively doing nothing.
# Example: cd .

# cd ~
# Change Directory. Use it to change directories to your home directory.
# Example: cd ~

# cp
# copy. Use it to copy/duplicate files.
# Example: cp Astro-98

# mv
# Move. Use it to move or change the name of files.
# Example: mv homework1 Astro-98   

# rm
# remove. Use it to permanently delete files
# Example: rm homework1

# clear
# Clear. Use it to clear your terminal screen.
# Example: clear

# grep
# Global Regular Expression Print. Search a file for a specific instance of text
# Example: grep "hello world" homework1

# Questions

# Q1: nano. nano. Use it to create and edit a text file. nano homework1
# touch. touch. Create a new empty file. touch hello_world
# open. open. Open a file. open homework1

# Q2: the difference between ls and ls -a is that ls -a shows hidden files.

# Q3: Hidden files are files that start with . that are not typically shown in file managers like Finder to prevent deletion.

# Q4: 1. ls -l, modifier of ls that lists permissions for each file and more detailed information
# 2. ls -t, modifier of ls that lists the files my when they were last opened and/or modified
# 3. rm -r, modifier of rm that recursively deletes files, necessary to remove an entire folder.




