
function displayAlert (element)
    {
        alert (element.innerText + "'s" + " weather report is loading...") ;

    }
function dismissCookies()
    {
        document.querySelector (".cookie").remove();
    }
function convertTemperture (element)
    {
        var maxs = document.getElementsByClassName("max");
        var mins = document.getElementsByClassName("min");
        if (element.value == "F")
            {
                for (i=0; i<maxs.length; i++)
                    {
                        maxs[i].innerText = Math.round(maxs[i].innerText * 9/5 + 32);
                        mins[i].innerText = Math.round(mins[i].innerText * 9/5 + 32);
                    }
            }
        else
            {
                for (i=0; i<maxs.length; i++)
                    {
                        maxs[i].innerText = Math.round((maxs[i].innerText -32) * 5/9);
                        mins[i].innerText = Math.round((mins[i].innerText -32) * 5/9);
                    }
            }
    }

async function getWeather(element) 
    {
        alert (element.innerText + "'s" + " weather report is loading...") ;
        var response1 = await fetch ("http://api.openweathermap.org/geo/1.0/direct?q="+element.innerText+"&appid=f0986ac06f5078827b18050fd31c9a91");
        var coordinate = await response1.json();
        console.log(coordinate);
        var response = await fetch("https://api.openweathermap.org/data/2.5/weather?lat="+coordinate[0].lat+"&lon=" +coordinate[0].lon+"&appid=f0986ac06f5078827b18050fd31c9a91");
        var data = await response.json();
        console.log(data);
        description = document.getElementsByClassName("test");
        max = document.getElementsByClassName('max');
        min = document.getElementsByClassName("min");
        temp = document.getElementsByClassName("temperture");
        console.log(temp)
        if (temp[0].value == "C" ) {
            min[0].innerHTML = Math.round(data.main.temp_min)-273,15 ; 
            max[0].innerHTML = Math.round(data.main.temp_max)-273,15 ;
        }
        else {
            min[0].innerHTML = ((Math.round(data.main.temp_min)-273,15)*9/5) + 32 ; 
            max[0].innerHTML = ((Math.round(data.main.temp_max)-273,15)*9/5) + 32
        }
        
        description[0].innerHTML = data.weather[0].description.charAt(0).toUpperCase() + data.weather[0].description.slice(1);
        city = document.getElementsByClassName('city') ;
        current = document.getElementsByClassName('current') ;
        url = document.getElementsByClassName('url')
        url[0].src = "https://openweathermap.org/img/wn/" + data.weather[0].icon + "@2x.png";
        city[0].innerText = data.name;
        current[0].innerHTML = "Current";
        // temp = getbyid
    }