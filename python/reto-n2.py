"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(palabra):
    i = 0
    count = 0
    invertido = palabra[::-1]
    caracteres = len(palabra)
    for i in range(caracteres):
        if palabra[i] == invertido[i]:
            count += 1
    if count == caracteres:
        print("Es un anagrama")
    else:
        print("No es un anagrama")


palabra = input("Ingrese una palabra: ")

anagrama(palabra)
