monthlyBudget = float(input('enter a number: '))
expenses = float(input('enter monthly expense: '))
stop = 'stop'
i=0

while expenses != 'stop':
    print('your running monthly expenses are')
    print('$',expenses, 'dollars.')
    i+=1

    anotherCharge = float(input('enter antother charge'))
    expenses = anotherCharge + expenses

    if expenses > monthlyBudget:
        print ('you are over budget by', monthlyBudget - expenses)
    else:
        print('your running monthly expenses are')
        print(expenses)
print(expenses/ i)





