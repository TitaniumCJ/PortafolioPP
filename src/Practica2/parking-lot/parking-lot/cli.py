from models.estacionamiento import Estacionamiento
from models.vehiculo import Auto, Moto
from models.tarifas import TarifaPorHora

def menu():
    politica = TarifaPorHora()
    sistema = Estacionamiento(politica)
    
    while True:
        print("1 registrar entrada")
        print("2 registrar salida")
        print("3 ver ocupacion")
        print("4 salir")
        op = input("opcion: ")
        
        if op == "1":
            p = input("placa: ")
            t = input("1 auto 2 moto: ")
            v = Auto(p) if t == "1" else Moto(p)
            res = sistema.registrar_entrada(v)
            if res: print(f"ticket {res.id_ticket}")
            else: print("sin lugar")
        elif op == "2":
            tid = int(input("id: "))
            h = float(input("horas: "))
            c = sistema.registrar_salida(tid, h)
            if c: print(f"pago {c}")
        elif op == "3":
            for e in sistema.espacios:
                est = "lleno" if e.ocupado else "libre"
                print(f"{e.id_space} {est}")
        elif op == "4":
            break

if __name__ == "__main__":
    menu()