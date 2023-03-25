function updateButton(element)
    {
        if (element.innerText == "Login")
            {
                element.innerText ="Logout";
            }
        else if (element.innerText == "Add Definition")
            {
                element.remove();
            }
    }