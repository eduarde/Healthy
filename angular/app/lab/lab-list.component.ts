import { Component, OnInit } from '@angular/core';

import { ILab } from './lab';
import { LabService } from './lab.service';

@Component({
    moduleId: module.id,
    templateUrl: 'lab-list.component.html'
})
export class LabListComponent implements OnInit {

    pageTitle: string = "Labs";
    listRefNumberFilter: string;
    listDateFilter: Date;    
    datepickerOpts = {
        autoclose: true,
        todayBtn: 'linked',
        todayHighlight: true,
        assumeNearbyYear: true,
        format: 'yyyy-mm-dd',
        icon: 'fa fa-calendar'
    }

    errorMessage: string;
    labs: ILab[];

    constructor(private _labService: LabService) { }

    ngOnInit(): void {
        this._labService.getLabs()
            .subscribe(labs => this.labs = labs,
            error => this.errorMessage = <any>error);
    }

    deleteFilters(): void {
        this.listDateFilter = null;
        this.listRefNumberFilter = "";
    }

}