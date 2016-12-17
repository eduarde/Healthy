import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule  } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { RouterModule } from '@angular/router';

import { AppComponent }  from './app.component';
import { HomeComponent } from './home/home.component';

import { DictionaryModule } from './dictionary/dictionary.module';
import { LabModule } from './lab/lab.module';


@NgModule({
  imports: [ 
    BrowserModule,
    HttpModule,
    RouterModule.forRoot([
    
      { path: 'home', component: HomeComponent},
      { path: '', redirectTo: 'home', pathMatch: 'full' },
      { path: '**', redirectTo: 'home', pathMatch: 'full' }
    ]),
    DictionaryModule,
    LabModule

  ],
 

  declarations: [ 
    AppComponent,
    HomeComponent
  ],

  // providers: [ providers here ],

  bootstrap: [ 
    AppComponent
     ]
})
export class AppModule { }
