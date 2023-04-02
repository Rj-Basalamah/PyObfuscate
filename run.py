import os, platform

os.system('git pull')

 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from Brute import login
 
        login()
 
 
 
elif bit == "32bit":
	try:
		from Bruta import login
		login() 
	except Exception as e:
		os.system('python ganteng.py')
else:
	os.system('python ganteng.py') 
