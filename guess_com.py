import random 

def guess(n):

	random_number = random.randint(1,n)
	guess = 0

	while guess != random_number:

		guess = int(input("Enter the number between 1 and {}: ".format(n)))

		if guess < random_number:
			print("Sorry, try again.Is too low...")
		elif guess > random_number:
			print("Sorry,try again.Is too high..")



	print("Yeah, you guess the number {} correctly".format(random_number))

guess(10)

