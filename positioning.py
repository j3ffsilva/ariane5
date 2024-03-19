import math

class GPS:
    def __init__(self):
        """
        Construtor da classe GPS.

        Inicializa um objeto GPS definindo uma posição base (origem), 
        que pode ser usada como referência para cálculos de posição.
        """
        # Inicializa uma posição base com valores de latitude e longitude iguais a 0.0.
        self.posicao_base = (0.0, 0.0)

    def get_posicao(self, t):
        """
        Calcula e retorna a posição do GPS em um determinado momento.

        Args:
            t (int): Tempo em segundos a partir do qual a posição deve ser calculada.

        Returns:
            tuple: Um par de valores (latitude, longitude) representando a nova posição do GPS.
        """
        # Simula a trajetória de movimento linear baseada no tempo 't'.
        # Para cada unidade de tempo 't', avança a posição em 0.001 graus tanto em latitude quanto em longitude.
        nova_posicao = (self.posicao_base[0] + t * 0.001, self.posicao_base[1] + t * 0.001)
        return nova_posicao

class CalculadoraVelocidade:
    @staticmethod
    def haversine(pos1, pos2):
        """
        Calcula a distância entre dois pontos na superfície da Terra usando a fórmula de Haversine.

        Args:
            pos1 (tuple): Primeiro ponto geográfico (latitude, longitude).
            pos2 (tuple): Segundo ponto geográfico (latitude, longitude).

        Returns:
            float: A distância entre os dois pontos em metros.
        """
        # Raio da Terra em metros.
        R = 6371000
        
        # Converte as coordenadas de ambos os pontos de graus para radianos.
        lat1, lon1 = map(math.radians, pos1)
        lat2, lon2 = map(math.radians, pos2)
        
        # Calcula a diferença de coordenadas.
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        # Aplica a fórmula de Haversine para calcular a distância.
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Calcula a distância final multiplicando o ângulo pelo raio da Terra.
        distancia = R * c
        return distancia

    @staticmethod
    def calcular_velocidade(pos1, pos2, tempo_segundos):
        """
        Calcula a velocidade necessária para percorrer a distância entre dois pontos 
        no tempo especificado.

        Args:
            pos1 (tuple): Primeiro ponto geográfico (latitude, longitude).
            pos2 (tuple): Segundo ponto geográfico (latitude, longitude).
            tempo_segundos (int): O tempo em segundos para percorrer entre os dois pontos.

        Returns:
            float: Velocidade em metros por segundo.
        """
        # Calcula a distância entre os dois pontos usando a fórmula de Haversine.
        distancia = CalculadoraVelocidade.haversine(pos1, pos2)
        
        # Calcula a velocidade dividindo a distância pelo tempo. Evita divisão por zero.
        if tempo_segundos > 0:
            velocidade = distancia / tempo_segundos  # Velocidade em metros por segundo.
            return velocidade
        else:
            # Retorna 0 se o tempo for 0 ou negativo.
            return 0
