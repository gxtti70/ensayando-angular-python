from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permite peticiones desde Angular

@app.route('/api/datos')
def get_datos():
    # Ejemplo: crear un DataFrame y devolverlo como JSON
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'Carlos'],
        'edad': [23, 34, 29]
    })
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
