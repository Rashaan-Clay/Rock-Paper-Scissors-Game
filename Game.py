import random

print("Welcome to the Game!")
name = input("\n Enter your name: ")
print("\n Welcome", name)

items = ["Rock", "Paper", "Scissors"]
print("Select your weapon:\n", "\n".join(items))
user = input("Select: ").capitalize()

bot = random.choice(items)
print("\n\tThe bot selects", bot)

if user == bot:
    print("\tIt's a Draw!")
elif (user == "Rock" and bot == "Scissors") or \
     (user == "Paper" and bot == "Rock") or \
     (user == "Scissors" and bot == "Paper"):
    print("\tYou won!")
else:
    print("\tYou lost!")