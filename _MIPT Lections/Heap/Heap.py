"""
Модуль реализации Кучи Heap (Структура данных пирамида)
"""

import sys
import math

class A_Heap():
	def __init__(self):
		self.heap = []

	def levels(self):
		if self.is_empty():
			return 0
		else:
			levels = math.ceil(math.log(len(self.heap)+1,2))
			return levels

	def is_empty(self):
		return len(self.heap) == 0

	def len(self):
		return len(self.heap)

	def get_parent_id(self, child_id):
		parent_id = (child_id-1)//2
		return parent_id

	def get_childs_id(self, parent_id):
		child1_id = parent_id*2+1
		child2_id = parent_id*2+2
		if child1_id >= len(self.heap):
			return []
		elif child2_id >= len(self.heap):
			return [child1_id]
		else:
			return [child1_id, child2_id]

	def push(self, item):
		self.heap.append(item)
		current_index = self.len()-1
		if current_index == 0:
			return current_index
		self.check_heap(current_index)

	def check_heap(self, current_index):
		current_value = self.heap[current_index]
		parent_id = self.get_parent_id(current_index)
		if current_value > self.heap[parent_id]:
			self.heap[current_index], self.heap[parent_id]  = self.heap[parent_id], self.heap[current_index]
		if parent_id != 0:
			self.check_heap(parent_id)

	def __str__(self):
		res_str = "_\n"
		for l in range(self.levels()):
			res_str += f"level: {l}, nodes ({2**l-1}-{(2**l-1)*2}): {self.heap[(2**l-1):(2**l-1)*2+1]}" + "\n" 
			# print(
		res_str += "\n^^^^^^^"
		return res_str

	def pop(self):
		pop_item = self.heap[0]
		childs = self.get_childs_id(0)
		parent_id = 0
		while len(childs) > 0:
			if len(childs) == 0:
				self.heap.pop(-1)
				return None
			elif len(childs) == 1:
				id_max_child = childs[0]
			elif self.heap[childs[0]] > self.heap[childs[1]]:
				id_max_child = childs[0]
			else:
				id_max_child = childs[1]
			self.heap[parent_id] = self.heap[id_max_child]
			parent_id = id_max_child
			childs = self.get_childs_id(id_max_child)
		self.heap[id_max_child] = self.heap[-1]
		self.heap.pop(-1)

if __name__ == "__main__":
	h = A_Heap()
	print(f"levels: {h.levels()}")
	h.push(7)
	print(h)
	print(f"levels: {h.levels()}")
	h.push(5)
	print(h)
	h.push(6)
	print(h)
	
	top_item = h.pop()
	print(f"top_item: {top_item} ")


	print(h)
	h.push(1)
	print(h)
	h.push(13)
	print(h)
	h.push(18)
	print(h)
	h.push(21)
	print(h)
	top_item = h.pop()
	print(f"top_item: {top_item} ")
	print(h)
	print(f"levels: {h.levels()}")
	h.push(34)
	print(h)
	h.push(4)
	print(h)
	h.push(1)
	print(h)
	h.push(3)
	print(h)
	h.push(4)
	print(h)
