import os 
os.system('clear')
import random 

# Information:
print('type \'quit\' to exit the game\n')
print()

######################### ANSWER-LIST ##########################
answer_list = ['rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors']
######################## ANSWER-LIST ###########################

#Scoreboard:
score_user = 0
score_user2 = 0

print('scoreboard')
print(f'	|user:{score_user}')
print(f'	|computer:{score_user2}')
print()

# Actual Game Interface:

# Input From User:
while score_user < 5 and score_user2 < 5:
  user2_choice = random.choice(answer_list)
  user_choice = input('Enter your choice: ')
 
# Win results:
  if user_choice == 'rock' and user2_choice == 'scissors':
   os.system('clear')
   print(f'you chose {user_choice} and computer chose {user2_choice}')
   print()
   score_user += 1
   print('scoreboard')
   print(f'	|user: {score_user}')
   print(f'	|computer: {score_user2}')
   print()
  elif user_choice == 'paper' and user2_choice == 'rock':
   os.system('clear')
   print(f'you chose {user_choice} and computer chose {user2_choice}')
   print()
   score_user += 1
   print('scoreboard')
   print(f'	|user: {score_user}')
   print(f'	|computer: {score_user2}')
   print()
  elif user_choice == 'scissors' and user2_choice == 'paper':
   os.system('clear')
   print(f'you chose {user_choice} and computer chose {user2_choice}')
   print()
   score_user += 1
   print('scoreboard')
   print(f'	|user: {score_user}')
   print(f'	|computer: {score_user2}')
   print()
  elif user_choice == user2_choice:
   os.system('clear')
   print(f'you chose {user_choice} and computer chose {user2_choice}')
   print()
   print('scoreboard')
   print(f'	|user: {score_user}')
   print(f'	|computer: {score_user2}')
   print()
  elif user_choice == 'quit':
   os.system('clear')
   print('quitting...\n')
   break

# Lose results:
  else:
   os.system('clear')
   print(f'you chose {user_choice} and computer chose {user2_choice}')
   print()
   score_user2 += 1
   print('scoreboard')
   print(f'	|user: {score_user}')
   print(f'	|computer: {score_user2}')
   print()
# Scoreboard when either won:  	
if score_user2 == 5 or score_user == 5:
	os.system('clear')
	print('game over\n')
	print()
	print('scoreboard')
	print(f'	|user: {score_user}')
	print(f'	|computer: {score_user2}\n')
	print()
	
	if score_user > score_user2:
		print('You won')
	elif score_user2 > score_user:
		print('Computer won')
	else:
		print('The game ended in a draw!')
    
# Result if User typed 'quit':
else:
  print('game ended\n')
