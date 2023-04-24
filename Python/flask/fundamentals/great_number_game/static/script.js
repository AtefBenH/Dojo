
function checkValue()
    {
        var element = document.querySelector("#guess")

        if (!(Number.isInteger(parseInt(element.value, 10))))
            {
                alert('Please pick a valid number');
            }
    }
