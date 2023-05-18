document.getElementById('loginForm').addEventListener('submit', function (event) {
  event.preventDefault();

  // Récupérer les données du formulaire
  var formData = new FormData(this);

  // Effectuer la requête AJAX
  fetch("http://localhost:5000/login", { method: 'POST', body: formData })
      .then(response => response.json())
      .then(data => console.log(data))
      if (data.message == "noPass"){
        console.log('Wrong Password')
      }
      else if (data.message == "noEmail"){
        console.log("Email doesn't Exist")
      }
      else {
        console.log("Welcome")
      }
})
    // loginForm.reset();
    // location.reload();
    // getUser(data);
//       if (response.redirected) {
//         // Le formulaire a été validé avec succès
//         // Traiter la réponse ici
//         console.log('OK')
//         console.log(response);
//       } else {
//         // Le formulaire n'a pas été validé
//         // Afficher un message d'erreur ou effectuer une autre action
//         console.log('KO')
//         console.log(response);
//       }
//     })
//     .catch(function (error) {
//       // Une erreur s'est produite lors de la requête AJAX
//       console.log('Erreur AJAX:', error);
//     });
// });
// function validate() {
//   var loginForm = document.getElementById('loginForm');
//   loginForm.onsubmit = function (e) {
//     // "e" is the js event happening when we submit the form.
//     // e.preventDefault() is a method that stops the default nature of javascript.
//     e.preventDefault();
//     // create FormData object from javascript and send it through a fetch post request.
//     var form = new FormData(loginForm);
//     // this how we set up a post request and send the form data.
//     fetch("http://localhost:5000/login", { method: 'POST', body: form })
//       .then(response => response.json())
//       .then(data => getUser(data))
//     loginForm.reset();
//     // location.reload();
//     // getUser(data);
//   }}
