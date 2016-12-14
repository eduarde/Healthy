import { Component } from '@angular/core';
import { DictionaryComponent } from './dictionary/dictionary.component'
import { DictionaryService } from './dictionary/dictionary.service'

@Component({
  selector: 'my-app',
  template: `<h1>{{pageTitle}}</h1>
              <dictionaries></dictionaries>`,
  directives: [DictionaryComponent],
  providers: [DictionaryService]
})

export class AppComponent {
  pageTitle: string = 'Dictionary'

  constructor() {
  }
}
