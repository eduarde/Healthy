import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';

import { IResult } from './result';

@Injectable()
export class LabResultService {

    private _resultsUrl = "http://localhost:8000/lab/"

    constructor(private _http: Http) {

    }

    getResults(lab: number): Observable<IResult[]> {

        let url = this._resultsUrl + lab.toString() + '/results/';

        return this._http.get(url)
            .map((respone: Response) => <IResult[]>respone.json())
            ._catch(this.handleError);
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');

    }


}