import { IUser } from './user';

export interface IUserProfile {
    user: IUser;
    gender: string;
    dob: Date;
    blood_type: string;
    url_gravatar: string
}