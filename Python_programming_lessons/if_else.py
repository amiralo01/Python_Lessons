Idade = int(input("Digite sua idade: "))
resp = Idade >= 18

if resp == True:
    print("Você pode beber a vontade")

if resp == False:
    print("Voce só pode beber água e refrigerante")

#ou você pode colocar
#if resp:
#    print("Você pode beber a vontade")
#if resp != True:
#    print("Voce só pode beber água e refrigerante")
#print(resp)

#ou
#if idade >= 18:
#    print("Você pode beber a vontade")
#if idade < 18:
#    print("Voce só pode beber água e refrigerante")

#Para acrescentar e agregar mais uma condição ao programa segue um exemplo
if resp >= 21:
    print("Você é VIP")

#ou 
#if resp == True:
#    print("Você pode beber a vontade")
#    if resp >= 21:
#        print("Você é VIP")
#Não há ´roblema colocar um if dentro de outro

print(resp)

#Para o else(Se não)
if Idade >= 18:
    print("Você pode beber a vontade")
    if Idade >= 21:
        print("Você é VIP")
else:
    print("Você só pode beber refrigerante e água")
print(Idade)

#Exercício: Faça um Programa que peça dois números e imprima o maior dos dois

num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))

if num1 >= num2:
    print(num1)
else:
    print(num2)
"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário as quantidades de latas de tinta
a serem compradas e o preço total.
"""

area = int(input("Digite a área a ser pintada: "))
litros = area//3

if litros % 3 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Você precisara de", latas, "latas.")
print("Você vai pagar R$", latas*80)
#print(litros)
#print(latas) 