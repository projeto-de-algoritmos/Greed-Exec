class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # Inicializa o fim do último intervalo não sobreposto como 0 e a contagem de intervalos sobrepostos como 0.
        fim, count = float('-inf'), 0

        # Ordena os intervalos pelo termino.
        for comeco, proxFim in sorted(intervals, key=lambda x: x[1]):
            # Se o início do intervalo atual é maior ou igual ao fim do último intervalo não sobreposto,
            # atualiza o fim do último intervalo não sobreposto.
            if comeco >= fim: 
                fim = proxFim
            else: 
                # Caso contrário, incrementa a contagem de intervalos sobrepostos.
                count += 1

        # Retorna a contagem de intervalos sobrepostos.
        return count
