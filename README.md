
# Sistema Médico de Bater Ponto

Este é um projeto de estudo em Python que simula um mini sistema de controle de ponto médico. O sistema permite que médicos façam login, batam ponto e verifiquem se estão dentro do raio permitido do hospital, entre outras funcionalidades. O projeto visa praticar habilidades de desenvolvimento em Python com foco em organização de código, modularização e boas práticas.

## Funcionalidades

- **Login de Médicos**: O sistema valida o telefone e a senha para o login dos médicos.
- **Verificação de Localização**: Confere se o médico está dentro de um raio de 200 metros do hospital antes de permitir bater o ponto.
- **Sistema de Tentativas**: Após 3 tentativas de login com falha, o sistema bloqueia o acesso por 10 segundos.
- **Médicos e Hospitais Cadastrados**: Inclui dados fictícios de médicos e hospitais para simular um ambiente real.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no desenvolvimento.
- **Geopy**: Biblioteca usada para verificar a localização dos médicos em relação aos hospitais.
- **Poetry**: Ferramenta para gerenciamento de dependências e ambiente virtual.
- **Ruff**: Ferramenta de linting para garantir boas práticas de código.
- **Taskipy**: Ferramenta para automatização de tarefas dentro do projeto.

## Estrutura do Projeto

```
projeto_sistema_medico/
│
├── hospital/                  # Módulo responsável pelos dados dos hospitais
├── medicos/                   # Módulo que contém a lógica relacionada aos médicos
├── verificacoes_sistema/       # Verificações e validações, como localização e login
├── telas_sistema/              # Tela para Menus do sistema
├── app.py                     # Arquivo principal para execução do projeto
├── pyproject.toml              # Arquivo de configuração do Poetry e dependências
└── README.md                  # Documentação do projeto
```

## Como Executar

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/FillipeBerssot/sistema-medico-bater-ponto.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd projeto-sistema-medico
   ```

3. Instale as dependências do projeto usando o Poetry:
   ```bash
   poetry install
   ```

4. Inicie a aplicação:
   ```bash
   poetry run python app.py
   ```

## Contribuição

Este projeto é apenas para fins educacionais.
