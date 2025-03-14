class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Área del rectángulo
        """
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        perimetro = (2*base) + (2*altura)
        return perimetro
    
    def area_circulo(self, radio):
        import math
        area = (math.pi)*radio**2
        return area
    
    def perimetro_circulo(self, radio):
        import math
        perimetroc = 2*(math.pi)*radio
        return perimetroc
    
    def area_triangulo(self, base, altura):
        area = (base * altura)/2
        return area
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        return perimetro
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        a = 0
        if ((lado1 + lado2)>lado3):
            a += 1
        else:
            a -= 1
        if ((lado2 + lado3)>lado1):
            a += 1
        else:
            a -= 1
        if ((lado3 + lado1)>lado2):
            a += 1
        else:
            a -= 1
        if (a == 3):
             return True
        else:
             return False
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        area = (((base_mayor + base_menor))/2)*altura
        return area
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        area = (diagonal_mayor * diagonal_menor)/2
        return area
    
    def area_pentagono_regular(self, lado, apotema):
        perimetro = lado * 5
        area = (perimetro * apotema)/2
        return area
    
    def perimetro_pentagono_regular(self, lado):
        perimetro = lado * 5
        return perimetro
    
    def area_hexagono_regular(self, lado, apotema):
        area = 3 * lado * apotema
        return area
    
    def perimetro_hexagono_regular(self, lado):
        perimetro = lado *6
        return perimetro
    
    def volumen_cubo(self, lado):
        volumen = lado ** 3
        return volumen
    
    def area_superficie_cubo(self, lado):
        area = 6*(lado ** 2)
        return area
    
    def volumen_esfera(self, radio):
        import math
        volumen = (4/3)*math.pi*radio**3
        return volumen
    
    def area_superficie_esfera(self, radio):
        import math
        area = 4*math.pi*radio**2
        return area
    
    def volumen_cilindro(self, radio, altura):
        import math
        volumen = math.pi*(radio**2)*altura
        return volumen
    
    def area_superficie_cilindro(self, radio, altura):
        import math
        area = (2*math.pi*(radio**2)) + 2*math.pi*radio*altura
        return area
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        import math
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(distancia, 2)
    
    def punto_medio(self, x1, y1, x2, y2):
        punto_x = ((x1 + x2)/2)
        punto_y = ((y1 + y2)/2)
        return punto_x, punto_y
    
    def pendiente_recta(self, x1, y1, x2, y2):
        pendiente = ((y2 - y1)/(x2 - x1))
        return pendiente
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        A = (y2 - y1)
        B = -(x2 - x1)
        C = -(A * x1 + B * y1)
        return (A, B, C)
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        perimetro = lado * num_lados
        area = (perimetro * apotema)/2
        return round(area,2)
    
    def perimetro_poligono_regular(self, num_lados, lado):
        perimetro = lado * num_lados
        return perimetro