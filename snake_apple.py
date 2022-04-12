from Vector3n import *
from Rendering2D import *
import random

#snake and apple classes

class Snake:
	def __init__(self):
		self.head = Vector3n(500.0, 375.0, 0.0)
		self.tail = [Vector3n(480.0, 375.0, 0.0), Vector3n(460.0, 375.0, 0.0), Vector3n(440.0, 375.0, 0.0)] #Vector3n(460.0, 375.0, 0.0), Vector3n(420.0, 375.0, 0)
		self.vel = Vector3n(16.0, 0.0, 0.0)
		self.size = 3

	def move_forward(self):
		if(self.size == 0):
			self.head = self.head + self.vel
		elif(self.size == 1):
			temp = self.head
			self.head = self.head + self.vel
			self.tail[0] = temp
		elif(self.size > 1):
			temp = self.head
			self.head = self.head + self.vel
			i = self.size - 1
			while(i >= 1):
				self.tail[i] = self.tail[i - 1]
				i -= 1
			self.tail[0] = temp
		


	def change_direction(self, x, y):
		if(x != self.vel.x and y != self.vel.y):
			vector = Vector3n(x, y, 0)
			self.vel = vector

	def check_collision(self):
		i = 0
		while(i < len(self.tail)):
			if(float(self.head.x) == float(self.tail[i].x) and float(self.head.y) == float(self.tail[i].y)):
				self.vel = Vector3n(0, 0, 0)
				#end of game
			i += 1


	def wrap_edges(self):
		if(self.head.x > 1000.0):
			self.head.x = self.head.x % 1000.0

		elif(self.head.x < 0.0):
			self.head.x = 1000.0

		elif(self.head.y > 750.0):
			self.head.y = self.head.y % 750.0

		elif(self.head.y < 0.0):
			self.head.y = 750.0 

	def add(self, x, y):
		vect = self.head - self.vel
		self.tail.insert(1, vect)
		self.size += 1
		

	def show(self):
		pSize(15.0)
		fill("008000") #fill("00FF00")
		point(self.head.x, self.head.y)
		i = 0
		for t in self.tail:
			i += 1
			point(t.x, t.y)
		

	def check_eaten(self, apple):
		if( (float(self.head.x) >= float(apple.pos.x) - 8.0  and float(self.head.x) <= float(apple.pos.x) + 8.0) and (float(self.head.y) >= float(apple.pos.y) - 8.0 and float(self.head.y) <= float(apple.pos.y) + 8.0)):
			apple.eaten = True
		return apple.eaten


class Apple:
	def __init__(self):
		self.pos = Vector3n(float(random.randint(0, 1000)), float(random.randint(0, 750)), 0.0)
		self.eaten = False

	def show(self):
		if(self.eaten == False):
			fill("FF0000")
			pSize(15.0)
			point(self.pos.x, self.pos.y)



