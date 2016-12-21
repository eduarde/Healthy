import { Component } from '@angular/core';
import { VaadinCharts, DataSeries } from '../../bower_components/vaadin-charts/directives/vaadin-charts';


@Component({
    moduleId: module.id,
    templateUrl: 'chart-list.component.html'

})
export class ChartListComponent {
    pageTitle: string = 'Trends';
    chartTitle: string = 'Leucocite';

    max_t = [35, 28, 50, 70, 93, 78];
    value = [30, 35, 43, 68, 80, 74];
    min_t = [ 29, 11, 40, 63, 65, 61 ];

}