import random
import time
import sys

termWidth = 80
minDrop = 3
maxDrop = 7
r = random.Random()
dropCharacter = '.'
numDrops = 2
sleep_ms = 15

def rainbyclass(lines):
	''' generates 'rain' on screen '''
	droplets = [droplet(termWidth),droplet(termWidth),droplet(termWidth)]
	
	class droplet:
		def __init__(self,termWidth):
			self.location = r.randint(0,termWidth)
			self.length = r.randint(3,7)
			self.current_length = 0
		def get(self):
			self.length -= 1
			if self.length < 0:
				raise IndexError("length is less than 0")
			return self.location, self.length-self.current_length

	def buildOutput():
		''' builds the string output to the screen from droplets'''
		pass
	
	def replace(s, i, sub):
		ret = s[:i-1]+sub+s[i:]
		return ret

	for drop in range(droplets):
		out = ' '*termWidth
		#out.
		

def rainByBits():
	''' 010000101001001 '''
	''' 010000101001001 '''
	''' 010000100001001 '''
	''' 010000100001001 '''
	
	starter = long('01000010100100100000')
	itt = r.getrandbits(20)
	added = starter & itt
	starter
	

def simpleRain():
	for i in range(100):
		a = r.randint(0,termWidth)

#def rainByThree():
def replace(s, i, sub):
	ret = s[:i-len(sub)/2-1]+sub+s[i+len(sub)/2:]
	#assert (len(s) <= termWidth), "s'{}' len'{}'".format(s,len(s))
#	if len(s) > termWidth:
#		print '  {}'.format(s)
#		print "Len(s): {}>{}; loc: {}, sub: '{}'".format(
#				len(s),termWidth, i, sub)
#		raise Exception("wider than terminal width")
	return ret
class droplet:
	def __init__(self, r, termWidth, minDrop, maxDrop, 
			angle=2, front=['|'],tail='.'):
		self.r = r
		self.termWidth = termWidth
		self.minDrop = minDrop
		self.maxDrop = maxDrop
		self.front = front
		self.tail = tail
		self.angle = angle
		self.reset_all()
	def reset_all(self):
		self.location = self.r.randint(0, self.termWidth)
		self.totalLength = self.r.randint(self.minDrop, self.maxDrop)
		self.seq = 0
		self.angleSeq = 0
		self.streak = self.front
		self.streak.extend(
			[self.tail for i in range(self.totalLength)])
		#for i in range(self.totalLength):
		#	self.streak.append(self.tail)
	def reset_angleSeq(self):
		self.angleSeq = 0
		self.location += 1
	def itt(self):		
		self.seq += 1
		if self.angle != 0:
			self.angleSeq += 1
	def get(self):
		if self.angle != 0 and self.angleSeq > self.angle:
			self.reset_angleSeq()
		if self.seq > self.totalLength or self.location > self.termWidth:
			self.reset_all()

		
		ret = self.location,self.streak[self.seq]
		self.itt()
		return ret
		
class snowflake:
	def __init__(self, r, termWidth, minDrop, maxDrop, front):
		self.r = r
		self.termWidth = termWidth
		self.minDrop = minDrop
		self.maxDrop = maxDrop
		self.front = front	#some 3x3 symetric array
		self.tail = '.'
		self.seq = 0
		self.renew()
	def renew(self):
		self.location = self.r.randint(len(front)/2+1 ,
						self.termWidth-len(front)/2-1)
		self.length = self.r.randint(self.minDrop, self.maxDrop)
		self.seq = 0
	def get(self):
		if self.length <= 0:
			self.renew()
		if self.seq >= len(front):
			print self.location, self.front[self.seq]
			ret = (self.location,self.front[self.seq])
			print ret
			self.length -= 1
			self.seq += 1
			return ret
		else:
			self.length -= 1
			ret = (self.location,self.tail)
			print ret
			return ret
def rain(numDrops,front):
	drops = []
	for i in range(numDrops):
		drops.append(droplet(r, termWidth, minDrop, maxDrop,front=front))
	for i in range(1000):
		s = ' '*termWidth
		for drop in drops:
			loc,char = drop.get()
			#print loc, char
			s = replace(s, loc, char)
		#print s
		print '{}{}'.format(len(s),s)
		time.sleep(sleepTime)


def snow(numDrops, front):
	drops = []
	for i in range(numDrops):
		drops.append(snowflake(r, termWidth, minDrop, maxDrop,front))
	for i in range(1000):
		s = ' '*termWidth
		for drop in drops:
			loc,char = drop.get()
			s = replace(s, loc, char)
		#print s
		print '{}{}'.format(len(s),s)
		time.sleep(sleepTime)
		


def runCurses(win):
	def ins(s):
		win.move(0,0)
		win.insertln()
		win.addstr(s)
		win.refresh()
	win_y, win_x = win.getmaxyx()
	front = ['|']

	drops = []
	for i in range(numDrops):
		drops.append(droplet(r, win_x, minDrop, maxDrop,front=front))
	while True:
		s = ' '*termWidth
		for drop in drops:
			loc,char = drop.get()
			#print loc, char
			s = replace(s, loc, char)
		#print s
		#print '{}{}'.format(len(s),s)
		ins(s)
		curses.napms(sleep_ms)
	curses.endwin()
	



if __name__ == "__main__":
	import curses
	
	#front = ['\\ /', '-- --', '/ \\']
	#front = [' | ', '- -', ' | ']
	#front = ['|']
	#rain(int(sys.argv[1]),front)
	
	curses.wrapper(runCurses)
	print 'done'
	#snow(2,front)	
