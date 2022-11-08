#Traverse Arrays

#QUESTION 1
array = ["yes", "yes", "maybe", "no", "no", "no"]

countyes = array.count("yes")
countno = array.count("no")
countmaybe = array.count("maybe")

print("Count of yes: ", countyes)
print("Count of no: ", countno)
print("Count of maybe: ", countmaybe)




#QUESTION 2
ages = [14, 17, 15, 12, 19, 23, 38]

limit = 18

# GREATER THAN 18
count = 0
for i in ages :
	if i > limit :
		count = count + 1

print ("The numbers greater than 18 : " + str(count))

# LESS THAN 18
count = 0
for i in ages :
	if i < limit :
		count = count + 1

print ("The numbers less than 18 : " + str(count))




# QUESTION 3

prices = [15, 10, 21, 48, 54, 60] 

limit2 = 20
limit3 = 50

# LESS THAN 20
count = 0
for i in prices :
	if i > limit2 :
		count = count + 1

print ("The prices less than 20 : " + str(count))

# MORE THAN 50
count = 0
for i in prices :
	if i < limit3 :
		count = count + 1

print ("The prices more than 50 : " + str(count))

# BETWEEN 20-49

for x in range in prices (20, 49):
  print(x)


