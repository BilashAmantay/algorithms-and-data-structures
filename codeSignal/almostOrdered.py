def almostIncreasingSequence(sequence):
    count =0
    ln = len(sequence)-1
    i=0
    while i< ln:
        # print(sequence[i])
        # print('i= ',i, ' ',sequence[i-1] , sequence[i] , sequence[i+1])
        if sequence[i-1] < sequence[i] < sequence[i+1]:
            pass
        elif sequence[i-1] <  sequence[i+1]:
            count+=1
            # print('count = ', count, ' at i=',i)
            sequence.pop(i)
            ln = len(sequence)-1
            print('new arr ',sequence)
        if count >1:
            return False
        i+=1
    return True



sequence  = [1, 3, 2, 1]
print(almostIncreasingSequence(sequence))