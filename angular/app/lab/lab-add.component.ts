import { Component } from '@angular/core';

@Component({
    moduleId: module.id,
    templateUrl: 'lab-add.component.html'
})
export class LabAddComponent {
    pageTitle: string = "Add lab";

    datepickerOpts = {
        autoclose: true,
        todayBtn: 'linked',
        todayHighlight: true,
        assumeNearbyYear: true,
        format: 'yyyy-mm-dd',
        icon: 'fa fa-calendar'
    }
}