# Linked list
class Node:

	def __init__(self, label):
		self.label = label
		self.next = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next


class LinkedList:

		def __init__(self):
			self.first = None
			self.last = None
			self.len_list = 0

		def push(self, label, index):

			if index >= 0:
				# Cria o novo nó
				node = Node(label)
				# Verifica se a lista está vazia
				if self.empty():
					self.first = node
					self.last = node
				else:

					if index == 0:
						# Inserção no início
						node.setNext(self.first)
						self.first = node
					elif index >= self.len_list:
						# Inserção no final
						self.last.setNext(node)
						self.last = node
					else: 
						# Inserção no meio
						prev_node = self.first
						curr_node = self.first.getNext()
						curr_index = 1


						while curr_index != None:
							if curr_index == index:
								# seta o curr_node como o próximo do nó
								node.setNext(curr_node)
								# seta o node como o próximo do prev_node
								prev_node.setNext(node)
								break

							prev_node = curr_node
							curr_node = curr_node.getNext()
							curr_index += 1

				# Atualiza o tamanho o da lista
				self.len_list += 1


	def pop(self, index):

		if 




















