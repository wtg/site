// Project holds everything we want to display on a project card
export default class Project {
    public name: string;
    public url: string;
    public description: string;
    public webpage: string;

    constructor(name: string, url: string, description: string, webpage: string) {
        this.name = name;
        this.url = url;
        this.description = description;
        this.webpage = webpage;
    }
}
