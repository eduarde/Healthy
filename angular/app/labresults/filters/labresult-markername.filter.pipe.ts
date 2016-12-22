import { Pipe, PipeTransform } from '@angular/core';

import { IResult } from '../result';

@Pipe({
    name: 'labResultMarkerNameFilter'
})
export class LabResultMarkerNameFilter implements PipeTransform {

    transform(value: IResult[], filterBy: string) {
        return filterBy ? value.filter(
            (result: IResult) =>
                result.marker_ref.name.toLocaleLowerCase().indexOf(filterBy.toLowerCase()) !== -1) : value;
    }

}