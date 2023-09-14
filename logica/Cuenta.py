class Cuenta():
    def __init__(self, saldo):
        self.saldo = saldo
    def interes(self):
        if self.saldo < 10000 :
            self.saldo = self.saldo * (1 + 0.03)
        else:
           self.saldo = self.saldo * (1 + 0.04)

    def imprimirSaldo(self):
        print(f"Nuevo saldo: {}")
        print(f"{primerSumando} + {segundoSumando} = {suma.CalcularSuma()}")