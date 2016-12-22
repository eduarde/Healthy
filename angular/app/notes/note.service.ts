import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';

import { INote } from './note';

@Injectable()
export class NoteService {

    private _notesUrl = "http://localhost:8000/lab/"

    constructor(private _http: Http) {

    }

    getNotes(lab: number): Observable<INote[]> {

        let url = this._notesUrl + lab.toString() + '/notes/';

        return this._http.get(url)
            .map((respone: Response) => <INote[]>respone.json())
            ._catch(this.handleError);
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');

    }


}