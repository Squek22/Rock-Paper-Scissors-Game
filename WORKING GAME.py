# Name: Christopher Michaels
# Date Nov. 26 2022
# CEIS110, Coding Challenge.


# Create a rock paper scissors game
# Uses random module, while and for loops, if statements and functions

# imports random module as rd
import random as rd
import time

# defines game variables and list
rock = "rock"
paper = "paper"
scissors = "scissors"
playerScore = 0
computerScore = 0
list = ["rock", "paper", "scissors"]
# creates or opens leaderboard.txt
leaderboard = open("leaderboard.txt","w+")
# writes to the text file 
leaderboard.write("**Rock, Paper, Scissors Recent Scores**\n")
leaderboard.close()
print("Welcome to Rock, Paper, Python!")
time.sleep(1)
# defines the functions for the computer to use random module to pick its turn
def turn(playerPick):
    computerPick = rd.choice(list).lower()
    print("The computer picked", str(computerPick))
    if playerPick == rock and computerPick == scissors or playerPick == paper and computerPick == rock or playerPick == scissors and computerPick == paper:
        return 1
    elif playerPick == rock and computerPick == paper or playerPick == paper and computerPick == scissors or playerPick == scissors and computerPick == rock:
        return 2
    elif playerPick == paper and  computerPick == paper or playerPick == rock and computerPick == rock or playerPick == scissors and computerPick == scissors:
        return 3
    
    
#create function for normal mode, regular rock paper scissors game 
def normal():
    global playerScore
    global computerScore
    for i in range(1,int(numRounds)+1):
        playerPick = input("Do you pick rock, paper or scissors?  ").lower()
        while playerPick != rock and playerPick != paper and playerPick != scissors:
                playerPick = input("You entered, " + playerPick +'.' + " Please enter 'Rock', 'Paper', or 'Scissors'!   ").lower()
        gameResult = turn(playerPick)
        if gameResult == 1:
                print("You won!")
                playerScore = playerScore + 1
                print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore)) 
        elif gameResult == 2:
                print("You Lost")
                computerScore = computerScore + 1
                print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore)) 
        elif gameResult == 3:
                print("It's a Draw")
                print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore))  

#create function for a hard mode version, where computer has second chance when it doesnt win. 
def hardmode(): 
    global gameResult
    global playerScore
    global computerScore
    for i in range(1,int(numRounds)+1):
        playerPick = input("Do you pick rock, paper or scissors?  ").lower()
        while playerPick != rock and playerPick != paper and playerPick != scissors:
                playerPick = input("You entered, " + playerPick +'.' + "\nPlease enter 'Rock', 'Paper', or 'Scissors'!   ").lower()
        gameResult = turn(playerPick)
        if gameResult == 1:
            gameResult = turn(playerPick)
            if gameResult == 1:
                print("You won!")
                playerScore = playerScore + 1
            elif gameResult == 2:
                print("You Lost")
                computerScore = computerScore + 1
            elif gameResult == 3:
                print("It's a Draw")
            print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore)) 
        elif gameResult == 2:
            print("You Lost")
            computerScore = computerScore + 1
            print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore)) 
        elif gameResult == 3:
            gameResult = turn(playerPick)
            if gameResult == 1:
                print("You won!")
                playerScore = playerScore + 1
            elif gameResult == 2:
                print("You Lost")
                computerScore = computerScore + 1
            elif gameResult == 3:
                print("It's a Draw")   
            print('Current Score is\nUser:', str(playerScore), '\nComputer:', str(computerScore)) 
    
# create new game variable, which is used to define while loop for continous gameplay
newGame = 'yes'

# begin while loop to move through game rounds
while newGame == "yes":
    playerName = str(input("Please Enter Your Name: "))
    playerScore = 0
    computerScore = 0
    
    # Variable user-defined for number of rounds to play(Used in for loop in line 40)
    numRounds = input("How many rounds would you like to play? ")
    while numRounds.isnumeric() == False:
        numRounds = input(numRounds + " isn't a valid integer, please enter an integer.")
    
    # while loop to validate numRounds is an integer
    while numRounds == False:
        numRounds = input("Please Enter a valid number!")
                        

        
    gameMode = input("Would you like to play the Challenge Mode, or Normal Mode?\n|Enter Challenge or Normal| ").lower()
    if gameMode == 'challenge':
        hardmode()
    elif gameMode == 'normal':
        normal()
            
    print("\n\n\n*****\n\n\n")
    print("Calculating total score...")
    if playerScore > computerScore:
        print("Congratulations, you won!")
    elif playerScore < computerScore:
        print("You lost!")
    else:
        print("It's a Draw!")
    print('Final Score was... \nUser:{}\nComputer:{}\n\n\n'.format(playerScore,computerScore))
    
    scoreBoardUpDate = "***\nPlayer: {} | Score: {} \nMode: {} | Rounds Played: {}\n".format(str(playerName),str(playerScore),gameMode.upper(),numRounds)
    leaderboard = open('leaderboard.txt','a')
    leaderboard.write(scoreBoardUpDate)
    leaderboard.close()

    leaderboard = open('leaderboard.txt','r')

    print(leaderboard.read())
    leaderboard.close()
    print()
    newGame = input("Would you like to play again? \n|Type 'Yes' to continue!| ").lower()


    
else:
    print("\nThank you for playing!")
    time.sleep(1)
    leaderboard.close()