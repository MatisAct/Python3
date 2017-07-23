import string
import random

chars_fixed = string.ascii_letters + string.digits
min_size_pass = 3
max_size_pass = 5
for i in range(0,100):
	password = ''.join(random.choice(chars_fixed) for x in range(random.randint(min_size_pass,max_size_pass)))
	#'' để in ra kí tự gần nhau
	print ("This is your password : vidu%s" % password)



