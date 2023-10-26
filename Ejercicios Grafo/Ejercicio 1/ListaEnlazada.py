class Nodo:

	__value: int
	__next: None

	def __init__(self, value: int, next):
		self.__value = value
		self.__next = next

	def value(self):
		return self.__value

	def next(self):
		return self.__next

	def setNext(self, next):
		self.__next = next


class ListaEnlazada:

	__cabeza: Nodo | None

	def __init__(self):
		self.__cabeza = None

	def insertar(self, value: int):
		self.__cabeza = Nodo(value, self.__cabeza)

	def has(self, value: int):
		nodo = self.__cabeza
		while nodo is not None:
			if nodo.value() == value:
				return True
			nodo = nodo.next()
		return False
	
	def __getitem__(self, item):
		return self.has(item)
