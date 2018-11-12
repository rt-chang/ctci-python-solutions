import unittest
from enum import Enum, auto


class Node:
	def __init__(self, data, number):
		self.data = data
		self.number = number
		self.next = None


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def enqueue(self, val, number):
		n = Node(val, number)
		
		if not self.head:
			self.head = n
			self.tail = n
		else:
			self.tail.next = n
			self.tail = n
		
	def dequeue(self):
		target = self.head
		if target:
			self.head = target.next
		return target
		
	def peek(self):
		return self.head


class Animal:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		

class AnimalType(Enum):
	DOG = auto()
	CAT = auto()
	
		
class Shelter:
	def __init__(self):
		self.dogs = Queue()
		self.cats = Queue()
		self.number = 0
		
	def enqueue(self, animal):
		if animal.type is AnimalType.DOG:
			self.dogs.enqueue(animal, self.number)
		else:
			self.cats.enqueue(animal, self.number)
		self.number += 1
			
	def dequeueAny(self):
		oldest_dog = self.dogs.peek()
		oldest_cat = self.dogs.peek()
		# Lower the number, the older the animal
		if (oldest_dog.number < oldest_cat.number):
			return self.dogs.dequeue()
		return self.cats.dequeue()
	
	def dequeueDog(self):
		return self.dogs.dequeue()
		
	def dequeueCat(self):
		return self.cats.dequeue()
		

class TestClass(unittest.TestCase):
	def test_shelter(self):
		s = Shelter()
		s.enqueue(Animal("Bradley", AnimalType.DOG))
		s.enqueue(Animal("Mittens", AnimalType.CAT))
		s.enqueue(Animal("Rags", AnimalType.CAT))
		s.enqueue(Animal("Rufus", AnimalType.DOG))
		
		self.assertEqual(s.dequeueCat().data.name, "Mittens")
		self.assertEqual(s.dequeueDog().data.name, "Bradley")
		self.assertEqual(s.dequeueAny().data.name, "Rags")
	

if __name__ == '__main__':
	unittest.main()
		

		
	