#!/usr/bin/env python3

# ask for grade score
grade = int(input("What score did you receive? "))

if grade > 100:
    print("Not possible, 100 is the highest score")
elif grade >= 90:
    print("Congrats, you got an A")
elif grade >= 80:
    print("Really good, you got a B")
elif grade >= 70:
    print("Not bad, you got a C")
elif grade >= 60:
    print("Just made it with a D")
else:
    print("Sorry, you got a F")

