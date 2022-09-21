#!/usr/bin/python3
"""
a 1 hour script test to see what i can make
"""
import random
import os
os.system('clear')
print ("Hello and welcome to my casino game")
money=100

def money_increase(value_bet):
	global money
	money+=int(value_bet)

def money_decrease(value_bet):
	global money
	money-=int(value_bet)

def higher_lower():

	random_number_1=random.randint(1,10)
	random_number_2=random.randint(1,10)
	
	print ("Your first number is ",random_number_1)
	value_of_bet=input("how much do you want to bet?")
	print ("Is the second number higher(h) of lower(l) for 1 money?")
	USER_INPUT_HL=input("")
	#ACCEPTABLE_INPUT_HL=["h","l"]
	#if USER_INPUT_HL not in ACCEPTABLE_INPUT_HL:
	if USER_INPUT_HL=="h":
	#Higher
		if random_number_2 >=random_number_1:
			money_increase(value_of_bet)
			print("Winner")
			print ("RN2=",random_number_2)
		else: 
			money_decrease(value_of_bet)
			print("Looser")
			print ("RN2=",random_number_2)

	else:
		if random_number_2 >=random_number_1:
			money_decrease(value_of_bet)
			print("Looser")
			print ("RN2=",random_number_2)
		else:
			money_increase(value_of_bet)
			print("Winner")
			print ("RN2=",random_number_2)

	# Lower


def horse_race():
	global money
	
	print("there are 3 horses blue (evens), orange(2/1) and red(7/1)")
	print("by default you can only bet 1£")
	USER_INPUT_HR=input("please choose a horse (b/o/r)")
	try:
		#HORSES_IN_RACE=["b","b,"b","o","o","o","r"]
		HORSES_IN_RACE=["b","b","b","o","r"]
	except:
		print ("Errored")
		import pdb
		pdb.set_trace()
		
	HORSE_RESULT=random.choice(HORSES_IN_RACE)
	print ("Winner of the race is " ,HORSE_RESULT)
	if USER_INPUT_HR==HORSE_RESULT:
		print ("yeh you won")
		if USER_INPUT_HR=="b":
			money_increase(value_bet=1)
		elif USER_INPUT_HR=="o":
			money_increase(value_bet=2)
		else:
			money_increase(value_bet=7)
	else:
		print("you lost")
		money_decrease(value_bet=1)
		
			
		

	

	

def menu_choice():
	print("You have money left=",money)
	print ("Your Choices are...")
	print ("1 player high or lower")
	print ("2 bet the horses")
	USER_INPUT=input("")
	ACCEPTABLE_INPUT=[1,2]
	if int(USER_INPUT) not in ACCEPTABLE_INPUT:
		print ("bad input please return to where you came from")
		return(0)
	else:
		if int(USER_INPUT)==1:
			higher_lower()
		else:
			horse_race()
			pass

while money > 0:
	menu_choice()
	print ()
print ("you have ran out of money please come again soon")
	

