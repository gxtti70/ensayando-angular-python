from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # Permite peticiones desde Angular

# Datos simulados para el inventario
inventario = {
    'categorias': [
        {'id': 1, 'nombre': 'Electrónicos', 'descripcion': 'Productos electrónicos y tecnología'},
        {'id': 2, 'nombre': 'Ropa', 'descripcion': 'Vestimenta y accesorios'},
        {'id': 3, 'nombre': 'Hogar', 'descripcion': 'Artículos para el hogar'},
        {'id': 4, 'nombre': 'Deportes', 'descripcion': 'Equipamiento deportivo'},
        {'id': 5, 'nombre': 'Libros', 'descripcion': 'Libros y material educativo'}
    ],
    'productos': [
        {'id': 1, 'nombre': 'Laptop HP', 'categoria_id': 1, 'precio': 899.99, 'stock': 15, 'stock_minimo': 5, 'descripcion': 'Laptop HP Pavilion 15.6"'},
        {'id': 2, 'nombre': 'Mouse Inalámbrico', 'categoria_id': 1, 'precio': 25.50, 'stock': 50, 'stock_minimo': 10, 'descripcion': 'Mouse inalámbrico ergonómico'},
        {'id': 3, 'nombre': 'Camiseta Básica', 'categoria_id': 2, 'precio': 19.99, 'stock': 100, 'stock_minimo': 20, 'descripcion': 'Camiseta de algodón 100%'},
        {'id': 4, 'nombre': 'Balón de Fútbol', 'categoria_id': 4, 'precio': 45.00, 'stock': 30, 'stock_minimo': 8, 'descripcion': 'Balón oficial tamaño 5'},
        {'id': 5, 'nombre': 'Libro Python', 'categoria_id': 5, 'precio': 35.00, 'stock': 25, 'stock_minimo': 5, 'descripcion': 'Aprende Python desde cero'},
        {'id': 6, 'nombre': 'Lámpara de Mesa', 'categoria_id': 3, 'precio': 65.00, 'stock': 12, 'stock_minimo': 3, 'descripcion': 'Lámpara LED ajustable'},
        {'id': 7, 'nombre': 'Teclado Mecánico', 'categoria_id': 1, 'precio': 120.00, 'stock': 8, 'stock_minimo': 5, 'descripcion': 'Teclado mecánico RGB'},
        {'id': 8, 'nombre': 'Pantalón Jeans', 'categoria_id': 2, 'precio': 49.99, 'stock': 75, 'stock_minimo': 15, 'descripcion': 'Jeans clásicos azul'},
        {'id': 9, 'nombre': 'Raqueta de Tenis', 'categoria_id': 4, 'precio': 85.00, 'stock': 20, 'stock_minimo': 5, 'descripcion': 'Raqueta profesional'},
        {'id': 10, 'nombre': 'Novela Bestseller', 'categoria_id': 5, 'precio': 22.50, 'stock': 40, 'stock_minimo': 10, 'descripcion': 'Novela más vendida del año'}
    ],
    'movimientos': []
}

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

# API para el sistema de inventario
@app.route('/api/inventario/categorias')
def get_categorias():
    return jsonify(inventario['categorias'])

@app.route('/api/inventario/productos')
def get_productos():
    # Agregar información de categoría a cada producto
    productos_con_categoria = []
    for producto in inventario['productos']:
        categoria = next((cat for cat in inventario['categorias'] if cat['id'] == producto['categoria_id']), None)
        producto_completo = producto.copy()
        producto_completo['categoria_nombre'] = categoria['nombre'] if categoria else 'Sin categoría'
        productos_con_categoria.append(producto_completo)
    return jsonify(productos_con_categoria)

@app.route('/api/inventario/productos', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    
    # Validar datos requeridos
    if not all(key in data for key in ['nombre', 'categoria_id', 'precio', 'stock', 'stock_minimo']):
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    # Generar nuevo ID
    nuevo_id = max([p['id'] for p in inventario['productos']]) + 1 if inventario['productos'] else 1
    
    nuevo_producto = {
        'id': nuevo_id,
        'nombre': data['nombre'],
        'categoria_id': data['categoria_id'],
        'precio': float(data['precio']),
        'stock': int(data['stock']),
        'stock_minimo': int(data['stock_minimo']),
        'descripcion': data.get('descripcion', '')
    }
    
    inventario['productos'].append(nuevo_producto)
    
    # Registrar movimiento
    registrar_movimiento(nuevo_id, 'Entrada inicial', int(data['stock']), 'Entrada inicial de stock')
    
    return jsonify({'mensaje': 'Producto agregado exitosamente', 'producto': nuevo_producto})

@app.route('/api/inventario/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    data = request.get_json()
    producto = next((p for p in inventario['productos'] if p['id'] == producto_id), None)
    
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    # Actualizar campos
    if 'nombre' in data:
        producto['nombre'] = data['nombre']
    if 'categoria_id' in data:
        producto['categoria_id'] = data['categoria_id']
    if 'precio' in data:
        producto['precio'] = float(data['precio'])
    if 'stock_minimo' in data:
        producto['stock_minimo'] = int(data['stock_minimo'])
    if 'descripcion' in data:
        producto['descripcion'] = data['descripcion']
    
    return jsonify({'mensaje': 'Producto actualizado exitosamente', 'producto': producto})

@app.route('/api/inventario/productos/<int:producto_id>/stock', methods=['POST'])
def ajustar_stock(producto_id):
    data = request.get_json()
    producto = next((p for p in inventario['productos'] if p['id'] == producto_id), None)
    
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    cantidad = int(data['cantidad'])
    tipo_movimiento = data['tipo']  # 'entrada' o 'salida'
    motivo = data.get('motivo', '')
    
    if tipo_movimiento == 'salida' and producto['stock'] < cantidad:
        return jsonify({'error': 'Stock insuficiente'}), 400
    
    # Ajustar stock
    if tipo_movimiento == 'entrada':
        producto['stock'] += cantidad
    else:
        producto['stock'] -= cantidad
    
    # Registrar movimiento
    registrar_movimiento(producto_id, tipo_movimiento, cantidad, motivo)
    
    return jsonify({
        'mensaje': f'Stock ajustado exitosamente',
        'nuevo_stock': producto['stock']
    })

@app.route('/api/inventario/movimientos')
def get_movimientos():
    movimientos_con_producto = []
    for movimiento in inventario['movimientos']:
        producto = next((p for p in inventario['productos'] if p['id'] == movimiento['producto_id']), None)
        movimiento_completo = movimiento.copy()
        movimiento_completo['producto_nombre'] = producto['nombre'] if producto else 'Producto eliminado'
        movimientos_con_producto.append(movimiento_completo)
    return jsonify(movimientos_con_producto)

@app.route('/api/inventario/alertas')
def get_alertas():
    alertas = []
    for producto in inventario['productos']:
        if producto['stock'] <= producto['stock_minimo']:
            alertas.append({
                'producto_id': producto['id'],
                'producto_nombre': producto['nombre'],
                'stock_actual': producto['stock'],
                'stock_minimo': producto['stock_minimo'],
                'tipo': 'stock_bajo'
            })
    return jsonify(alertas)

@app.route('/api/inventario/estadisticas')
def get_estadisticas():
    total_productos = len(inventario['productos'])
    total_categorias = len(inventario['categorias'])
    valor_total = sum(p['precio'] * p['stock'] for p in inventario['productos'])
    productos_bajo_stock = len([p for p in inventario['productos'] if p['stock'] <= p['stock_minimo']])
    
    # Estadísticas por categoría
    stats_por_categoria = {}
    for categoria in inventario['categorias']:
        productos_categoria = [p for p in inventario['productos'] if p['categoria_id'] == categoria['id']]
        stats_por_categoria[categoria['nombre']] = {
            'cantidad_productos': len(productos_categoria),
            'valor_total': sum(p['precio'] * p['stock'] for p in productos_categoria),
            'stock_total': sum(p['stock'] for p in productos_categoria)
        }
    
    return jsonify({
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'valor_total_inventario': round(valor_total, 2),
        'productos_bajo_stock': productos_bajo_stock,
        'stats_por_categoria': stats_por_categoria
    })

def registrar_movimiento(producto_id, tipo, cantidad, motivo):
    movimiento = {
        'id': len(inventario['movimientos']) + 1,
        'producto_id': producto_id,
        'tipo': tipo,
        'cantidad': cantidad,
        'motivo': motivo,
        'fecha': datetime.now().isoformat()
    }
    inventario['movimientos'].append(movimiento)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
