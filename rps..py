import random
humanoptions, computeroptions = ("rock", "paper", "scissors", "clark"),  ("rock", "paper", "scissors")
human = "nothing"
while not human in humanoptions:
  human = input("Do you pick rock, paper, or scissors? ")
computer = random.choice(computeroptions)
print ("You picked " + human + " and the computer picked " + computer)
if (human == "clark"):
  print ("Cheat code activated, Clark always wins!")
  exit()
if human == computer:
  print ("it is a tie")
if human == "rock" and computer == "scissors":
  print ("You win!")
elif human == "paper" and computer == "rock":
  print ("You win!")
elif human == "scissors" and computer == "paper":
  print ("You win!")
else:
  print ("You lose!")
