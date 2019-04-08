import axios from 'axios';
//import * as searchView from './views/searchView';

export default class Search {
    constructor(query) {
        this.query = query;
    }

    async getResults() {
        const proxy = 'https://cors-anywhere.herokuapp.com/';
        const key = '030e87af855e7aa4fb4d43626792ac87';
        try {
            const res = await axios(`${proxy}https://www.food2fork.com/api/search?key=${key}&q=${this.query}`);
            this.result = res.data.recipes;
            
        } catch (error) {
            alert(error)
        }
    }
}