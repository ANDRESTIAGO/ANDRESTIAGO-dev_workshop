class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        if n < 0:
            print("n debe ser un número entero no negativo")
            return
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            print("n debe ser un número entero positivo")
            return
        secuencia = []
        a, b = 0, 1
        for i in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia
    
    def es_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        if n < 2:
            return []

        primos = []
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n):
        if n <= 0:
            return False

        suma_divisores = 0
        for i in range(1, n):
            if n % i == 0:
                suma_divisores += i
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []

        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            return None

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        mayor = max(a, b)
        menor = min(a, b)
        mcm = mayor
        while mcm % menor != 0:
            mcm += mayor
        return mcm
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass