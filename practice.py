students = input("How many students are in your class?: ")  # this is an interactive variable and the value is set by the user through a prompt
print("there are", students, "students in your class?")  # this is the built in print function in python. 

miss_cleo = input("i have a prediction, i can guess your name, what is your cats name?: ")

def name():                        # this is defining the function named name()
    name = "Charles"               # this assigns a value to name()
    return name                    # this returns the value name to the funciton name() to be able to be called globally outside of the function

print("you're name is", name(), "was i right?")    # this prints the quoted text and the value of name() defined inside the function name()
name1 = "Henry"                    # this is a new name variable, this is a global variable
message = "and your friend's name is "  # this is also a variable
last_message = message + name1     # this variable is the value of the last 2 variables values combined str + str
print(last_message)                # this prints the value of the last_message variable 
print(name() + ", you are friends with", name1)   # this prints the name() function value from the variable inside the function name, the quoted text, and the new name variable

def name2():
    name2 = "Terry"                # this is a local variable, it is not available outside of the function, the function uses the built in print function in python in the next line
    print(name2)

print(name2(), "this prints None because the function returns a value of None because the variable name2 is not stored outside the function")   # this will print None because the function doesnt return a value for name2() and therefore has no value or a value of None in python because every function produces a value even if the value is None
print("The last variable is a local variable and cannot be called outside of the function name2() but the function name2() prints Terry. Confused? So was I lol")  # The last variable is a local variable and cannot be called outside of the function

hour = input("How many hours do you study each day?: ")  # this is a str
minutes = int(hour) * 60           # i convert the str value of hour into an int to multiply by 60
seconds = float(minutes) * 60      # i convert the int value of minutes to a float value
milliseconds = (seconds) * 1000    # i didnt need to convert this to a float because seconds is already a float and the product of a float and an int will be a float value by default 
per_week = int(hour) * 5           # i converted the str to an int here to multiply by 5

print(f"if you study {hour} hours a day, then you study {minutes} minutes every day. You also study {seconds} seconds and {milliseconds} milliseconds each day as well. You study a grand total of {per_week} hours per week in a 5 day week")

print(hour,":hours")         # just printing all of the variables values and their data types respectively here to show i understand the concept. 
print(type(hour))              

print(minutes,":minutes")
print(type(minutes))

print(seconds,":seconds")      # that long f string on line 30, i learned i could do one long f string and call all the variables with curly brackets in the string from a fellow maestro student on the reddit community
print(type(seconds))

print(milliseconds,":milliseconds")
print(type(milliseconds))

print(per_week,":hours/week")
print(type(per_week))


# i decided to add in some data types and converstions and some math at the bottom of this code. python is pretty damn cool. this was another week one material practice session in vscode
# another spell conjured by the terminal wizard wifiknight