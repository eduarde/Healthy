import { Component, OnInit } from '@angular/core';
import { DictionaryService } from '../../services/dictionaryService'

@Component({
  selector: 'dictionaries',
  template: `<ul><li *ngFor="let dictionary of dictionaries">{{dictionary.text}}</li></ul>`
})
export class DictionaryComponent implements OnInit {
  dictionaries: any[];
  error: any;

  constructor(private dictionaryService: DictionaryService) { }

  getDictionaries() {
    this.dictionaryService
        .getDictionary()
        .then(dictionaries => this.dictionaries = dictionaries)
        .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getDictionaries();
  }
}
