import { Component } from '@angular/core';

@Component({
  selector: 'app-emprendimiento',
  templateUrl: './emprendimiento.component.html',
  styleUrls: ['./emprendimiento.component.scss']
})
export class EmprendimientoComponent {
  preguntas = [
    { texto: '¿Tienes experiencia previa en emprendimientos?', tipo: 'select', opciones: ['Sí', 'No'], valor: '' },
    { texto: '¿Cuentas con capital inicial?', tipo: 'select', opciones: ['Sí', 'No'], valor: '' },
    { texto: '¿Has realizado un estudio de mercado?', tipo: 'select', opciones: ['Sí', 'No'], valor: '' },
    { texto: '¿Tienes un equipo de trabajo?', tipo: 'select', opciones: ['Sí', 'No'], valor: '' },
    { texto: '¿Tu producto/servicio es innovador?', tipo: 'select', opciones: ['Sí', 'No'], valor: '' }
  ];
  resultado: number|null = null;
  detalles: any = null;

  calcularExito() {
    let puntaje = 0;
    let razones = [];
    this.preguntas.forEach((p, i) => {
      if (p.valor === 'Sí') {
        puntaje += 20;
      } else {
        razones.push(p.texto);
      }
    });
    this.resultado = puntaje;
    this.detalles = {
      razones,
      puntaje
    };
  }

  reiniciar() {
    this.preguntas.forEach(p => p.valor = '');
    this.resultado = null;
    this.detalles = null;
  }
} 