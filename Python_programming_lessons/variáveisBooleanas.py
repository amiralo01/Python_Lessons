#Pode receber valor True = verdadeiro ou False = falso
#Criação de um sistema para o controle de jovens
# Que podem ou não ingerir bebidas alcólicas de acordo com sua idade
x = True
y = False
print(x, "Se a pessoa tiver a idade maior ou igual a 18")
print( y, "Se a pessoa tiver a idade menor a 18")
Idade = int(input("Digite sua idade: "))
Autorizado = Idade >= 18
print(Autorizado)

#<, >, >=. <=, ==, !=
#True == 1 e False == 0

#Qualquer numero inteiro que se insira no bool o python retorna como verdadeiro ou falso
#Ele não aceita None, False, [], {}, (), '', "", 0, 0.0  e etc.
xy = bool(217)
