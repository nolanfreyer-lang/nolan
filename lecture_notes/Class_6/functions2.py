
# Second Function Lecture

# Secret code ??? = boolean

# list = [3,2,5,8,2,10,94939,23,-42]

# def minval(list):
#     print(min(list))

# def maxval(list):
#     print(max(list))

# minval(list)

# maxval(list)

# PRIME NUMBER DEMO

def isprime(num):
    if num <= 0 or type(num) != int:
        return "try again. choose a new number"
    else: 
        if num == 1:
            return "neither"
        elif num == 2:
            return "Prime number"
        else:
            if num % 2 == 0:
                return "Composite number"
            else:
                for i in range(2,num):
                    if num % i:
                        return "Composite number"
                    else: 
                        return "Prime number"

print(isprime(99902909109384019839831207894273049827037))
