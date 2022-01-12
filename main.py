import sqlite3

from DAOsAndDTOs import Hat, Supplier, Order
from repository import repo





def config(configFile):

    with open(configFile) as file:
        lines = file.readlines()
    firstLine=lines[0].split(',')
    lines=lines[1:]
    hatsSize=int(firstLine[0])
    suplliersSize=int(firstLine[1])
    for i in range(hatsSize):
        lines[i]=lines[i].rstrip("\n")
        currLine=lines[i].split(',')
        repo.hats.insert(Hat(*currLine))
    for i in range(hatsSize,hatsSize+suplliersSize):
        lines[i] = lines[i].rstrip("\n")
        currLine = lines[i].split(',')
        repo.suppliers.insert(Supplier(*currLine))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def executeOrders(ordersFile):
    global idCounter
    outputList=[]
    hatsToSuppliers=repo.getHatIdWithSupllierName()
    with open(ordersFile) as file:
        lines = file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        currLine = line.split(',')
        topping=currLine[1]
        orderdHat=(repo.hats.findID(topping))
        repo.hats.updateQuntity(orderdHat)

        if(int(orderdHat.quantity)==1):
            repo.hats.delete(orderdHat.id)
        repo.orders.insert(Order( idCounter,currLine[0],orderdHat.id))
        idCounter=int(idCounter)+1
        for Object in hatsToSuppliers:
            if(Object.hatId==orderdHat.id):
                outputList.append(str(topping+","+Object.supplierName+","+currLine[0]))
                break
    with open("output.txt", "w") as file:
        for element in outputList:
            file.write(element + "\n")#todo delete last \n

if __name__ == '__main__':
    idCounter = 1
    repo.create_tables()

    config("config.txt")

    executeOrders("orders.txt")
