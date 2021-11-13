#Program 1: PUP Grading System
#Create a program that will ask for grade percentage.
#Display the equivalent Grade/Mark and Description
#Example:
#Input grade: 87.6
#Grade/Mark: 1.75
#Description: Very Good
import re
import sys

def gradeConvert():
    while True:
        print("(No need for percentage sign)")
        gradePercentage1 = (input("What is your grade in percentage? "))
        if gradePercentage1.isalpha():
            print("Only input grade in percentage!")
        else:
            break
    gradePercentage = float(gradePercentage1)
    if gradePercentage >= 97 and gradePercentage <= 100:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 1.0")
        print("Description: Excellent")    
    elif gradePercentage >=94 and gradePercentage <= 96:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 1.25")
        print("Description: Excellent")
    elif gradePercentage >=91 and gradePercentage <= 93:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 1.5")
        print("Description: Very Good")   
    elif gradePercentage >= 88 and gradePercentage <= 90:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 1.75")
        print("Description: Very Good")
    elif gradePercentage >= 85 and gradePercentage <= 87:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 2.0")
        print("Description: Good")
    elif gradePercentage >= 82 and gradePercentage <= 84:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 2.25")
        print("Description: Good") 
    elif gradePercentage >= 79 and gradePercentage <= 89:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 2.5")
        print("Description: Satisfactory")
    elif gradePercentage >= 76 and gradePercentage <= 78:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 2.75")
        print("Description: Satisfactory")
    elif gradePercentage == 75:
        print(f"Input Grade: {gradePercentage}%")
        print("Grade Mark: 3.0")
        print("Description: Passing")
    elif gradePercentage >= 65 and gradePercentage <= 74:
        print(f"Input Grade: {gradePercentage}")
        print("Grade Mark: 5.00")
        print("Description: Failure")

def extra():
    f = "done"
    print("")
    print("Extra Questions")                   
    while True:
        Inc = input('Is "Inc." writter in your record? Y/N: ')
        if re.match("[a-m, o-x, z, A-M, O-X, Z 0-9,]*$", Inc):
            print('Only write "Y/y or N/n')
        elif re.match("[y, n, Y, N]*$", Inc):
            if Inc.upper() == 'Y':
                print("You are incomplete")
                break
            elif Inc.upper() == 'N':
                break
    while True:
        W = input('Is "W" written in your record? Y/N: ')
        if re.match("[a-m, o-x, z, A-M, O-X, Z 0-9,]*$", W):
                print('Only write "Y/y or N/n"')
        elif re.match("[y, n, Y, N]*$", W):
            if W.upper() == 'Y':
                print("You are already withdrawn.")
                return f
            elif W.upper() == 'N':
                while True:
                    D = input('Is "D" written in your record? Y/N: ')
                    if re.match("[a-m, o-x, z, A-M, O-X, Z 0-9,]*$", D):
                        print('Only write "Y/y or N/n"')
                    elif re.match("[y, n, Y, N]*$", D):
                        if D.upper() == 'Y':
                            print("You are already dropped.")   
                            return f
                        elif D.upper() == 'N':
                            print('Done!')
                            return f

#Function asks for input.
#Function interprets the grade in percentage to grade mark.
#Fuction displays the inputted grade, grade mark, and its description.
f = gradeConvert()

#Function asks if user has "Inc.", "W", or "D" in their record.
#Fuction displays an answer if answered with a "Y/y".
#Function stops if the answer is "N/n"
f = extra()
                                                                                                                   