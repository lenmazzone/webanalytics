# hello world
print("Hello world")
print("This is a python program!")

thisString = "I am a string stored in a variable"

print(thisString)

def thisfunction(count):
    for char in thisString:
        print(char)
    while count > 0:
        print("this is a while loop on pass:", count)
        count -= 1


thisfunction(10)
