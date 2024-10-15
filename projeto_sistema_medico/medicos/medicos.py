class Medico:
    def __init__(self, **kwargs):
        self.nome = kwargs.get('nome')
        self.especialidade = kwargs.get('especialidade')
        self.hospital = kwargs.get('hospital')
        self.telefone = kwargs.get('telefone')
        self.senha = kwargs.get('senha')

    def __repr__(self):
        return f'Medico({self.nome}, {self.especialidade}, {self.hospital})'


medicos_cadastrados = [
    Medico(
        nome='Dr. Thiago Tancredi',
        especialidade='Pediatra',
        hospital='Hugol',
        telefone='62991536051',
        senha='senha123',
    ),
    Medico(
        nome='Dr. Fillipe Berssot',
        especialidade='Pronto Socorro',
        hospital='Hugol',
        telefone='62991536052',
        senha='senha123',
    ),
    Medico(
        nome='Dr. Alberdan Fernandes',
        especialidade='Pediatra',
        hospital='Hugol',
        telefone='62991536053',
        senha='senha123',
    ),
    Medico(
        nome='Dra. Maria Alice',
        especialidade='Pronto Socorro',
        hospital='Dona Iris',
        telefone='62991536054',
        senha='senha123',
    ),
    Medico(
        nome='Dra. Ana Luiza',
        especialidade='Pediatra',
        hospital='Dona Iris',
        telefone='62991536055',
        senha='senha123',
    ),
    Medico(
        nome='Dr. João da Silva',
        especialidade='Pronto Socorro',
        hospital='Dona Iris',
        telefone='62991536056',
        senha='senha123',
    ),
]
