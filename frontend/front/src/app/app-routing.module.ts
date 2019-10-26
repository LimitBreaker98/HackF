import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CampesinoDetailComponent } from './campesino/campesino-detail/campesino-detail.component';
import { CompradorDetailComponent } from './comprador/comprador-detail/comprador-detail.component';
import { FinancieroDetailComponent } from './financiero/financiero-detail/financiero-detail.component';


const routes: Routes = [
  {path: 'campesino', component: CampesinoDetailComponent},
  {path: 'comprador', component: CompradorDetailComponent},
  {path: 'financiero', component: FinancieroDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  CampesinoDetailComponent,
  CompradorDetailComponent,
  FinancieroDetailComponent
]
