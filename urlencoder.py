def D2H(num):
	hex = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
	rem = 20
	val = ''
	while num != 0:
		rem = num % 16
		if rem in hex.keys():
			hex1 = hex.get(rem)
			val += hex1
		else:
			val += str(rem)
		num = num//16
	return '%'+val[::-1]

def Ascii(character):
	return ord(character)

def urlend(url):
	url2 = ''
	characters = ['/','\\','|','<','>','\'','%','$','#','"','@','`','?','&','^','*','(',')','-','_','+','=','{','}','[',']','~',':',';']
	for char in url:
		if char in characters:
			url2 += D2H(Ascii(char))
		elif char == '':
			url2 += '+'
		else:
			url2 += char
	return url2

def main():
	url = input('enter the url or characters to encode: ')
	print(urlend(url))

main()
