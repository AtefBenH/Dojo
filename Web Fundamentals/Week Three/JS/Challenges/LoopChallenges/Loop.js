var i, fact=1;

// 1- Print odds 1-20
function printOdd ()
    {
        for (i=1; i<=20; i++)
            {
                if (i%2 != 0)
                    {
                        console.log(i);
                    }
            }
    }
    
// 2- Decreasing Multiples of 3
function decMultThree()
    {
        for (i=100; i>3; i--)
            {
                if (i%3 == 0)
                    {
                        console.log(i);
                    }
            }
    }

// 4- Sigma
function sigma ()
    {
        var sum =0;
        for (i=1; i<=100; i++)
            {
                sum += i;
            }
        console.log (sum);
    }

// 5- Factorial
function factorial (i)
    {
        if (i==0)
            return 1;
        else 
            return i*factorial (i-1);
    }

// Main
// printOdd ();
// decMultThree ();
// sigma();
console.log(factorial (12));