import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NKDatetimeModule } from 'ng2-datetime/ng2-datetime';


import { LabListComponent } from './lab-list.component';
import { LabService } from './lab.service';

import { LabRefNumberFilter } from './lab-ref_number.filter.pipe';
import { LabDateFilter } from './lab-date.filter.pipe';



@NgModule({
    declarations: [
        LabListComponent,
        LabRefNumberFilter,
        LabDateFilter
    ],

    imports: [
        NKDatetimeModule,
        RouterModule.forChild([
            { path: 'labs', component: LabListComponent }
        ]),
        CommonModule,
        FormsModule
    ],

    providers: [
        LabService,
        LabRefNumberFilter,
        LabDateFilter
    ]
})
export class LabModule {

}