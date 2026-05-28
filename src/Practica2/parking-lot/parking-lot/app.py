from flask import Flask, render_template, request, redirect
from models.estacionamiento import Estacionamiento
from models.tarifas import TarifaPorHora
from models.vehiculo import Auto, Moto

app = Flask(__name__)

# iniciamos el sistema en memoria como pide la practica
politica = TarifaPorHora()
sistema = Estacionamiento(politica)

@app.route('/')
def inicio():
    # enviamos datos al dashboard
    return render_template('dashboard.html', espacios=sistema.espacios, tickets=sistema.tickets_activos)

@app.route('/entrada', methods=['GET', 'POST'])
def entrada():
    if request.method == 'POST':
        placa = request.form['placa']
        tipo = request.form['type']
        vehiculo = Auto(placa) if tipo == 'AUTO' else Moto(placa)
        
        if sistema.registrar_entrada(vehiculo):
            print("vehiculo guardado") # sin tildes ni puntos
            return redirect('/')
        return "lleno", 409
    return render_template('entrada.html')

@app.route('/salida', methods=['GET', 'POST'])
def salida():
    if request.method == 'POST':
        id_t = int(request.form['ticket_id'])
        hrs = float(request.form['hours'])
        costo = sistema.registrar_salida(id_t, hrs)
        
        if costo is not None:
            return render_template('confirmacion.html', cost=costo)
        return "error", 404
    return render_template('salida.html')

if __name__ == "__main__":
    # revisando carga de modelos
    print("modelos cargados con exito")
    app.run(debug=True)
    