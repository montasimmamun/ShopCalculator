import os

sum = 0

if os.path.exists("Receipt.txt"):
    os.remove("Receipt.txt")

file = open("Receipt.txt", 'a')

while (True):
    userInput = input("Enter product price> ")

    if(userInput != 'q'):
        sum = sum + float(userInput)
        print(f"Your Bill So Far: {sum}")

        file.write(str(userInput))
        file.write(" + ")

    else:
        file = open("Receipt.txt", 'r')
        print("\n")
        for x in file:
            print(x)
        file.close()

        print(f"Your Total Bill Is: {sum}")
        print("Thanks for shoping with us")
        break
