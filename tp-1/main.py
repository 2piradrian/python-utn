vehicleID = input("Ingese la patente del vehiculo correspondiente: ")
# se realiza la verificacion antes de realizar la siguiente consulta por temas de User Experience.
# creemos que es mejor que el usuario sepa que ingreso mal la patente antes de que se le solicite el tipo de vehiculo.

# la eliminacion de esta seccion del codigo se debe al cambio de consigna
#if len(vehicleID) < 7 or len(vehicleID) > 7:
    #print("La patente ingresada es invalida, debe tener 7 caracteres")

# se realiza la consulta del tipo de vehiculo
vehicleType = int(input("Ingrese el tipo de vehiculo (0: motocicleta, 1: automovil, 2: camion): "))

# si no se encuentra en el rango de valores permitidos, se informa al usuario.
if not (vehicleType in (0, 1, 2)):
    print("El tipo de vehiculo no corresponde a los valores permitidos")

# se realiza la consulta del tipo de pago
typeOfPayment = int(input("Ingrese el tipo de pago (0: manual, 1: telepeaje): "))

# si no se encuentra en el rango de valores permitidos, se informa al usuario.
if not (typeOfPayment in (0, 1)):
    print("El tipo de pago no corresponde a los valores permitidos")

# se realiza la consulta del pais de origen
countryOfOrigin = int(input("Ingrese pais de origen (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))

# si no se encuentra en el rango de valores permitidos, se informa al usuario.
if not (countryOfOrigin in (0, 1, 2, 3, 4)):
    print("El pais de origen no corresponde a los valores permitidos")

# se realiza la consulta de la distancia entre cabinas
distanceBetweenCabines = float(input("Ingrese la distancia entre cabinas (en km). Si recien inicia ponga cero: "))

# variable que almacenara el valor del peaje
ticketPrice = None
vehicleIDCountry = None

# validacion de la patente y pais de origen
# usando la funcion isalpha() y isdigit() de la clase string
# con vehicleID[valor de inicio : valor de fin] para subdividir la patente

if vehicleID[:2].isalpha() and vehicleID[2:5].isdigit() and vehicleID[5:].isalpha():
    vehicleIDCountry = "Argentina"
    ticketPrice = 300.0
elif vehicleID[:3].isalpha() and vehicleID[3].isdigit() and vehicleID[4].isalpha() and vehicleID[5:].isdigit():
    vehicleIDCountry = "Brasil"
    ticketPrice = 400.0
elif vehicleID[:2].isalpha() and vehicleID[2:].isdigit():
    vehicleIDCountry = "Bolivia"
    ticketPrice = 200.0
elif vehicleID[:4].isalpha() and vehicleID[4:].isdigit():
    vehicleIDCountry = "Paraguay"
    ticketPrice = 300.0
elif vehicleID[:3].isalpha() and vehicleID[3:].isdigit():
    vehicleIDCountry = "Uruguay"
    ticketPrice = 300.0
else:
    ticketPrice = 300.0
    vehicleIDCountry = "Otro"

# validacion y descuento aplicado
if vehicleType == 0:
    ticketPrice -= ticketPrice * 0.5
elif vehicleType == 2:
    ticketPrice += ticketPrice * 0.6

if typeOfPayment == 1:
    ticketPrice -= ticketPrice * 0.1

print("El valor del peaje es de: $", ticketPrice)
if distanceBetweenCabines == 0:
    print("con un promedio de $", round(ticketPrice / distanceBetweenCabines, 2), "por km")
