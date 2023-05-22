
function login(){
    loginForm = document.getElementById('loginForm');

    var formData = new FormData(loginForm);

    fetch("http://localhost:5000/login", { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.message == "Error") {
                // console.log("Wrong Password");
                error = document.getElementById('logErrorMessage');
                error.innerText = "Wrong Informations";
                loginForm.reset();
            }
            else {
                window.location.replace('/dashboard');
            }
        })
}

function registration()
    {
        regForm = document.getElementById('registrationForm');
        var formData = new FormData(regForm);
        fetch("http://localhost:5000/users/create", { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            error = document.getElementById('regErrorMessage');
            error.innerHTML = ""
            if (data.errors.length !=0){
                for (key in data.errors) {
                    error.innerHTML += data.errors[key] + '<br>';
                    if (data.errors[key] == "First Name must contain at least 2 characters"){
                        field = document.getElementById('first_name');
                        // field.value = "";
                        field.style.backgroundColor = "lightcoral";
                    }
                    if (data.errors[key] == "Last Name must contain at least 2 characters"){
                        field = document.getElementById('last_name');
                        // field.value = "";
                        field.style.backgroundColor = "lightcoral";
                    }
                    if (data.errors[key] == "Email Already Exists" || data.errors[key] == "Email not valid"){
                        field = document.getElementById('email');
                        // field.value = "";
                        field.style.backgroundColor = "lightcoral";
                    }
                    if (data.errors[key] == "Password Must Have More Than 8 Characters" || data.errors[key] == "Password Must Contain At Least A Number And An Uppercase Character"){
                        field = document.getElementById('password');
                        field.value = "";
                        field.style.backgroundColor = "lightcoral";
                        field = document.getElementById('confirm_password');
                        field.value = "";
                    }
                    if (data.errors[key] == "Password and Confirmation Doesn't Match"){
                        field = document.getElementById('confirm_password');
                        field.value = "";
                        field.style.backgroundColor = "lightcoral";
                    }
                }
            }
            else {
                window.location.replace('/dashboard');
            }
        })
    }
