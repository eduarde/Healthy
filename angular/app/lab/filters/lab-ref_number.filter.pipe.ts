import { Pipe, PipeTransform } from '@angular/core';

import { ILab } from './lab';

@Pipe({
    name: 'labRefNumberFilter'
})
export class LabRefNumberFilter implements PipeTransform {

    transform(value: ILab[], filterBy: string): ILab[] {
      
        return filterBy ? value.filter((lab: ILab) => lab.ref_number.toString().indexOf(filterBy) !== -1) : value;
    }

}