import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors" ]

while True:
    user_input = input("type rock/paper/scissors OR q to quit: ").lower()
    
    if user_input == "q":
       break
    
    
    if user_input not in options:           #if user_input not in ["rock", "paper", "scissors" ]:
        continue
    
    random_number = random.randint(0 , 2)   # rock:0/paper:1/scissors:2
    
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        user_win += 1
        print("you win.")
        
    
    elif user_input == "scissors" and computer_pick == "paper":
        user_win += 1
        print("you win.")
        
    
    elif user_input == "paper" and computer_pick == "rock":
        user_win += 1
        print("you win.")
       
    elif user_input == computer_pick:
        print("Tie")    
       
    
    else:
        print("you lost!")
        computer_win += 1
    
print("you won", user_win, "times.")
print("the compuer won", computer_win, "timea")    

print("goodbye")    