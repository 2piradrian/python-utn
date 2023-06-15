# lee el archivo de patentes
def readPlateList():
    return open("peajes.txt", "rt")

# verifica el tipo de vehiculo y el tipo de pago para obtener el descuento
def checkDiscount(vehicleType, typeOfPayment, ticketPrice):
    basic = ticketPrice

    if vehicleType == 0:
        basic -= basic * 0.5
    elif vehicleType == 2:
        basic += basic * 0.6

    if typeOfPayment == 2:
        basic -= basic * 0.1

    return basic

def checkTicketPrice(country):
    ticketPrice = 300.0
    if country == 2:
        ticketPrice = 400.0
    elif country == 1:
        ticketPrice = 200.0

    return ticketPrice


# verifica el pais de origen de la patente
def checkPlate(vehicleID):

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

    elif vehicleID[:2].isalpha() and vehicleID[2:].isdigit():
        vehicleIDCountry = "Bolivia"

    else:
        vehicleIDCountry = "Otro"

    return vehicleIDCountry
    
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

def calculatePercent(totalPlates, other):
    return round((other * 100) / totalPlates, 2)



# lee patentes linea por linea
def readPlate(plateList):
    language = ""
    isFirstLine = True
    isFirstPlate = True
    firstPlate = ""
    firstPlateCounter = 0
    finalAmountList = 0
    higgestAmount = 0
    higgestAmountPlate = ""
    argToBrazilPlateCounter = 0
    argToBrazilDistanceCounter = 0

    arg, chi, par, uru, bra, bol, oth = 0, 0, 0, 0, 0, 0, 0

    while True:
        line = plateList.readline()
        # < ---- Verificando lineas ---- > #
        if isFirstLine:
            isFirstLine = False
            language = checkLanguage(line)
            continue

        if line == "":
            break        
        # < ----!- --- ------ --- -!---- > #

        plate, vehicleType, payment, country, distance = handleLine(line)
        vehicleIDCountry = checkPlate(plate)
        ticketPrice = checkTicketPrice(int(country))
        basic = checkDiscount(int(vehicleType), int(payment), int(ticketPrice))

        finalAmountList += basic

        if basic > higgestAmount:
            higgestAmount = basic
            higgestAmountPlate = plate

        if isFirstPlate:
            isFirstPlate = False
            firstPlate = plate

        if plate == firstPlate:
            firstPlateCounter += 1

        if vehicleIDCountry == "Argentina":
            arg += 1
        elif vehicleIDCountry == "Chile":
            chi += 1
        elif vehicleIDCountry == "Paraguay":
            par += 1
        elif vehicleIDCountry == "Uruguay":
            uru += 1
        elif vehicleIDCountry == "Brasil":
            bra += 1
        elif vehicleIDCountry == "Bolivia":
            bol += 1
        else:
            oth += 1

        if (vehicleIDCountry == "Argentina" and int(country) == 2):
            argToBrazilPlateCounter += 1
            argToBrazilDistanceCounter += int(distance)


    totalPlates = arg + chi + par + uru + bra + bol + oth

    otherPercent = calculatePercent(totalPlates, oth)

    argToBrazilAvarage = round(argToBrazilDistanceCounter / argToBrazilPlateCounter, 2)        

    print('(r1) - Idioma a usar en los informes:', language)
    print()
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro país:', cotr)
    print()
    print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)
    print()
    print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)
    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)
    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')

def main():
    plateList = readPlateList()
    readPlate(plateList)

main()



