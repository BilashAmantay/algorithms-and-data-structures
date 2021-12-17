"""


"""

def solution(inputString):
    print('inputString: ',inputString)
    l = inputString.split('.')
    
    if len(l)!=4:
        return False
    
    if all([x.isdigit() for x in l]):
        digit = [int(x) for x in l]
    else:
        return False
        
    if not (all([0<=x<255 for x in digit[:3]]) and 1<=digit[-1]<255):
        return False
    
    ## check if added 0 prefix, for example 01.233.22.009
    for i in range(len(l)):
        if digit[i]<10 and len(l[i])!=1:
            return False
        if 10<=digit[i]<99 and len(l[i])!=2:
            return False
        if 100<=digit[i]<255 and len(l[i])!=3:
            return False
   
    if not all([0<=int(x)<256 for x in l[:3]]):
        return False
    
    return True

inputString = '0.254.255.0'
print(solution(inputString))