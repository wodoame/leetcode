open_brackets = {'(': 1, '[': 1, '{': 1}
close_brackets = {
    ')':'(', 
    ']':'[', 
    '}': '{'
}

def isValid(s): 
    stack = []
    for element in s: 
        if open_brackets.get(element):
            stack.append(element)
        elif close_brackets.get(element): 
            # stack may either be empty or contain the wrong matching brackets as the last element
            # If so then we return False, If not we pop the matching bracket from the stack
            if not stack or stack[-1] != close_brackets.get(element):
                return False
            else:
                stack.pop()
    # run into this case where there was just one opening bracket '[' in the stack
    # It escapes the checks so there needs to be a last check
    # stack must be empty so that is checked before we return
    return len(stack) == 0
s = "()"


print(isValid(s))