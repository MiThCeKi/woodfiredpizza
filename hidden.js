
function showMainGraph () {
  console.log('indicator for showMainGraph')
  const showMainGraph = document.getElementById('MainGraph')
  const hideGraphHighlights = document.getElementById('GraphHighlights')
  hideGraphHighlights.className += 'hidden'
  showMainGraph.className += 'show_main_graph'
}


function showGraphHighlights () {
  console.log('indicator for showGraphHighlights')
  const hideMainGraph = document.getElementById('MainGraph')
  const showGraphHighlights = document.getElementById('GraphHighlights')
  hideMainGraph.className += 'hidden'
  showGraphHighlights.className += 'show_GraphHighlights'
}
showMainGraph()
showGraphHighlights()
// to keep DRY, I would have some sort of listen or way to capture
// what I clicked and then feed that into the ID
//should I use the ${}?
// I'd also have to set up that when this happens to hide the current one.
// OR I could set up a boolean ?
