
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