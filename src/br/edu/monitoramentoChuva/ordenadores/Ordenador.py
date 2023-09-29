class Ordenador:
    def ordenar(self, array):
        """
        (d.3) ordenação crescente dos dados considerando os valores lidos dos sensores para cada coisa monitorada;
        Complexidade: O(n^2), onde 'n' é o número de elementos no array.
        """
        # Loop externo percorre todos os elementos do array, exceto o último
        for i in range(len(array) - 1):
            indice_do_menor = i

            # Loop interno encontra o índice do menor elemento não ordenado
            for j in range(i + 1, len(array)):
                if array[j] < array[indice_do_menor]:
                    indice_do_menor = j

            # Troca o elemento atual com o menor elemento encontrado
            array[i], array[indice_do_menor] = array[indice_do_menor], array[i]
