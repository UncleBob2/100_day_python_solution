
# # create random generator without repeating
# for _ in range(len(data)+1):
#     new = randint(1,len(data))
#     if new not in selected_num:
#         selected_num.append(new)

from day_14_artwork import logo, vs
from day_14_game_data import data
from random import randint
import os


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for windows platfrom
        _ = os.system("cls")
    print(logo)
    # print out some text


def check_answer(score, choosen, choiceA, choiceB):
    num_followers_A = int(choiceA['follower_count'])
    num_followers_B = int(choiceB['follower_count'])
    #print(followers_A, followers_B)
    if (num_followers_A > num_followers_B and choosen =="a") or (num_followers_B > num_followers_A and choosen == "b") :
        screen_clear()
        score +=1
        print(f"You're right! Current score: {score}.")
        return score
    else:
        screen_clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        score = -1
        return score 


screen_clear()
selected_num = []
ranA = randint(0,len(data)-1)
choiceA_info = (data[ranA])
score = 0
answer = True

while score != -1:
    print('Compare A: '+ choiceA_info['name'] + ', ' + choiceA_info['description'] + ', from ' + choiceA_info['country'])

    ranB = randint(0,len(data)-1)
    if ranA == ranB:
        ranB = randint(0,len(data)-1)
    choiceB_info = (data[ranB])
    print(vs)
    print('Compare B: '+ choiceB_info['name'] + ', ' + choiceB_info['description'] + ', from ' + choiceB_info['country'])
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    score = check_answer(score, choose, choiceA_info, choiceB_info)
    choiceA_info = choiceB_info

