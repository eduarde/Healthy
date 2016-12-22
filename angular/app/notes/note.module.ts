import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { NoteListComponent } from './note-list.component';
import { NoteService } from './note.service';

@NgModule({

    imports: [

        CommonModule,
        FormsModule
    ],
    declarations: [
      NoteListComponent
    ],

    providers: [
        NoteService
    ],

    exports: [
        NoteListComponent
    ]

})
export class NoteModule {

}