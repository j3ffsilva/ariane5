from flask import Flask, jsonify, request
from positioning import CalculadoraVelocidade

calc_veloc_app = Flask(__name__)

@calc_veloc_app.route('/calcular_velocidade', methods=['POST'])
def calcular_velocidade():
    """
    Calcula a velocidade entre dois pontos geográficos baseada na distância percorrida
    e no tempo decorrido.
    
    O corpo da requisição deve ser um JSON contendo:
    - pos1: Tupla com latitude e longitude do ponto inicial (ex: [lat1, long1]).
    - pos2: Tupla com latitude e longitude do ponto final (ex: [lat2, long2]).
    - tempo_segundos: Tempo decorrido entre os dois pontos, em segundos.
    
    Retorna a velocidade calculada em metros por segundo.
    """

    data = request.get_json()
    pos1 = data['pos1']  # Ponto inicial
    pos2 = data['pos2']  # Ponto final
    tempo_segundos = data['tempo_segundos']  # Tempo decorrido

    velocidade = CalculadoraVelocidade.calcular_velocidade(pos1, pos2, tempo_segundos)
    
    return jsonify({"velocidade_metros_por_segundo": velocidade})

if __name__ == '__main__':
    calc_veloc_app.run(host="0.0.0.0", port=8082, debug=True)
