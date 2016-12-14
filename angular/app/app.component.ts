import { Component } from '@angular/core';
import { DictionaryComponent } from './components/dictionary/dictionary'
import { DictionaryService } from './services/dictionaryService'

@Component({
  selector: 'my-app',
  template: `<h1>Dictionaries</h1>
              <dictionaries></dictionaries>`,
  directives: [DictionaryComponent],
  providers: [DictionaryService]
})

export class AppComponent {
  

  constructor() {
  }
}
