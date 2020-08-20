#! python3

import random

def start_round():
	player_1 = []
	for i in range(int(lives1)):
		player_1.append(random.randint(1,6))
		player_1.sort()

	print(player_1)

	player_2 = []
	for i in range(int(lives2)):
		player_2.append(random.randint(1,6))
		player_2.sort()

	#print(player_2)

	player_3 = []
	for i in range(int(lives3)):
		player_3.append(random.randint(1,6))
		player_3.sort()

	#print(player_3)

def human_turn():
	if turn ==1:													#something to make it so on first round this happens, but if the bets go round again, a different set is available with Dudo
		value = 0
		while int(value) > 6 or int(value) < 2:                       #cannot be 1, must be a number between 1,6 (die), need to keep asking them this question till they get it right
			print('What value die would you like to bet on?')
			try:
				value = int(input())
				if value ==1:
					print('You cannot open bidding on 1s')
				if value > 6 or int(value) < 2:
					print('The value must be between 2 and 6')

			except ValueError as error:                                     #will need an error so only integers can be passed to this
				print('please enter an number from the number pad.')

		print(str(value) + ' is your chosen value')
			
		quantity = 0
		while int(quantity) < 1 or int(quantity) > (lives1+lives2+lives3):						#quantity between 1 and sum of lives remaining
			print('How many ' + str(value) + 's would you like to bet?')
			try:
				quantity = int(input())
				if quantity <1:
					print('You need to bet at least 1, silly!')
				if quantity > (lives1+lives2+lives3):
					print('I don\'t think you\'ll win this bet... Please bet fewer than the total remaning die.')

			except ValueError as error:                                     #will need an error so only integers can be passed to this
				print('please enter an number from the number pad.')

		print('You have bet ' + str(quantity) + ' ' + str(value) + 's' )
	else:
		input()
		#non opening turns
		#option to call Dudo
		#option to bid more quantity on the same value
		#option to change the value - this has an affect on quantity, presumably must add 1

def computer2_turn():
	#will need an option for if they have to open bidding - maybe to do with quantity and value being empty - these must be wiped at the end of a round
	#check their die to see how many of each number they have
	#calculate the odds of each value given the limits on quantity
	#calculate odds of current bet being wrong
	#choose option with highest value
	#if Dudo chosen need a checking function
	#leads to someone losing a life depending on if check right or wrong
	#new round restarts with loser, by setting turn
	print('comp2')
	global lives1
	lives1 = lives1 -1
	#print(lives1)
	return lives1

def computer3_turn():
	#basically copy computer 2
	#currently an attempt to see if it is possible to reduce lives from a turn function
	#which eventually ends the while loop or prevents a player taking a turn
	#leading to a winner
	print('comp3')
	global lives2
	lives2 = lives2 - 1
	#print(lives2)
	livesleft()
	return lives2

def livesleft():
	LivesLeft = []
	if lives1 > 0:
		LivesLeft.append(lives1)
	if lives2 > 0:
		LivesLeft.append(lives2)
	if lives3 > 0:
		LivesLeft.append(lives3)
	global PlayersLeft
	PlayersLeft = LivesLeft
	print(PlayersLeft)
	print(len(PlayersLeft))
	return PlayersLeft

def winner():
	if lives1 != 0:
		print('You have conquered the machines human! Thank you for playing Perudo!')
	if lives2 != 0:
		print('Computer 2 won in the end, restart the program to see if you can beat them next time!')
	if lives3 != 0:
		print('Computer 3 won in the end, restart the program to see if you can beat them next time!')

lives1 = 5
lives2 = 5
lives3 = 5
PlayersLeft = []
value = 0
quantity = 0

livesleft()

while len(PlayersLeft) > 1 :
	start_round()
	for turn in range(1,10000):
		if (int(turn)%3 == 1) and (int(lives1) != 0):
			human_turn()
			livesleft()
		if (int(turn)%3 == 2) and (int(lives2) != 0):
			computer2_turn()
			livesleft()
		if (int(turn)%3 == 0) and (int(lives3) != 0):
			computer3_turn()
			livesleft()

winner()