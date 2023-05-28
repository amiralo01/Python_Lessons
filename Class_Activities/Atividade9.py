"""Faça um programa que leia três númeors e mostre o maior e o menor entre eles"""

# Maneira comum:

"""numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
elif numero2 < menor:
    menor = numero2

if numero3 > maior:
    maior = numero3
elif numero3 < menor:
    menor = numero3

print(f'Maior número = {maior} e menor número = {menor}')"""

# Com listas

numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print(f'O maior número é {max(numeros)} e o menor é {min(numeros)}')