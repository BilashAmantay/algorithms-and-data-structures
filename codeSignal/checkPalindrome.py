def checkPalindrome(inputString):
    ln = len(inputString)
    if ln==1:
        return True
    i,j = 0, ln
    
    def check(substr):

       if len(substr)>1 and substr[0]!=substr[-1]:
           return False
    while i<j:
        check(inputString[i:j])
        i+=1
        j-=1
    return True

print(checkPalindrome('aabbcebbaa'))
                    

