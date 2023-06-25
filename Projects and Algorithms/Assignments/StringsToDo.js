function removeBlanks(string){
    var result = "";
    for (var i=0; i<string.length; i++){
        if (string[i] != " "){
            result += string[i];
        }
    }
    return result;
}

function getDigits(string){
    var result = "";
    for (var i=0; i<string.length; i++){
        if (!isNaN(Number(string[i]))){
            result += string[i];
        }
    }
    return result;
}

function acronym(string){
    var splitted = string.split(' ');
    var result = "";
    for (i = 0; i < splitted.length; i++) {
        if(splitted[i].toUpperCase()){
            result += splitted[i][0].toUpperCase();
        }
    }
    return result;
}

function countNonSpaces(string){
    var count = 0;
    for(i=0; i<string.length; i++){
        if (string[i] != " "){
            count++;
        }
    }
    return count;
}

function removeShorterStrings(array, val){
    result = [];
    index = 0;
    for (i=0; i<array.length; i++){
        if(array[i].length >= val){
            result[index] = array[i];
            index++;
        }
    }
    return result;
}

// console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
// console.log(removeBlanks("I can not BELIEVE it's not BUTTER"));

// console.log(getDigits("abc8c0d1ngd0j0!8"));
// console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"));

// console.log(acronym(" there's no free lunch - gotta pay yer way. "));
// console.log(acronym("Live from New York, it's Saturday Night!"));

// console.log(countNonSpaces("Honey pie, you are driving me crazy"));
// console.log(countNonSpaces("Hello world !"));

// console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));
// console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));


