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

#contar el total de una lista
TotalDeElementoList = len(Lista)
print(TotalDeElementoList);

#contamos cuantos elementos se repiten en una lista
print(Lista_2.count(2))

#Eliminar el ultimo elemento de la lita con el metodo pop
Lista.pop()
print(Lista)

#Eliminar un elemento en especifico
Lista_2.remove(2)
print(Lista_2)

#Ordenar elementos de una lista DESC
Lista.reverse()
print(Lista)

#Ordenar lista siempre encuando tengan el mismo tipo de dato
Lista.sort()
print(Lista)

#Utilizando Tupla, las tuplas no son dinamicas
Tuplas = ('Hola','Mundo','Estoy','Aprendiendo','Paython')
print(Tuplas[0])

#para hacer dinamica mi lista tuplas, debo de convertirla a tipo de lista
ListaTuplas = list(Tuplas)
ListaTuplas.append("Ahora ya soy Dinamica")
print(ListaTuplas)

