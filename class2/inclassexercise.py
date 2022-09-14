x = -10

if x > 0:
    if x > 10:
        output = "x > 10"
    else:
        output = "0<x<=10"
elif x < 0:
    if x > -10:
        output = "-10<x<0"
    else:
        output = "x<=-10"
else:
    output = "x==0"

print(output)
