import os
os.system ("clear")

#Questão 8:
#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço. A loja está atualmente com a seguinte tabela de preços.  

cor = input("Digite uma cor (verde, azul, amarelo, vermelho): ")

match cor:
    case "verde":
        print("Preço: R$ 10,00")
    case "azul":
        print("Preço: R$ 20,00")
    case "amarelo":
        print("Preço: R$ 30,00")
    case "vermelho":
        print("Preço: R$ 40,00")
    case _:
        print("Opção inválida")











