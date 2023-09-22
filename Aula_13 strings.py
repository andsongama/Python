# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Aula 13
#Exercício 1: Escreva um programa que verifique se a palavra "python"
#está presente na string "Estou aprendendo Python".

texto = "Estou aprendendo Python"
if "Python" or "python" in texto:
    print("A substring 'python' está na string.")
else:
  print("A substring 'python' não está na string.")

#exercício 2: Escreva um programa que peça ao usuário para digitar
#seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).


x = input("Digite o seu nome: ")
if x.startswith("A"):
    print("A string começa com 'A'.")
elif x.startswith("a"):
    print("A string começa com 'a'.")
else:
  print("A string não começa com 'A' ou 'a'.")

#Exercício 3: Escreva um programa que peça ao usuário para digitar uma
#senha e verifique se a senha contém pelo menos 8 caracteres.

senha = input("Digite a sua senha:")
senha2 = senha.len()
if senha2 < 8:
  print(f"A senha digitada não possui a quatidade mínima de caracteres (8)")
else:
  print(f"A senha digitada atende posssui pelo menos 8 caracteres")

#Exercício 4: Escreva um programa que peça ao usuário para digitar
#um número e verifique se o número é uma representação numérica (não contém
#letras ou símbolos).

z = input("Digite sua senha: ")
if z.isnumeric():
    print("A string contém apenas dígitos numéricos.")
else:
  print("A string não contém apenas dígitos numéricos.")

#Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase
#e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

a = input("Digite uma frase qualquer: ")
print(a.count("a"))
print(a.count("A"))