h =  6
w = 60

for i in range(h):
    for j in range(w):
        print("|", end = "")

    print("")

counter = 2
add = 2
for i in range(h):
    space = " " * int(w/2 - counter/2 )
    print(space, end="")
    for j in range(counter):
        print("@" ,end = "")
    
    if counter == 2 and add == -2:
        print("")
        break
    counter += add
    if counter == 6:
        add = -2
    

    print("")

for i in range(h):
    for j in range(w):
        print("\U0001F49A", end = "")

    print("")


