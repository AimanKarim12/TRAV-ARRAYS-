#Traverse Arrays

#QUESTION 1
array = ["yes", "yes", "maybe", "no", "no", "no"]

yes = 0
no = 0
maybe = 0
for x in array:
	if x == "yes":
		yes += 1
	elif x == "no":
		no += 1
	else: x == "maybe"
	maybe += 1


#QUESTION 2
ages = [14, 17, 15, 12, 19, 23, 38]

limit = 18

# GREATER THAN 18
count = 0
for i in ages :
	if i > limit :
		count = count + 1

print (f"The numbers greater than 18 : {count}")

# LESS THAN 18
count = 0
for i in ages :
	if i < limit :
		count = count + 1

print (f"The numbers less than 18 : {count}")


#QUESTION 3	A

prices = [15, 10, 21, 48, 54, 60] 

count = 0
count1 = 0
count2 = 0
for x in prices:
	if x <= 20:
		count = count + 1
	elif x <= 49:
		count1 = count + 1
	else: x <= 50
count2 = count + 1

print(f"the number of product under 20 is: {count}")
print(f"the number of product between 20 and 49 is: {count1}")
print(f"the number of product 50 or higher is: {count2}")

# QUESTION 3 B

for i in range(len(prices)):
 prices[i] += 2

# C 
for i in range(len(prices)):
 prices[i] *= 1.05

# D

for i in range(len(prices)):
 prices[i] *= 0.8


