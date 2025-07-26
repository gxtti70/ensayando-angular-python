from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permite peticiones desde Angular

@app.route('/api/datos')
def get_datos():
    # Simula agregar un registro nuevo automáticamente en cada petición
    if not hasattr(get_datos, 'datos'):
        get_datos.datos = [
            {'nombre': 'Ana', 'edad': 23},
            {'nombre': 'Luis', 'edad': 34},
            {'nombre': 'Carlos', 'edad': 29}
        ]
    nuevo_nombre = f'Nuevo{len(get_datos.datos)+1}'
    nueva_edad = 20 + len(get_datos.datos)
    get_datos.datos.append({'nombre': nuevo_nombre, 'edad': nueva_edad})
    df = pd.DataFrame(get_datos.datos)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
