class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        pass
    
    def invertir_cadena(self, texto):
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida
        return invertida
    
    def contar_vocales(self, texto):
        n = 0
        texto = texto.lower()
        for elemento in texto:
            if elemento == "a" or elemento == "e" or elemento == "i" or elemento == "o" or elemento == "u":
                n = n+1
        return (n)     
    
    def contar_consonantes(self, texto):
        n = 0
        texto = texto.lower()
        for elemento in texto:
            if elemento in ("aeiou"):
                n = n+1
        return n
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        pass
    
    def contar_palabras(self, texto):
        palabras = 0
        for palabra in texto.split():
            palabras += 1
        return(palabras)
    
    def palabras_mayus(self, texto):
        resultado = ""
        for palabra in texto.split(" "):
            if palabra:
                resultado += palabra[0].upper() + palabra[1:] + " "
            else:
                resultado += " "
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        for elemento in texto:
            if elemento == ".":
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones