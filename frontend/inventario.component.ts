import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Producto {
  id: number;
  nombre: string;
  categoria_id: number;
  categoria_nombre: string;
  precio: number;
  stock: number;
  stock_minimo: number;
  descripcion: string;
}

interface Categoria {
  id: number;
  nombre: string;
  descripcion: string;
}

interface Movimiento {
  id: number;
  producto_id: number;
  producto_nombre: string;
  tipo: string;
  cantidad: number;
  motivo: string;
  fecha: string;
}

interface Alerta {
  producto_id: number;
  producto_nombre: string;
  stock_actual: number;
  stock_minimo: number;
  tipo: string;
}

interface Estadisticas {
  total_productos: number;
  total_categorias: number;
  valor_total_inventario: number;
  productos_bajo_stock: number;
  stats_por_categoria: any;
}

@Component({
  selector: 'app-inventario',
  templateUrl: './inventario.component.html',
  styleUrls: ['./inventario.component.scss']
})
export class InventarioComponent implements OnInit {
  productos: Producto[] = [];
  categorias: Categoria[] = [];
  movimientos: Movimiento[] = [];
  alertas: Alerta[] = [];
  estadisticas: Estadisticas | null = null;
  
  // Estados de la aplicación
  loading = false;
  error: string | null = null;
  vistaActual = 'productos'; // 'productos', 'movimientos', 'alertas', 'estadisticas'
  
  // Formulario para nuevo producto
  nuevoProducto = {
    nombre: '',
    categoria_id: 1,
    precio: 0,
    stock: 0,
    stock_minimo: 0,
    descripcion: ''
  };
  
  // Formulario para ajuste de stock
  ajusteStock = {
    producto_id: 0,
    cantidad: 0,
    tipo: 'entrada',
    motivo: ''
  };
  
  // Filtros
  filtroCategoria = 0;
  filtroStock = 'todos'; // 'todos', 'bajo', 'normal'
  
  constructor(private http: HttpClient) {}
  
  ngOnInit() {
    this.cargarDatos();
  }
  
  cargarDatos() {
    this.loading = true;
    this.error = null;
    
    // Cargar productos
    this.http.get<Producto[]>('http://localhost:5000/api/inventario/productos')
      .subscribe({
        next: (data) => {
          this.productos = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = 'Error al cargar productos';
          this.loading = false;
        }
      });
    
    // Cargar categorías
    this.http.get<Categoria[]>('http://localhost:5000/api/inventario/categorias')
      .subscribe({
        next: (data) => {
          this.categorias = data;
        },
        error: (err) => {
          console.error('Error al cargar categorías:', err);
        }
      });
  }
  
  cargarMovimientos() {
    this.http.get<Movimiento[]>('http://localhost:5000/api/inventario/movimientos')
      .subscribe({
        next: (data) => {
          this.movimientos = data;
        },
        error: (err) => {
          console.error('Error al cargar movimientos:', err);
        }
      });
  }
  
  cargarAlertas() {
    this.http.get<Alerta[]>('http://localhost:5000/api/inventario/alertas')
      .subscribe({
        next: (data) => {
          this.alertas = data;
        },
        error: (err) => {
          console.error('Error al cargar alertas:', err);
        }
      });
  }
  
  cargarEstadisticas() {
    this.http.get<Estadisticas>('http://localhost:5000/api/inventario/estadisticas')
      .subscribe({
        next: (data) => {
          this.estadisticas = data;
        },
        error: (err) => {
          console.error('Error al cargar estadísticas:', err);
        }
      });
  }
  
  cambiarVista(vista: string) {
    this.vistaActual = vista;
    
    switch (vista) {
      case 'movimientos':
        this.cargarMovimientos();
        break;
      case 'alertas':
        this.cargarAlertas();
        break;
      case 'estadisticas':
        this.cargarEstadisticas();
        break;
    }
  }
  
  agregarProducto() {
    if (!this.nuevoProducto.nombre || this.nuevoProducto.precio <= 0) {
      this.error = 'Por favor completa todos los campos requeridos';
      return;
    }
    
    this.loading = true;
    this.error = null;
    
    this.http.post<any>('http://localhost:5000/api/inventario/productos', this.nuevoProducto)
      .subscribe({
        next: (response) => {
          this.cargarDatos();
          this.limpiarFormularioProducto();
          this.loading = false;
        },
        error: (err) => {
          this.error = 'Error al agregar producto';
          this.loading = false;
        }
      });
  }
  
  ajustarStock() {
    if (!this.ajusteStock.producto_id || this.ajusteStock.cantidad <= 0) {
      this.error = 'Por favor completa todos los campos';
      return;
    }
    
    this.loading = true;
    this.error = null;
    
    this.http.post<any>(`http://localhost:5000/api/inventario/productos/${this.ajusteStock.producto_id}/stock`, this.ajusteStock)
      .subscribe({
        next: (response) => {
          this.cargarDatos();
          this.limpiarFormularioStock();
          this.loading = false;
        },
        error: (err) => {
          this.error = err.error?.error || 'Error al ajustar stock';
          this.loading = false;
        }
      });
  }
  
  limpiarFormularioProducto() {
    this.nuevoProducto = {
      nombre: '',
      categoria_id: 1,
      precio: 0,
      stock: 0,
      stock_minimo: 0,
      descripcion: ''
    };
  }
  
  limpiarFormularioStock() {
    this.ajusteStock = {
      producto_id: 0,
      cantidad: 0,
      tipo: 'entrada',
      motivo: ''
    };
  }
  
  getProductosFiltrados(): Producto[] {
    let productos = this.productos;
    
    // Filtro por categoría
    if (this.filtroCategoria > 0) {
      productos = productos.filter(p => p.categoria_id === this.filtroCategoria);
    }
    
    // Filtro por stock
    switch (this.filtroStock) {
      case 'bajo':
        productos = productos.filter(p => p.stock <= p.stock_minimo);
        break;
      case 'normal':
        productos = productos.filter(p => p.stock > p.stock_minimo);
        break;
    }
    
    return productos;
  }
  
  getValorTotal(producto: Producto): number {
    return producto.precio * producto.stock;
  }
  
  getEstadoStock(producto: Producto): string {
    if (producto.stock <= producto.stock_minimo) {
      return 'bajo';
    } else if (producto.stock <= producto.stock_minimo * 2) {
      return 'medio';
    } else {
      return 'normal';
    }
  }
  
  formatearFecha(fecha: string): string {
    return new Date(fecha).toLocaleString('es-ES');
  }
} 