import { Component } from '@angular/core';
import { VaadinCharts, DataSeries } from '../../bower_components/vaadin-charts/directives/vaadin-charts';


@Component({
    moduleId: module.id,
    templateUrl: 'chart-list.component.html'

})
export class ChartListComponent {
    pageTitle: string = 'Trends';
    chartTitle: string = 'Leucocite';

    max_t = [35, 35, 35, 35, 36, 36, 37,37,37];
    value = [30, 35, 43, 68, 40, 34, 40, 39, 36];
    min_t = [ 29, 29, 29, 29, 30, 30, 31, 31, 31 ];



}