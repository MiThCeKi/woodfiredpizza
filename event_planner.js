

const event_planner_form  = document.querySelector('#event_planner_form');

event_planner_form.addEventListener('submit', function (e) {
  e.preventDefault();
  const formData = new FormData(event_planner_form);
  const jsonPayload = JSON.stringify(Object.fromEntries(formData));
  
  fetch('https://6191267b41928b001768ff71.mockapi.io/wfp/pizza',{method: 'post',body: 'jsonPayload',

  }).then(function (response) {
    // response.ok returns a truthy(?) if the response returned successfully
    if (response.ok) {
      console.log('its working!', response);
      // .json() is a method that creates a js object from the JSON body. 
      return response.json();
    } else {

      return Promise.reject(response);
    }
  }).then(function (data) {
    console.log(data);
  }).catch(function (error){
    console.warn('something is a foot', error)
    // what should I do here after an error is found. Can I perform any preprogrammed steps to handle it and recover?
  })
});

