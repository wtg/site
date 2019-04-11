// Contributor represents a single contributor on one project
// The contributions are based on the project it is stored in, not global.
export default class Contributor {
    public username: string;
    public avatarURL: string;
    public contributions: number;
    public profileURL: string;

    constructor(username: string, avatarURL: string, contributions: number, profileURL: string) {
        this.username = username;
        this.avatarURL = avatarURL;
        this.contributions = contributions;
        this.profileURL = profileURL;
    }
}
