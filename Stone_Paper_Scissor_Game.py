import random

com_choice = ["stone", "paper", "scissor"]
while True:
    print("Stone Paper Scissor Game:")
    user_win = 0
    com_win = 0
    draw = 0
    wrong_input = 0
    for i in range(1, 11):
        print("This game contains 10 Rounds")
        print(f"Round {i} start:")
        print("Press 1 for stone, 2 for paper, 3 for scissor\n")
        user_input = int(input("Enter your input ==> "))

        if user_input == 1:
            print("\nYou select: stone")
            user_input = "stone"

        elif user_input == 2:
            print("\nYou select: paper")
            user_input = "paper"

        elif user_input == 3:
            print("\nYou select: scissor")
            user_input = "scissor"

        else:
            wrong_input += 1
            print("\nInvalid Choice.\n")
            break

        computer_choice = random.choice(com_choice)
        print(f"Computer select: {computer_choice} \n")

        if user_input == computer_choice:
            draw += 1
            print("This Round is Draw:\n")
        elif (user_input == "stone" and computer_choice == "scissor") or ( user_input == "scissor" and computer_choice == "paper") or (user_input == "paper" and computer_choice == "stone"):
            user_win += 1
            print("You win this Round:\n")
        else:
            com_win += 1
            print("Computer win this Round\n")

    if user_win > com_win:
        print("You win the game:\n")
        print(f"Your score: {user_win} , Computer score: {com_win} , Draw score: {draw}\n")
    elif com_win > user_win:
        print("Computer win the game:\n")
        print(f"Computer score: {com_win} , User score: {user_win} , Draw score: {draw}\n")
    else:
        print("Match Draw\n")
        print(f"Your score: {user_win} , Computer score: {com_win} , Draw score: {draw}\n")

    print("Do you want to play again?")
    print("Press y for yes,Press any key to quit the game.")
    user_choice = input("Enter here --> ")

    if user_choice.lower() == "y":
        continue
    else:
        break
