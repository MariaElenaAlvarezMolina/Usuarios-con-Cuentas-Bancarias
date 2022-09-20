class Cuenta_bancaria:

    #lista_cuentas = []

    def __init__(self, deposito, retiro, interes, balance):
        self.hacer_deposito = deposito
        self.hacer_retiro = retiro
        self.generar_interes = interes
        self.balance = balance
        #Cuenta_bancaria.lista_cuentas.append(self)
    
    """def depositos(self, monto_dep):
        self.hacer_deposito += monto_dep

    def retiros(self, monto_retiro):
        self.hacer_retiro += monto_retiro

    def intereses(self, monto_interes):
        self.balance = self.hacer_deposito - self.hacer_retiro
        self.generar_interes = self.balance * monto_interes

    def balance_cuenta(self):
        self.balance = self.balance - self.generar_interes
        print(self.balance)
        if Cuenta_bancaria.fondos_insuficientes(self.balance):
            print("Fondos insuficientes")

    @staticmethod
    def fondos_insuficientes(balance):
        if balance < 0:
            return True
        else:
            return False

    @classmethod
    def imprime_lista(cls):
        print("Total de cuentas:",len(cls.lista_cuentas))
        for cuentas in cls.lista_cuentas:
            print(cuentas.nombre)"""