import os
os.system ("clear")


#Questão 7:
#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto será de 2% 
#- Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
#- Se quantidade > 10 o desconto será de 5%.

produto = input("Digite o nome do produto: ")
quantidade_adquirida = float(input("Quantidade: "))
preco_unitario = float(input("Preço do produto: "))

if quantidade_adquirida <= 5:
    desconto = (preco_unitario * quantidade_adquirida)* 0.20
if quantidade_adquirida > 5 <= 10:
    desconto = (quantidade_adquirida * preco_unitario) * 0.30
if quantidade_adquirida > 10:
    desconto = (preco_unitario * quantidade_adquirida) * 0.50

total = quantidade_adquirida * preco_unitario
total_a_pagar = total - desconto

print(f"Total a pagar: {total_a_pagar}")









