# Get Speed and Hours
speed = float(input('Enter the speed in mph: '))
time = float(input('How many hours traveled? '))
distanceTraveled = float(0.0)

print ('Hours \t Distance Traveled')
print ('----------------------------')

# Calculate Distance Traveled
for time in range (1, 1 + int(time)):
    distanceTraveled = speed * time
    print (time, '\t', distanceTraveled, 'miles')