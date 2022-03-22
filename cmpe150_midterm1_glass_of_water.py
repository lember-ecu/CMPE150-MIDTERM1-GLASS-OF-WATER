width = int(input())
height = int(input())
x = int(input())

change = 0

for a in range(x):
    change = change + int(input())
    filled = change // width
    plus = change % width
    for i in range(height-filled-1):
        print("#", end="")
        for j in range(width):
            print(" ",end="")
        print("#")

    print("#", end="")
    for i in range(plus):
        print("0",end="")
    for i in range(width-plus):
        print(" ",end="")
    print("#")

    for i in range(filled):
        print("#",end="")
        for j in range(width):
            print("0",end="")
        print("#")

    for i in range(width+2):
        print("#", end="")

    print()

