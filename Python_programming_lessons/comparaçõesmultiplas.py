idade = int(input("Digite sua idade: "))
"""
Da forma tradicional como foi apresentado antes
O código seria ferito desta maneira:

if idade >= 18:
    if idade < 70:
        print("Você pode receber o benefício")
    else:
        print("Você não pode receber o benefício")
else:
    print("Você não pode receber o benefício")

Porém, não é uma boa forma, é considerado como código sujo
podendo deixar ele mais limpo, como:
"""
idade = int(input("Digite sua idade: "))

if 18 <= idade <70:
    print("Você pode receber o benefício")
else:
    print("Você não pode receber o benefício")