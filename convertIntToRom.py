varNum = int(input("Enter number"))
arrayList = ['I', 'V', 'X', 'L', 'C']
def lessThanTen(number):
	if number >= 1 and number < 4:
		print(arrayList[0] * number)
	elif number == 4:
		print(arrayList[0] + arrayList[1])
	elif number == 5:
		print(arrayList[1])
	elif number > 5 and number < 9:
		print(arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(arrayList[0] + arrayList[2])
	elif number == 10:
		print(arrayList[2])
def biggerThanTenAndLessThanFourty(number):
	varAmount = number // 10
	stringTens = arrayList[2] * varAmount
	number = number % 10
	if number == 0:
		print(stringTens)
	elif number >= 1 and number < 4:
		print(stringTens + arrayList[0] * number)
	elif number == 4:
		print(stringTens + arrayList[0] + arrayList[1])
	elif number == 5:
		print(stringTens + arrayList[1])
	elif number > 5 and number < 9:
		print(stringTens + arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(stringTens + arrayList[0] + arrayList[2])
	elif number == 10:
		print(stringTens + arrayList[2])
def biggerThanFourtyAndLessThanFifty(number):
	varAmount = number // 10
	stringTens = arrayList[2]  + arrayList[3]
	number = number % 10
	if number == 0:
		print(stringTens)
	elif number >= 1 and number < 4:
		print(stringTens + arrayList[0] * number)
	elif number == 4:
		print(stringTens + arrayList[0] + arrayList[1])
	elif number == 5:
		print(stringTens + arrayList[1])
	elif number > 5 and number < 9:
		print(stringTens + arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(stringTens + arrayList[0] + arrayList[2])
	elif number == 10:
		print(stringTens + arrayList[2])
def biggerThanFourtyAndLessThanFifty(number):
	varAmount = number // 10
	stringTens = arrayList[2]  + arrayList[3]
	number = number % 10
	if number == 0:
		print(stringTens)
	elif number >= 1 and number < 4:
		print(stringTens + arrayList[0] * number)
	elif number == 4:
		print(stringTens + arrayList[0] + arrayList[1])
	elif number == 5:
		print(stringTens + arrayList[1])
	elif number > 5 and number < 9:
		print(stringTens + arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(stringTens + arrayList[0] + arrayList[2])
	elif number == 10:
		print(stringTens + arrayList[2])
		#print(varAmount,stringTens,number)
def biggerThanFiftyAndLessThanNinety(number):
	varAmount = number // 10
	stringTens = arrayList[3] + arrayList[2] * ((number - 50)//10)
	number = number % 10
	print(varAmount,stringTens,number)
	if number == 0:
		print(stringTens)
	elif number >= 1 and number < 4:
		print(stringTens + arrayList[0] * number)
	elif number == 4:
		print(stringTens + arrayList[0] + arrayList[1])
	elif number == 5:
		print(stringTens + arrayList[1])
	elif number > 5 and number < 9:
		print(stringTens + arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(stringTens + arrayList[0] + arrayList[2])
	elif number == 10:
		print(stringTens + arrayList[2])
def biggerThanNinetyAndLessThanOneHundred(number):
	varAmount = number // 10
	stringTens = arrayList[2] + arrayList[4]
	number = number % 10
	#print(varAmount,stringTens,number)
	if number == 0:
		print(stringTens)
	elif number >= 1 and number < 4:
		print(stringTens + arrayList[0] * number)
	elif number == 4:
		print(stringTens + arrayList[0] + arrayList[1])
	elif number == 5:
		print(stringTens + arrayList[1])
	elif number > 5 and number < 9:
		print(stringTens + arrayList[1] + arrayList[0] * (number - 5))
	elif number == 9:
		print(stringTens + arrayList[0] + arrayList[2])
	elif number == 10:
		print(stringTens + arrayList[2])
if varNum > 0 and varNum <= 100:
	if varNum <= 10:
		lessThanTen(varNum)
	elif varNum > 10 and varNum < 40:
		biggerThanTenAndLessThanFourty(varNum)
	elif varNum >= 40 and varNum < 50:
		biggerThanFourtyAndLessThanFifty(varNum)
	elif varNum >= 50 and varNum < 90:
		biggerThanFiftyAndLessThanNinety(varNum)
	elif varNum >= 90:
		biggerThanNinetyAndLessThanOneHundred(varNum)