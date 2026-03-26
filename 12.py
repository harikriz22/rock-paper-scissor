# # math
# # time
# # random
# # os
# # sys


# import math

# # print(math.sqrt(25))
# # print(math.factorial(5))


# # print(math.floor(35.6))
# # print(math.ceil(35.6))
# # floor -- 35.6  -- 35
# # ceil  --  35.6 -- 36

# import random

# # random.randint()
# # random.choice()

# # print(random.randint(1,100000))

# # fruits = ['apple', 'orange', 'pienapple',
# #           'grapes', 'banana', 'mango', 'watermelon']


# # print(random.choice(fruits))

# # coin toss 


# # ch = ['heads','tails']

# # print(random.choice(ch))


# # ch = random.randint(0,1)
# # if ch:
# #     print('heads')
# # else:
# #     print('tails')

# # bool(0) - false
# # bool(1) - True


# create a rock paper scissor game 

import random

ch =['rock','paper','scissor']

comp = random.choice(ch)

player = ''

while player not in ch:
    player = input(('enter your choice : rock/paper/scissor:-')).lower()

print(f'computer chose {comp} player chose {player}')

if player == comp:
    print('its a tie !!!!!!!!!!!!!!!')
elif player == 'rock':
    if comp =='paper':
        print(f'paper covers rock ,computer wins ')
    else:
        print(' rock beats scissor player wins')        
elif player == 'paper':
    if comp =='scissor':
        print('computer wins scisssor cuts paper')
    else:
        print("paper covers rock player wins")

elif player == 'scissor':
    if comp == 'rock':
        print('rock beats scissor comp wins')
    else:
        print('scissor cuts paper player wins ')


# a = 'mOhAn DaS'

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
