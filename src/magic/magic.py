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
        suma = 0
        for digito in str(abs(n)):
            suma += int(digito)
        return suma
    
    def es_numero_armstrong(self, n):
        digitos = str(n)
        suma = sum(int(digito) ** len(digitos) for digito in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False

        suma_magica = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_magica:
                return False

        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_magica:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False

        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_magica:
            return False

        return True