#Population - Page 163 (45 points)
#Submit a file called pop.py.
#Make sure to use a loop that is based on the number of days to multiply that the user enters


organisms = int(input('enter the starting amount of organisms.'))
dailyIncrease = float(input('enter the percent daily increase.'))/100
days = int(input('enter how many days they will multiply over.'))
first= True
print()
print('Day' '\t' 'population')

for number in range (organisms, days+1):
    if first:
        print(1, '\t', organisms )
        first = False
    population = organisms * dailyIncrease
    organisms = population + organisms
    print(number, '\t', organisms)