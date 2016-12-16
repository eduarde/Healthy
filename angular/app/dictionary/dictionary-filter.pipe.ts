import { PipeTransform, Pipe } from '@angular/core';

import { IDictionary } from './dictionary';

@Pipe({
    name: 'dictionaryFilter'
})
export class DictionaryFilterPipe implements PipeTransform{

    transform(value: IDictionary[], filterBy: string): IDictionary[] {
        filterBy = filterBy ? filterBy.toLowerCase() : null;
        return filterBy ? value.filter((dictionary: IDictionary) => dictionary.marker_ref.name.toLowerCase().indexOf(filterBy) !== -1) : value;
    }

}