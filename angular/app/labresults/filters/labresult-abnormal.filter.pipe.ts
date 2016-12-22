import { Pipe, PipeTransform } from '@angular/core';

import { IResult } from '../result';

@Pipe({
    name: 'labResultAbnormalFilter'
})
export class LabResultAbnormalFilter implements PipeTransform {

    transform(value: IResult[], filterBy: boolean) {

        return filterBy ? value.filter((result: IResult) => result.abnormal_result == filterBy) : value;

    }

}