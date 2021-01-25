while True :
	import random
	numguess = 0
	
	name = input('What is your name?\n')
	
	num = random.randint(1,9)
	print('The number I am thinking of is between 1 to 9\n')
	
	while numguess < 3:
		print('\nTake a guess\n')
		guess = input()
		guess = int(guess)
		numguess = numguess + 1
		if guess < num :
			print('The number is too low!!')
			
		elif guess > num :
			print('The number is too high!!')
		
		else :
			break
			
	if guess == num :
		numguess = str(numguess)
		print('Well done ' + name, 'you guessed it correct in ' + numguess, 'guesses!\n')
		
	if guess != num :
		numguess = str(numguess)
		print('Wrong! the correct answer is', + num, '\n')