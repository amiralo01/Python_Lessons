"""
Faça um programa que pessa as 4 notas bimestrais e mostre a média do aluno.
"""
nota1 = int(input("1° Semestre: "))
nota2 = int(input("2° Semestre: "))
nota3 = int(input("3° Semestre: "))
nota4 = int(input("4° Semestre: "))

print(nota1, "+", nota2, "+", nota3, "+", nota4, "=", (nota1+nota2+nota3+nota4))
print("Média = ", (nota1+nota2+nota3+nota4)/4)