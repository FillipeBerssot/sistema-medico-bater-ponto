from geopy.distance import geodesic

from projeto_sistema_medico.hospital.hospitais import hospitais
from projeto_sistema_medico.medicos.localizacao_medicos import (
    localizacao_medicos,
)

distancia_maxima = 200


def verificar_localizacao_medico(telefone):
    """
    Verifica se o medico esta dentro do raio permitido para realizar o ponto.
    Função recebe o telefone do medico cadastrado, busca suas coordenadas e
    as coordenadas do hospital associado.
    Calcula a distancia entre ambos usando a função geodesic.
    Retornando mensagem se o médico está ou não dentro do raio permitido para
    realizar o sistema de bater ponto.
    """
    if telefone in localizacao_medicos:
        info_medico = localizacao_medicos[telefone]
        coordenadas_medico = info_medico['coordenadas']
        coordenadas_hospital = hospitais[info_medico['hospital']][
            'coordenadas'
        ]
        distancia = geodesic(coordenadas_medico, coordenadas_hospital).meters
        if distancia <= distancia_maxima:
            return (
                f'\nO médico está a {distancia:.2f} metros do hospital,'
                ' está dentro do raio permitido (200m do hospital).\n'
            )
        else:
            return (
                f'\nO médico está a {distancia:.2f} metros do hospital,'
                ' está fora do raio permitido (no maximo 200m do hospital).\n'
            )
    else:
        return 'Médico não encontrado.'
