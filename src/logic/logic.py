class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        r = a and b
        return r
    
    def OR(self, a, b):
        r = a or b
        return r
    
    def NOT(self, a):
        r = not a
        return r
    
    def XOR(self, a, b):
        r = (a or b) and not (a and b)
        return r
    
    def NAND(self, a, b):
        r = not(a and b)
        return r
    
    def NOR(self, a, b):
        r = not(a or b)
        return r
    
    def XNOR(self, a, b):
        r = not((a or b) and not (a and b))
        return r
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        pass
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        pass
    
    
