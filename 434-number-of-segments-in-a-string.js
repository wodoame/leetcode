const countSegments = (s) => {
    let count = 0, encountered_space = true;
    for(const element of s){
        if(element == ' '){
            encountered_space = true; 
        }
        else if(encountered_space){
            // If a space was encounted before this character then we must have arrived at a new word so we increment the count
            // We set the encountered_space to false to prevent all other subsequent characters from counting up 
            count++;
            encountered_space = false;
        }
    }
    return count;
}

s = "Hello, my name is John"

console.log(countSegments(' h e hello world'));