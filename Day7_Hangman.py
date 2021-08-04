import random
from words import words_list
from art import logo,stages
word = random.choice(words_list)


print(logo)
lives = 6
display = []
for _ in word:
 
	display += "_"


is_letter = True
while is_letter:
    stage = stages[lives]

    guess = input("Guess a letter: ").lower()
    

    for num in range(len(word)):
       letter = word[num]

       if guess == letter:

       	 if guess in display:
       	 	print("You guess '{}' already in display".format(guess))

         display[num] = guess


    
    print(''.join(display))

    
    if guess not in word:
    	lives -= 1
    	print("You guess letter '{}' not in word,you lose life".format(guess))
    	if lives == 0:
    		is_letter = False
    		print("You lose")
    		print(word) 
			
    

    elif  "_" not in display:
        is_letter = False
        print("Yeah, you guess correctly")

    
    print(stages[lives])
    