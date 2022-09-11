"""
Модуль по работе со стеком
>>> s1 = Stack1()
>>> s1.clear()
>>> s1.is_empty()
True
>>> s1.push(8)
0
>>> s1.push(2)
1
>>> s1.len()
2
>>> s1.is_empty()
False
>>> s1.push(4)
2
>>> s1.push(3)
3
>>> s1.len()
4
>>> s1.is_empty()
False
>>> s1.pop()
3
>>> s1.pop()
4
>>> s1.pop()
2
>>> s1.pop()
8
>>> s1.len()
0
>>> s1.is_empty()
True
"""
class Stack1():
	def __init__(self):
		self.size = 0
		self.stack = []

	def push(self, item):
		"""Добавляет элемент в стек
		>>> s2 = Stack1()
		>>> s2.clear()
		>>> s2.push(3)
		0
		>>> s2.len()
		1
		"""
		self.stack.append(item)
		self.size += 1
		return self.size-1

	def is_empty(self):
		return self.size == 0

	def pop(self):
		"""Удаляет элемент из стека
		>>> s2 = Stack1()
		>>> s2.clear()
		>>> s2.push(3)
		0
		>>> s2.pop()
		3
		>>> s2.len()
		0
		"""
		if self.is_empty():
			return None
		item = self.stack.pop()
		self.size -= 1
		return item

	def len(self):
		return self.size

	def top(self):
		return self.stack[-1]

	def clear(self):
		self.stack.clear()
		self.size = 0

	def __repr__(self):
		return f"{' '.join([str(x) for x in self.stack ]) }"

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)