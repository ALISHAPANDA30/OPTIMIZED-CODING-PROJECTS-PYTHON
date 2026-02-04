def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 won!"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 won!"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 won!"
    
    else:
        return "Player 2 won!"


# ---- User Input ----
player1 = input("Enter Player 1 move (rock/paper/scissors): ").lower()
player2 = input("Enter Player 2 move (rock/paper/scissors): ").lower()

result = rps(player1, player2)
print(result)
