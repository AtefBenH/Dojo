// function pizzaOven (crustType, sauceType, cheeses, toppings)
//     {
//         var pizza = {};
//         pizza.crustType = crustType;
//         pizza.sauceType = sauceType;
//         pizza.cheeses = cheeses;
//         pizza.toppings = toppings;
//         return pizza;
//     }
function getRandomNumber(min, max) 
    {
        return Math.floor(Math.random() * (max - min) + min);
    }
function randomPizza()
    {
        crustType =["Deep Dish", "Hand Tossed", 
                    "Stuffed Crust", "Cracker Crust",
                    "Flat Bread Crust", "Thin Crust",
                    "Cheese Crust", "Thick Crust",
                    "Wrapping It Up"
                    ]
        sauceType =["Sweet Pizza Sauces", "Spicy Red Sauces", 
                    "Peppery Red Sauce", "Pesto Sauce",
                    "Creamy Alfredo Sauce", "Ranch Sauce",
                    "Mayonnaise Sauce"
                    ]
        cheeses =   ["Mozzarella Cheese", "Provolone Cheese", 
                    "Cheddar Cheese", "Parmesan Cheese",
                    "Gouda", "Gruyere",
                    "Ricotta"
                    ]
        toppings =   ["Pepperoni", "Mushroom", "Sausage",
                    "Fresh Garlic", "Fresh Basil",
                    "Extra Cheese", "Onion"
                    ]
        var pizza = {};

        var x = getRandomNumber(0, 8);
        pizza.crustType = crustType[x];

        x = getRandomNumber(0, 7);
        pizza.sauceType = sauceType[x];

        x = getRandomNumber(0, 7);
        pizza.cheeses = cheeses[x];

        x = getRandomNumber(0, 7);
        
        var y = getRandomNumber(0, 7);
        while (y == x)
            {
                y = getRandomNumber(0, 7);
            }
        var z = getRandomNumber(0, 7);
        while (z == x ||z == y)
            {
                z = getRandomNumber(0, 7);
            }
        
        pizza.toppings = [toppings[x], toppings[y], toppings[z]];
        return pizza;
    }

// var pizza1 = pizzaOven ("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
// console.log("Fisrt Pizza : ", pizza1);
// var pizza2 = pizzaOven ("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
// console.log("Second Pizza : ", pizza2);
var randomP = randomPizza();
console.log(randomP);
