# ACEYDUCEY
# program that simulates the card game Acey Ducey

import random

def main():
	'''main game program'''
	# giving an introduction to the game
	introduction()
	print()

	# setting an initial money
	Q = initial_money()
	print()

	# entering the game loop
	while True:

		# showing the cash load with the player
		print(f"You now have {Q} dollars.")

		# dealing the initial two cards
		d1, d2 = deck("start")
		print()

		# taking bets
		while True:
			bet = int(input("What is your bet? "))
			if bet == 0:
				print("Chicken!")

			# checking if player has money available or not
			if bet > Q:
				print("You cannot bet more than you have")
				print()
			else:
				break

		# dealing the third card
		d3 = deck("third")

		# checking the win/lose condition
		state = check(d1, d2, d3)

		# monetary calculation for the bet
		if state == "win":
			print("You win!!!")
			Q += bet
		elif state == "lose":
			print("You lose!")
			Q -= bet
		print()

		# condition for game end
		if Q <= 0:
			print("GAME OVER.")
			break


def introduction():
	'''printing the introduction'''
	with open("introduction.txt") as file:
		for line in file:
			print(line, end='')


def initial_money(n=100):
	'''setting initial cash load with player'''
	while True:
		start = input("Do you want to start with $100? (y/n): ").lower()
		if start == "n" or start == "no":
			n = int(input("Enter your starting cash load: "))
			if n >= 0:
				return n
			else:
				print("Enter a positive number.")
		elif start == "y" or start == "yes":
			return n
		else:
			print("Enter only 'y' or 'n'.")


def deck(arg):
	'''dealing cards'''
	seq = ["ACE", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "JOKER", "QUEEN", "KING"]
	if arg == "start":
		print("Here are your next two cards...")
		deal1 = random.choice(seq)
		deal2 = random.choice(seq)
		print('\t', deal1, '\n', '\t', deal2)
		return deal1, deal2
	elif arg == "third":
		deal3 = random.choice(seq)
		print("The third card is ...", deal3)
		return deal3


def check(val1, val2, val3):
	'''checking the cards'''
	seq = ["ACE", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "JOKER", "QUEEN", "KING"]
	if seq.index(val1) < seq.index(val3) < seq.index(val2):
		return "win"
	elif seq.index(val1) > seq.index(val3) > seq.index(val2):
		return "win"
	else:
		return "lose"


if __name__ == "__main__":
	main()
