from CuentaBancaria import Cuenta_bancaria

class Usuario:

    def __init__(self, nombre, deposito, retiro, interes, balance):
        self.nombre = nombre
        self.cuenta = Cuenta_bancaria(0, 0, 0, 0)

#Depósitos
    def depositos(self, monto_dep):
        self.cuenta.hacer_deposito += monto_dep

#Retiros
    def retiros(self, monto_retiros):
        self.cuenta.hacer_retiro += monto_retiros

#Balance
    def balance(self):
        self.cuenta.balance = self.cuenta.hacer_deposito - self.cuenta.hacer_retiro
        print(self.cuenta.balance)