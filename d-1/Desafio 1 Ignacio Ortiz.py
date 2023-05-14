seg = int(input('Ingrese la cantidad de segundos: '))
horas = 0
minutos = 0
segundos = 0

if seg > 89999:
    print('Excedido')

else:
    horas = seg // 3600
    minutos = seg % 3600 // 60
    segundos = seg % 3600 % 60

print('Los segundos equivalen a', horas, 'horas', minutos, 'minutos', segundos, 'segundos')

horas = int(input('Ingrese la cantidad de horas: '))
minutos = int(input('Ingrese la cantidad de minutos: '))
segundos = int(input('Ingrese la cantidad de segundos: '))

segundos = horas * 3600 + minutos * 60 + segundos

print('El total de sugundos son: ', segundos)




