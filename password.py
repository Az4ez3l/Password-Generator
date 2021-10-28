# Declare Password class
class Password:
	# declare initialization method
	def __init__(self, primaryKey, name, email, password):
		# declare variable to hold app/site name
		self.__primaryKey = primaryKey
		# declare variable to hold app/site name
		self.__name = name
		# declare a variable to hold email address called email
		self.__email = email
		# declare variable to hold password
		self.__password = password

	# declare method to get primary key, called getKey
	def getKey(self):
		return self.__primaryKey

	# declare method to set primary key, called setKey
	def setKey(self, pKey):
		self.__primaryKey = pKey

	# declare method to get password name, called getName
	def getName(self):
		# return password name
		return self.__name
	
	# declare method to set password name. called setName
	def setName(self, userName):
		# assign name to password name variable
		self.__name = userName

	# declare method to get password email call getEmail
	def getEmail(self):
		# return password email
		return self.__email

	# declare method to get password email, called setEmail
	def setEmail(self, userEmail):
		# assign email to password email variable
		self.__email = userEmail

	# declare method to get password, called getPassword
	def getPassword(self):
		# return password
		return self.__password

	# declare method to set password, called setPassword
	def setPassword(self, userPassword):
		# assign paswword to password variable
		self.__password = userPassword
