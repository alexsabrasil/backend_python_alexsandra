import saudacao
import matematica
import tabuada as tb
from conversao import celsius_para_fahrenheit
import random
from constantes import PI

# Saudação
saudacao.bom_dia("Seu Nome")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Matematica 
print("Soma:", matematica.soma(a, b))
print("Subtração:", matematica.subtracao(a, b))

# Tabuada
tb.mostrar_tabuada(7)

# Conversão
c = float(input("Digite a temperatura em Celsius: "))
f = celsius_para_fahrenheit(c)
print(f"{c}°C em Fahrenheit é {f}°F")

# Usando Módulos Internos do Python
numero_sorteado = random.randint(1, 10)
tentativa = int(input("Adivinhe o número entre 1 e 10: "))

if tentativa == numero_sorteado:
    print("Parabéns! Você acertou!")
else:
    print(f"Errou! O número era {numero_sorteado}.")

# Constantes
raio = float(input("Digite o raio do círculo: "))
area = PI * raio ** 2
print(f"A área do círculo é {area:.2f}")
