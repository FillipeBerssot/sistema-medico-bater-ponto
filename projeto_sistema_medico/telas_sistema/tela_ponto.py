from projeto_sistema_medico.verificacoes_sistema. \
    verificacao_localizacao import verificar_localizacao_medico
from projeto_sistema_medico.verificacoes_sistema.verificacao_ponto import (
    validar_ponto,
)


def bater_ponto(medico):
    """
    Solicita ao médico o dia da semana e
    o horário para fazer o registro.
    Utiliza as coordenadas do medico para
    poder realizar ou nao o sistema de bater ponto.
    Utiliza o dicionário com as informações do médico,
    nome, telefone e hospital.
    """

    resultado_localizacao = verificar_localizacao_medico(medico['telefone'])

    if 'fora do raio' in resultado_localizacao:
        print(resultado_localizacao)
        return

    print(resultado_localizacao)

    dia_inserido = input(
        '\nInsira o dia da semana (ex: Segunda-feira): '
    ).strip()
    horario_inserido = input('Insira o horário atual (ex: 08:00): ').strip()

    validar_ponto(medico, dia_inserido, horario_inserido)

    input('Pressione Enter para voltar ao menu.\n')
