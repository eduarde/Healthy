import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { ActivatedRoute, Router } from '@angular/router';

import { INote } from './note';
import { NoteService } from './note.service';

@Component({
    selector: 'lab-notes',
    moduleId: module.id,
    templateUrl: 'note-list.component.html',
    styleUrls: ['note-list.component.css']

})
export class NoteListComponent implements OnInit, OnDestroy {

    notes: INote[];
    errorMessage: string;
   
    private sub: Subscription;

    constructor(private _noteService: NoteService,
        private _router: Router,
        private _route: ActivatedRoute) {

    }

    ngOnInit(): void {
        this.sub = this._route.params.subscribe(
            params => {
                let id = +params['id'];
                this.getNotes(id);
            });
    
    }

    ngOnDestroy(): void {
        this.sub.unsubscribe();
    }


    getNotes(id: number) {
        this._noteService.getNotes(id).
            subscribe(notes => this.notes = notes, error => this.errorMessage = <any>error);
    }



}