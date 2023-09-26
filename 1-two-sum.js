var twoSum = function(nums, target) {
    const arr = nums; 
    const map = new Map();
    for(let i=0; i < arr.length; i++){
        let element = arr[i]; 
        j = map.get(element);
        if(j != undefined){
            return [j, i];
        }
        else{
            let to_find = target - element; 
            map.set(to_find, i); 
        }  
    }
};