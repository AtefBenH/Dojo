

function changeName (newName)
    {
        document.querySelector(".card-body h1").innerText = newName ;
        document.querySelector(".card-head img").src = "Pictures/images/walter-white.png";
        document.querySelector(".card-body p").innerHTML = "Also Known as Heisenberg | High School Teacher | Chemist" + '<br>' +       
        "Drug Lord and friend of Jesse Pinkman";
        document.getElementsByClassName("location")[0].innerText = "Albuquerque";
    }
function acceptUser (user)
    {
        document.getElementById (user).remove();
        document.querySelector("#ConReq").innerText --;
        document.querySelector("#activeCon").innerText ++;
    }
function denyUser (user)
    {
        document.getElementById (user).remove();
        document.querySelector("#ConReq").innerText --;
    }