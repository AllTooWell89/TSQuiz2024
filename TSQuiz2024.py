print("Welcome to my Taylor Swift quiz!")

playing = input("Ready to play? ")

if playing != "yes":
    quit()

print("Okay! Let's Start.")
score = 0


answer = input("What is Taylor Swift's middle name? ")
if answer == "Alison":
    print('Correct!')
if answer == "alison":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What album did Taylor release in 2012? ")
if answer == "Red":
    print('Correct!')
if answer == "RED":
    print('Correct!')
if answer == "red":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    

answer = input("What is the name of Taylor's 2019 documentary? ")
if answer == "Miss Americana":
    print('Correct!')
if answer == "miss americana":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    

answer = input("What is Taylor's brother's first and last name? ")
if answer == "Austin Swift":
    print('Correct!')
if answer == "austin swift":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What is Taylor's favorite number? ")
if answer == "13":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print ("You scored " + str(score) + " questions correct!")
print ("You scored " + str((score/5) *100) + "%. ")

