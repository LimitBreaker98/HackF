import { Component, OnInit } from '@angular/core';
import { CampesinoMatchesService } from '../campesino-matches.service';


@Component({
  selector: 'app-campesino-detail',
  templateUrl: './campesino-detail.component.html',
  styleUrls: ['./campesino-detail.component.css']
})
export class CampesinoDetailComponent{

  constructor(private service: CampesinoMatchesService) { 

  }

  // Variables para chart 1

  title1 = 'Porcentaje ganancia de productos de cultivo';
  type1='PieChart';
  data1 = [
    ['Aguacate Hass', 45.0],
    ['Ahuyama', 26.8],
    ['Ajo', 12.8],
    ['Apio', 8.5],
    ['Cebolla Cabezona Blanca', 6.9],
  ];
  columnNames1 = ['Participacion', 'Porcentaje'];
  options1 = {
  colors1: ['#e0440e', '#e6693e', '#ec8f6e', '#f3b49f',], is3D: true
  };
  width1 = 750;
  height1 = 600;

  // Variables para chart 2

  title2 = 'Costo y utilidad de productos en millones';
   type2 = 'ComboChart';
   data2 = [
      ["Aguacate", 3, 2, 2.5],
      ["Ahuyama",2, 3, 2.5],
      ["Ajo", 1, 5, 3],
      ["Apio", 3, 9, 6],
      ["Cebolla", 4, 2, 3]
   ];
   columnNames2 = ['Costo', 'Utilidad', 'Neto','Promedio'];
   options2 = {   
      hAxis: {
         title: 'Producto'
      },
      vAxis:{
         title: 'Dinero'
      },
      seriesType: 'bars',
      series: {2: {type: 'line'}}
   };
   width2 = 750;
   height2 = 600;
}

  // Variables para chart 3

