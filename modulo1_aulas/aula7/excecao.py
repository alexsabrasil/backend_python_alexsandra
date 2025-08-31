try: 
    numero = int(input('Digite um número: '))
    resultado = 10/numero
    print('Resultado:' , resultado)
except ValueError:
    print('Erro: O número que você digitou está incorreto')
except ZeroDivisionError: 
    print("Erro: não é possível dividir por zero.")
else:
    print('Resultado:', resultado)