"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura de tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem comparadas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
"""
area = int(input('Digite a area a ser pintada? '))
litros = area//6
if litros > 1:
    print(litros, 'litros')
if litros == 1:
    print(litros, 'litro')
print('Escolha sua Opção:')
print('''
[1°] comprar apenas latas de 18 litros -> R$80,00.
[2°] comprar apenas galões de 4 litros -> R$25,00.
[3°] misturar latas e galões, de forma q o preço seja menor.''')
opc = int(input('Digite sua opção.'))
if opc == 1:
    if litros <= 18:
        print('Voce vai gastar 80 R$ com uma lata de 18 Litros.')
        print(f'E sobraram {18 - litros} litros de tinta.')
    elif litros > 18:
        div = litros//18
        if div % 3 > 0:
            div += 1
        print(f'Voce precisara de {div} Litros.')
        print(f'Que custaram {div*80}R$')
elif opc == 2:
    if litros < 4:
        print(f'Voce vai compra um galão de 4 litros.E vai paga 25R$')
    elif litros > 4:
        div = litros//4
        if div % 3 > 0:
            div += 1
        inc = (div*4)//litros
        print(f'Voce precisa de mais de {div} Galões de 4 litros.')
        print(f'Que vão te custar {div*25}R$ no total.')
        print(f'E sobrará {inc+1} Litros.')
if opc == 3:
    resp = int(input('Quantas latas de 18 litros? '))
    resp2 = int(input('Quantas latas de 4 litros? '))
    if litros <= 70:#coloquie uma condição para melhorar/não tem logica o cara querer dividir se é pouca tinta.
        certz = str(input('Observação: A quantidade de litros é pouca,Tem certeza que deseja continuar. ')).strip().lower()[0]
        if certz == 's':
            soma = ((resp*80) + resp2*25)
            desc = soma + (soma * 10) / 100
            print(f"total a pagar com 10% de desconto {desc}")
            sobra = ((resp*18) + resp2*4)
            print(f'Sobrará {sobra - litros} Litros de tinta..')