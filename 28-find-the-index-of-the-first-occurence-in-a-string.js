var strStr = function(haystack, needle) {
    n = needle.length; 
    for(let i=0; i<haystack.length; i++){
        if(haystack[i] == needle[0]){
          let substring = haystack.slice(i, i + n);   
          if(substring == needle){
              return i; 
          } 
        }
    }
    return -1;
};