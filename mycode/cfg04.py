#!/usr/bin/env python3

user_file = input("What is the file to open?")

## posible option to replace the with statement
## with open(input("What is the file to open?"). "r") as configfile:

## create file object in "r"ead mode
with open(user_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

