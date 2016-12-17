import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ILab } from './lab'

@Component({
    moduleId: module.id,
    templateUrl: 'lab-detail.component.html'

})
export class LabDetailComponent implements OnInit {

    lab: ILab;
    idLab: number;
    pageTitle: string = "Lab Results";

    constructor(private _route: ActivatedRoute) {

    }

    ngOnInit(): void {
        let id = +this._route.snapshot.params['id'];
        this.idLab = id;
        this.pageTitle += `: ${id}`;

    }
}