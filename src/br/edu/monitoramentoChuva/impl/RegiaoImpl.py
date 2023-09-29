class RegiaoImpl:
    def __init__(self):
        # Inicializa uma lista vazia chamada nome_regiao para armazenar nomes de regiões. Complexidade: O(1);
        self.nome_regiao = []

    def adicionar_regiao(self, nome):
        # Adiciona um nome de região à lista nome_regiao. Complexidade: O(1);
        self.nome_regiao.append(nome)

    def buscar_regiao(self, indice): # Complexidade: O(1);
        # Retorna o nome de uma região com base em um índice fornecido,
        # retornando None se o índice estiver fora dos limites da lista
        if 0 <= indice < len(self.nome_regiao):
            return self.nome_regiao[indice]
        else:
            return None

    def imprimir_regioes(self):
        """
        (d.1) imprimir a lista das pessoas ou dos objetos sendo monitorados;
        Complexidade: O(n), complexidade linear, onde n é o número de elementos na lista nome_regiao.
        """

        # Imprime uma lista de nomes de regiões presentes na lista nome_regiao
        print("Regiões em monitoramento:")
        for nome in self.nome_regiao:
            print("     " + nome)
