import { Component, OnInit, OnDestroy } from '@angular/core'
import { Subscription } from 'rxjs/Subscription';
import { ActivatedRoute, Router } from '@angular/router';

import { IResult } from './result';
import { LabResultService } from './labresults.service';

@Component({
    selector: 'lab-results',
    moduleId: module.id,
    templateUrl: 'labresults-list.component.html'
})
export class LabResultsListComponent implements OnInit, OnDestroy {

    results: IResult[];
    errorMessage: string;
    filterMarkerName: string;
    filterAbnormal: boolean;

    private sub: Subscription;

    constructor(private _labResultService: LabResultService,
        private _router: Router,
        private _route: ActivatedRoute) {

    }

    ngOnInit(): void {
        this.sub = this._route.params.subscribe(
            params => {
                let id = +params['id'];
                this.getResults(id);
            });

    }

    ngOnDestroy(): void {
        this.sub.unsubscribe();
    }

    getResults(id: number) {
        this._labResultService.getResults(id).
            subscribe(results => this.results = results, error => this.errorMessage = <any>error);
    }

    deleteFilters(): void {

        this.filterMarkerName = "";
        this.filterAbnormal = false;
    }


}