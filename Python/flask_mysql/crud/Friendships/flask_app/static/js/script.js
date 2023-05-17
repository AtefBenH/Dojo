function getFriends(element){
    console.log(element.innerHTML)
    fetch('/notfriends/'+element.value)
        .then(res =>  res.json())
        .then(data => {
            var friends = document.getElementById('friend');
            friends.innerHTML = ""
            for( let i = 0; i < data.length; i++){
                friends.innerHTML = ('<option value='+data[i].id+'>'+data[i].first_name + ' ' +data[i].last_name +'</option>') + friends.innerHTML;
                
            }
        })

}