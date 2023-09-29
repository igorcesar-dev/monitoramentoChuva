# Importando as classes necessárias do pacote 'ordenadores'
from ordenadores.Ordenador import Ordenador

# Importando as classes necessárias do pacote 'impl'
from impl.MonitoramentoImpl import MonitoramentoImpl
from impl.QuantidadeChuvaImpl import QuantidadeChuvaImpl
from impl.RegiaoImpl import RegiaoImpl

# Função principal que será executada quando o script for iniciado
def main():
    # Instanciando objetos das classes necessárias
    chuva = QuantidadeChuvaImpl()   
    monitoramento = MonitoramentoImpl()   
    regiao = RegiaoImpl()   
    ordenador = Ordenador()   

    # Adicione as regiões usando os métodos da classe RegiaoImpl
    for regiao_nome in [
        "Planalto", "Vitória da Conquista", "Poções", "Barra do Choça",
        "Jequié", "Ilhéus", "Feira de Santana", "Salvador", "Brumado", "Cândido Sales"
    ]:
        regiao.adicionar_regiao(regiao_nome)


    # Lista vazia para armazenar dados de chuva
    chuvas = []

    # Loop para gerar dados de chuva para 10 dias
    for i in range(10):
        # Gerando dados de chuva para o dia atual
        chuva_dia = chuva.gerar_milimetros(10)
        
        # Ordenando os dados de chuva
        ordenador.ordenar(chuva_dia)  
        
        # Adicionando os dados de chuva à lista 'chuvas'
        chuvas.append(chuva_dia) 
        
        # Adicionando os dados de monitoramento para a região atual
        monitoramento.adicionar_monitoramento(regiao.buscar_regiao(i), chuva_dia)


    # Testando d.1;
    regiao.imprimir_regioes()

    # Testando d.2 e d.3
    monitoramento.imprimir_monitoramentos() 

    # Testando d.4
    monitoramento.calcular_diferenca_chuva_entre_regioes()   

if __name__ == "__main__":
    main()
