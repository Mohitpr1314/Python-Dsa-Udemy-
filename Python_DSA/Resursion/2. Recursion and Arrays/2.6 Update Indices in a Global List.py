
ansList=[]


def UpdateAllIndicesOfAnElementInGlobalList(l1,x,index):
    if(len(l1)==index):
        return
    
    if(l1[index]==x):
        ansList.append(index)

    UpdateAllIndicesOfAnElementInGlobalList(l1,x,index+1)




UpdateAllIndicesOfAnElementInGlobalList([3,2,5,2,8,2,1],2,0)

print(ansList)


# ======================================================================
# Print all Index of Element using Recursion



def find_indices(arr, element):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code h
    ast =[]
    def helper(arr, element, index):
        if len(arr) == index:
            return []
            
        if arr[index] == element:
            ast.append(index)
            
        return helper(arr, element, index+1)
    helper(arr, element, 0)
    return ast
        
            
    
