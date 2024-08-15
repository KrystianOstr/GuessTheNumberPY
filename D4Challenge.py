#Guess the number

from random import randint

user_name = input('What is ur name? ')
print(f"Well {user_name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")

random_number_between_1_and_100 = randint(1,100)

attempts = 1


while attempts != 9:

    user_number_input = int(input(f'What is your number?\n'))

    if user_number_input > 100 and user_number_input < 1:
        print(f'You have chosen a number that is out of play.')
    elif user_number_input > random_number_between_1_and_100:
        print(f'The secret number is lower than {user_number_input}')
    elif user_number_input < random_number_between_1_and_100:
        print(f'The secret number is higher than {user_number_input}')
    else:
        print(f'The secret number is {random_number_between_1_and_100}. YOU WON')
        print(f'You did it in {attempts} attempt/s')
        break


    if attempts < 8:
        print(f"It was your {attempts} attempt")
    else:
        print(f'Try again. {attempts} attempt. The number was: {random_number_between_1_and_100}')
    attempts +=1
