import random

Max = 100
player1squarenumber = 0 
player2squarenumber = 0

print("""Welcome to Snake and Ladder Game.


    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Type R to roll the dice
      6. Type Q to quit.
      7. Have fun!""")
      
player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]
      
snakeBite = [
    "woops",
    "ow",
    "snake bite",
    "oh no",
    "sorry"
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh good ...",
    "yaayyy"
]

snakes = {
    8: 5,
    18: 1,
    26: 8,
    39: 7,
    51: 2,
    54: 23,
    56: 1,
    60: 20,
    75: 30,
    83: 40,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 5
}

ladders = {
    2: 20,
    6: 19,
    11: 28,
    15: 39,
    17: 78,
    22: 37,
    38: 50,
    49: 61,
    57: 77,
    61: 76,
    73: 87,
    81: 97,
    88: 98
}

print("\n")
print("\n")
        
def getDiceValue():
    dicevalue = random.randint(1, 6)
    print("It is a " + str(dicevalue))
    return dicevalue
        
def GotSnakeBite(old_value, current_value, player_name):
    print("\n" + random.choice(snakeBite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " you got a snake bite. You are down from " + str(old_value) + " to " + str(current_value))


def LadderJump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " you climbed the ladder from " + str(old_value) + " to " + str(current_value))   
    
def GameStart():
    player1squarenumber = 0 
    player2squarenumber = 0 
    
    player1name = input("Please enter a name for first player: ")
    player2name = input("Please enter a name for second player: ")
    print("\n")
    print("Game will be played between '" + player1name + "' and '" + player2name + "'.")
    print("\n")
    
    while True:
        input1 = input(player1name + ": " + random.choice(player_turn_text) + " Press R to roll the dice: ")
        if input1 == "Q":
            break
        print("Rolling dice...")
        diceValue = getDiceValue()
        if player1squarenumber + diceValue > Max:
            print("You need " + str(Max - player1squarenumber) + " to win.")
        else:
            player1squarenumber = player1squarenumber + diceValue
            
        if player1squarenumber == Max:
            print("Congratulations! " + player1name + " won the game.")
            print("\n")
            break
        elif player1squarenumber in ladders:
            old_value = player1squarenumber
            player1squarenumber = ladders[player1squarenumber]
            LadderJump(old_value, player1squarenumber, player1name)
            
        elif player1squarenumber in snakes:
            old_value = player1squarenumber
            player1squarenumber = snakes[player1squarenumber]
            GotSnakeBite(old_value, player1squarenumber, player1name)
            
        print(player1name + " current number: " + str(player1squarenumber))
        print("\n")
            
        input2 = input(player2name + ": " + random.choice(player_turn_text) + " Press R to roll the dice: ")
        if input2 == "Q":
            break
        print("Rolling dice...")
        diceValue = getDiceValue()
        
        if player2squarenumber + diceValue > Max:
            print("You need " + str(Max - player2squarenumber) + " to win.")
        else:
            player2squarenumber = player2squarenumber + diceValue
            
        if player2squarenumber == Max:
            print("Congratulations! " + player2name + " won the game.")
            break
        elif player2squarenumber in ladders:
            old_value = player2squarenumber
            player2squarenumber = ladders[player2squarenumber]
            LadderJump(old_value, player2squarenumber, player2name)
            
        elif player2squarenumber in snakes:
            old_value = player2squarenumber
            player2squarenumber = snakes[player2squarenumber]
            GotSnakeBite(old_value, player2squarenumber, player2name)
            
        print(player2name + " current number: " + str(player2squarenumber))
        print("\n")
            
GameStart()
