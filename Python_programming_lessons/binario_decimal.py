def bin_dec(binary):
    decimal = 0
    p = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * 2 ** p
        p -= 1
    return decimal

binario_numero = input("Digite o número binário a ser convertido: ")
decimal_numero = bin_dec(binario_numero)
print(decimal_numero)