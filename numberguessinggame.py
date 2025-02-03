#number guessing game! not sure how to prevent valueerror when entering a non integer during main game loop yet, but besides for that everything should be robust.
import random

attempts = 0

print('')
print('+------------------------------------+')
print('|Welcome to the Number Guessing Game!|')
print('|   Please Select a Difficulty:      |')
print('|   Easy      Medium      Hard       |')
print('+------------------------------------+')
print('')

#difficulty selection and error prevention via while statement
dif = input('Difficulty: ')
while dif != 'Easy' and dif != 'Medium' and dif != 'Hard':
    print('')
    print('+----------------------------------------+')
    print('|Error! Please Select a Valid Difficulty!|')
    print('+----------------------------------------+')
    print('')
    dif = input('Difficulty: ')
    
#secret number assigned based on difficulty
if dif == 'Easy':
    ans = random.randint(1, 10)
    print('')
    print('+------------------------------------+')
    print('|    The Number is Between 1 and 10. |')
    print('|        You Have 5 Guesses.         |')
    print('+------------------------------------+')
    print('')
elif dif == 'Medium':
    ans = random.randint(1, 25)
    print('')
    print('+------------------------------------+')
    print('|    The Number is Between 1 and 25. |')
    print('|        You Have 5 Guesses.         |')
    print('+------------------------------------+')
    print('')
elif dif == 'Hard':
    ans = random.randint(1, 50)
    print('')
    print('+------------------------------------+')
    print('|    The Number is Between 1 and 50. |')
    print('|        You Have 5 Guesses.         |')
    print('+------------------------------------+')
    print('')
    
    
#main Game loop
guess = int(input('Guess: '))
while guess != ans and attempts < 4:
    if guess < ans:
        print('')
        print('+------------------+')
        print('|Higher! Try Again!|')
        print('|Attempts Left: ',4 - attempts,'| ')
        print('+------------------+')
        print('')
        guess = int(input('Guess: '))
        attempts = attempts + 1
    elif guess > ans:
        print('')
        print('+------------------+')
        print('|Lower! Try Again! |')
        print('|Attempts Left: ',4 - attempts,'| ')
        print('+------------------+')
        print('')
        guess = int(input('Guess: '))
        attempts = attempts + 1

#runs after main game loop breaks, either because the player is out of attempts or they have guessed correctly.
if guess != ans:
    print('')
    print('+--------------------------+')
    print('|Out of Attempts, You lose!|')
    print('|The Secret Number Was',ans,' |')
    print('+--------------------------+')
    print('')
else:
    print('')
    print('+--------+')
    print('|You Win!|')
    print('+--------+')
    print('')