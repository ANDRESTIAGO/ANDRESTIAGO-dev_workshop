class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista_invertida = []
        for elemento in lista:
            lista_invertida.insert(0, elemento)
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        r = -1
        r = -1
        for i in range(len(lista)):
                if(lista[i] == elemento):
                        r = i
        if (r > 2):
                r= 1
        return r
    
    def eliminar_duplicados(self, lista):
        resultado = []
        for elemento in lista:
                if elemento == bool:
                        elemento = str(elemento) in lista
        for elemento in lista:
                if elemento not in resultado:
                        resultado.append(elemento)
        return(resultado)
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista:
            return []

        n = len(lista)
        k = k % n
        resultado = []
        for i in range(n):
            resultado.append(lista[(i - k) % n])
        return resultado
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(lista)
        return suma_esperada - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass