import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NKDatetimeModule } from 'ng2-datetime/ng2-datetime';


import { LabListComponent } from './lab-list.component';
import { LabDetailComponent } from './lab-detail.component';
import { LabService } from './lab.service';

import { LabRefNumberFilter } from './filters/lab-ref_number.filter.pipe';
import { LabDateFilter } from './filters/lab-date.filter.pipe';
import { LabAbnormalFilter } from './filters/lab-abnormal.filter.pipe';

import { LabDetailGuard } from './lab-guard.service';
import { LabResultsListComponent } from '../labresults/labresults-list.component';
import { LabResultService } from '../labresults/labresults.service';

@NgModule({
    declarations: [
        LabListComponent,
        LabDetailComponent,
        LabResultsListComponent,
        LabRefNumberFilter,
        LabDateFilter,
        LabAbnormalFilter,
    ],

    imports: [
        NKDatetimeModule,
        RouterModule.forChild([
            { path: 'labs', component: LabListComponent },
            {
                path: 'lab/:id',
                canActivate: [LabDetailGuard],
                component: LabDetailComponent
            }
        ]),
        CommonModule,
        FormsModule
    ],

    providers: [
        LabService,
        LabResultService,
        LabDetailGuard
    ]
})
export class LabModule {

}