import random
user_W=0
comp_w=0

while True:
    user_input = input("Enter rock, paper, scissors or quit to exit: ").lower()
    if user_input == "quit":
        print("Thanks for playing!")
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue

    comp_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {comp_choice}")

    if user_input == comp_choice:
        print("It's a tie!")
    elif (user_input == "rock" and comp_choice == "scissors") or \
         (user_input == "paper" and comp_choice == "rock") or \
         (user_input == "scissors" and comp_choice == "paper"):     
        print("You win this round!")
        user_W += 1 
    else:
        print("Computer wins this round!")
        comp_w += 1
    print(f"Score - You: {user_W}, Computer: {comp_w}\n")
    