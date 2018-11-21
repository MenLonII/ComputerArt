"""
import gopherlib, sys
host = 'quux.org'
files = '/'
f = gopherlib.send_selector(files, host)
print('waiting...')
for line in f.readlines():
        sys.stdout.write(line)
"""
"""
import urllib, sys
host = 'quux.org'
files = '/'
f = urllib.urlopen('gopher://%s%s'%(host, files))
for line in f.readlines():
        sys.stdout.write(line)
"""
'''
import urllib, sys
#host = 'gopher://quux.org/'
#host = 'http://http.us.debian.org/debian/ls-lR.gz | gunzip | more'
f = urllib.urlopen(sys.argv[1])
while 1:
        buf = f.read(2048)
        if not len(buf):
                break
        sys.stdout.write(buf)
'''
'''
import socket, sys, struct, time

hostname = 'localhost'
port = 51429

host = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('', (host, port))

print('Looking for replies; press Ctrl-C to stop')
buf = s.recvfrom(2048)[0]
print('buf', buf)
if len(buf) != 4:
	print('Wrong-sized reply %d: %s' % (len(buf), buf))
	sys.exit(1)
secs = struct.unpack("!I" ,buf)[0]
print('secs', secs)
secs -= 2208988800
print(time.ctime(int(secs)))
'''
'''
def f(m,n):
#	m, n = (m, n) if m>n else (n,m)
	r = m % n
	a = 1
	while(r!=0):
		m = n
		n = r
		a=a+1
		r = m % n
	print(a)
	return n
#print(f(2166,6099))
f(1,5)

def f2(m, n):
	while 1:
	  m = m % n
	  if m==0:
	  	return n
	  n = n%m 
	  if n == 0:
	  	return m

print(f2(2166, 6099))
'''
'''
import sys
 
def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
 


print(gcd(8,6))
'''


'''
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
'''

class Car(object):
	def __init__(self, name):
		self.name = name
	def move(self):
		print('%s is moving...' % self.name)

class LCar(Car):
	pass

class BCar(Car):
	pass


class CarStore(object):
	def createCar(self, name):
		pass
	def order(self):
		self.car = self.createCar()
		self.car.move()

class Factory(object):
    __instance = None
    __firstInit = False

    def __new__(cls):
    	if not cls.__instance:
    		cls.__instance = object.__new__(cls)
    	return cls.__instance

    def __init__(self):
    	pass
	
	def buildCar(self,name):
		if name == 'LCar':
			car = LCar('LCar')
		elif name == 'BCar':
			car = BCar('BCar')
		return car

class FourSCarstore(CarStore):
	def createCar(self, name):
		return Factory().buildCar(name)

store = FourSCarstore()
l = store.createCar('LCar')
b = store.createCar('BCar')
print(l.move())
print(b.move())

s1 = FourSCarstore()
s2 = FourSCarstore()
print(id(s1))
print(id(s2))

