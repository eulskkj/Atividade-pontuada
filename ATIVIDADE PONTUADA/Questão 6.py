import os
os.system ("clear")

#Questão 6:
#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas. O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0), média até 4,0, o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado.

primneira_nota = float(input("Digite sua nota: "))
segunda_nota = float(input("Digite sua nota: "))
media = primneira_nota + segunda_nota / 2

if media >= 6:
    print ("Aprovado!")
else:
    print ("Reprovado!")




