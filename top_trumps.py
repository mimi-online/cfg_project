""" TOP TRUMPS """

# By Mariya Ivanenkiv

#The target of the program is to get a character from
#Star wars and record the score during the game.


import random
import requests

user_count = 0 # 1. At first we set our score count to zero for both of the players.
opp_count = 0

def random_char(): # 2. Here the program generates a random star wars character for us, and return values about it such as mass or height.
    star_wars_num = random.randint(1, 10)
    url = 'https://swapi.dev/api/people/{}/'.format(star_wars_num)
    response = requests.get(url)
    people = response.json()

    return {
        'name':people['name'], #3. Here our programme will pull the information out of the API ready to be used,
        'height':people['height'], #chosen by player.
        'mass':people['mass']   
    }


def game(user_count, opp_count): #4. In the function we add the arguments for user and opponent count,
    user_char = random_char()    #for the function to be pass here it will be our scores.

    print('Your character is {}'.format(user_char['name'])) #5. Here our code reveals to the player what their character is.
    choice_of_stat = input('Which stat do you want to use ? (height, mass)') #6. Here our opponent recieves the choice parametre to use to

    opp_char = random_char()
    print('The opponent chose {}'.format(opp_char['name'])) #6. Our programme generates a random character for our opponent.

    user_stat = user_char[choice_of_stat] 
    opp_stat = opp_char[choice_of_stat]

    if user_stat > opp_stat: #7. Our result is generated by the if, elif and else block! 
        print("You win !")
        user_count = user_count + 1 # We add one to our current score for user

    elif user_stat < opp_stat:
        print("You lose !")
        opp_count = opp_count + 1 # We add one to our current score for opponent

    else:
        print("Draw !")

    return user_count, opp_count # 8. Our programme returns the score for 

num_of_rounds = int(input('How many rounds do you want to play? ')) # We ask the user to choose a number of rounds, so the
                                                                    # function knows how many rounds of the game to run and record scores of.
i = 0 # We use a loop to run the game function as many times as we want (the rounds).
while i < num_of_rounds:
    user_count, opp_count = game(user_count=user_count, opp_count=opp_count) # To not clear our values to zero after running the program
                                                                             # each time, we will say that.
    i += 1


with open('scores.txt', 'w+') as scores_file: # We will open a file and records the scores of our rounds at the end of running our program.
    scores = 'Scores \nUser = {} \nOpponent = {}'.format(user_count, opp_count)
    scores_file.write(scores)