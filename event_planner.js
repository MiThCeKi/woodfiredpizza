

const event_planner_form  = document.querySelector('#event_planner_form');

event_planner_form.addEventListener('submit', function (e) {
  e.preventDefault()
  
  const formData = new FormData(event_planner_form)

  const jsonPayload = JSON.stringify(Object.fromEntries(formData));

  fetch ('https://jsonplaceholder.typicode.com/todos/1', {
      method: 'post',
      body: 'jsonPayload',
  }).then(function (response) {
    console.log(response.text)
    console.log(response.body)
    return response.text;
  }).catch(function (error){
    console.warn('something is a foot', error);
  })

});
