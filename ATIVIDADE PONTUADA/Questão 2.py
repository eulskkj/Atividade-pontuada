import os
os.system ("clear")

#Questão 2:
#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo(M para masculino ou F para feminino): ")
estado_civil = input("Digite seu estado civil: ")

if sexo == "F" and estado_civil == "casada":
    tempo_casada = float(input("Digite tempo de casada (anos): ")) 
    print(f"Tempo de casada: {tempo_casada}")
else:
    resultado = "FIM!"

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")









