class MonitoramentoImpl:
    
    # Inicializa a instância da classe com um dicionário vazio para armazenar os dados de monitoramento.
    def __init__(self):
        self.monitoramento = {}

    # Adiciona dados de monitoramento para uma região específica no dicionário | Complexidade: O(1)
    def adicionar_monitoramento(self, regiao, qtdchuva):
        self.monitoramento[regiao] = qtdchuva

    # (d.2) Imprime os dados de monitoramento para todas as regiões armazenadas no dicionário | Complexidade: O(n)
    def imprimir_monitoramentos(self):
        for chave, valores in self.monitoramento.items():
            print('--------------------------------------------------------------------------------------------------------------------------')
            print(f"Quantidade de chuva detectada para a região de {chave}:")
            for valor in valores:
                print(f"     {valor} mm/h")

    # (d.4) Funcionalidade extra | Complexidade: O(n^2)
    def calcular_diferenca_chuva_entre_regioes(self):
        print('--------------------------------------------------------------------------------------------------------------------------')
        print("Diferença de chuva entre regiões:")
        regioes = list(self.monitoramento.keys())
        for i in range(len(regioes)):
            for j in range(i + 1, len(regioes)):
                regiao1 = regioes[i]
                regiao2 = regioes[j]
                chuva_regiao1 = self.monitoramento[regiao1]
                chuva_regiao2 = self.monitoramento[regiao2]

                diferenca = abs(sum(chuva_regiao1) - sum(chuva_regiao2))

                diferenca_formatada = round(diferenca, 2)
                print(f"        Diferença entre {regiao1} e {regiao2}: {diferenca_formatada} mm")