import os
os.system ("clear")

#Questão 4: 
#Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input("Quantidade de morango em KG: "))
maca = float(input("Quantidade de maca em KG: "))

if morango >= 5:
    preco_morango = 2.20
else:
    preco_morango = 2.50
if maca >= 5:
    preco_maca = 1.50
else:
    preco_maca = 1.80

total_morango = morango * preco_morango
total_maca = maca * preco_maca
total_compra = total_maca + total_morango

peso_total = morango + maca

if peso_total >= 10 or total_compra >=15:
    desconto = total_compra * 0.10 
    total_compra -= desconto
print(f"O total da compra é: {total_compra}")















