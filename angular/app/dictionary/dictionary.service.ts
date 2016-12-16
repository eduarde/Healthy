import { Injectable } from '@angular/core';
import { Http,Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';
 

import { IDictionary } from './dictionary';

@Injectable()
export class DictionaryService {
    
    private _dictionaryUrl = 'http://localhost:8000/dictionary/';

    constructor(private _http: Http) {}

    getDictionaries(): Observable<IDictionary[]> {
        return this._http.get(this._dictionaryUrl)
        .map((response: Response) => <IDictionary[]> response.json())
        .catch(this.handleError);
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');

    }
}