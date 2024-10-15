from geopy.distance import geodesic  # type: ignore

from projeto_sistema_medico.hospital.hospitais import hospitais
from projeto_sistema_medico.medicos.localizacao_medicos import (
    localizacao_medicos,
)


class VerificacaoLocalizacao:
    def __init__(self, distancia_maxima=200):
        self.distancia_maxima = distancia_maxima

    def verificar_localizacao(self, telefone, nome):
        """
        Verifica se o médico está dentro do raio permitido para
        realizar o ponto.
        A função recebe o telefone do médico cadastrado, busca suas
        coordenadas e
        as coordenadas do hospital associado. Calcula a distância
        entre ambos
        usando a função geodesic. Retorna uma mensagem se o médico
        está ou não
        dentro do raio permitido para realizar o sistema de
        bater ponto.
        """
        if telefone in localizacao_medicos:
            info_medico = localizacao_medicos[telefone]
            coordenadas_medico = info_medico['coordenadas']
            coordenadas_hospital = hospitais[
                info_medico['hospital']
            ].coordenadas
            distancia = geodesic(
                coordenadas_medico, coordenadas_hospital
            ).meters

            if distancia <= self.distancia_maxima:
                return (
                    f'\n{nome} com login: {telefone} está dentro do '
                    'raio permitido.'
                )
            else:
                return (
                    f'\n{nome} com login: {telefone} está fora do '
                    f'raio permitido ({distancia:.2f} metros).'
                )
        return 'Médico não encontrado.'
