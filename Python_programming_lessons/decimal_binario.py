def dec_bin(num):
    # Conversão de decimal para binário
    if num > 1:
        dec_bin(num // 2)
    print (num % 2, end='')

#Ex:
print ("Digite o número decimal a ser convertido para binário")
num_decimal = int(input(''))
print ("O número decimal", num_decimal, "em binário é")
dec_bin(num_decimal)
