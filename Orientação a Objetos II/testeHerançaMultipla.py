class Funcionario:
	def __init__(self, nome):
		self.nome = nome

	def registrar_horas(self, horas):
		print(f'Horas Registradas.')

	def mostrar_tarefas(self):
		print('Fez muita coisa... ')


class Caelum(Funcionario):
	def mostrar_tarefas(self):
		print('Fez muita coisa, Caelumer')

	def buscar_cursos_do_mes(self, mes=None):
		print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
	# def mostrar_tarefas(self):
	# 	print('Fez muita coisa, Alurete!')

	def buscar_perguntas_sem_resposta(self):
		print('Mostrando perguntas sem resposat do fórum.')


class Hipster:
	def __str__(self):
		return f'Hipster, {self.nome}'


class Junior(Alura):
	pass


class Pleno(Alura, Caelum, Hipster):
	pass


jose = Junior('José')
jose.buscar_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.buscar_perguntas_sem_resposta()
luan.buscar_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)
