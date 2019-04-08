// Global app controller
import Search from './models/Search'
import * as searchView from './views/searchView'
import { elements } from './views/base'
/*
    Global state of app
    - Search object
    - Current recipe object
    - Shopping list object
    - Liked recipes

*/
const state = {};

const controlSearch  = async () => {
    // 1) Get query from view
    const query = searchView.getInput();
   

    if (query) {
        //2. New search object and add to state
        state.search = new Search(query);

        //3. Prepare UI for results 
        searchView.clearInput();
        searchView.clearResults();
        // 4. Seatch for recipes 
        await state.search.getResults(); //returns promise automaticly becouse we call async

        //5.Render results on UI
        searchView.renderResults(state.search.result);

    }
}

elements.searchForm.addEventListener('submit', e => {
    e.preventDefault();
    controlSearch();
})