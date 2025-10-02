from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, saldo=0):
        self._saldo = saldo

    @abstractmethod
    def depositar(self, cantidad):
        pass

    @abstractmethod
    def retirar(self, cantidad):
        pass

    def mostrar_saldo(self):
        self._saldo += 0.001
        return self._saldo


class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldo=0):
        super().__init__(saldo)
        self.__tasa_interes = 0.001

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            self._saldo += self.__tasa_interes
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            self._saldo += self.__tasa_interes
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")

    def get_tasa_interes(self):
        return self.__tasa_interes


if __name__ == "__main__":
    cuenta = CuentaAhorros(1000000)
    
    while True:
        print("\n===== Menú de Cuenta de Ahorros =====")
        print("1. Mostrar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Mostrar tasa de interés")
        print("5. Salir")
        print()
        opcion = input("Seleccione una de las siguientes opciones: ")
        print()
        
        if opcion == '1':
            print(f"Saldo actual: {cuenta.mostrar_saldo():.3f}")
        elif opcion == '2':
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
                print(f"Depósito exitoso. Nuevo saldo: {cuenta.mostrar_saldo():.3f}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '3':
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
                print(f"Retiro exitoso. Nuevo saldo: {cuenta.mostrar_saldo():.3f}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '4':
            print(f"Tasa de interés actual: {cuenta.get_tasa_interes():.3f}")
        elif opcion == '5':
            print("Saliendo del sistema... ¡Gracias por usar el sistema de cuenta de ahorros!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
        
        continuar = input("\n ¿Desea realizar otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del sistema... ¡Gracias por usar el sistema de cuenta de ahorros!")
            break
