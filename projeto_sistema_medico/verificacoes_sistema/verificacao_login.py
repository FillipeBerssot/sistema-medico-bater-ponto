import time

from projeto_sistema_medico.medicos.medicos import medicos_cadastrados


class VerificacaoLogin:
    def __init__(self, **kwargs):
        self.tentativas_maximas = kwargs.get('tentativas_maximas', 3)
        self.telefone_maximo = kwargs.get('telefone_maximo', 11)
        self.senha_minima = kwargs.get('senha_minima', 6)

    def verificar_telefone(self, telefone):
        return len(telefone) == self.telefone_maximo and telefone.isdigit()

    def verificar_senha(self, senha):
        return len(senha) >= self.senha_minima

    def verificar_tentativas(self):
        """
        Verifica as tentativas do médico para realizar o bloqueio.
        Se o usuario ultrapassar 3 tentativas, o bloqueio é de 10 segundos,
        depois voltando ao normal.
        """
        tentativas = 0

        while tentativas < self.tentativas_maximas:
            print(
                f'\n===== Tentativa {tentativas + 1} '
                f'de {self.tentativas_maximas} ====='
            )

            telefone = input(
                'Digite seu telefone cadastrado (11 dígitos): '
            ).strip()

            if not self.verificar_telefone(telefone):
                print('Erro: Telefone inválido. Deve conter 11 dígitos.\n')
                tentativas += 1
                print(
                    f'Tentativas restantes: '
                    f'{self.tentativas_maximas - tentativas}'
                )
                continue

            medico = next(
                (m for m in medicos_cadastrados if m.telefone == telefone),
                None,
            )
            if medico:
                senha = input('Digite sua senha: ').strip()
                if not self.verificar_senha(senha):
                    print(
                        'Erro: Senha inválida. Deve ter pelo menos 6 '
                        'caracteres.\n'
                    )
                    tentativas += 1
                    print(
                        f'Tentativas restantes: '
                        f'{self.tentativas_maximas - tentativas}'
                    )
                elif senha == medico.senha:
                    return medico
                else:
                    print('Erro: Senha incorreta.\n')
                    tentativas += 1
            else:
                print('Erro: Telefone não cadastrado.\n')
                tentativas += 1

            if tentativas == self.tentativas_maximas:
                print(
                    'Você atingiu o número máximo de tentativas. '
                    'Aguarde 10 segundos '
                    'segundos.\n'
                )
                time.sleep(10)
        return None
