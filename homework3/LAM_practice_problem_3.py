# Question 1
list1 = []
for item in range(1, 21):
    list1.append(item)
print(list1)

# Question 2
list2 = []
for item in range(1, 21):
    if 40 < item ** 2 < 120:
        list2.append(item)
print(list2)

# Question 3
list3 = []
list4 = []

for item in range(1, 21):
    if 40 < item ** 2 < 120:
        list3.append(item)
    else:
        list4.append(item)
print(list3, "\t", list4)

# Question 3.5
list5 = []
list6 = []
list7 = []

for item in range(1, 21):
    if 40 < item ** 2 < 120:
        list5.append(item)
    elif item < 10:
        list6.append(item)
    else:
        list7.append(item)
print(list5, "\t", list6, "\t", list7)

# Question 4
my_dict = {1: 'partridge in a pear tree',
           2: 'turtles',
           3: 'french hens',
           4: 'calling birds',
           5: 'golden rings',
           6: 'geese a laying',
           7: 'swans a swimming',
           8: 'maids a milking',
           9: 'ladies dancing',
           10: 'lords a leaping',
           11: 'pipers piping',
           12: 'drummer drumming',
           13: 'platinum rings'}

for key, value in my_dict.items():
    print(key, value)
    if "rings" in value:
        print(value)
        my_dict[key] = "really big " + value
    elif "turtles" in value:
        print(value)
        my_dict[key] = "ninja " + value
print(my_dict)

# Question 5
reversed_dict = {}

for key, value in my_dict.items():
    reversed_dict[value] = key
print(reversed_dict)

# Question 6
shopping_list = {}
for key, value in reversed_dict.items():
    if value < 6:
        shopping_list[key] = 6 - value

print(shopping_list)

# Question 7
with open("shakespeare.txt", mode="r", encoding="utf-8") as f:
    library = f.read().splitlines()
# my line count seems to be 1 off from the one suggested in the problem -- but the below includes the first line of
# the sonnet, slicing from 303 does not
print(*library[302:316], sep="\n")
