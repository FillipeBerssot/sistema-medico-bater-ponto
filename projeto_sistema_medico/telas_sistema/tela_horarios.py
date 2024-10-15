from projeto_sistema_medico.medicos.horarios import horarios_trabalho


def mostrar_horarios(medico):
    """
    Exibe os horários e escalas de trabalho do médico, incluindo o hospital.
    Os horários são importados dos horarios cadastrados.
    """
    telefone = medico.telefone
    horarios = horarios_trabalho.get(telefone)

    if not horarios:
        print(f'\nNenhum horário de trabalho definido para {medico.nome}.\n')
        return

    print(
        f'\n===== Horários de Trabalho de {medico.nome} '
        f'no {medico.hospital} ====='
    )

    for dia, horario in horarios.items():
        print(f'{dia}: {horario}')
    print('=================================\n')

    input('Pressione Enter para voltar ao menu.\n')
