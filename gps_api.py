from flask import Flask, jsonify
from positioning import GPS

# Criação da aplicação Flask.
gps_app = Flask(__name__)

# Definição da rota '/gps/<int:t>' com o método HTTP GET.
# Esta rota é usada para obter a posição GPS em um determinado tempo 't'.
@gps_app.route('/gps/<int:t>', methods=['GET'])
def get_gps_position(t):
    """
    Obtém a posição GPS para um tempo especificado.

    :param t: Inteiro representando o tempo para o qual a posição GPS é requisitada.
    :return: Objeto JSON contendo a latitude e longitude para o tempo 't'.
    """
    gps = GPS()
    
    # Obtém a posição GPS para o tempo 't' usando o método 'get_posicao' da classe GPS.
    posicao = gps.get_posicao(t)
    
    return jsonify({"latitude": posicao[0], "longitude": posicao[1]})


if __name__ == '__main__':
    gps_app.run(host="0.0.0.0", port=8081, debug=True)

