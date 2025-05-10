from flask import Flask, jsonify

app = Flask(__name__)

# Datos simulados de 10 estudiantes y sus 3 notas
estudiantes = [
    {"id": 1, "nombre": "Juan", "notas": [8.5, 9.0, 7.5]},
    {"id": 2, "nombre": "Ana", "notas": [7.0, 8.0, 9.0]},
    {"id": 3, "nombre": "Carlos", "notas": [9.0, 6.5, 8.5]},
    {"id": 4, "nombre": "Marta", "notas": [8.0, 7.5, 9.0]},
    {"id": 5, "nombre": "Luis", "notas": [6.0, 7.0, 7.5]},
    {"id": 6, "nombre": "Elena", "notas": [9.5, 9.0, 8.0]},
    {"id": 7, "nombre": "Pedro", "notas": [7.0, 6.0, 7.5]},
    {"id": 8, "nombre": "Sofia", "notas": [8.5, 8.0, 9.0]},
    {"id": 9, "nombre": "Andres", "notas": [7.5, 7.0, 6.5]},
    {"id": 10, "nombre": "Lucia", "notas": [9.0, 8.5, 9.5]}
]

# Ruta principal: Obtener todos los estudiantes con sus notas
@app.route('/notas', methods=['GET'])
def obtener_notas():
    return jsonify(estudiantes)

# Ruta para obtener las notas de un estudiante específico por nombre
@app.route('/notas/<nombre>', methods=['GET'])
def obtener_notas_estudiante(nombre):
    estudiante = next((e for e in estudiantes if e["nombre"].lower() == nombre.lower()), None)
    if estudiante:
        return jsonify(estudiante)
    else:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

# Ruta para obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    nombres = [e["nombre"] for e in estudiantes]
    return jsonify(nombres)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
