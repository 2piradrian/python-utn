# lee el archivo de patentes
def readPlateList():
    return open("peaje100.txt", "rt")


# lee patentes linea por linea
def readPlate(plateList):
    isFirstLine = True

    while True:
        line = plateList.readline()
        # < ---- Checking lines ---- > #
        if isFirstLine:
            isFirstLine = False
            continue

        if line == "":
            break

        if line[:1] == " ":
            line = line[1:]
        # < ----!- --- -- --- -!---- > #

        print(line)
        

# detecta el pais de origen
def detectCountry(plate):
    if (len(plate) < 6 or len(plate) > 7):
        return "Error"
    

def main():
    plateList = readPlateList()
    
    readPlate(plateList)

main()



