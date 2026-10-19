foods = ["crab", "tacos", "sushi", "pizza", "ramen"]
print(foods[1])
print(foods[-1])
foods.append("peas")
foods.insert(0, "apple")
del foods[2] # error of putting foods.remove(2), which didn't exist
print(len(foods))
for food in foods:
    print(food.upper())
foods2 = [foods[0], foods[-1]]
print(foods2)
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(0,21))

def get_first_15(numbers):  
    return(numbers[:15])

step1 = get_first_15(numbers)

def get_every_5th(step1):
    return(step1[::5])

step2 = get_every_5th(step1)

def reverse_and_stride(step2):
    return(step2[::-3])

numbers2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(numbers2[2])
print(numbers2[2][1])
numbers2.append([10, 11, 12]) #tried numbers2.append[3]([10, 11, 12]) to say where to append but realized [3] wasn't needed

def sum_nested(nested_list):
    sum=0
    for list in nested_list:
        for number in list:
            sum += number
    return sum
print(sum_nested(numbers2))

def create_list():
    numbers = []
    num = 1

    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        numbers.append(row)

    return numbers

new_list = create_list()

def threes(num):
    list = []

    for i in range(5):
        row = []
        for j in range(5):
            if num[i][j] % 3 == 0:
                row.append("?")
            else:
                row.append(num[i][j])
        list.append(row)
    return list

print(threes(new_list))

def sum_list(lists):
    sum = 0
    
    for i in range(5):
        for j in range(5):
            if lists[i][j] != "?":
                sum += lists[i][j]
    
    return sum

print(sum_list(threes(new_list)))

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")
print(ages)

for name, age in ages.items():
    print(name, age)

print(threes(new_list))