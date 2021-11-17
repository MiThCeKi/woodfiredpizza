

const event_planner_form  = document.querySelector('#event_planner_form');

event_planner_form.addEventListener('submit', function (e) {
  e.preventDefault();
  const formData = new FormData(event_planner_form);
  // the jsonpayload is created from the form data. The form data into an js object that is then put into a JSON string.
  const jsonPayload = JSON.stringify(Object.fromEntries(formData));
  
  fetch('https://6191267b41928b001768ff71.mockapi.io/wfp/pizza',{method: 'post',body: 'jsonPayload',

  }).then(function (response) {
    // response.ok returns a truthy if the response returned successfully
    if (response.ok) {
      console.log('its working!', response);
      // so is this where I would do the business logic of calculating #of pizzas etc.? and then use those variables to display CSS?
      // .json() is a method that creates a js object from the JSON body. 
      return response.json();
    } else {

      return Promise.reject(response);
    }
    // in the tutorial on go make things I don't undrestand on how he can put in this (data). Where does it come from?
  }).then(function (data) {
    console.log(data);
  }).catch(function (error){
    console.warn('something is a foot', error)
    // what should I do here after an error is found. Can I perform any preprogrammed steps to handle it and recover?
    // I'm thinking like if the connection is down for a moment - what error would arrive - and then we put in a wait and then run the function again.
  })
});