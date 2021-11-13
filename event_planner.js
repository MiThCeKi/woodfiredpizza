

const event_planner_form  = document.querySelector('#event_planner_form');

event_planner_form.addEventListener('submit', function (e) =>{
  e.preventDefault()
  
  const formData = new FormData(event_planner_form)

  const jsonPayload = JSON.stringify(Object.fromEntries(formData));

  fetch ('<MOCK-API-PLACEHOLDER>',  {
      method: 'post',
      body: 'jsonPayload',
  }).then(function (response) {
    console.log(response.text)
    console.log(response.body)
    return response.text;
  }).catch(function (error){
    console.error(error);
  })

})
