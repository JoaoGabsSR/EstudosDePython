import menu
import arquivo
import dados

opcoes = {
    1: 'Ver pessoas cadastradas',
    2: 'Cadastrar pessoas',
    3: 'Sair do programa'
}

arq = 'dadosusuario.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    try:
        menu.menuPrincipal(opcoes)
        escolha = int(input('\033[1;33mSua Escolha: \033[m '))

        if escolha not in opcoes.keys():
            print(f'\033[31mOpção escolhida não existe, escolha uma opção válida!\033[m')
        else:
            # Lista de cadastros
            if escolha == 1:
                menu.titulo('PESSOAS CADASTRADAS')
                arquivo.lerArquivo(arq)

            # Novos cadastros
            if escolha == 2:
                menu.titulo('CADASTRAR PESSOAS')

                nome = input('Nome: ').strip()
                idade = dados.leiaInt('Idade: ')

                arquivo.cadastrar(arq, nome, idade)

            # Saida do programa
            if escolha == 3:
                menu.titulo('VOLTE SEMPRE!')
                break

    except (ValueError, TypeError):
        print(f'\033[31mOpção escolhida inválida!\033[m')
    except KeyboardInterrupt:
        print(f'\033[31mPrograma encerrado de forma forçada!\033[m')
        break
