#aca va un comentario
if 3 > 5 :
    print("Esto no se impreme en pantalla")

#if 5 > 3 : #Esto si se cumple
    #print("5 es mayor que 3")

#creando sintaxis de variables
x = 5
y = 'soy una variable'

#imprimo las dos variables
print(x, y)

#asigno una nueva variable
correo = 'correo@demo.com'

# print(correo)

#Asignar datos en una misma linea
a, b, c = 'LaLA','LeLe', 'LiLi'

print(a, b, c)

#Mandamos el mismo valor de una variable
valor1 = valor2 = valor3 = "Chuchito feliz"

# print(valor1, valor2, valor3)

#contatenar dos varaibles
inicio = 'Hola '
final = 'Mundo'

print(inicio + final)

Palabra = 'Esto es una palabra' #tipo String
Oracion = "Esto tambien es un string solo con comillas dobles" #tipo String

Entero = 1 #Intiger
ConDecimal = 20.0 #float

Complejo = 1j #numero complejo

# print(Palabra, Oracion, Entero, ConDecimal,Complejo)


#creando listas array()

Lista = [1,2,3]

#imprmimos lista

print(Lista)

Lista.append(4) #añadimos nuevos atributos en las lista
print(Lista)

#copiamos la lista1 con la lista 2
Lista_2 = Lista.copy()
print(Lista_2)
