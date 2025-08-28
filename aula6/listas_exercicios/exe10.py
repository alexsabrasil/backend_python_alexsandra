"""
Exercício 10: Maior de três números (if/elif/else) Leia três números e mostre qual é o
maior.

"""

def maior_de_tres(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número:  "))
n3 = float(input("Digite o terceiro número: "))

print(f"O maior número é: {maior_de_tres(n1, n2, n3)}")

# a, b, c = map(int, input("Digite três números separados por espaço: ").split()) 
# print("O maior número é:" , max(a,b,c))