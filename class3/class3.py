my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for item in my_list:
    total += item
    print(f"total: {total}")
for item in my_list:
    if item > 5:
        print("I'm printing an item")
        print(item)
    print("Done!")

print("Done with progam!")

my_dict = {'Dog': 'Hund', "Cat": "Katse", "Mouse": "Maus"}

for key, value in my_dict.items():
    print(key, value)

list1 = [1, 3, 5]
list2 = [2, 4, 6]

for x in list1:
    if x > 3:
        for y in list2:
            print(f"{x * y}")

    print(f"\n")

better_list = ["string", "more string", 0, 1, 2, 3]

for i in range(len(better_list)):
    print(f"{better_list[i]}")
