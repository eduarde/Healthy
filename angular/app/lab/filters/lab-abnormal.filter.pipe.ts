import { Pipe, PipeTransform } from '@angular/core';

import { ILab } from '../lab';

@Pipe({
    name: 'labAbnormalFilter'
})
export class LabAbnormalFilter implements PipeTransform {

    transform(value: ILab[], filterBy: boolean) {

        return filterBy ? value.filter((lab: ILab) => lab.abnormal_lab == filterBy) : value;

    }

}