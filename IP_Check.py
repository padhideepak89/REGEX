#!/usr/bin/python
import re

a=('192.168.1.121','192.0.0.1','256.0.0.0','0.0.0.0','255.255.244.255')
p=[]
for i in a:
	ip=re.search(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',i)
	if ip:
		p.append(ip.group())
print p