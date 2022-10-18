class Conta:

	def __init__(self, numero, titular, saldo, limite):
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite

	@property
	def saldo(self):
		return self.__saldo

	@property
	def titular(self):
		return self.__titular

	@property
	def limite(self):
		return self.__limite

	@staticmethod
	def codigo_banco():
		return '001'

	@staticmethod
	def codigos_bancos():
		return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

	@limite.setter
	def limite(self, valor):
		self.__limite = valor

	def extrato(self):
		print(f'Saldo de R${self.__saldo:.2f} do titular {self.__titular}')

	def depositar(self, valor):
		self.__saldo += valor

	def __pode_sacar(self, valor):
		valor_disponivel_de_saque = self.__saldo + self.__limite

		return valor <= valor_disponivel_de_saque

	def sacar(self, valor):
		if self.__pode_sacar(valor):
			self.__saldo -= valor
		else:
			print(f'O valor R${valor:.2f} passou do limite de saque desta conta!')

	def tranferir(self, valor, destino):
		self.sacar(valor)
		destino.depositar(valor)
