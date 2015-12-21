import random
import time
import sys

termWidth = 80
minDrop = 3
maxDrop = 7
r = random.Random()
dropCharacter = '.'
numDrops = 2
sleepTime = .025

class FallingObject:
	def __init__(self, r, termWidth, streak, angle=2):
		self.r = r
		self.termWidth = termWidth
		self.angle = angle
		self.streak = streak
		self.reset_all()
	def reset_all(self):
		self.location = self.r.randint(0, self.termWidth)
		self.seq = 0
		self.angleSeq = 0
		self.reset_local()

	def reset_local(self):
		pass
		
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
		if self.seq > len(self.streak) or self.location > self.termWidth:
			self.reset_all()

		ret = self.location,self.streak[self.seq]
		self.itt()
		return ret
	def randint(self, mi, ma):
		return self.r.randint(mi, ma)
	#def toString()


class Raindrop(FallingObject):
	def __init__(self, r, termWidth, angle, 
			minDrop, maxDrop, front, tail ):
		self.r = r
		self.minDrop = minDrop
		self.maxDrop = maxDrop
		self.front = front
		self.tail = tail
		self.reset()
		super.__init__(FallingObject, r, termWidth, self.streak, angle)
		
	def reset(self):
		""" called automatically by the parrent to reset the raindrop """
		#what do i do with instance variables in an abstract class
		totalLength = self.r.randint(self.minDrop, self.maxDrop)
		self.streak = [self.front]
		self.streak.extend(
			[self.tail for i in range(totalLength)] )

class Snowflake(FallingObject):
	def __init__(self):
		parent.__init__(self)
		pass
