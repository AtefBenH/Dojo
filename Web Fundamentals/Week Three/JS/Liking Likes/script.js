

function addLike(element)
    {
        if (element.className == "btn")
            {
                document.querySelector("#number").innerText ++;
            }
        else if (element.className == "btn1")
            {
                document.querySelector("#number1").innerText ++;
            }
        else if (element.className == "btn2")
            {
                document.querySelector("#number2").innerText ++;
            }
        else
            {
                document.querySelector("#number3").innerText ++;
            }
    }