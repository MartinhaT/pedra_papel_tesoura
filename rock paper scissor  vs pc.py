import random


x1 = input("Player 1(choose rock, paper or scissors):").lower()
x2 = random.choice(['rock', 'paper', 'scissors'])
print(f"Resposta do Mickey {x2}") 
if x1 == x2:
    print("Empate!")
if (x1 == "rock" and x2 == "scissors") or (x2 == "rock" and x1 == "paper"):
    print("Player 1 Wins!")
if (x1=="rock" and x2=="paper") or (x2=="rock" and x1=="scissors"):
    print("Player 2 Wins!")

else:
    print("Opps! Try again!")
