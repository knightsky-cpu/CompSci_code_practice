scored = input("what was the student's score?: ")
score = int(scored) * 1

print("please give your student the keyboard and let them find out if they made the cut or not")

def check_score():
    student_check = input("would you like to see your score? type yes to see your results and type no to skip to finding out if you passed or failed: ")

    if student_check == "yes":
        print("checking score... please stand bye")
        print("score checked")
        print(f"your score was: {score}.")
    elif student_check == "no":
        print("okay your choice, now we shall see if you passed")
    elif student_check != "yes" and student_check != "no":
        print("if you do not follow the instructions you will never find out if you passed or failed, please try again!")
        return check_score()    # i think this makes it a return loop. i was trying to get it to force the use to either type yes or no or be redirected to the original prompt. success! i still am unsure what this is called though lol
    
check_score()

if score >= 70 and score <= 100:
    print("you PASSED!")
elif score <= 0:
    print("there has been an anomoly and you need to retake the test")
elif score > 100:
    print("you PASSED with flying colors!!! Great job earning that extra credit!!!")
elif score <= 40:
    print("Congrats!! you FAILED!!! and you performed so poorly we didnt know how to tell you without being disrespectful, please gather your things and remove yourself from the exam room")
elif score <= 40 or score < 70:
    print("you FAILED")



# this works really well, i like this trick i will have to keep this around to use it in future builds!!