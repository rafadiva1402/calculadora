def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    if b!=0:
        return a/b
    else:
        return "não é possivel."

def multiplicacao(a,b):
    return a*b

numero_1 = int(input("informe o primeiro número: "))
numero_2 = int(input("informe o segundo número: "))
operador = input("informe o operador: \n+adição \n-subtração \n/divisão \n*multiplicação \n=> ")

if operador == "+":
    print("resultado: ", soma(numero_1, numero_2))
elif operador == "-":
    print("resultado: ", subtracao(numero_1, numero_2))
elif operador == "/":
    print("resultado: ", divisao(numero_1, numero_2))
elif operador == "*":
    resultado = numero_1 * numero_2
    print("resultado: ", multiplicacao(numero_1, numero_2))
else:
    print("escolha uma das 4 opções")
