from itertools import *
import os

print('''this is a wordlist generator,where you enter the words(separate them with a
	space and in lower case) and you are asked the minimum and maximum length of the password''')
words = [x for x in input().split(' ')]
m = int(input('enter minimun password length: '))
M = int(input('enter maximum password length: '))
y = 100

for k in words:
	if len(k) < y and len(k) > 1:
		y = len(k)
z = M//y + 1

#Words = words[:]
def case1(words):
	Words = []
	for word in words:
		if not word.isalpha():
			Words.append(word)
		else:
			Words.append(word.lower())
	return Words


def case2(words):
	Words = []
	for word in words:
		if not word.isalpha():
			Words.append(word)
		else:
			Words.append(word.upper())
	return Words

def case3(words):
	Words = []
	for word in words:
		if not word.isalpha():
			Words.append(word)
		else:
			Words.append(word.title())
	return Words

def case4(words):
	Words = words[:]
	for word in words:
		if not word.isalpha():
			continue
		else:
			Words.append(word.upper())
	return Words

def case5(words):
	Words = words[:]
	for word in words:
		if not word.isalpha():
			continue
		else:
			Words.append(word.title())
	return Words


def case6(words):
	Words = words[:]
	for word in words:
		if not word.isalpha():
			continue
		else:
			Words.append(word.upper())
			if len(word) > 1:
				Words.append(word.title())
	return Words


print('''now you are to the cases by their number
		Each case tells you the form of the password created
		they are as follows:
		case 1:involves a combination of lowercase letters and other characters(if given)
		case 2:involves a combination of uppercase letter and other characters(if given)
		case 3:involves a combinaton title case and other characters(if given)
		case 4:involves a combination of lower and upper case and other char(if given)
		case 5:involves a combination of lower and title case and other char(if given)
		case 6:involves a combination of lower,upper and title case and other char(if given)
		''')

k = int(input('enter the case you want: '))
if k == 1:
	x = case1(words)
elif k == 2:
	x = case2(words)
elif k == 3:
	x = case3(words)
elif k == 4:
	x = case4(words)
elif k == 5:
	x = case5(words)
else:
	x = case6(words)
	

def wordlist(words,x,m,M):
	Word1 = x
	combn = Word1[:]
	cwd = os.getcwd()
	passwdlist = open(os.path.join(cwd,'wordlist.txt'),'w')
	for pd in combn:
		if len(pd)>= m and len(pd)<= M:
			passwdlist.write(pd + '\n')
	for k in range(2,z+1):
		combn1 = combinations_with_replacement(x,k)
		for word in combn1:
			if len(''.join(word))<= M and len(''.join(word))>= m:
				combn2 = permutations(word,r=k)
				pwd = ''
				pwdlist = []
				for result in combn2:
					if ''.join(result) not in pwdlist:
						pwd = ''.join(result)
						pwdlist.append(pwd)
						passwdlist.write(pwd + '\n')
	passwdlist.close()


wordlist(words,x,m,M)
print('wordlist is stored in your current working directory')
