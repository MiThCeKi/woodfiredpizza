
// const pages = [document.querySelector('#MainGraph'), document.querySelector('#GraphHighlights'), document.querySelector('#EventPlanner')]

// is only executed once DOM is in place. The arrow function declares a function too and exists for reasons unknown at this time. let it be.
// Function showMainGraph () { } are the same showMainGraph = () => { }

//  can declare a variable in global scope to be used. No value. 
let activePage

// review this code and learn a tiny bit about arrow functions. 
window.onload = () => {
  activePage = document.querySelector('#MainGraph')
  activePage.classList.remove('hidden')
}

// try to get a console.log printout of something I click on. 
// make this more DRY by using event listeners at some point.

function showGraphHighlights () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#GraphHighlights')
  activePage.classList.remove('hidden')
  const item_to_render = "Do you see this text?";
  document.getElementById("fill").innerHTML = item_to_render;
}

function showMainGraph () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#MainGraph')
  activePage.classList.remove('hidden')
}

function showEventPlanner () {
  activePage.classList.add('hidden')
  activePage = document.querySelector('#EventPlanner')
  activePage.classList.remove('hidden')
}

window.addEventListener('click', (event) => {
  wantedElement = event.target
  idOfWantedElement = wantedElement.id
  console.log(wantedElement.id)
  return idOfWantedElement
})

//  function genericShow (){
//    activePage = document.querySelector('')
// }
