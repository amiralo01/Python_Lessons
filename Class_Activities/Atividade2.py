"""
Faça um programa que pergunte quanto vc ganha por hora e o número de horas que trabalhou
Calcule e mostre o total do seu salário no referido mês.  
"""
hora = int(input("quanto você ganha por hora:"))
nhoras = int(input("quantas horas você trabalhou nete mês:"))

print(hora,"R$", "*", nhoras, "horas", "=", (hora*nhoras), "R$")
print("Seu salário do mês =", (hora*nhoras), "R$")