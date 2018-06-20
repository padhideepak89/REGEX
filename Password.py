#!/usr/bin/python
#At least 8 characters long, but not more than 15 characters long
# It includes at least one uppercase letter, one lowercase letter
#one numeric digit, and one symbol.
import re

pass=['Deepak76@','amitPare34','yasH@rma97','aJ45#']
b=[]
for i in server:
	password=re.search(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[~!@#$%^&*()_\-+=|\\{}[\]:;<>?/])\S{8,15}$',(pass))
	if password:
		b.append(password.group())
print b

