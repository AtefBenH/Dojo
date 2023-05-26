async function refresh()
    {
        location.reload();
    }

function login()
    {
        loginForm = document.getElementById('loginForm');
        var formData = new FormData(loginForm);

        fetch("http://localhost:5000/login", { method: 'POST', body: formData })
            .then(response => response.json())
            .then(data => {
                if (data.message == "Error") 
                    {
                        error = document.getElementById('logErrorMessage');
                        error.innerText = "Wrong Informations";
                        loginForm.reset();
                    }
                else 
                    {
                        window.location.replace('/dashboard');
                    }
            });
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
                    if (data.errors[key] == "This Email is Blacklisted"){
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

function validateBook(){
    loginForm = document.getElementById('addBookForm');

    var formData = new FormData(loginForm);

    fetch("http://localhost:5000//books/create", { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => 
            {
                error = document.getElementById('addBookErrorMessage');
                error.innerHTML = ""
                if (data.errors.length !=0){
                    for (key in data.errors) {
                        error.innerHTML += data.errors[key] + '<br>';
                        if (data.errors[key] == "Book Must Have a Title"){
                            field = document.getElementById('title');
                            // field.value = "";
                            field.style.backgroundColor = "lightcoral";
                        }
                        if (data.errors[key] == "Author must contain at least 2 characters"){
                            field = document.getElementById('author');
                            // field.value = "";
                            field.style.backgroundColor = "lightcoral";
                        }
                        if (data.errors[key] == "Description must contain at least 5 characters"){
                            field = document.getElementById('description');
                            // field.value = "";
                            field.style.backgroundColor = "lightcoral";
                        }
                    }
                }
                else {
                    window.location.replace('/dashboard');
                }
            })
}

function createLike(element)
    {
        let book_id = element.value;
        fetch("/likes/"+book_id+"/create")
        .then(response => response.json())
        .then(data => {
            let newElement = document.createElement("span");
                newElement.textContent = "This is one of your favorites";
                newElement.classList.add("fst-italic");
                element.replaceWith(newElement);
                count = parseInt(document.getElementById('count').innerText);
                document.getElementById('count').innerText = count+1;
        })
        setTimeout(() => {
            location.reload();
        }, 100);
    }

function updateBook(element)
    {
        updateForm = document.getElementById('updateBookForm');

        var formData = new FormData(updateForm);

        let book_id = element.value;
        fetch("/books/"+book_id+"/update", { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            error = document.getElementById('updateBookError');
            error.innerHTML = ""
            if (data.errors.length !=0){
                for (key in data.errors) {
                    error.innerHTML += data.errors[key] + '<br>';
                    if (data.errors[key] == "Book Must Have a Title"){
                        field = document.getElementById('title');
                        field.style.backgroundColor = "lightcoral";
                    }
                    if (data.errors[key] == "Author must contain at least 2 characters"){
                        field = document.getElementById('author');
                        field.style.backgroundColor = "lightcoral";
                    }
                    if (data.errors[key] == "Description must contain at least 5 characters"){
                        field = document.getElementById('description');
                        field.style.backgroundColor = "lightcoral";
                    }
                }
            }
            else {
                window.location.replace('/dashboard');
            }
        })
    }

function deleteLike(element)
    {
        let book_id = element.value;
        fetch("/likes/"+book_id+"/delete")
        .then(response => response.json())
        .then(data => {
            if (data.message){
                parent = element.parentNode;
                parent.remove();
                element.remove();
                count = parseInt(document.getElementById('count').innerText);
                document.getElementById('count').innerText = count-1;
            }
        })
    }

async function getBookInfo(element)
    {
        let book_id = element.getAttribute("data-value1");
        let book_title = element.getAttribute("data-value2");
        let book_author = element.getAttribute("data-value3");
        console.log(book_author);
        let response = await fetch("https://openlibrary.org/search.json?title="+book_title+"&author="+book_author);
        let data = await response.json();
        let isbn = data.docs[0].isbn[0];
        first_publish_year=data.docs[0].first_publish_year;
        rating = data.docs[0].ratings_average.toPrecision(3);
        console.log(rating);
        subjects = [];
        for (let i = 0; i < 3; i++)
            {
                subjects.push(data.docs[0].subject[i].charAt(0).toUpperCase() + data.docs[0].subject[i].slice(1));
            }
        response  = await fetch("https://covers.openlibrary.org/b/isbn/"+isbn+"-M.jpg");
        if (response.status==200)
            {
                imgSrc = response.url;
            }
        else 
            {
                imgSrc = "flask_app/static/img/notFound.png"
            }
        data = {
            'first_publish_year' : first_publish_year,
            'rating' : rating,
            'subjects' : subjects,
            'imgSrc' : imgSrc
        }
    fetch("http://localhost:5000/book/api", {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            window.location.replace("/books/"+book_id+"/view");
            // console.log("DATA : ", data);
        });
}