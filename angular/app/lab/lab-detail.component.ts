import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { Subscription } from 'rxjs/Subscription';

import { ILab } from './lab';
import { LabService } from './lab.service';

@Component({
    moduleId: module.id,
    templateUrl: 'lab-detail.component.html'

})
export class LabDetailComponent implements OnInit, OnDestroy {

    pageTitle: string = "Lab Results";
    lab: ILab;
    errorMessage: string;
    idLab: number;

    private sub: Subscription;


    constructor(private _route: ActivatedRoute,
        private _router: Router,
        private _labService: LabService) {

    }

    ngOnInit(): void {
        this.sub = this._route.params.subscribe(
            params => {
                let id = +params['id'];
                this.idLab = id;
                this.getLab(id);
            });
    }

    ngOnDestroy(): void {
        this.sub.unsubscribe();
    }

    getLab(id: number) {
        this._labService.getLab(id).
            subscribe(lab => this.lab = lab, error => this.errorMessage = <any>error);
    }
}