import random
tempList = []
sum = 0;
for i in range(7):
	tempList.append(random.randint(26,40))
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
shelly = 0
for i in range (len(tempList)):
	if tempList[i]%2 == 0:
		shelly+=1;
highest = 0
lowest = 0
for i in range (len(tempList)):
	sum+=tempList[i]
	if tempList[highest] < tempList[i]:
		highest = i
	if tempList[lowest] > tempList[i]:
		lowest = i 
avg = sum/7
aboveAvg = []
for i in range (len(tempList)):
	if tempList[i] > avg:
		aboveAvg.append(days[i])
for i in range (7):
	print(days[i] + ": " + str(tempList[i]))
print("*\n*")
print( "Shelly had " + str(shelly) + " good days")
print("*\n*")
print("The hottest day was " + str(days[highest]) + " the temp was " + str(tempList[highest]))
print("The coldest day was " + str(days[lowest]) + " the temp was " + str(tempList[lowest]))
print("*\n*")
print("The average temp was " + str(avg))
print("Days hotter than average: " + str(aboveAvg))

#bonus
tempListSorted = [0,0,0,0,0,0,0]
for i in range(len(tempList)):
	location = 0
	num = tempList[i];
	for j in range(len(tempList)):
		if num > tempList[j]:
			location+=1
	while tempListSorted[location] != 0 and location<7:
		location+=1
	tempListSorted[location] = num
print(tempListSorted)
