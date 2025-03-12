import os
os.system ("clear")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que a A + B é maior que C.

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

soma = a + b

if soma > c:
    resultado = ("Número maior que o c ")
else:
    resultado = ("Número menor que o c ")
print(f"Primeiro número: {a}")
print(f"Segundo número: {b}")
print(f"Terceiro número: {c}")
print(f"Soma {soma}")
print(f"Resultado: {resultado}")




