def palindrome_helper(s1,start,end):
 
    if(start>=end):
        return True
    
    if(s1[start]!= s1[end]):
        return False
    
    return palindrome_helper(s1,start+1,end-1)
    

def palindrome(s1):
    return palindrome_helper(s1,0,len(s1)-1)



print(palindrome('nitinr'))


# ================================================================
def is_palindrome(s):
    """
    Function to check if a string is a palindrome using recursion.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    def helper(s, start, end):
        if start >= end:
            return True
            
            
        if s[start] != s[end]:
            return False
        
        return helper(s, start+1, end-1)
        
    return helper(s,0,len(s)-1)
    
