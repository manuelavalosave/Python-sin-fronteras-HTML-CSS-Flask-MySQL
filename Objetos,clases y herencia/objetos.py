class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    #creando un metodo
    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)



#creando una herencia
class Admistrador(Usuario):
    def superSaludo(self):
        print('Hola! soy,', self.nombre,' Y soy el Administrador')

usuario = Usuario('Solitario','Avalos')
usuario.saludo()
usuario.nombre = 'Manuel'
usuario.saludo()

adm = Admistrador('Solitario','Avalos')
adm.saludo()
adm.superSaludo()