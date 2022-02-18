# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Brian Goin
# Creation Date: 2/18/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
#####Missing the parentheses at the end of line 6, after them)
import random
import time

def displayintro():  ## Intro should be lowecase, referred to as LC from herein
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def choosecave(): ##LC
	cave = ()
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return (cave)  #### missing parentheses, caves should be singular

def checkcave(chosencave): ##LC cave
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlycave = random.randint(1, 2)  ##LC cave

	if chosen cave == str(friendlycave): ## LC cave and space
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')  ##Missing parenthases ('Gobbles you down in one bite!')

playagain = 'yes' ##LC
while playagain = 'yes' or playagain = 'y':  ##Can't have a single variable with two different definitions, missing
	displayintro()      ## the colon after while:  Line 45  ## LC again in line 45 and intro in 46
	caveNumber = choosen cave:()  ##Should be chosen cave:()  missing space
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for playing")   ## should be playing not planing

