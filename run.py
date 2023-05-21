import os, platform

os.system('git pull')

 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from enc64 import MainMenu
 
        MainMenu()
 
 
 
elif bit == "32bit":
	try:
		from enc32 import MainMenu
		MainMenu() 
	except Exception as e:
		print('Device tidak mendukung')
else:
	print('Device tidak mendukung')
