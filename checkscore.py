import time

scored = input("what was the student's score?: ")
score = int(scored)

print("please give your pupil the terminal and let them find out if they made the cut or not")

def check_score():
    student_check = input("would you like to see your score? type yes or no only: ")

    if student_check == "yes" and score != 0:
        print("checking score... please stand bye")
        time.sleep(2)
        print("score checked")
        time.sleep(1)
        print(f"your score was: {score}.")
    elif student_check == "no" and score >= 40 and score <= 100:
        print("okay your choice") # here i skip the checking score text lines because they do not want to know the number, so we dont tell them
    elif student_check == "no" and score < 40 and score != 0:
        print("dont pretend you dont know how poorly you did")
    elif student_check != "yes" and student_check != "no":
        print("if you do not follow the instructions you will never find out if you passed or failed, please try again!")
        return check_score()   # i think this makes it a return loop. i was trying to get it to force the user to either type yes or no or be redirected to the original prompt. success! i still am unsure what this is called though lol
    
check_score()

if score >= 70 and score <= 100:
    time.sleep(1)
    print(f"you PASSED!")
elif score <= 0:
    time.sleep(1)
    print("there has been an anomoly and you need to retake the test")
elif score > 100:
    time.sleep(1)
    print("drum roll please")
    time.sleep(1)
    print(f"you PASSED with flying colors!!! Great job earning that extra credit!!! and seriously look at this score !!!{score}!!!")
elif score < 40:
    time.sleep(1)
    print(f"you FAILED!! and you need to see you got a {score}.")
elif score <= 40 or score < 70:
    time.sleep(1)
    print("you FAILED")

# this works really well, i like this trick i will have to keep this around to use it in future builds!!

# maestro got mad at me for writing this code because i added elif into the code and we "havent learned that yet" but i used it properly and demonstrated my understanding of the concepts
# if and else, and, not, and or, with this bit of code. oh well i guess AI doesnt appreciate creativity lol. another bit of class practice 
# another spell conjured by the terminal wizard wifiknight!!