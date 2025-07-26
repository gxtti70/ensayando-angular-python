// app.component.ts
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Angular + Python';
  loading = false;
  error: string | null = null;
  datos: any = null;

  constructor(private http: HttpClient) {}

  cargarDatos() {
    this.loading = true;
    this.error = null;
    this.datos = null;
    this.http.get('http://localhost:5000/api/datos')
      .subscribe({
        next: (data) => {
          this.datos = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = 'Error al cargar datos';
          this.loading = false;
        }
      });
  }
}
