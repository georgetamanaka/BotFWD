#Author: Marcelo de Moraes
#https://github.com/niiu/

from __future__ import print_function
from sys import stdin
import re
import string

for line in stdin:
	#captalize the first char of each word
	myString = string.capwords(line)
	#split line in list of words
	wordList = re.sub("[*]", " ",  myString).split()
	
	for p in range(len(wordList)):
		if p > 0:
			#lower the connectives 
			if (wordList[p] == "As" or wordList[p] == "Os" or wordList[p] == "O" or wordList[p] == "A" or wordList[p] == "De" or wordList[p] == "Da" or wordList[p] == "Do" or p == "Uma" or wordList[p] == "Um" or wordList[p] == "E"):
				wordList[p] = wordList[p].lower()

		if p+1 == len(wordList): #if is the last word in list
			print(wordList[p], end='\n')

		else:
			print(wordList[p], end=' ')
