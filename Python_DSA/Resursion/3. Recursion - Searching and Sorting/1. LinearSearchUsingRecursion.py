"""

Searching Using Recursion

1. Linear Search
2. Binary Search

"""

def LinearSearchUsingRecursionBetter(l1,x,index):
    # Base Case
    if(len(l1) == index):
        return False
    
    if(l1[index]==x):
        return True
    
    return LinearSearchUsingRecursionBetter(l1,x,index+1)

    

def LinearSearchUsingRecursion(l1,x,index):
    # Base Case
    if(len(l1) == index):
        return False
    
    

    ansFromRecursion = LinearSearchUsingRecursion(l1,x,index+1)

    # if(ansFromRecursion == True):
    #     return True
    
    # if(l1[index]==x):
    #     return True
    # return False

    return l1[index] == x or ansFromRecursion


l1 = [i for i in range(100000)]
ans = LinearSearchUsingRecursionBetter(l1,10,0)

print(ans)



# ==================================================================================
def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    # Your code here
    if len(arr) == 0:
        return False
    if arr[0] == target:
        return True
    return linear_search(arr[1:], target)