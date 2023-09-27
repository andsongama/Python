#Aula 15
#Exercício 1:
#Calcule a raiz quadrada de um número inteiro inserido pelo usuário usando o módulo math.

import math

x = float(input("Digite um número para calculo da raiz -> "))
y = math.sqrt(x)
print(y)



#Exercício 2:
#Calcule o valor absoluto de um número decimal inserido pelo usuário usando o módulo math

a = float(input("Digite um número decimal qualquer -> "))
b = math.fabs(a)
print(b)


#Exercício 3:
#Arredonde um número decimal inserido pelo usuário para o inteiro mais próximo 
#usando o módulo math

c = float(input("Digite um número decimal qualquer -> "))
d = math.ceil(c)
print(d)    ''


#Exercício 4:
#Calcule o seno de um ângulo em graus inserido pelo usuário usando o módulo math.

angulo = int(input("Digite um ângulo para cálculo do seno -> "))
seno = math.sin(angulo)
print(seno)  

