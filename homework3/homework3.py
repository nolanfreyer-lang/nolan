def say_goodbye(name):
    print("Goodbye,", name)

def area_circle(r):
    #returns area of a circle with radius r
    return 3.14 * r ** 2

def sub(a, b):
    #subtracts b from a
    return a - b

def mult(a, b):
    #multiplies a and b
    return a * b

def div(a, b):
    #divides a by b
    return a / b

# DO THE OTHER QUESTION HERE uihsaofiuahodfiuHOiuafhaosidufhaosiudfhoaiusdfhoisdfhoaisudhfoaiushdfoaiushdfoaiushdfoiuahsdofiuahsodfiu

def is_weekend(day):
    if day == 6 or day == 7:
        return "It's the weekend!"
    elif day == 5:
        return "Ehhhhhh depends on who you ask"
    else:
        return "It's not the weekend."  
    
def fuel_efficiency(miles, gallons):
    return miles/gallons

def encrypt(int):
    return (int%10,int//10)

def exponentiate(x, y):
    result = 1
    multipliers_left = 0
    while multipliers_left < y:
        multipliers_left += 1
        result *=x
    return result
    

min_max_set = [1, 2, 3, 4, 5]



