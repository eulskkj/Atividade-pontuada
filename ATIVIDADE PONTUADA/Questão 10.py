import os
os.system ("clear")

#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

quantidade_litros = float(input("Quantidade de litros: "))
tipo_combustivel = input("Tipo de combustivél (A para álcool e G para gasolina): ").upper()

preco_alcool = 3.79
preco_gasolina = 6.59

match tipo_combustivel:
    case "A":
        if quantidade_litros <= 25:
            desconto = 0.02
        else:
            desconto = 0.04
    case "G":
        if quantidade_litros <= 25:
            desconto = 0.03 
        else:
            desconto = 0.5
desconto = quantidade_litros * desconto
preco_desconto = quantidade_litros - desconto
valor_total = quantidade_litros * preco_desconto

print(f"Preço com desconto: {preco_desconto}")
print(f"Quantidade de litros: {quantidade_litros}")
print(f"Tipo combustivel: {tipo_combustivel}")
print(f"Desconto: {desconto}")
print(f"Valor total: {valor_total}")








