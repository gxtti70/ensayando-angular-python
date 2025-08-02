# 🏪 Sistema de Gestión de Inventario - Angular + Python

Un sistema completo de gestión de inventario desarrollado con Angular en el frontend y Python Flask en el backend.

## 🚀 Características

### 📦 Gestión de Productos
- **Agregar productos** con nombre, categoría, precio, stock inicial y stock mínimo
- **Filtrar productos** por categoría y estado de stock
- **Visualizar** información completa de cada producto
- **Calcular** valor total del inventario por producto

### 🏷️ Categorías
- **Categorías predefinidas**: Electrónicos, Ropa, Hogar, Deportes, Libros
- **Organización** automática de productos por categoría
- **Estadísticas** por categoría

### 📊 Gestión de Stock
- **Entradas y salidas** de stock con motivo
- **Historial completo** de movimientos
- **Alertas automáticas** cuando el stock está bajo
- **Validación** de stock disponible para salidas

### ⚠️ Sistema de Alertas
- **Alertas visuales** para productos con stock bajo
- **Indicadores de estado** (Bajo, Medio, Normal)
- **Notificaciones** en tiempo real

### 📈 Estadísticas y Reportes
- **Dashboard** con métricas principales
- **Valor total** del inventario
- **Estadísticas** por categoría
- **Productos bajo stock**

## 🛠️ Tecnologías Utilizadas

### Frontend (Angular)
- **Angular** - Framework principal
- **TypeScript** - Lenguaje de programación
- **SCSS** - Estilos avanzados
- **HTTP Client** - Comunicación con API

### Backend (Python)
- **Flask** - Framework web
- **Flask-CORS** - Manejo de CORS
- **Pandas** - Manipulación de datos
- **JSON** - Intercambio de datos

## 📁 Estructura del Proyecto

```
ensayando-angular-python-master/
├── frontend/
│   ├── app.component.html          # Componente principal
│   ├── app.component.ts
│   ├── app.component.scss
│   ├── inventario.component.html   # 🆕 Sistema de inventario
│   ├── inventario.component.ts
│   ├── inventario.component.scss
│   ├── emprendimiento.component.html
│   ├── emprendimiento.component.ts
│   ├── futbol.html
│   └── index.html                  # Página de inicio
├── python/
│   └── backend.py                  # 🆕 API completa de inventario
└── README.md                       # 🆕 Documentación
```

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd ensayando-angular-python-master
```

### 2. Instalar dependencias del frontend
```bash
cd frontend
npm install
```

### 3. Instalar dependencias del backend
```bash
cd ../python
pip install flask flask-cors pandas
```

### 4. Ejecutar el backend
```bash
python backend.py
```
El servidor estará disponible en `http://localhost:5000`

### 5. Ejecutar el frontend
```bash
cd ../frontend
ng serve
```
La aplicación estará disponible en `http://localhost:4200`

## 📋 API Endpoints

### Productos
- `GET /api/inventario/productos` - Obtener todos los productos
- `POST /api/inventario/productos` - Agregar nuevo producto
- `PUT /api/inventario/productos/{id}` - Actualizar producto
- `POST /api/inventario/productos/{id}/stock` - Ajustar stock

### Categorías
- `GET /api/inventario/categorias` - Obtener todas las categorías

### Movimientos
- `GET /api/inventario/movimientos` - Obtener historial de movimientos

### Alertas
- `GET /api/inventario/alertas` - Obtener alertas de stock bajo

### Estadísticas
- `GET /api/inventario/estadisticas` - Obtener estadísticas del inventario

## 🎨 Características de Diseño

### Interfaz Moderna
- **Diseño responsive** que se adapta a cualquier dispositivo
- **Gradientes y sombras** para un aspecto profesional
- **Animaciones suaves** para mejor experiencia de usuario
- **Iconos emoji** para mejor identificación visual

### Navegación Intuitiva
- **Pestañas organizadas** por funcionalidad
- **Filtros avanzados** para búsqueda rápida
- **Formularios validados** con feedback visual
- **Tablas interactivas** con hover effects

### Estados Visuales
- **Colores semánticos**: Verde (normal), Naranja (medio), Rojo (bajo)
- **Indicadores de estado** con iconos
- **Alertas destacadas** para atención inmediata
- **Loading states** para mejor UX

## 📊 Datos de Ejemplo

El sistema incluye datos de ejemplo para demostrar todas las funcionalidades:

### Productos Predefinidos
- Laptop HP (Electrónicos)
- Mouse Inalámbrico (Electrónicos)
- Camiseta Básica (Ropa)
- Balón de Fútbol (Deportes)
- Libro Python (Libros)
- Y más...

### Categorías
- Electrónicos
- Ropa
- Hogar
- Deportes
- Libros

## 🔧 Funcionalidades Avanzadas

### Gestión de Stock
- **Control de inventario** en tiempo real
- **Trazabilidad** completa de movimientos
- **Prevención** de stock negativo
- **Alertas automáticas** de reabastecimiento

### Reportes
- **Valor total** del inventario
- **Estadísticas** por categoría
- **Productos más/menos** vendidos
- **Tendencias** de stock

### Seguridad
- **Validación** de datos en frontend y backend
- **Manejo de errores** robusto
- **CORS** configurado correctamente
- **Sanitización** de inputs

## 🚀 Próximas Mejoras

- [ ] **Base de datos persistente** (SQLite/PostgreSQL)
- [ ] **Autenticación de usuarios**
- [ ] **Gráficos interactivos** con Chart.js
- [ ] **Exportación a Excel/PDF**
- [ ] **Notificaciones push**
- [ ] **API REST completa**
- [ ] **Tests unitarios**
- [ ] **Docker containerization**

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Desarrollado como parte del proyecto de integración Angular + Python.

---

**¡Disfruta gestionando tu inventario de manera eficiente! 🎉** 