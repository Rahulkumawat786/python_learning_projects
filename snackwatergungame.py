from random import choice
print("welcom to snack water gun game!!!")
computer_win = 0
user_win = 0
chances = 10
print("you have total 10 chances")
choices = ["snack","water","gun"]
while chances>0:
    print("\t1.snack")
    print("\t2.water")
    print("\t3.gun")
    user_choice = choices[int(input("Enter your choice = "))-1]
    computer_choice = choice(choices)
    if computer_choice==choices[0]:
        if user_choice==choices[0]:
            print("computer and you both have choosed same choice no one is winner!")
        elif user_choice==choices[1]:
            print("computer have choosed snack so you have lost!")
            computer_win+=1
        else:
            print("computer have choosed sanck so you have won!")
            user_win+=1
    elif computer_choice==choices[1]:
        if user_choice==choices[0]:
            print("computer have choosed water so you have won!")
            user_win+=1
        elif user_choice==choices[1]:
            print("computer and you both have choosed same choice no one is winner!")
        else:
            print("computer have choosed water so computer have won!")
            computer_win+=1
    else:
        if user_choice==choices[0]:
            print("computer have choosed gun so you have lost")
            computer_win+=1
        elif user_choice==choices[1]:
            print("computer have choosed gun so you have won!")
            user_win+=1
        else:
            print("computer and you both have choosed same choice no one is winner!")

    chances-=1

if computer_win>user_win:
    print("computer score: ",computer_win)
    print("your score: ",user_win)
    print("you have lost the game and computer has won try again!")
elif computer_win<user_win:
    print("computer score: ", computer_win)
    print("your score: ", user_win)
    print("congratulation you have won the game!")
else:
    print("computer score: ", computer_win)
    print("your score: ", user_win)
    print("you and computer have same score so no one has won the game!")