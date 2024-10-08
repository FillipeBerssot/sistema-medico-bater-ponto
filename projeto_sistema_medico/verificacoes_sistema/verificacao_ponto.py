from datetime import datetime, timedelta

from projeto_sistema_medico.medicos.horarios import horarios_trabalho

horas_tamanho = 2
minutos_tamanho = 2
horas_maxima = 23
minutos_maximo = 59


def padronizar_dia(dia_inserido):
    """
    Padroniza o dia inserido, remove os espaços extras e
    converte para o formato correto.
    Retorna None se o dia não for um dia da semana válido.
    """
    dia_inserido = dia_inserido.strip().lower()

    dias_corretos = {
        'segunda': 'Segunda-feira',
        'segunda feira': 'Segunda-feira',
        'terça': 'Terça-feira',
        'terça feira': 'Terça-feira',
        'terca': 'Terça-feira',
        'terca feira': 'Terça-feira',
        'quarta': 'Quarta-feira',
        'quarta feira': 'Quarta-feira',
        'quinta': 'Quinta-feira',
        'quinta feira': 'Quinta-feira',
        'sexta': 'Sexta-feira',
        'sexta feira': 'Sexta-feira',
        'sábado': 'Sábado',
        'sabado': 'Sábado',
        'domingo': 'Domingo',
    }

    return dias_corretos.get(dia_inserido)


def validar_formato_horario(horario_inserido):
    """
    Verifica se o horário inserido está no formato correto.
    """
    if not horario_inserido or len(horario_inserido) == 0:
        return False

    partes = horario_inserido.split(':')

    if len(partes) != horas_tamanho:
        return False

    horas, minutos = partes

    if not (horas.isdigit() and minutos.isdigit()):
        return False

    if len(horas) != horas_tamanho or len(minutos) != minutos_tamanho:
        return False

    horas = int(horas)
    minutos = int(minutos)

    if 0 <= horas <= horas_maxima and 0 <= minutos <= minutos_maximo:
        return True

    return False


def validar_horario(horario_medico, horario_inserido):
    """
    Verifica se o horário inserido está dentro de uma janela de 15 minutos
    do horário registrado.
    """
    horario_inicio, horario_fim = [
        datetime.strptime(h, '%H:%M') for h in horario_medico.split(' - ')
    ]
    horario_inserido_dt = datetime.strptime(horario_inserido, '%H:%M')

    margem = timedelta(minutes=15)

    if (
        horario_inicio - margem
        <= horario_inserido_dt
        <= horario_inicio + margem
        or horario_fim - margem <= horario_inserido_dt <= horario_fim + margem
    ):
        return True
    return False


def validar_ponto(medico, dia_inserido, horario_inserido):
    """
    Valida se o ponto pode ser batido no dia e horário informados.
    """
    horarios = horarios_trabalho.get(medico['telefone'])

    if not horarios:
        print(f"Nenhum horário de trabalho definido para {medico['nome']}.")
        return

    if not validar_formato_horario(horario_inserido):
        print(
            'Horário inserido é inválido.'
            ' Deve estar no formato HH:MM (ex: 08:00).'
        )
        return

    dia_padronizado = padronizar_dia(dia_inserido)

    if not dia_padronizado:
        print(f"Dia '{dia_inserido}' é inválido. Tente novamente.")
        return

    if dia_padronizado not in horarios:
        print(f"{medico['nome']} não trabalha em {dia_padronizado}.")
        return

    horario_medico = horarios[dia_padronizado]

    if validar_horario(horario_medico, horario_inserido):
        print(
            f"\nPonto registrado para {medico['nome']} no {medico['hospital']}"
        )
        print(f'Dia: {dia_padronizado}')
        print(f'Horário: {horario_inserido}')
        print(f'Horário de trabalho: {horario_medico}')
        print('=================================\n')
    else:
        print(
            'Horário inválido! O ponto deve ser batido dentro de 15 minutos'
            ' do horário de trabalho definido.'
        )
