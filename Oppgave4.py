#!/usr/bin/python
import re

lists = re.findall(r"[+*\-\/]", r"[0-9]")

for list in lists:
	print list
