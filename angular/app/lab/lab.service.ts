import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';

import { ILab } from './lab';

@Injectable()
export class LabService {

    private _labsUrl = 'http://localhost:8000/labs/';

    constructor(private _http: Http) { }

    getLabs(): Observable<ILab[]> {
        return this._http.get(this._labsUrl)
            .map((response: Response) => <ILab[]>response.json())
            ._catch(this.handleError);

    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
    
}