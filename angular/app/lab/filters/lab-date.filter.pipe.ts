import { Pipe, PipeTransform } from '@angular/core';

import { ILab } from '../lab';

@Pipe({
    name: 'labDateFilter'
})
export class LabDateFilter implements PipeTransform {

    d: Date = new Date("2016-12-09")
    e: Date = new Date("2016-12-09")

    transform(value: ILab[], filterBy: Date): ILab[] {
        if(filterBy){
 
         console.log("d: " + this.d.getTime());
         console.log('filter: ' + filterBy.getTime());   

         if( this.d.getTime() == filterBy.getTime()) {
            console.log('egale');
        }
        }

       
        return filterBy ? value.filter((lab: ILab) => new Date((lab.date)).getTime() == filterBy.getTime()  ) : value;
    }

}