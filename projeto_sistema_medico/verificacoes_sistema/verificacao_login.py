import time

from projeto_sistema_medico.medicos.medicos import medicos_cadastrados

tentativas_maximas = 3
telefone_maximo = 11
senha_minima = 6

verificar_telefone = lambda telefone: (
    len(telefone) == telefone_maximo and telefone.isdigit()
)

verificar_senha = lambda senha: len(senha) >= senha_minima


def verificar_tentativas():
    """
    Verifica as tentativas do médico para realizar o bloqueio.
    Se o usuario ultrapassar 3 tentativas, o bloqueio e de 10 segundos,
    depois voltando ao normal.
    """
    tentativas = 0

    while tentativas < tentativas_maximas:
        print(
            f'\n===== Tentativa {tentativas + 1} de {tentativas_maximas} ====='
        )

        telefone = input(
            'Digite seu telefone cadastrado (11 dígitos): '
        ).strip()

        if not verificar_telefone(telefone):
            print('Erro: Telefone inválido. Deve conter 11 dígitos.\n')
            tentativas += 1
            print(f'Tentativas restantes: {tentativas_maximas - tentativas}')
            continue

        senha = input('Digite sua senha (mínimo de 6 caracteres): ').strip()

        if not verificar_senha(senha):
            print('Erro: Senha inválida. Deve ter pelo menos 6 caracteres.\n')
            tentativas += 1
            print(f'Tentativas restantes: {tentativas_maximas - tentativas}')
            continue

        medico = busca_medico(telefone, senha)

        if medico:
            print('\nLogin realizado com sucesso!\n')
            return medico
        else:
            print('Telefone ou senha incorretos.\n')
            tentativas += 1
            print(f'Tentativas restantes: {tentativas_maximas - tentativas}')

    print(
        'Você excedeu o número máximo de tentativas.'
        ' Sistema bloqueado por 10 segundos.'
    )
    time.sleep(10)
    print('\nVocê pode tentar novamente.\n')
    return None


def busca_medico(telefone, senha):
    for medico in medicos_cadastrados:
        if medico['telefone'] == telefone and medico['senha'] == senha:
            return medico
    return None
