# Exemplo de código em Python com if, if-else, for, while, array e list

# Definindo uma lista
lista_numeros = [1, 2, 3, 4, 5]

# Utilizando o loop for para percorrer a lista
print("Usando o loop for para imprimir elementos da lista:")
for numero in lista_numeros:
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")

# Utilizando o loop while para imprimir elementos da lista
print("\nUsando o loop while para imprimir elementos da lista:")
indice = 0
while indice < len(lista_numeros):
    print(f"Elemento na posição {indice}: {lista_numeros[indice]}")
    indice += 1

# Exemplo de if-elif-else
numero = 7
if numero > 0:
    print(f"{numero} é positivo.")
elif numero == 0:
    print("O número é zero.")
else:
    print(f"{numero} é negativo.")

# Utilizando array (poderia ser uma lista também)
array_valores = [10, 20, 30, 40, 50]

# Adicionando um valor ao final do array
array_valores.append(60)

# Imprimindo os valores do array
print("\nValores do array:")
for valor in array_valores:
    print(valor)

# Exemplo de utilização de list comprehension para criar uma lista com quadrados dos números de 1 a 5
quadrados = [x ** 2 for x in range(1, 6)]

# Imprimindo a lista de quadrados
print("\nQuadrados dos números de 1 a 5:")
print(quadrados)
