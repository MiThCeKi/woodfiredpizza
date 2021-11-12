

const event_planner_form  = document.querySelector('#event_planner_form');

event_planner_form.addEventListener('submit', function (e) =>{
  e.preventDefault()
  
  const formData = new FormData(event_planner_form)

  fetch ('<some address>, {
    method: 'post',
    body: 'event_planner_form',
  }).then(function (response) {
    console.log(response.text)
    console.log(response.body)
    return response.text
  }

})
