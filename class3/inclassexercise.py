import os

print(os.getcwd())
os.chdir("../")
print(os.getcwd())
os.chdir("class3")

with open("simple_file.txt", mode="r", encoding="utf-8") as f:
    my_file = f.read().split("\n")
print(my_file)
