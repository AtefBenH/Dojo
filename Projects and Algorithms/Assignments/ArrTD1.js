
function pushFront(array, val) {
    for (i = array.length; i >= 0; i--) {
        array[i] = array[i - 1];
    }
    array[0] = val;
    return array;
}

function popFront(array){
    aux = array[0];
    for (i=0; i<array.length -1; i++){
        array[i] = array[i+1];
    }
    array.length = array.length - 1;
    console.log("New Array : ", array);
    return aux;
}

function insertAt(array, index, val){
    for (i=array.length; i>=index; i--){
        array[i] = array[i - 1];
    }
    array[index] = val;
    return array;
}

function removeAt(array, index){
    aux = array[index];
    for (i=index; i<array.length-1; i++){
        array[i] = array[i+1];
    }
    array.length = array.length - 1;
    console.log("New Array : ", array);
    return aux;
}

function swapPairs(array){
    if ((array.length)%2 == 0){
        for(var i=0; i<=array.length-2; i=i+2){
            aux = array[i];
            array[i] = array[i+1];
            array[i+1] = aux;
        }
    }
    else{
        for(var i=0; i<=array.length - 3; i=i+2){
            aux = array[i];
            array[i] = array[i+1];
            array[i+1] = aux;
        }
    }
    return array;
}

function removeAtV2(array, index){
    aux = array[index];
    for (i=index; i<array.length-1; i++){
        array[i] = array[i+1];
    }
    array.length = array.length - 1;
    return array;
}

function removeDupes(array){
    for(i=0; i<array.length - 1; i++){
        if (array[i] == array[i+1]){
            removeDupes(removeAtV2(array, i));
        }
    }
    return array;
}

// console.log(pushFront([5,4,3,2,1], 6));

// pop = popFront([0,5,10,15]);
// console.log("Front : ", pop);

// console.log(insertAt([100,200,5], 2, 311));
// console.log(insertAt([9,33,7], 1, 42));

// pop = removeAt([1000,3,204,77], 1);
// console.log("Remove = ", pop);

// console.log(swapPairs([1,2,3,4,5,6]));
// console.log(swapPairs(["My", "Bond", "Is", "Name", "Bond"]));

// console.log(removeDupes([-2,-2,3.14,5,5,10]));
// console.log(removeDupes([9,19,19,19,19,19,29]));

