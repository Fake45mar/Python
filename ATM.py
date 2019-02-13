import random
users = []
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
	def __init__(self, pin, full_name):
		self.pin = pin
		self.full_name = full_name
	def const(pincode, fullname):
		if pincode == pin:
			print(True)
			print(True)
	def change_pin():
		pin = int(input("Enter a new pin code"))
	def get(action):
		#action = input("Enter an action")
		action = {
			0:number_card1 + " " + number_card2 +  " " + number_card3 + " " + number_card4,
			1:full_name,
			2:bank,
			3:change_pin()
		}
		return action.get(action, "nothing")

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
	name_file = name + ".txt"
	file = open(name_file, "a")
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
	file.write(str(deposit))
	file.close()
	users.append(User)
	for loop in range(len(users)):
		print(loop)
		if "lev" in users[loop].full_name:
			print(True)
	print(User.bank, User.number_card1, User.number_card2, User.number_card3, User.number_card4, User.full_name, User.pin, User.deposit)
def cash_withdraw():
	pin = int(input("Enter pin - "))
	name = input("Enter your full name wich declared when you registered bank account")
	#cash = int(input("Enter amount withdraw"))
	User = user()
	#if user.deposit < cash:
		#print("Doesn't enough money!")
		#entrance(action)
	#elif user.deposit >= cash_withdraw:
		#user.deposit = user.deposit - cash
def entrance(action):
	if action == 1:
		add_user()
	elif action == 2:
		cash_withdraw()
if __name__ == "__main__":
	print("1-add new user" + "\n" + "2-cash withdraw"  + "\n")
	action = int(input("Enter an action"))
	entrance(action)
		
		#case "cash withdraw":
		#	#
		#	break
		#case "add new user":
		#	add_user()
		#	break
		#default:
		#	print("Don't forget your card")

