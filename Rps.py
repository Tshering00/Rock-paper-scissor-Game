import random
print("Welcome to the ROCK PAPER SCISSOR Game !!!!")
print("________Note____")
print('1 = "Rock"')
print('2 = "Paper"')
print('3 = "Scissors"')
while True:
    computer_choice = random.randrange(1,4)
    print("Computer has choosen his move. Now your turn: ")
    
    try:
        player_choice = int(input("Enter your move(1-3): "))
        if player_choice not in [1,2,3]:
            print("Invalid Choice!!")     
            continue
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print(f"Computer chose: {choices[computer_choice]}")
        print(f"You chose: {choices[player_choice]}")
        
        if computer_choice == player_choice:
            print("It's a draw")
        elif (computer_choice == 3 and player_choice == 1) or (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 3):
            print("You won!")
        else:
            print("You lost!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "yes":
            print("Thank you for playing!!!")
            break
        
    except ValueError:
        print("Invalid input. Please input valid number(1,2,3)")      
    