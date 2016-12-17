import { Component, OnInit } from '@angular/core';
const url = 'app/assets/js/creative.min.js';

@Component({
    selector: 'healthy-app',
    moduleId: module.id,
    templateUrl: `app.component.html`,

})
export class AppComponent implements OnInit {

    pageTitle: string = 'Healthy';
    user: string = 'User';

    ngOnInit(): void {
        let node = document.createElement('script');
        node.src = url;
        node.type = 'text/javascript';
        node.async = true;
        node.charset = 'utf-8';
        document.getElementsByTagName('body')[0].appendChild(node);

    }


}
