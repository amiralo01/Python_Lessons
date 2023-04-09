print('Eu tenho', 5, 'gatos')
print('Eu tenho', 7, 'gatos')
print('Eu tenho', 2, 'gatos')
#para que não fique tão repetitivo os números a serem digitados, criamos uma variável que no caso será o num.
num=5
print('Eu tenho', num, 'gatos')
#para mudar de número vc pode criar outra váriavel ou então somente mudar o número dela.
nume=3
print('Eu tenho', nume, 'gatos machos')
num=2
print('Eu tenho', num, 'gatas fêmeas')

#Criação de váriáveis que podem se interagir entre elas.
x=1
y=x
z=y
#depois da criação da variável x eu posso alterar o seu valor e assim como os demais que não ocorrerá erro no sistema pois o ultimo valor é quem conta.
x=y=z=2
print('Eu tenho', x, 'gatas fêmeas')
print('Eu tenho', y, 'gatas fêmeas')
print('Eu tenho', z, 'gatas fêmeas')

#logo depois pode ser feito mais alterções assim como está.
x, y, z = 1, 2, 3
#imprimindo o valor de cada váriavel
print(x)
print(y)
print(z)

'''
Existem alguns erros em váriaveis que não são aceitos, por exemplo:
num espaço = 10.
com esse espaço esta váriavel não é aceito pois é necessário a variável ser somente uma palavra.

Também não é aceito caracteres especiais como variáveis, por exemplo:
    !@#$%"&*()[]{}'?/|\ º°;:^~+` ´,<>.ª-¨¬§
O Anderline: _
Ele pode ser usado como um espaço para um nome de váriavel.
'''
print('Exemplos de Anderlines')
ação = 10
peso_meu = 10
_pesinho = 5
peso_ = 10

print(ação)
print(peso_meu)
print(_pesinho)
print(peso_)

#Não pode colocar como variàvel aqueles que são os carecteres reservados em python, são lidos de maneira especial.
#Exemplo, class e while.
#Mas também existem os que podem como o print e o int.

#também funciona, porém não é recomendável. 
float = 10
print(float)