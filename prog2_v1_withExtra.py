#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number

def lowestFinder():
    while True:
        number1 = input('Number 1: ')
        if number1.isalpha():
            print('Only write numbers!')
        elif number1.isdigit():
            break
    while True:
        number2 = input('Number 2: ')
        if number2.isalpha():
            print('Only write numbers!')
        elif number2.isdigit():
            break
    while True:
        number3 = input('Number 3: ')
        if number3.isalpha():
            print('Only write numbers!')
        elif number3.isdigit():
            break
    if number1 < number2 and number1 < number3:
        print('Number 1 is the lowest number.')
    elif number2 < number1 and number2 < number3:
        print('Number 2 is the lowest number.')
    elif number3 < number1 and number3 < number2:
        print('number 3 is the lowest number.')
    else:
        print('The numbers are equal!')


lowestFinder()