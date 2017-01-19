import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
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
            .do(data => console.log('All: ' + JSON.stringify(data)))
            ._catch(this.handleError);

    }

    /* getLab(id: number): Observable<ILab> {
         return this.getLabs()
             .map((labs: ILab[]) => labs.find(l => l.pk === id));
     }*/

    getLab(id: number): Observable<ILab> {
        let lab_url = this._labsUrl + id.toString() + '/';
        return this._http.get(lab_url)
            .map((response: Response) => <ILab>response.json())
            .do(data => console.log('All: ' + JSON.stringify(data)))
            ._catch(this.handleError);
    }

    addLab(lab: ILab) {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let body = JSON.stringify(lab);

        return this._http.post(this._labsUrl, body, headers)
            .map((res: Response) => res.json())
            ._catch(this.handleError);
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }

}