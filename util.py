from os import system, name

def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')
		#for linux and mac (name = 'posix')
	else:
		_ = system('clear')