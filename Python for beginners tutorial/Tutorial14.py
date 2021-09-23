#Break and Continue statement in python
i = 0
while(True):
    if i + 1 < 5:
        i = i + 1
        continue

    print(i+1, end=" ")
    if(i==44):
        break
    i = i + 1


print("\n")

#Take a input from the user untill it is not greater than 100
while(True):
    inp = int(input("Enter a number:-"))

    if inp>100:
        print("Congratulations you entered number greater than 100")
        break

    else:
       print("Try again\n")
       continue