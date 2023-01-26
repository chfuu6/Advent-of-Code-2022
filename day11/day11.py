import math
f = open('puzzle.txt', 'r')
lines = f.read().split('\n')
monkey0 = [99, 63, 76, 93, 54, 73]
monkey1 = [91, 60, 97, 54]
monkey2 = [65]
monkey3 = [84, 55]
monkey4 = [86, 63, 79, 54, 83]
monkey5 = [96, 67, 56, 95, 64, 69, 96]
monkey6 = [66, 94, 70, 93, 72, 67, 88, 51]
monkey7 = [59, 59, 74]
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
primary = 2*17*7*11*19*5*13*3
def worry(name, items):
	global count0, count1, count2, count3, count4, count5, count6, count7
	if name == 'monkey0':
		for item in items:
			item *= 11
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 2 == 0:
				monkey7.append(item)
			else:
				monkey1.append(item)
			count0 += 1
		items.clear()
	elif name == 'monkey1':
		for item in items:
			item += 1
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 17 == 0:
				monkey3.append(item)
			else:
				monkey2.append(item)
			count1 += 1
		items.clear()
	elif name == 'monkey2':
		for item in items:
			item += 7
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 7 == 0:
				monkey6.append(item)
			else:
				monkey5.append(item)
			count2 += 1
		items.clear()
	elif name == 'monkey3':
		for item in items:
			item += 3
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 11 == 0:
				monkey2.append(item)
			else:
				monkey6.append(item)
			count3 += 1
		items.clear()
	elif name == 'monkey4':
		for item in items:
			item *= item
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 19 == 0:
				monkey7.append(item)
			else:
				monkey0.append(item)
			count4 += 1
		items.clear()
	elif name == 'monkey5':
		for item in items:
			item += 4
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 5 == 0:
				monkey4.append(item)
			else:
				monkey0.append(item)
			count5 += 1
		items.clear()	
	elif name == 'monkey6':
		for item in items:
			item *= 5
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 13 == 0:
				monkey4.append(item)
			else:
				monkey5.append(item)
			count6 += 1
		items.clear()
	elif name == 'monkey7':
		for item in items:
			item += 8
			item = item % primary
			# item /= 3
			# item = math.floor(item)
			if item % 3 == 0:
				monkey1.append(item)
			else:
				monkey3.append(item)
			count7 += 1
		items.clear()
			
for i in range(10000):
	worry('monkey0', monkey0)
	worry('monkey1', monkey1)
	worry('monkey2', monkey2)
	worry('monkey3', monkey3)
	worry('monkey4', monkey4)
	worry('monkey5', monkey5)
	worry('monkey6', monkey6)
	worry('monkey7', monkey7)


ans = [count0, count1, count2, count3, count4, count5, count6, count7]
ans.sort()

print(ans[-1]*ans[-2])

