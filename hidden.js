
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

//try to get a console.log printout of something I click on. 
//make this more DRY by using event listeners at some point.

function showGraphHighlights () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#GraphHighlights')
  activePage.classList.remove('hidden')
}

function showMainGraph () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#MainGraph')
  activePage.classList.remove('hidden')
}

window.addEventListener('click', (event) => {
  wantedElement = event.target
  console.log(wantedElement)
  console.log(wantedElement.id)
  idOfWantedElement = wantedElement.id
  return idOfWantedElement
})


function ShowClickedPage () {
  idOfWantedElement.classList.remove('hidden')
  //need to have something adding the other. But how do I get the id
  //of an itdem that I haven't clicked.
}
// noticed a small side effect. Everything that is clicked has its id printed in 
//console.