from projeto_sistema_medico.telas_sistema.tela_medico import mostrar_informacoes_medico
from projeto_sistema_medico.verificacoes_sistema.verificacao_login import VerificacaoLogin


class TelaLogin:
    def __init__(self):
        self.verificacao_login = VerificacaoLogin()

    def menu(self):
        """
        Exibe o menu inicial para o médico logar ou sair com 2 opções.
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

    def login(self):
        """
        Realiza o login do médico.
        Verifica as tentativas e, se tudo corresponder, exibe as informações do usuario.
        """
        medico = self.verificacao_login.verificar_tentativas()
        if medico:
            mostrar_informacoes_medico(medico)

    def iniciar_sistema(self):
        """
        Inicia o loop principal do sistema.
        Sistema continua executando até que o médico escolha sair.
        """
        while True:
            opcao = self.menu()
            if opcao == '1':
                self.login()
            elif opcao == '2':
                print('Saindo do sistema.')
                break
            else:
                print('Opção inválida. Tente novamente.')
