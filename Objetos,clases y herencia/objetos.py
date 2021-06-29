class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    #creando un metodo
    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)

usuario = Usuario('Solitario','Avalos')
usuario.saludo()