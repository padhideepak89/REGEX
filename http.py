#!/usr/bin/python
import re

server=['http://www.nowhere.com','https://www.nowhere.com?product=28&color=blue','deepak']
b=[]
for i in server:
	http=re.search(r'^(?:https|http):\/\/([\w\.\/\?#\=&]+)$',(i))
	if http:
		b.append(http.group())
print b

