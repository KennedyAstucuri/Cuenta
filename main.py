from logica.Cuenta import

if __name__ == '__main__':
    saldoInicial = float(input("Ingrese el saldo inicial: "))
    cuenta = Cuenta(saldoInicial)
    cuenta.interes()
    cuenta.imprimirSaldo()