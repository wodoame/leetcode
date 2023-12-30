const kidsWithCandies = (candies, extraCandies) => {
    // const maximum = candies.reduce((greatest, element)=>{return Math.max(element, greatest)}, candies[0]);
    const maximum = Math.max(...candies); // spread operator is more readable than the above
    const result = candies.map((element)=>{return (element + extraCandies) >= maximum}); 
    return result;
};

console.log(kidsWithCandies([1, 2, 3, 4, 5], 3))