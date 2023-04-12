print("Aprendendo mais sobre comparações multiplas em Python")
"""
Faça um Programa que leia um número e exiba o dia correpondente da semana.
(1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

"""dia = int(input("Digite o dia da semana: "))

#Variável auxiliar que verifica o dia correspondente
#Por definição para verificar cada dia se declara como "False"
#Afirmando que não bate como nenhum dia da semana
verifica = False

#Caso ele seja correspondente a algum dia da semana ele verifica com o "True"
if dia == 1:
    print("Domingo")
    verifica = True

if dia == 2:
    print("Segunda")
    verifica = True

if dia == 3:
    print("Terça")
    verifica = True

if dia == 4:
    print("Quarta")
    verifica = True

if dia == 5:
    print("Quinta")
    verifica = True

if dia == 6:
    print("Sexta")
    verifica = True

if dia == 7:
    print("Sabádo")
    verifica = True

# Se verifica for diferente de True a mensagem será retornada    
if verifica != True:
    print("Entrada Inválida")
"""

# O programa funciona porém o programa não está elegante!

"""
Não é recomendável o comando a seguir 
Pois só retornara a mensagem de maneira exata se o valor for maior que 7
else:
    print("Valor inválido")
Pois a mensagem ainda aparecerá se o valor for menor que 7
"""

#Para tornar o código mais elegante é recomendável utilizar o "elif"
#Funcionando como uma segunda condição caso a primeira não seja cumprida
"""dia = int(input("Digite o dia da semana: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabádo")
else:
    print("Entrada Inválida")"""

"""Faça um programa que leia três números e mostre-os em ordem decrescente."""

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

"""
if a < b:
    if a < c:
        if b < c:
            print(c, b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
Este programa funciana porém é pouco prático e eficiente
"""

#Exemplo de um programa mais funcional:
if a>=b>=c:
    print (a, b, c)
elif a>=c>=b:
    print(a, c, b)
elif b>=a>=c:
    print(b, a, c)
elif b>=c>=a:
    print(b,c, a)
elif c>=a>=b:
    print(c, a, b)
else:
    print(c, b, a)