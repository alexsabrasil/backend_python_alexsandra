# Sistema de Recomendação de Consumo de Água Diária

# Entrada de dados
nome = input("Digite seu nome: ")
whatsapp = input("Digite seu número de WhatsApp com DDD: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Cálculo da ingestão diária de água (em litros)
agua_ml = peso * 35
agua_litros = agua_ml / 1000  # conversão para litros

# Saída formatada
print("\n===== Resultado =====")
print(f"Nome: {nome}")
print(f"WhatsApp: {whatsapp}")
print(f"Peso: {peso:.1f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Ingestão diária de água recomendada: {agua_litros:.2f} litros ({agua_ml:.0f} ml)")