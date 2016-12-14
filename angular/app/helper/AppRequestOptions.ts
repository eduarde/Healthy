import {BaseRequestOptions, RequestOptions, RequestOptionsArgs} from '@angular/http';
import { Injectable, Inject  } from '@angular/core';

@Injectable()
export class AppRequestOptions extends RequestOptions  {
  
  constructor(@Inject('webApiBaseUrl') private webApiBaseUrl:string) {
    super();
  }

  merge(options?:RequestOptionsArgs):RequestOptions {
    options.url = this.webApiBaseUrl + options.url;
    
    if (options.method === 'put' ||
         options.method === 'post' ||
         options.method === 'patch') {
      let headers = options.headers ;
      headers['Content-Type'] = 'application/json';
      options.headers = headers;
      }

    return super.merge(options);
  }
}