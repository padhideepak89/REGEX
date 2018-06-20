#!/usr/bin/python
import re

mail=['padhideepak89@gmail.com','padhi.d@husky.neu.edu','deepak']
b=[]
for i in mail:
	email=re.search(r'\b[\w\.]+@[\w\.]+\b',(i))
	if email:
		b.append(email.group())
print b