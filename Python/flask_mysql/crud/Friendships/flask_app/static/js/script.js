function envoyerValeur() {
    var liste = document.getElementById("user");
    var valeurSelectionnee = liste.options[liste.selectedIndex].value;

    // Effectuer une requête HTTP au serveur pour envoyer la valeur
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("valeur=" + encodeURIComponent(valeurSelectionnee));

    // Réagir à la réponse du serveur si nécessaire
    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        // Traitement de la réponse du serveur
        console.log(xhr.responseText);
    }
    };
}