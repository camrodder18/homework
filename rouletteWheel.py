#Roulette Wheel Colors - Page 117 (40 points)
#Submit a file called wheel.py
#Your program must use if statements, relational operators and logical operators.
#You are not allowed to solve this problem by hard coding the list of red, black and green numbers.

number = int(input('enter a number between 0 and 36.'))

if number < 0 or number >36:
    print ('please enter a number between 0 and 36.')
else:
    if number == 0:
        print('your color is green')
    else:
        if number >0 and number <11:
            if number %2 == 0:
                print ('your color is black.')
            else:
                print ('your color is red.')
        else:
            if number >10 and number <19:
                if number %2 == 0:
                    print('your number is red')
                else:
                    print('your number is black')
            else:
                if number >18 and number <29:
                    if number %2 == 0:
                        print('your number is black.')
                    else:
                        print('your number is red.')
                else:
                    if number >28 and number <37:
                        if number %2 == 0:
                            print('your number is red')
                        else:
                            print('your number is black')






