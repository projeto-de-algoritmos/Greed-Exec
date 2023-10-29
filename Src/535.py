import heapq

# Definindo a estrutura de um nó da árvore de Huffman
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

# Função para criar a tabela de Huffman a partir da árvore de Huffman
def criar_tabela_huffman(node, codificacao, tabela_huffman):
    # Se o nó é uma folha (não tem filhos), adiciona a codificação na tabela de Huffman
    if node.left is None and node.right is None:
        tabela_huffman[node.char] = codificacao
        return
    # Se o nó não é uma folha, continua a construção da tabela para os filhos do nó
    criar_tabela_huffman(node.left, codificacao + "0", tabela_huffman)
    criar_tabela_huffman(node.right, codificacao + "1", tabela_huffman)

# Função para calcular as frequências dos caracteres no texto
def calcular_frequencias(texto):
    frequencias = {}
    for char in texto:
        if char not in frequencias:
            frequencias[char] = 0
        frequencias[char] += 1
    return frequencias

# Função para construir a árvore de Huffman a partir das frequências dos caracteres
def construir_arvore_huffman(frequencias):
    fila_prioridade = [Node(char, freq) for char, freq in frequencias.items()]
    heapq.heapify(fila_prioridade)
    while len(fila_prioridade) > 1:
        a = heapq.heappop(fila_prioridade)
        b = heapq.heappop(fila_prioridade)
        heapq.heappush(fila_prioridade, Node(None, a.freq + b.freq, a, b))
    return fila_prioridade[0]

class Codec:
    def __init__(self):
        self.tabela_huffman = {}
        self.raiz = None

    # Função para codificar o texto usando a árvore de Huffman
    def encode(self, longUrl):
        frequencias = calcular_frequencias(longUrl)
        self.raiz = construir_arvore_huffman(frequencias)
        criar_tabela_huffman(self.raiz, "", self.tabela_huffman)
        return "".join(self.tabela_huffman[char] for char in longUrl)

    # Função para decodificar o texto usando a árvore de Huffman
    def decode(self, shortUrl):
        texto_decodificado = []
        node = self.raiz
        for bit in shortUrl:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.left is None and node.right is None:
                texto_decodificado.append(node.char)
                node = self.raiz
        return "".join(texto_decodificado)