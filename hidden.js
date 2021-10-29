
//const pages = [document.querySelector('#MainGraph'), document.querySelector('#GraphHighlights'), document.querySelector('#EventPlanner')]

//is only executed once DOM is in place. The arrow function declares a function too and exists for reasons unknown at this time. let it be.
//Function showMainGraph () { } are the same showMainGraph = () => { }

//can declare a variable in global scope to be used. No value. 
let activePage

//review this code and learn a tiny bit about arrow functions. 
window.onload = () => {
  activePage = document.querySelector('#MainGraph')
  activePage.classList.remove('hidden')
}

//make this more DRY by using event listeners at some point.
function showGraphHighlights () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#GraphHighlights')
  activePage.classList.remove('hidden')
}


// to keep DRY, I would have some sort of listen or way to capture
// what I clicked and then feed that into the ID
//should I use the ${}?
// I'd also have to set up that when this happens to hide the current one.
// OR I could set up a boolean ?
