import { Pipe, PipeTransform } from '@angular/core';

import { ILab } from './lab';

@Pipe({
    name: 'labDateFilter'
})
export class LabDateFilter implements PipeTransform {

    transform(value: ILab[], filterBy: string): ILab[] {

        return filterBy ? value.filter((lab: ILab) => lab.date == filterBy) : value;
    }

}