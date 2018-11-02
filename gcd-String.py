
s = ''
def gcd(m,n):
	global s
	step = 0
	s = 'a'*m+'b'*n
	while step != 5:
		#step0
		if step == 0:
			if  s.find('ab') != -1:
				index = s.find('ab')
				s = s[:index] + s[index+2:]
				step = 1
			else:
				step = 2
		#step1
		if step == 1:
			s = 'c' + s
			step = 0
			continue
		#step2
		if step == 2:
			s = s.replace('a', 'b')
			step = 3
		#step3
		if step == 3:
			s = s.replace('c', 'a')
			step = 4
		#step4
		if step == 4:
			if s.find('b') != -1:
				step = 0
				continue
			else:
				step = 5
		if step == 5:
			return len(s)

print('gcd is %d'%gcd(2166,6099))
