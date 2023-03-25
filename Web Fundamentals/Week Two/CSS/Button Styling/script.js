function reverse (element)
    {
        if (element.innerText == "Search")
            element.innerText = "Found";
        else if (element.innerText == "+")
            element.innerText = "-"; 
        else if (element.innerText == "Create Account")
            element.innerText = "Account Created";

    }