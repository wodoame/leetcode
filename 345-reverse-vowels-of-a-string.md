```python
vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}; 
# I saw other solutions using a set instead
def reverseVowels(s): 
   # The idea is that when you are reversing a string the last element becomes the first and ...
   # ... the rest of the elements also swap in that same order. 
   # example 'abcde' becomes 'edcba'
   # If we want to reverse the vowels then we can use that same logic
   # The first vowel we encounter will go to the position of the last vowel and the last ... 
   # ... goes to the position of the first 
   # for example 'hello' becomes 'holle'
   # So we use two pointers to swap the vowels
   k = len(s)
   left = 0
   right = k - 1 
   split_s = list(s)
   while True: 
      #  I check all letters from the left until I get a vowel then I stop at that index
      #  Some people used the condition 'while left < right' at the part where I used ...
      #  ... 'while left < k'. They did same for where I did 'while right > -1' 
      #  I don't think it makes much of a difference due to the nature of my code but I'll put that version below this one
      while left < k and not vowels.get(s[left]):
         left += 1
      
      # I check all letters on from the right until a vowel is encountered
      while right > -1 and not vowels.get(s[right]): 
         right -= 1  
      
      # It's safe to swap when left pointer has not exceeded the right pointer otherwise we don't have ...
      # ... anything else to swap so we just return the string
      if left < right: 
         split_s[left], split_s[right] = split_s[right], split_s[left]
         left += 1 
         right -= 1
      else: 
         return "".join(split_s)
```

# The other way

```python
   def reverseVowels(s):
      k = len(s)
      left = 0
      right = k - 1 
      split_s = list(s)
      while left < right: 
            while left < right and not vowels.get(s[left]):
               left += 1
               
            while left < right  and not vowels.get(s[right]): 
               right -= 1  
      
            split_s[left], split_s[right] = split_s[right], split_s[left]
            left += 1 
            right -= 1
      return "".join(split_s)
```

    