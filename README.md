# Simulação de GPS e Calculadora de Velocidade para Foguete

Este projeto simula, de forma simplista, a interação entre o sistema de GPS de um foguete e uma calculadora de velocidade. O objetivo é demonstrar a importância dos testes de integração em sistemas complexos, inspirado pelo desastre do foguete Ariane 5, que explodiu 40 segundos após o lançamento devido a falhas de integração que não foram adequadamente testadas.

O desastre do Ariane 5 destaca a crítica necessidade de testes de integração em sistemas de software, especialmente aqueles que lidam com a vida humana e equipamentos valiosos. Este projeto serve como um lembrete e uma ferramenta educacional sobre a importância de validar a integração entre diferentes componentes de um sistema.

## Visão Geral

O projeto consiste em duas partes principais:

- **API de GPS**: Simula a obtenção de posições geográficas de um foguete em diferentes momentos do seu voo.

- **API de Calculadora de Velocidade**: Calcula a velocidade do foguete entre dois pontos no tempo, utilizando as posições fornecidas pela API de GPS.

As APIs são construídas usando o framework Flask para Python.

## Como Executar

### Requisitos
- Python 3
- Flask
- pytest (para execução de testes)

### Configuração e Execução

1. Clone o repositório para o seu ambiente local ou para uma EC2.

2. Instale as dependências utilizando `pip install -r requirements.txt`.

3. Inicie as APIs de GPS e Calculadora de Velocidade executando os arquivos correspondentes:
   - Para a API de GPS: `python gps_api.py`
   - Para a API de Calculadora de Velocidade: `python calc_veloc_api.py`

4. Execute os testes de integração para verificar a correta interação entre as APIs utilizando `pytest`.

## Estrutura do Projeto

- `gps_api.py`: Contém a implementação da API de GPS.

- `calc_veloc_api.py`: Contém a implementação da API de Calculadora de Velocidade.

- `tests/`: Diretório contendo testes de integração que simulam o uso conjunto das APIs de GPS e Calculadora de Velocidade.

## Contribuindo

Este é um projeto educacional e está aberto a contribuições. Se você tem ideias para melhorar a simulação ou para expandir o escopo do projeto, sinta-se à vontade para criar um pull request ou abrir uma issue.