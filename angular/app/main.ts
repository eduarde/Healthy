import { bootstrap }    from '@angular/platform-browser-dynamic';
import { HTTP_PROVIDERS } from '@angular/http';
import { RequestOptions } from '@angular/http';
import { AppRequestOptions } from './helper/AppRequestOptions'
import { provide } from '@angular/core'

import { AppComponent } from './app.component';

bootstrap(AppComponent, [
	HTTP_PROVIDERS,
	provide(RequestOptions, { useClass: AppRequestOptions }),
	provide('webApiBaseUrl', {useValue: 'http://localhost:8000'})
]);