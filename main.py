#Eliseo Josías Paz Ocampo, v1.0, 2/11/2022
import funciones

cN = "123"
pin = "1234"
funciones.addUser(cN, pin)
funciones.printUsers()


def main():
    numero = input("Numero de tarjeta: ")
    pin = input("Pin: ")
    if (funciones.getUser(numero, pin) != False):
        op = 0
        while (op != 4):
            funciones.menu()
            op = int(input("Elija su opción: "))
            if (op == 1):
                funciones.deposit(numero, pin)
            elif (op == 2):
                funciones.remove(numero, pin)
            elif (op == 3):
                funciones.showBalance(numero, pin)
            elif (op == 4):
                print("Bye")
                break
    else:
        print("Credenciales incorrectas")
        main()


main()