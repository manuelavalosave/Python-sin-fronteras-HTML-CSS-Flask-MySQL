#crear una calculadora solo de suma

primeroNumero  = input("Introduce el primer Numero: ")
try:
    primeroNumero = int(primeroNumero)
except:
    primeroNumero = 0

segundoNumero  = input("Introduce el Segundo Numero: ")
try:
    segundoNumero = int(segundoNumero)
except:
    segundoNumero = 0
signo = input("Ingrese operacion: ")

if signo == '+':
        print('Suma:', primeroNumero + segundoNumero)
elif signo == '-':
    print('Resta:', primeroNumero - segundoNumero)
elif signo == '*':
    print('Multiplicado', primeroNumero * segundoNumero)
elif signo == '/':
    print('Divicion', primeroNumero / segundoNumero)
else:
    print('El simbolo ingresado no es valido')

print(primeroNumero + segundoNumero)
