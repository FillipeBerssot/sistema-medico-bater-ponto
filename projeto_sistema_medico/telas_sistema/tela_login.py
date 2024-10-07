from projeto_sistema_medico.telas_sistema.tela_medico import (
    mostrar_informacoes_medico,
)
from projeto_sistema_medico.verificacoes_sistema.verificacao_login import (
    verificar_tentativas,
)


def menu():
    """
    Exibe o menu inicial para o médico logar ou sair.
    Com 2 opções.
    """
    print('\n==============================')
    print('  Bem-vindo ao Sistema Médico  ')
    print('==============================')
    print('1. Login')
    print('2. Sair')
    print('==============================')
    opcao = input('Escolha uma opção: ').strip()
    print()

    return opcao


def login():
    """
    Realiza o login do médico.
    Verifica as tentativas e se tudo corresponder,
    exibe as informações do usuario.
    """
    medico = verificar_tentativas()
    if medico:
        mostrar_informacoes_medico(medico)


def iniciar_sistema():
    """
    Inicia o loop principal do sistema.
    Sistema continua executando até que o médico escolha sair.
    """
    while True:
        opcao = menu()
        if opcao == '1':
            login()
        elif opcao == '2':
            print('Saindo do sistema... Até logo!')
            break
        else:
            print('Opção inválida! Tente novamente.\n')
