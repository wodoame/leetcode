const canPlaceFlowers = (flowerbed, n) => { 
    let can_plant = true, count = 0;
    const k = flowerbed.length
    for(let i=0; i < k - 1; i++){
       const spot = flowerbed[i];
       if(spot == 1){
        // We cannot plant at this position or at the next position
        can_plant = false;
       }  
       else if(can_plant && flowerbed[i + 1] == 0){
         count++; // we have planted but we cannot plant at the next position so we set cant_plant=false
        // a premature return for when we discover than we can plant exactly or  more than what is required
        if(count >= n){
            return true;
        }
         can_plant = false;
       }
       else{
        // We cannot plant at this position but let's now assume that we can plant at the next position
        can_plant = true;
       }
    }
    
    // This condition is here because we may end up with a situation like this [..., 0, 0]
    // Note that for the for loop we end at the first-to-last element
    // If can_plant is true at that element (first-to-last) we won't be able to plant at the last position...
    // .. since we'd be out of the for loop.
    // So we check if can_plant=true and the element is 0 then since no other element comes after it and ...
    // ... the preceding element must be 0 we can plant there
    if(can_plant && flowerbed[k - 1] == 0){
        count++;
    }
    
    console.log(count);
    return count >= n;  // >= n because the problem said to return whether n new plants can be planted. It's possible that we could have 
}; 

const flowerbed = [0,0,1,0,0];
const n = 1;

console.log(canPlaceFlowers(flowerbed, n));
