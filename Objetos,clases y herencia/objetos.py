class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

usuario = Usuario('Solitario','Avalos')

print(usuario.nombre, usuario.apellido)