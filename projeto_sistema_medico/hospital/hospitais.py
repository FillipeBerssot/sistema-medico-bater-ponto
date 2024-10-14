class Hospital:
    def __init__(self, nome, coordenadas, medicos):
        self.nome = nome
        self.coordenadas = coordenadas
        self.medicos = medicos

    def __repr__(self):
        return f"Hospital({self.nome}, Coordenadas: {self.coordenadas}, Medicos: {len(self.medicos)})"


hospitais = {
    'Hospital A': Hospital(nome='Hugol', coordenadas=(-16.64718, -49.33797), medicos=['62991536051', '62991536052', '62991536053']),
    'Hospital B': Hospital(nome='Dona Iris', coordenadas=(-16.71719, -49.24120), medicos=['62991536054', '62991536055', '62991536056']),
}
