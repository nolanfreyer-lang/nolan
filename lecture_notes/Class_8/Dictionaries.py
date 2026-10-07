
bugs = {"ants": ["black","fire"], "spiders": ["black widow", "tarantula"], "flys": ["horse","house"]}

# print(bugs.items())
# print(bugs.values())

star = {
    "name": "Vega",
    "magnitude": 0.57,
    "distance": 25.05 #light years
}

for key in star.keys():
    print(key)

for value in star.values():
    print(value)

list1 = list(range(0,11))

# print(list1)
# print(list1[:5])
# print(list1[1::2])
# print(list1[::-1])

a = [2,4,6]
b = [8,10,12]
c = [14,16,18]
nested_list = [a,b,c]

# print(nested_list[2][1])
# print(nested_list)

# stars_data = {
#     "name":["Sirius","Vega","Altair"],
#     "magnitude":[-1.46,0.03,0.77],
#     "disntance_ly":[8.6,25.0,16.7],
#     "constellation":["Canis Major", "Lyra", "Aquila"]
# }

# for star in stars_data["name"]:
#     print(star)

