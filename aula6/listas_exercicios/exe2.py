"""""
Exercício 2: Classificação de idade (if/elif/else) Peça a idade de uma pessoa e
classifique como Criança, Adolescente ou Adulto.
"""
idade = int(input("Digite a idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
