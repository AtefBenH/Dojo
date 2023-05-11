var cardsDiv = document.querySelector("#cards");
var currentUsername = "";

function getUsername(element) {
    console.log(element.value);
    currentUsername = element.value;
}

function makeCoderCard(data) {
    var res =  `<div class="card" style="width: 18rem;">
    <img src="${data.avatar_url}" class="card-img-top" alt="${data.login}">
    <div class="card-body">
        <h5 class="card-title">${data.name}</h5>
        <p class="card-text">Location: ${data.location}</p>
        <p class="card-text">Followers: ${data.followers}</p>
        <p class="card-text">Repositories: ${data.public_repos}</p>
        <p class="card-text">Created at: ${data.created_at}</p>
        
    </div>
</div>`
    return res;
}

async function search() {
    var response = await fetch("https://api.github.com/users/" + currentUsername);
    var coderData = await response.json();
    // console.log(coderData);
    cardsDiv.innerHTML = makeCoderCard(coderData) + cardsDiv.innerHTML;
    console.log(coderData)

}

{/* <div class="card">
                    <img src="${data.avatar_url}" alt="${data.login}">
                    <div class="flex-1">
                        <h3>${data.login} - ${data.name}</h3> 
                        <p>Location: ${data.location}</p>
                        <p>Repositories: ${data.public_repos}</p>
                    </div>
                </div> */}