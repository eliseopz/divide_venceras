#Eliseo Josías Paz Ocampo, v1.0, 2/11/2022

class User:
    def __init__(self,cN,pin):
        self.CardNumber = cN
        self.Pin = pin
        self.Balance = 0

    def __str__(self):
        return f"""Card Number: {self.CardNumber}
Balance: {self.Balance}
"""