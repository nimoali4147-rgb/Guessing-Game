import random

number = random.randint(1, 100)

print("\n Pick a level:")
print("1: Easy - 10 trial")
print("2: Medium - 7 trial")
print("3: Hard - 5 trial")

level = input("Enter your choice:")

if level == "1":
    trial = 10
elif level == "2":
    trial = 7
elif level == "3":
    trial = 5
else:
    print("invalid choice")
    trial = 0

attemp = 0
while attemp < trial:
    print(f"\n You have {trial - attemp} gues left.")

    try:
        gues = int(input("Gues the number:"))

        attemp += 1

        if gues == number:
            print("Correct you won!")
            break
        elif gues > number:
            print("Too High")
        else:
            print("Too low")

    except ValueError:
        print("Enter a number.")

if attemp == trial and gues != number:
    print("\n Game Over!")
    print(f"The correct number is {number}.")
