import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CampesinoDetailComponent } from './campesino-detail/campesino-detail.component';
import { CampesinoMatchesService } from './campesino-matches.service';
import { GoogleChartsModule } from 'angular-google-charts';


@NgModule({
  declarations: [CampesinoDetailComponent],
  imports: [
    CommonModule,
    GoogleChartsModule
  ],
  providers: [CampesinoMatchesService]
})
export class CampesinoModule {}
