class Stack: # Pilha
	
	def __init__(self):
		self.stack = []

	def push(self, e):
		self.stack.append(e)

	def pop(self):
		if not self.empty():
			self.stack.pop(len(self.stack) - 1)

	def top(self):
		if not self.empty():
			return self.stack[-1]
		print('Pilha vazia!')

	def empty(self):
		if (len(self.stack) == 0):
			return True
		return False

	def length(self):
		return len(self.stack)


s = Stack()
print(s.empty())
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.empty())
s.pop()
print(s.top())
s.pop()
print(s.top())
s.pop()
s.top()
print(s.length())











