first_list = [1, 2, 3]

print(first_list)

first_list = [1, 50, 'hello world']

print(first_list)

length = len(first_list)

print(length)

print(first_list[-1])

new_list = first_list[1:]

print(new_list)

string1 = "this string" + "that string"

first_list = first_list + [100, 200, 500] + ['some string']

print(first_list, len(first_list))

first_list.append("yet another string")

print(first_list, len(first_list))

first_list.pop(2)
print(first_list, len(first_list))

num_list = [1234, 1234, 45, 454, 666, -1, 0, 12]

num_list.sort()

print(num_list)

char_list = ['z', 'x', 'f', 'e', 't']

char_list.sort(reverse=True)

print(char_list)

newest_list = char_list + first_list

print("newest list", newest_list)

list_of_lists = [newest_list, new_list, first_list, char_list]

print(list_of_lists[0][-1].upper())

print(list_of_lists[0][1][0].capitalize())

my_dict = {
    "thisis": 20, "next key": ['hello', 'world', 'somemore'], "key3": [1, 2, 4, 777], 50: 'string'
}

print(my_dict["thisis"])

for item in my_dict:
    print(item)

my_dict['some_key'] = {1: 'string', 2: 'q314523452'}

print(my_dict)

if True:
    print("true")

print(15 > -3)

print('a string' == 'another strinf', 'a' == 'a')

print(10 > 5 and 15 > 5)

x = [1, 2, 3]
y = [1, 2, 3]

z = x
print(x is y, x is z)

x = 1
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is 0")
else:
    print("EOF")

print("outside the conditional")

# This is a comment
