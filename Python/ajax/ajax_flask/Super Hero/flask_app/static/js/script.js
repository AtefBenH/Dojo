
function fetchSuper(e){
    e.preventDefault();
    var form = document.getElementById('myForm');
    var formData = new FormData(form);
    fetch("/superhero/search", { method: 'POST', body: formData })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                var searchResultDiv = document.getElementById('searchResult');
                searchResultDiv.innerHTML = "";
                var errorResultDiv = document.getElementById('Error');
                errorResultDiv.innerText = "";
                input = document.getElementById('superhero');
                input.value = "";
                if (data.error){
                    var par = document.createElement("p");
                    par.classList.add("text-danger");
                    par.innerText = data.error;
                    errorResultDiv.appendChild(par);
                }
                else{
                    
                    for (i=0; i<data.results.length; i++){
                        var searchResultDiv = document.getElementById('searchResult');
                        var div = document.createElement("div");
                        div.classList.add("col-"+(12/data.results.length));
                        div.classList.add("d-flex");
                        div.classList.add("justify-content-center");
                        searchResultDiv.appendChild(div);
                        var card = document.createElement("div");
                        card.classList.add("card");
                        card.setAttribute("style", "width: 18rem;");
                        div.appendChild(card);
                        var img = document.createElement("img");
                        img.setAttribute("src", data.results[i].image['url']);
                        card.appendChild(img);
                        var body = document.createElement("div");
                        body.classList.add("card-body");
                        card.appendChild(body);
                        var name = document.createElement("h4");
                        name.classList.add("card-title");
                        name.classList.add("text-primary");
                        name.innerText = data.results[i].biography['full-name']
                        body.appendChild(name);
                        var span = document.createElement("span");
                        span.classList.add("fw-bold");
                        if (data.results[i].biography['alignment'] == 'good'){
                            span.classList.add("text-success");
                        }
                        else {
                            span.classList.add("text-danger");
                        }
                        span.innerText = data.results[i].biography['alignment'].toUpperCase();
                        body.insertBefore(span, name.nextSibling);

                        var app = document.createElement("h6");
                        app.classList.add("card-title");
                        app.classList.add("text-danger");
                        app.innerText = "Appearence :"
                        body.appendChild(app);

                        var ul = document.createElement("ul");
                        ul.classList.add("list-group");
                        ul.classList.add("list-group-flush");
                        app.appendChild(ul);
                        var keys = Object.keys(data.results[i].appearance);
                        var values = Object.values(data.results[i].appearance);
                        for (let j = 0; j < keys.length; j++) {
                            let li = document.createElement("li");
                            li.classList.add("list-group-item");
                            li.innerText = keys[j] + " : " + values[j];
                            ul.appendChild(li);
                        }

                        var pow = document.createElement("h6");
                        pow.classList.add("card-title");
                        pow.classList.add("text-danger");
                        pow.innerText = "Power Stats :"
                        body.appendChild(pow);

                        var ul1 = document.createElement("ul");
                        ul1.classList.add("list-group");
                        ul1.classList.add("list-group-flush");
                        pow.appendChild(ul1);
                        var keys1 = Object.keys(data.results[i].powerstats);
                        var values1 = Object.values(data.results[i].powerstats);
                        for (let j = 0; j < keys1.length; j++) {
                            let li = document.createElement("li");
                            li.classList.add("list-group-item");
                            li.innerText = keys1[j] + " : " + values1[j];
                            ul1.appendChild(li);
                        }
                    }
                }
            });

}