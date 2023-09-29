import random

class QuantidadeChuvaImpl:
    def gerar_milimetros(self, numero_de_dias):
        """
        2) (a) gerar automaticamente (randomicamente) os dados. | Complexidade: O(n), onde n é o número de dias especificado pelo parâmetro numero_de_dias.
        """
        quantidade_de_chuva = [0.0] * numero_de_dias  # Inicializa um array com zeros para representar a quantidade de chuva em milímetros para cada dia

        for i in range(numero_de_dias):
            if random.randint(0, 1) == 1:
                quantidade_de_chuva[i] = round(random.uniform(0, 55), 2)  # Gera um valor aleatório entre 0 e 55 para representar a quantidade de chuva para o dia

        return quantidade_de_chuva  # Retorna o array de quantidade de chuva em milímetros para cada dia
