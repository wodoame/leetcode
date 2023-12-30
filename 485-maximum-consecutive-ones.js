const findMaxConsecutiveOnes = (nums) => {
    let max_1 = 0
    let one_count = 0
    for(const element of nums){
        if(element == 1){
            one_count++; 
             // We need to update the max after every 1 encountered
             max_1 = Math.max(one_count, max_1);
        }
        else{
            // When we encounter a zero then it means we must stop counting the ones 
            // We need to prepare the one counter (one_count) for the next segment of 1's
            one_count = 0;
        }
    }
  return max_1; 
};