# Insertion sort implementation

import random

from copy import deepcopy

array = [each for each in range(10)]
random.shuffle(array)

def insertion_sort(array=[], ascending=True):
	array = deepcopy(array)
	i, j = 0, 0
	while j < len(array):
		# swaps = 0
		while i < len(array) - 1:
			if ascending:
				expression = array[i] > array[i+1]
			else:
				expression = array[i] < array[i+1]
			if expression:
				# swaps += 1
				array[i], array[i+1] = array[i+1], array[i]
			i += 1
		j += 1
		# print('Pass', j, '-', array, 'Swaps', swaps)
		i = 0
	return array

print('Unsorted', array)
print('Ascending', insertion_sort(array))
print('Descending', insertion_sort(array, False))


# Rock, Paper and scissors Game

title = '''
=============================
|    Rock Paper Scissors    |
=============================
'''

msg = '''
Possible Choices
  1: Rock
  2: Paper
  3: Scissors

Enter choice: '''

BOT,YOU, TRIALS = 0, 0, 0
CHOICES = {
	1: 'Rock',
	2: 'Paper',
	3: 'Scissors'
}
POSSIBLE_CHOICES = (
	({1, 2}, 2),
	({1, 3}, 1),
	({2, 3}, 3),
	)

def bot_choice():
	return random.choice([1, 2, 3])

def results(data):
	for choice in POSSIBLE_CHOICES:
		if choice[0] == data:
			return choice[1]

print(title)

dashboard = '''
Dashboard
  Wins: {}
  Loses: {}
  Ties: {}
'''

while True:
	try:
		user_choice = int(input(msg).strip())
	except Exception as e:
		user_choice = None

	if user_choice is not None and user_choice in CHOICES:
		bot = bot_choice()
		print(f'You: {CHOICES[user_choice]} | Bot: {CHOICES[bot]}')
		if user_choice == bot:
			print('Tie!')
		else:
			if user_choice is results({user_choice, bot}):
				YOU += 1
				print('Won!')
			else:
				BOT += 1
				print('Lose!')
		TRIALS += 1
	else:
		print('Invalid choice')
	print(dashboard.format(YOU, BOT, TRIALS-(YOU+BOT)))

	next_attempt = input('\nDo you want to play again (y/n)? ').strip().lower()
	if next_attempt == 'n' or next_attempt not in ['y', 'n']:
		break