from Art import higher_and_lower_logo, vs_logo
from day_14 import data

import os
import random 


def high_low():
    '''This fuction displaces you the two choice'''
    print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]}")
    # print(A["follower_count"],B["follower_count"])
    print(vs_logo)
    print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]}")   

def compar(a,b):
    '''This function compare value of followers of your choice'''
    if a>b:
        return "A"
    else:
        return "B"



print(higher_and_lower_logo)
score_point=0
A=random.choice(data)
while True:

    B=random.choice(data)
    if A["follower_count"]==B["follower_count"]:
        B=random.choice(data)

    high_low()
    user_ask= input("Who has the more follower? Type 'A'or 'B' : ").upper()
    
    comparistion= compar(A["follower_count"],B["follower_count"])
    os.system("cls")
    print(higher_and_lower_logo)
    if comparistion==user_ask:
        score_point+=1
        print(f"You'r are right. Your Score is {score_point}")
    else:
        print(f"You'r are Wrong. Your Score is {score_point}")
        break
    
    A=B







