
function alwaysHungry(arr) 
    {
        isThereFood = false;
        for (var i=0; i<arr.length; i++)
            {
                if (arr[i] == "food")
                    {
                        console.log("Yummy");
                        isThereFood = true;
                    }
            }
        if (!isThereFood)
            {
                console.log("I'm hungry");
            }
    }

function highPass(arr, cutoff) 
    {
        var filteredArr = [];
        for (var i=0; i<arr.length; i++)
            {
                if (arr[i]>cutoff)
                    {
                        filteredArr.push(arr[i]);
                    }
            }
        return filteredArr;
    }

function betterThanAverage(arr) 
    {
        var sum = 0;
        for (i=0; i<arr.length; i++)
            {
                sum += arr[i];
            }
        var avg = sum / arr.length;
        
        var count = 0
        for (i=0; i<arr.length; i++)
            {
                if (arr[i]>avg)
                    {
                        count++;
                    }
            }
        return count;
    }

function reverse(arr) 
    {
        var maxindex = arr.length-1;
        var carr = [];
        for (i=maxindex; i>=0; i--)
            {
                carr [maxindex-i] = arr [i];
            }
        arr = carr;
        return arr;
    }
    

function fibonacciArray(n) 
    {
        // the [0, 1] are the starting values of the array to calculate the rest from
        var fibArr = [0, 1];
        for (i=fibArr.length; i<n; i++)
            {
                fibArr.push(fibArr[i-1]+fibArr[i-2]);
            }
        return fibArr;
    }
    



// Main

// alwaysHungry([3.14, "food", "pie", true, "food"]);
// alwaysHungry([4, 1, 5, 7, 2]);

// var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
// console.log(result); 

// var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
// console.log(result);

// var result = reverse(["a", "b", "c", "d", "e"]);
// console.log(result);

var result = fibonacciArray(10);
console.log(result);

