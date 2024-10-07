from projeto_sistema_medico.telas_sistema.tela_horarios import mostrar_horarios
from projeto_sistema_medico.telas_sistema.tela_ponto import bater_ponto


def mostrar_informacoes_medico(medico):
    """
    Exibe as informações do médico que fez login.
    Utiliza as informações cadastradas dos medicos.
    """
    print('\n===== Informações do Médico =====')
    print(f"Nome: {medico['nome']}")
    print(f"Especialidade: {medico['especialidade']}")
    print(f"Hospital: {medico['hospital']}")
    print(f"Telefone: {medico['telefone']}")
    print('=================================\n')

    mostrar_menu_medico(medico)


def mostrar_menu_medico(medico):
    """
    Exibe um menu para o médico logado.
    Com 3 opções.
    """
    while True:
        print('1. Ver horários e escalas de trabalho da semana')
        print('2. Bater ponto (Checkin / Checkout)')
        print('3. Sair')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            mostrar_horarios(medico)

        elif opcao == '2':
            bater_ponto(medico)

        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida! Tente novamente.\n')
