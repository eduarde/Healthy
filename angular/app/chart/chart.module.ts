import { NgModule, NO_ERRORS_SCHEMA  } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ChartListComponent } from './chart-list.component';
import {VaadinCharts, DataSeries} from '../../bower_components/vaadin-charts/directives/vaadin-charts';

@NgModule({
    declarations: [
        ChartListComponent,
        VaadinCharts,
        DataSeries,
       
    ],
    imports: [
        RouterModule.forChild([
            { path: 'charts', component: ChartListComponent }
        ]),
        CommonModule
    ],
     schemas: [NO_ERRORS_SCHEMA]

})
export class ChartModule {

}