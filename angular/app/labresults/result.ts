import { IMarker } from './marker';
import { IMarkerPredefined } from './marker.predefined';

export interface IResult {
    marker_ref: IMarker;
    value: number;
    lab_ref: number;
    predefined_red: IMarkerPredefined;
    abnormal_result: boolean;
}