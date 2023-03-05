import random as r
def batting():
    score=0
    while(True):
        user_input=int(input("Choose your option (0-6) :- "))  
        pc_input=int(r.randint(0,6))
        if(user_input>=0 and user_input<=6):
            print("PC :- ",pc_input,"\nYOU :- ",user_input)
            if(pc_input==user_input):
                print("Out !!!")
                print("Score :- ",score)
                break;
            else:
                score+=user_input
                print("Score :- ",score)
        else:
            break;
    return score

def bowlling():
    score=0
    while(True):
        user_input=int(input("Choose your option (0-6) :- "))  
        pc_input=int(r.randint(0,7))
        if(user_input>=0 and user_input<=6):
            print("PC :- ",pc_input,"\nYOU :- ",user_input)
            if(pc_input==user_input):
                print("Out !!!")
                print("Score :- ",score)
                break;
            else:
                score+=pc_input
                print("Score :- ",score)
        else:
            break;
    return score

print("ODD OR EVEN")
option=input("\nChoose your option :- \n1.BATTING\n2.BWOLING \n")
if(option=="1" or option.lower()=="batting"):
    print("Now you are Batting")
    battingScore=batting()
    print("Your total score :- ",battingScore)
    print("\nNow you are Bowling")
    bowllingScore=bowlling()
    print("Your score = ",battingScore,"\n PC Score = ",bowllingScore)
elif(option=="2" or option.lower()=="bowling"):
    print("Now you are Bowling")
    bowllingScore=bowlling()
    print("You required to score :- ",bowllingScore)
    print("\nNow you are Batting")
    battingScore=batting()
    print("Your score = ",bowllingScore,"\n PC Score = ",battingScore)
else:
    print("Error")

if(battingScore>bowllingScore):
    print("You win !!!")
elif(battingScore<bowllingScore):
    print("You Lose !!!")
else:
    print("Draw match")
