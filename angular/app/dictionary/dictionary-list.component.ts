import { Component, OnInit } from '@angular/core';

import { IDictionary } from './dictionary';
import { DictionaryService } from './dictionary.service';

@Component({
    moduleId: module.id,
    templateUrl: 'dictionary-list.component.html'
})
export class DictionaryListComponent implements OnInit {
    pageTitle: string = "Dictionaries";
    listFilter: string;
    errorMessage: string;
    dictionaries: IDictionary[];

    constructor(private _dictionaryService: DictionaryService) {

    }

    ngOnInit() : void {
        this._dictionaryService.getDictionaries()
            .subscribe(dictionaries => this.dictionaries = dictionaries,
                        error => this.errorMessage = <any>error );
    }
}