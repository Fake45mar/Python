import random
while True:
	users_obj = []
	users_files = []
	arr = []
	class user:
		def __init__(self, bank, number_card1, number_card2, number_card3, number_card4, full_name, pin, deposit):
			self.bank = bank
			self.number_card1 = number_card1
			self.number_card2 = number_card2
			self.number_card3 = number_card3
			self.number_card4 = number_card4
			self.full_name = full_name
			self.pin = pin
			self.deposit = deposit
		def const(pincode, fullname):
			if pincode == pin:
				print(True)
				print(True)
		def change_pin():
			try:
				pin = input("Enter pin - ")
				name = input("Enter your full name wich declared when you registered bank account")
				name = name.lower() + ".txt"
				file = open(name, "r")
				context_file = file.read()
				pinTrue = context_file.find("~" + pin)
				etc_context = context_file[:pinTrue]
				etc2_context = context_file[pinTrue + 5: len(context_file)]
				file.close()
				if pinTrue != -1:
					pin = int(input("Enter a new pin code"))
					file = open(name, "w")
					with open(name, "w"):
						pass
					file.write(etc_context + etc2_context)
					file.write("~" + str(pin))
			except:
				print("Your didn't enter a real pin-code, repeat")
				change_pin()
		def get():
			name = input("Enter a name that would you have to get info") + ".txt"
			try:
				file = open(name, "r")
				print(file.read())
				file.close()
			except:
				print("This file doesn't exist, try another something")
				get()

	def add_user():
		print("Choose the bank: 1-private, 2-american express, בנק ישראל(3)")
		bank_name = ""
		bank_choose = int(input("Enter a name of bank"))
		bank_switch = {
			1:"private",
			2:"american express",
			3:"Israel"
		}
		bank_name = bank_switch.get(bank_choose, "nothing")
		number_card1 = random.randrange(5168, 5376)
		number_card2 = random.randrange(1000, 9999)
		number_card3 = random.randrange(1000, 9999)
		number_card4 = random.randrange(1000, 9999)
		print("Enter your full name")
		name = input("Full name - ")
		if name == "" or name == " ":
			add_user()
		print("Choose the pin code and don't tell to anybody it")
		pin = int(input("Enter 4 numbers"))
		if pin > 10000 or pin < 1000:
			add_user()
		print("Pay deposit")
		deposit = int(input())
		User = user(bank_name, number_card1, number_card2, number_card3, number_card4, name, pin, deposit)
		name_file = name.lower() + ".txt"
		file = open(name_file, "a")
		with open(name, "w"):
			pass
		file.write("~")
		file.write(str(pin))
		file.write("\n")
		file.write(str(number_card1))
		file.write(" ")
		file.write(str(number_card2))
		file.write(" ")
		file.write(str(number_card3))
		file.write(" ")
		file.write(str(number_card4))
		file.write("\n")
		file.write(name)
		file.write("\n")
		file.write(bank_name)
		file.write("\n")
		file.write("=")
		file.write(str(deposit))
		file.write("+")
		file.close()
		users_obj.append(User)
		users_files.append(name_file)
		print(User.bank, User.number_card1, User.number_card2, User.number_card3, User.number_card4, User.full_name, User.pin, User.deposit)
	def cash_withdraw(num):
		pin = input("Enter pin - ")
		name = input("Enter your full name wich declared when you registered bank account")
		name = name.lower() + ".txt"
		file = open(name, "r")
		context_file = file.read()
		pinTrue = context_file.find("~" + pin)
		findDeposit = context_file.find("=")
		endDeposit = context_file.find("+")
		depositt = context_file[findDeposit + 1:endDeposit]
		etc_context = context_file[:findDeposit]
		etc2_context = context_file[endDeposit + 1: len(context_file)]
		print(depositt)
		file.close()
		if pinTrue != -1:
			depositt = int(depositt) - num
			result = depositt
			print("Your left cash is - " + str(depositt) + " and don't forget your money" + str(num))
			file = open(name, "w")
			with open(name, "w"):
				pass
			file.write("~" + pin)
			file.write("\n")
			file.write("=")
			file.write(str(depositt))
			file.write("+")
			file.write("\n")
			file.write(etc_context + etc2_context)
			file.close()
	def entrance(action):
		if action == 1:
			add_user()
		elif action == 2:
			summ = int(input("Enter a sum"))
			cash_withdraw(summ)
		elif action == 3:
			user.get()
		elif action == 4:
			user.change_pin()
	inp = input("Hello there, have you been here early? If you was here, leave free space.\n If you here as first, you have to enter something.\n If you just wanna check your current balance and info, tap 'get'.\n To exit enter exit.\n To change pin-code, enter - 'change'")
	if inp == "" or inp == " ":
		entrance(2)
	elif inp == "get":
		entrance(3)
	elif inp == "change":
		entrance(4)
	elif inp == "exit":
		break
	else:
		entrance(1)