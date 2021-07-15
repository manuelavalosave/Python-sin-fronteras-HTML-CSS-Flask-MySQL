class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un ', self.tipo,' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = "Gato"


class Perro(Animal):
    tipo = "Perro"

gato = Gato('Pancho','Maullido')
gato.saludo()

perro = Perro('Firulais','ladrido')
perro.saludo()
