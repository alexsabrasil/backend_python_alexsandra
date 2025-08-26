"""
Exercício 7: Verificação de vogais (função de string) Peça uma letra e verifique se é
uma vogal usando funções de string.
"""

def verificar_vogal(letra):
    letra = letra.lower()
    if letra in "aeiou":
        return f"A letra '{letra}' é uma vogal."
    else:
        return f"A letra '{letra}' não é uma vogal."

# Programa principal
letra_digitada = input("Digite uma letra: ").strip()

if len(letra_digitada) == 1:
    print(verificar_vogal(letra_digitada))
else:
    print("Digite apenas UMA letra.")



"""def eh_vogal(letra):
    if letra in "aeiouAEIOU":
        return True
    else:
        return False
    
# Programa principal
entrada = input("Digite uma letra:  ")

if eh_vogal(entrada):
    print("É uma vogal")
else:
    print("Não é vogal")

# Primeiro modo sem prestar atenção no enunciado
#letra = input("Digite uma letra: ").lower()
#if letra in "aeiou":
    #print("É uma vogal")
#else:
    #print("Não é uma vogal")

# Verificação de vogais
#letra = input("Digite uma letra: ")
#if letra in "aeiouAEIOU":
    #print("É uma vogal")
#else:
    #print("Não é uma vogal")
    """