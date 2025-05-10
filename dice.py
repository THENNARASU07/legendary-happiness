import random
def roll_dice():
    return random.randint(1, 6)
print(" Dice Roller Simulator ")
while True:
    user_input = input("Roll the dice? (yes/no): ").lower()
    if user_input == "yes":
        print(f"You rolled:{roll_dice()}")
    elif user_input =="no":
        print("Thanks for playing..!")
        break
    else:
        print("please type 'yes' or 'no'")

