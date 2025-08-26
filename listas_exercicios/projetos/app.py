# app.py

import matematica

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print(f"Soma: {matematica.somar(a, b)}")
    print(f"Subtração: {matematica.subtrair(a, b)}")
    print(f"Multiplicação: {matematica.multiplicar(a, b)}")
    print(f"Divisão: {matematica.dividir(a, b)}")

except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Ocorreu um erro inesperado:", e)
