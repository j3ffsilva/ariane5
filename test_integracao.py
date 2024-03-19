from flask.testing import FlaskClient
import pytest
from calc_veloc_api import calc_veloc_app  # Importa a aplicação Flask para calcular velocidade
from gps_api import gps_app  # Importa a aplicação Flask para obter posições GPS

@pytest.fixture
def gps_client():
    """
    Define um fixture do pytest que configura e retorna um cliente de teste para a aplicação Flask gps_app.
    
    :yield: Um cliente de teste para fazer requisições à aplicação gps_app.
    """
    with gps_app.test_client() as gps_client:
        yield gps_client

@pytest.fixture
def calc_veloc_client():
    """
    Define um fixture do pytest que configura e retorna um cliente de teste para a aplicação Flask calc_veloc_app.
    
    :yield: Um cliente de teste para fazer requisições à aplicação calc_veloc_app.
    """
    with calc_veloc_app.test_client() as calc_veloc_client:
        yield calc_veloc_client

def test_integracao_gps_calculadora_velocidade(gps_client: FlaskClient, calc_veloc_client: FlaskClient):
    """
    Testa a integração entre a API de GPS e a API de cálculo de velocidade.
    
    Este teste verifica se, ao obter duas posições diferentes de GPS e calcular a velocidade 
    entre esses dois pontos em um intervalo de 1 segundo, a velocidade calculada é positiva,
    indicando um movimento entre as posições.
    
    :param gps_client: Cliente de teste para a aplicação GPS.
    :param calc_veloc_client: Cliente de teste para a aplicação de cálculo de velocidade.
    """
    # Simula a obtenção de posição em dois momentos diferentes (t=0 e t=1) usando a API de GPS.
    resposta_gps_t0 = gps_client.get('/gps/0')
    posicao_t0 = resposta_gps_t0.get_json()

    resposta_gps_t1 = gps_client.get('/gps/1')
    posicao_t1 = resposta_gps_t1.get_json()

    # Prepara o payload com as posições obtidas para calcular a velocidade.
    payload = {
        'pos1': [posicao_t0['latitude'], posicao_t0['longitude']],
        'pos2': [posicao_t1['latitude'], posicao_t1['longitude']],
        'tempo_segundos': 1  # Considerando t1 - t0 = 1 segundo.
    }

    # Simula a requisição para calcular a velocidade com as posições obtidas usando a API de cálculo de velocidade.
    resposta_velocidade = calc_veloc_client.post('/calcular_velocidade', json=payload)
    data = resposta_velocidade.get_json()

    # Verifica se a velocidade calculada está dentro de uma faixa esperada.
    # A faixa específica depende da implementação e do quanto a posição muda entre t0 e t1.
    assert 'velocidade_metros_por_segundo' in data  # Verifica se a resposta inclui a velocidade.
    velocidade = data['velocidade_metros_por_segundo']
    assert velocidade > 0  # Verifica se a velocidade calculada é positiva, indicando movimento.