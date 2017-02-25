userBudget = float(input('please enter monthly budget: '))
runningCharges = '0'
totalExpenses = 0

while runningCharges == '0':
    userExpense = float(input('enter an expense: '))
    totalExpenses += userExpense
    runningCharges = input('do you have more charges?: Type y for yes,'+\
                           ' any key for no')
if totalExpenses > totalExpenses:
    print ('you are over your', userBudget, 'budgey by' totalExpenses - userBudget)
elif userBudget > totalExpenses
    print('you are under budeget of', userBudget, 'by', userBudget - totalExpenses)
else:
    print('you used exactly your budget of' userBudget".")