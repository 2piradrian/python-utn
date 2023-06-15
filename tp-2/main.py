# lee el archivo de patentes
def readPlateList():
    return open("peajes.txt", "rt")

# verifica el tipo de vehiculo y el tipo de pago para obtener el descuento
def checkDiscount(vehicleType, typeOfPayment, ticketPrice):
    base = ticketPrice
    basic = ticketPrice

    if vehicleType == 0:
        basic -= basic * 0.5
    elif vehicleType == 2:
        basic += basic * 0.6

    if typeOfPayment == 1:
        basic -= basic * 0.1

    print("El valor base del peaje es de: $", round(base, 2), "y el valor básico es de: $", round(basic, 2))

# verifica el pais de origen de la patente
def checkPlate(vehicleID):
    ticketPrice = 300
    if vehicleID[:2].isalpha() and vehicleID[2:5].isdigit() and vehicleID[5:].isalpha():
        vehicleIDCountry = "Argentina"

    elif vehicleID[1:5].isalpha() and vehicleID[5:].isdigit() and vehicleID[:1] == " ":
        vehicleIDCountry = "Chile"   

    elif vehicleID[:4].isalpha() and vehicleID[4:].isdigit():
        vehicleIDCountry = "Paraguay"

    elif vehicleID[:3].isalpha() and vehicleID[3:].isdigit():
        vehicleIDCountry = "Uruguay"  

    elif vehicleID[:3].isalpha() and vehicleID[3].isdigit() and vehicleID[4].isalpha() and vehicleID[5:].isdigit():
        vehicleIDCountry = "Brasil"
        ticketPrice = 400.0

    elif vehicleID[:2].isalpha() and vehicleID[2:].isdigit():
        vehicleIDCountry = "Bolivia"
        ticketPrice = 200.0  

    else:
        vehicleIDCountry = "Otro"

    return vehicleIDCountry, ticketPrice
    
# separa los datos de la linea
def handleLine(line):
    plate = line[:7]
    vehicleType = line[7:8]
    payment = line[8:9]
    country = line[9:10]
    distance = line[10:13]

    return plate, vehicleType, payment, country, distance

# verifica el idioma
def checkLanguage(line):
    if("PT" in line):
        print("Portugués")
    elif ("ES" in line):
        print ("Español")

# lee patentes linea por linea
def readPlate(plateList):
    isFirstLine = True

    while True:
        line = plateList.readline()
        # < ---- Verificando lineas ---- > #
        if isFirstLine:
            isFirstLine = False
            checkLanguage(line)
            continue

        if line == "":
            break        
        # < ----!- --- ------ --- -!---- > #
        plate, vehicleType, payment, country, distance = handleLine(line)

        checkDiscount(int(vehicleType), int(payment), int(distance))

def main():
    plateList = readPlateList()
    readPlate(plateList)

main()



