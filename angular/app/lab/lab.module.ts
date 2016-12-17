import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NKDatetimeModule } from 'ng2-datetime/ng2-datetime';


import { LabListComponent } from './lab-list.component';
import { LabDetailComponent } from './lab-detaiil.component';
import { LabService } from './lab.service';

import { LabRefNumberFilter } from './lab-ref_number.filter.pipe';
import { LabDateFilter } from './lab-date.filter.pipe';

import { LabDetailGuard } from './lab-guard.service';



@NgModule({
    declarations: [
        LabListComponent,
        LabDetailComponent,
        LabRefNumberFilter,
        LabDateFilter
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
        LabDetailGuard
    ]
})
export class LabModule {

}