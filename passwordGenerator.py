import sys, random
from password import Password
from util import clear

# Gloabal Variables
myList = [] # Declare list to hold object called myList


# Declare Main class
class Main:
	# declare initialization method
	def __init__(self):
		pass	
	
	# declare method to generate password called passwordGenerator
	def __passwordGenerator(self):
		# declare variable to hold string of password characters called passwordChars
		passwordChars = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[]{};:'\",.<>?"
		# declare pWord variable
		pWord = ""
		# generate 16 random integers and assign to variable pWord
		for x in range(16):
			randomNum = random.randint(0,95)
			pWord += passwordChars[randomNum]
		# return pWord
		return pWord

	# declare method to find password object which has parameter name, called findPassword
	def __findPassword(self, name):
		for obj in myList:
			if obj.getName() == name:
				# return obj
				return obj

	# declare method to delete password which has parameter name, called deletePassword
	def __deletePassword(self):
		# accept app/site name as user input  and assign to variable name
		self.name = input("\nEnter app/site name: ")
		# invoke find password function and pass name as argument
		obj = self.__findPassword(self.name)
		# display object to delete
		self.__display(obj)
		# display confirmation message
		choice = input("\nAre you sure y/n? ").lower()
		# if choice equals to y
		if choice == 'y':
			# delete obj from dictionary
			myList.pop(self.name)
			print("Password deleted successfully")
		# else if choice equals to n
		elif choice == 'n':
			# pass
			pass
		# else display choice again
		else:
			pass
		
	# declare method to display object information, has parameter obj, called display
	def __display(self, obj):
		# display primary key
		print(f"\n{obj.getKey()}.")
		# display name to user
		print(f"\tName: {obj.getName()}")
		# display email to user
		print(f"\tEmail: {obj.getEmail()}")
		# display pWord to user 
		print(f"\tPassword: {obj.getPassword()}")

	def __create(self):
		# declare variable to hold app/site name from user input, called name
		self.name = input("\nEnter app/site name: ")
		# declare variable to hold email address from user input, called email
		self.email = input("Enter email address: ")
		# invoke generate password function and assign return value to pWord
		print("Generating password...")
		self.pWord = self.__passwordGenerator()
		# make password object assign to variable passObj
		obj = Password(len(myList)+1, self.name, self.email, self.pWord)
		# display object information to user
		self.__display(obj)
		# add obj to dictionary
		myList.append(obj)

	def __view(self):
		# clear screen
		clear()
		# repeat
		for obj in myList:
			# display information for each object
			self.__display(obj)
		
		input("\n\nPress Enter to continue......")

	def __update(self):
		# accept app/site name as user input  and assign to variable name
		self.name = input("\nEnter app/site name: ")
		# invoke find password function and pass name as argument
		obj = self.__findPassword(self.name)
		# delete obj
		myList.pop(obj.getKey()-1)
		# display options to user
		print("\n1. Change app/site name")
		print("2. Change email address")
		print("3. Change password")
		# accept user choice
		choice = int(input("\nSelect choice: "))
		# if user choice equals to 1
		if choice == 1:
			# accept user input
			self.name = input("\nEnter app/site name: ")
			# change app/site name
			obj.setName(self.name)
		# else if user choice equals to 2
		elif choice == 2:
			# accept user input
			self.email = input("\nEnter email address: ")
			# change email address
			obj.setEmail(self.email)
		# if user choice equals to 3
		elif choice == 3:
			# generate a new password
			print("Generating password...")
			self.pWord = self.__passwordGenerator()
			# change password
			obj.setPassword(self.pWord)
		# else if other choice display warning and menu
		else:
			pass
		# add obj to dictionary
		myList.insert(obj.getKey()-1, obj)

	# declare main method
	def main(self):
		# display instructions for user
		print("\n1. Create and save password")
		print("2. View passwords")
		print("3. Change password for an app/site")
		print("4. Delete a password")
		print("5. Exit")
		try:
			# Declare variable to hold user input, called userChoice
			choice = int(input("\nSelect choice: "))

			# if user choice is equal to 1 (create)
			if choice == 1:
				# invoke create method
				self.__create()

			# else if user choice is equal to 2 (read)
			elif choice == 2:
				# invoke view method
				self.__view()

			# else if user choice is equal to 3 (update)
			elif choice == 3:
				# invoke update method
				self.__update()

			# else if user choice is equal to 4 (delete)
			elif choice == 4:
				# invokr delete method
				self.__deletePassword()

			# else if user choice equals to 5 (exit)
			elif choice == 5:
				# exit application
				clear()
				sys.exit()

			# else
			else:
				pass
		except Exception as e:
			pass

		# clears command line
		clear()
		# invoke main method
		self.main()


if __name__ == "__main__":
	# Instantiate Main object
	app = Main()
	# Invoke Main object main() method
	app.main()