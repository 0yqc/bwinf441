# OPEN INPUT

with open('./inp/ball07.txt', 'r') as f:
	inp = f.read().split('\n')
	inp.remove('')
	inp.pop(0)  # Don't need total number of hours

# schema = {'Montag': {13: 5, 14: 10, 15: 4}, 'Dienstag': {}}

# COMPILE TO LIST

needed = {}
highest = {'n':0, 'day':'', 'h':0}

for line in inp:
	values = line.split(' ')
	if not values[1] in needed:  # add new day to needed list if not added yet
		needed.update({values[1]:{}})
	for h in range(int(values[2]), int(values[3])):  # h: hour
		if not h in needed[values[1]]:  # add new hour if not added yet
			needed[values[1]].update({h:0})
		needed[values[1]][h] += int(values[4])  # add n of balls needed
		if needed[values[1]][h] > highest['n']:  # update the highest amount
			highest['n'] = needed[values[1]][h]
			highest['day'] = values[1]
			highest['h'] = h

# OUTPUT

print(f'''On {highest['day']} at {highest['h']}:00 to {highest['h'] + 1}:00, you need a maximum amount of {highest['n']} balls.''')
print(f'''Am {highest['day']} um {highest['h']}:00 bis {highest['h'] + 1}:00 Uhr werden mit {highest['n']} Bällen die meisten gleichzeitig gebraucht.''')
print()
print('Day: ', highest['day'])
print(f'''Hour: {highest['h']}:00 to {highest['h'] + 1}:00''')
print('Amount: ', highest['n'])
