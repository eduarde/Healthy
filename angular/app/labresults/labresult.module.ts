import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { LabResultService } from '../labresults/labresults.service';
import { LabResultsListComponent } from '../labresults/labresults-list.component';
import { LabResultAbnormalFilter } from './filters/labresult-abnormal.filter.pipe';
import { LabResultMarkerNameFilter } from './filters/labresult-markername.filter.pipe';


@NgModule({
    imports: [

        CommonModule,
        FormsModule
    ],
    declarations: [
        LabResultsListComponent,
        LabResultMarkerNameFilter,
        LabResultAbnormalFilter
    ],

    providers: [
        LabResultService
    ],

    exports: [
        LabResultsListComponent
    ]

})
export class LabResultModule {

}