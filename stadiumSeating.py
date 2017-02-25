#Your program should consist of 4 functions.  It should start and be driven from a main function.
#   There should be a function for each of the stadium seating classes.  These functions should take in one argument,
# the number of seats, and print out the appropriate revenue.
# Call these functions from your main.  The input should be collected in the main function.
#Make sure the output is formatted to two decimal places and looks like currency.

#NOTE: You do not have to output the total revenue of tickets sold.
# Only the revenue for class A tickets, class B tickets and class C tickets.

#For example, if you sold $100 of class a, $200 of class b and $400 of class c,
#  you would NOT have to say you sold $700 of total tickets, only the amount for the 3 classes.
#Add your .py file to a new git repository on your machine.

numClassA = 0
numClassB = 0
numClassC = 0

numTotal = 0

def ClassA():
    ticketsA =float(input('enter number of class a tickets'))
    return (ticketsA * 20)



def ClassB():
    ticketsB =float(input('enter number of class b tickets'))
    return (ticketsB * 15)

def ClassC():
    ticketsC = float(input('enter number of class c tickets'))
    return (ticketsC * 10)

def main():
    numClassA = format(ClassA(),',.2f')
    numClassB = format(ClassB(),',.2f')
    numClassC = format(ClassC(),',.2f')
    print('total class A $',numClassA, ' sales.')
    print('total class B $',numClassB, ' sales.')
    print('total class C $',numClassC, ' sales.')
main()