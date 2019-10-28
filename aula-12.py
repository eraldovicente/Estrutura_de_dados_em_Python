class Pessoa:

	# def __init__(self, nome):
	# 	self.__nome = nome

	def __init__(self):
		self.__nome = None

	# def getNome(self):
	# 	return self.__nome

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		self.__nome = nome

p = Pessoa('Marcos')
# print(p.nome)
# print(p.getNome())
p.nome = 'Marcos'
print(p.nome)