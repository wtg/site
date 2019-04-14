import Contributor from './contributor';

// Project holds everything we want to display on a project card
export default class Project {
    public name: string;
    public url: string;
    public description: string;
    public webpage: string;
    public slug: string;

    public contributors: Contributor[] = [];

    constructor(name: string, url: string, description: string, webpage: string, slug: string) {
        this.name = name;
        this.url = url;
        this.description = description;
        this.webpage = webpage;
        this.slug = slug;
    }

    public getImageUrl(): string {
        return '/static/images/' + this.slug + '.png';
    }

    // the project only has an image if it has a website
    public hasImage(): boolean {
        return this.webpage !== '';
    }
}
