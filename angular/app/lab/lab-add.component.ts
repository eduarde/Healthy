import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Observable } from 'rxjs/Observable';

import { LabService } from './lab.service';
import { ILab } from './lab';

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

    public labForm = this._fb.group({
        ref_number: ["", Validators.required],
        date: ["", Validators.required],
        doctor: ["", Validators.required],
        collection_point: ["",Validators.required],
        patient_code: ["", Validators.required]
    });

    constructor(public _fb: FormBuilder, private _labService: LabService) {

    }

    public saveLab(event) {

        let newLab : ILab = this.labForm.value;
        this._labService.addLab(newLab).subscribe(
            data => {
                // this.getLabs
                return true;
            }
        );

        console.log(event);
        console.log(this.labForm.value);
    }
}