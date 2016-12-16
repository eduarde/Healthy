import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { DictionaryListComponent } from './dictionary-list.component';
import { DictionaryService } from './dictionary.service';

import { DictionaryFilterPipe } from './dictionary-filter.pipe';

@NgModule({
    declarations: [
        DictionaryListComponent,
        DictionaryFilterPipe
    ],
    imports: [
        RouterModule.forChild([
            { path: 'dictionary', component: DictionaryListComponent }
        ]),
        CommonModule,
        FormsModule
    ],
    providers: [
        DictionaryService,
        DictionaryFilterPipe
    ]
})
export class DictionaryModule {

}