# rock paper scissors game
# against the computer

import random

comp = random.randint(0,2)

game = eval(input("scissor (0), rock(1), paper(2): "))

if comp == 0 and game == 0:
	print("The computer is scissor. You are scissor. It's a draw.")
elif comp == 0 and game == 1:
	print("The computer is scissor. You are rock. You won.")
elif comp == 1 and game == 0:
	print("The computer is rock. You are scissor. You lost.")
elif comp == 1 and game == 1:
	print("The computer is rock. You are rock. It's a draw.")
elif comp == 1 and game == 2:
	print("The computer is rock. You are paper. You won.")
elif comp == 2 and game == 1:
	print("The computer is paper. You are rock. You lost.")
elif comp == 2 and game == 2:
	print("The computer is paper. You are paper. It's a draw.")
elif comp == 2 and game == 0:
	print("The computer is paper. You are scissor. You won.")
elif comp == 0 and game == 2:
	print("The computer is scissor. You are paper. You lost.")