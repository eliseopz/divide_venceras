#Eliseo Josías Paz Ocampo, v1.0, 2/11/2022

from estructuras import User

AcountList = []


def addUser(cN, pin):
    newUser = User(cN, pin)
    AcountList.append(newUser)


def getUser(cN, pin):
    user = User(cN, pin)
    for i in AcountList:
        if (user.CardNumber == i.CardNumber and user.Pin == i.Pin):
            return i
        else:
            return False


def deposit(cN, pin):
    print("-" * 50)
    amount = int(input("Ingrese la cantidad del depósito: "))
    usuario = getUser(cN, pin)
    if amount % 100 == 0:
        usuario.Balance += amount
        print("Cantidad depositada satisfactoriamente")
    else:
        print("El valor debe de ser multiplo de 100")


def showBalance(cN, pin):
    print("-"*50)
    user = getUser(cN, pin)
    print(user)


def menu():
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver saldo")
    print("4. Salir")


def remove(cN, pin):
    print("-" * 50)
    amount = int(input("Ingrese la cantidad a retirar: "))
    print("-" * 50)
    usuario = getUser(cN, pin)
    if amount % 100 == 0:
        if (usuario.Balance >= amount):
            usuario.Balance -= amount
        else:
            print("No posee el saldo sufieciente")
    else:
        print("El valor debe de ser multiplo de 100")
    return 0


def printUsers():
    for i in AcountList:
        print(i)