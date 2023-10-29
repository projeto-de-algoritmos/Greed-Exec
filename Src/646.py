class Solution(object):
    def findLongestChain(self, pairs):
        # Ordena os pares pela extremidade final.
        parsOrdenados = sorted(pairs, key=lambda x: x[1])

        # Se a lista de pares está vazia, retorna 0.
        if len(parsOrdenados) == 0:
            return 0

        # Inicializa o fim do último par não sobreposto como o fim do primeiro par na lista ordenada e a contagem da cadeia como 1.
        fimAtual, comprimento = parsOrdenados[0][1], 1

        # Itera sobre cada par na lista ordenada.
        for par in parsOrdenados:
            # Se o fim do último par não sobreposto é menor que o início do par atual,
            # incrementa a contagem da cadeia e atualiza o fim do último par não sobreposto.
            if fimAtual < par[0]:
                comprimento += 1
                fimAtual = par[1]

        # Retorna a contagem da cadeia, que representa o comprimento da cadeia mais longa de pares.
        return comprimento