import { IMarker } from '../shared/marker';

export interface IDictionary {
    id: number,
    marker_ref: IMarker;
    text: string;
}