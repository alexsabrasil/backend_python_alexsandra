import math

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Triangulo:
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Lista com diferentes formas
formas = [
    Retangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4, 5, 5, 6)
]

# Polimorfismo: mesmos métodos, cálculos diferentes
print("📐 Calculadora de Formas Geométricas 📐")
for i, forma in enumerate(formas, 1):
    print(f"Forma {i}:")
    print(f"  Área: {forma.calcular_area():.2f}")
    print(f"  Perímetro: {forma.calcular_perimetro():.2f}")
    print("-" * 30)