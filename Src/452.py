class Solution(object):
    def findMinArrowShots(self, points):
        # Obtém o número de pontos
        n = len(points)
        
        # Se houver 1 ou nenhum ponto, retorna o número de pontos
        if n <= 1:
            return n

        # Ordena os pontos pela coordenada final
        points.sort(key=lambda x: x[1])
        
        # Inicializa a lista de pontos selecionados com o primeiro ponto
        selecionados = [points[0]]
        
        # Itera sobre os pontos restantes
        for i in range(1, n):
            # Se o início do ponto atual é maior que o fim do último ponto selecionado,
            # adiciona o ponto atual à lista de pontos selecionados
            if points[i][0] > selecionados[-1][1]:
                selecionados.append(points[i])

        # Retorna o número de pontos selecionados
        return len(selecionados)
