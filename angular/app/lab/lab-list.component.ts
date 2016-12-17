import { Component, OnInit } from '@angular/core';

import { ILab } from './lab';
import { LabService } from './lab.service';

@Component({
    moduleId: module.id,
    templateUrl: 'lab-list.component.html'
})
export class LabListComponent implements OnInit {

    listRefNumberFilter: string;
    errorMessage: string;
    labs: ILab[];

    constructor(private _labService: LabService) { }

    ngOnInit(): void {
        this._labService.getLabs()
            .subscribe(labs => this.labs = labs,
            error => this.errorMessage = <any>error);
    }

}